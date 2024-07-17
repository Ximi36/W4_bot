import os
import usos_api
import discord
from discord.ext import commands
import requests_oauthlib
from client_config import client

fields_of_study = {
    'cyberbezpieczeństwo': "CBE",
    'informatyka algorytmiczna': "INA",
    'inżynieria systemów': "INS",
    'informatyczne systemy automatyki': "ISA",
    'informatyka stosowana': "IST",
    'informatyka techniczna': "ITE",
    'sztuczna inteligencja': "SZT",
    'zaufane systemy sztucznej inteligencji': "TAI",
    'telekomunikacja': "TEL",
    'teleinformatyka': "TIN"
}

temp_users_tokens = []

def role_selection(students_programme):
    if not students_programme:
        return ""
    
    programme_shortcuts = []
    for student_data in students_programme:
        if student_data["programme"]["id"].startswith("W04"):
            programme_shortcuts.append(fields_of_study[student_data["programme"]["description"]["pl"].split(",")[0]])


    return programme_shortcuts


def start_veryfication_mech(server):

  @client.event
  async def on_member_join(member):
        url_to_authorize, oauth_token, oauth_token_secret = usos_api.request_for_link()
        temp_users_tokens.append({"user_id": member.id, "owner_key": oauth_token, "owner_secret": oauth_token_secret})
        
        emb=discord.Embed(colour=discord.Colour.from_rgb(153, 0, 0), title="WITaj w naszych skromnych discordowych progach!",description="Aby ułatwić nam pracę, kliknij w poniższy link i zaloguj się, aby zostać zweryfikowanym na serwerze. Po zalogowaniu się wyświetli Ci się kod PIN.\n:point_right: **WKLEJ GO W TEJ ROZMOWIE** :point_left:")
        emb.add_field(name="Twój link weryfikacyjny", value=url_to_authorize)
        emb.set_footer(text="Zapewniamy, iż Twoje dane są przetwarzane jedynie w celu weryfikacji i nie są nigdzie przechowywane. Wszelkie wątpilowści możesz kierować do administracji serwera")
        await member.send(embed=emb)
        
  @client.event
  async def on_member_remove(member):
      for temp_user_token in temp_users_tokens:
            if temp_user_token["user_id"] == member.id:
                temp_users_tokens.remove(temp_user_token)
        
    
async def second_step(message, server):
    temp_member = server.get_member(message.author.id)
    if message.author.id == temp_member.id:
        if len(temp_member.roles) == 1 or any(role.name == "Wódz" for role in temp_member.roles):
            if len(message.content) == 8 and message.content.isnumeric():
                for temp_user_token in temp_users_tokens:
                    if temp_user_token["user_id"] == message.author.id:
                        try:
                            resource_owner_key, resource_owner_secret = usos_api.authenticate(str(message.content), temp_user_token["owner_key"], temp_user_token["owner_secret"])
                        except:
                            url_to_authorize, oauth_token, oauth_token_secret = usos_api.request_for_link()
                            temp_user_token["owner_key"] = oauth_token
                            temp_user_token["owner_secret"] = oauth_token_secret

                            emb = discord.Embed(colour=discord.Colour.from_rgb(153, 0, 0), title="Bardzo mi przykro, ale proces weryfikacji nie przebiegł pomyślnie :frowning:", description="Pani z dziekanatu wygenerowała dla Ciebie nowy link, spróbuj jeszcze raz. Po zalogowaniu się wyświetli Ci się kod PIN.\n:point_right: **WKLEJ GO W TEJ ROZMOWIE** :point_left:")
                            emb.add_field(name="Twój link weryfikacyjny", value=url_to_authorize)
                            emb.set_footer(text="Zapewniamy, iż Twoje dane są przetwarzane jedynie w celu weryfikacji i nie są nigdzie przechowywane. Wszelkie wątpilowści możesz kierować do administracji serwera")
                            await message.author.send(embed=emb)
                        else:
                            temp_user_token["owner_key"] = resource_owner_key
                            temp_user_token["owner_secret"] = resource_owner_secret
                            await user_authorization(message, server)

            elif message.content == "$link":

                temp_token_storage = [temp_user_token for temp_user_token in temp_users_tokens if temp_user_token["user_id"] == message.author.id]

                if not temp_token_storage:
                    url_to_authorize, oauth_token, oauth_token_secret = usos_api.request_for_link()
                    temp_users_tokens.append({"user_id": message.author.id, "owner_key": oauth_token, "owner_secret": oauth_token_secret})

                    emb = discord.Embed(colour=discord.Colour.from_rgb(153, 0, 0), title="Aktywowano usługę LOGOWANIE+ :saluting_face:", description="W związku z aktywacją płatnej usługi **LOGOWANIE+** została pobrana opłata w wysokości 1 ECTS'a. Pani z dziekanatu wygenerowała dla Ciebie nowy link, spróbuj jeszcze raz. Po zalogowaniu się wyświetli Ci się kod PIN.\n:point_right: **WKLEJ GO W TEJ ROZMOWIE** :point_left:")
                    emb.add_field(name="Twój link weryfikacyjny", value=url_to_authorize)
                    emb.set_footer(text="Zapewniamy, iż Twoje dane są przetwarzane jedynie w celu weryfikacji i nie są nigdzie przechowywane. Wszelkie wątpilowści możesz kierować do administracji serwera")
                    await message.author.send(embed=emb)

                else:
                    for temp_user_token in temp_users_tokens:
                        if temp_user_token == temp_token_storage[0]:
                            url_to_authorize, oauth_token, oauth_token_secret = usos_api.request_for_link()
                            temp_user_token["owner_key"] = oauth_token
                            temp_user_token["owner_secret"] = oauth_token_secret

                            emb = discord.Embed(colour=discord.Colour.from_rgb(153, 0, 0), title="Aktywowano usługę LOGOWANIE+ :saluting_face:", description="W związku z aktywacją płatnej usługi **LOGOWANIE+** została pobrana opłata w wysokości 1 ECTS'a. Pani z dziekanatu wygenerowała dla Ciebie nowy link, spróbuj jeszcze raz. Po zalogowaniu się wyświetli Ci się kod PIN.\n:point_right: **WKLEJ GO W TEJ ROZMOWIE** :point_left:")
                            emb.add_field(name="Twój link weryfikacyjny", value=url_to_authorize)
                            emb.set_footer(text="Zapewniamy, iż Twoje dane są przetwarzane jedynie w celu weryfikacji i nie są nigdzie przechowywane. Wszelkie wątpilowści możesz kierować do administracji serwera")
                            await message.author.send(embed=emb)

            elif message.content == "$bruteforce" and any(role.name == "Wódz" for role in temp_member.roles):
                async for member in server.fetch_members(limit=None):
                    if not member.bot and not any(role.name == "Zweryfikowany" for role in member.roles):
                        emb=discord.Embed(colour=discord.Colour.from_rgb(153, 0, 0), title="WITaj ponownie! :beers:",description="Mój szósty zmysł pozwolił mi wykryć, iż nie jesteś jeszcze zweryfikowany na serwerze **Samorząd WITa**. Użyj w tej konwersacji komendy ```$link```Pani z dziekanatu wygeneruje dla Ciebie wówczas nowy link weryfikacyjny. Wszystkie instrukcje otrzymasz wraz z nowym linkiem :mechanical_arm:")

                        await member.send(embed=emb)

            else:
                emb = discord.Embed(colour=discord.Colour.from_rgb(153, 0, 0), title="Bajo jajo, bajo jajo :egg: :egg: :egg:", description="Co Ty tutaj odczyniasz? Na PIN mnie nie oszukasz :rage:")
                await message.author.send(embed=emb)

        else:
            emb = discord.Embed(colour=discord.Colour.from_rgb(153, 0, 0), title="Co za dużo to nie zdrowo!", description="**Wykryłem, że zostałeś już zweryfikowany!**\nJeśli uważasz inaczej, skontaktuj się z administracją serwera.\n\nJeśli napisałeś do mnie tylko i wyłącznie dlatego, że Ci się nudziło, to wiedz, że moi twórcy pracują nad tym, abym mógł z Tobą rozmawiać bez żadnych ograniczeń :shushing_face: :sunglasses:")
            await message.author.send(embed=emb)


    else:
        emb = discord.Embed(colour=discord.Colour.from_rgb(153, 0, 0), title="Nie jesteś użytkownikiem naszego serwera :rolling_eyes:", description="Zauważyłem, że nie jesteś użytkownikiem serwera \"Samorząd WITa\". Jeśli uważasz inaczej, skontaktuj się z administracją serwera.")
        await message.author.send(embed=emb)
                    
                                                   
                        
async def user_authorization(message, server):  
    for temp_user_token in temp_users_tokens:
        if temp_user_token["user_id"] == message.author.id:
            user_data = usos_api.fetch_data(temp_user_token["owner_key"], temp_user_token["owner_secret"], "users/user?fields=first_name|last_name|student_programmes|staff_status")
            temp_users_tokens.remove(temp_user_token)
                
    current_member = server.get_member(message.author.id)
    if not user_data["staff_status"] > 0:
        roles_names_to_add = (role_selection(user_data["student_programmes"]))
        roles_names_to_add.append("Zweryfikowany")
        
    roles_to_add = [discord.utils.get(server.roles, name=role_name_to_add)
    for role_name_to_add in roles_names_to_add
    ]
    roles_to_add = [role for role in roles_to_add if role is not None]
    
    await current_member.add_roles(*roles_to_add)
    await current_member.edit(nick=user_data["first_name"] + " " + user_data["last_name"])
    emb=discord.Embed(colour=discord.Colour.from_rgb(153, 0, 0), title="ALE BAZA!",description="Zostałes pomyślnie zweryfikowany.\nUstawiłem za Ciebie Twoje imię i nazwisko jako Twój nick na serwerze oraz dodałem rolę odpowiadającą Twojemu kierunkowi :sunglasses: Dodatkowe role możesz wybrać samemu na kanale <#1140343809054609409>\n\nJeśli coś się nie zgadza, napisz do jednego z adminów.")
    emb.add_field(name="Serdecznie zapraszamy do polubienia naszych profili w mediach społeczniościowych!", value="FB: https://www.facebook.com/samorzad.wita \n IG: https://www.instagram.com/team_w4n/")
    emb.set_image(url="https://media.discordapp.net/attachments/1096496301149016186/1175132385994625034/IMG_20230916_105203.jpg?ex=656a1e51&is=6557a951&hm=4a3b9fedb515d19b000236be3365f643b58274d2213a861776f51fd7bb9ce965&=&width=738&height=662")
        
    user_data.clear()

    await message.author.send(embed=emb)