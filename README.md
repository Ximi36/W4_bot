# Bot W4 do weryfikacji użytkowników na serwerze Discord

## Opis
Program służy do automatycznej weryfikacji użytkowników dołączających na serwer Discord. Umożliwia administratorom serwera łatwe i skuteczne zarządzanie nowymi członkami, zapewniając, że tylko zweryfikowane osoby mogą uzyskać pełny dostęp do serwera. Kompatybilny z sytemem USOS.

## Instrukcja
1. Uruchom program i skonfiguruj bota na swoim serwerze Discord.
2. Zdefiniuj kryteria weryfikacji użytkowników (obecnie możliwe jedynie poprzez modyfikację kodu).
3. Nowi użytkownicy dołączający na serwer zostaną automatycznie przekierowani do procesu weryfikacji.
4. Bot przeprowadzi użytkowników przez kroki weryfikacji zgodnie z ustalonymi kryteriami.
5. Po pomyślnym przejściu weryfikacji, użytkownik otrzyma odpowiednią rolę i pełny dostęp do serwera.
6. W przypadku niepowodzenia w weryfikacji, użytkownik zostanie powiadomiony i będzie miał możliwość ponowienia procesu.

## Wymagania
- Python 3.x
- Biblioteka `discord.py`
- Biblioteka `urllib`
- Biblioteka `requests_oauthlib`
- Konto Discord z uprawnieniami administracyjnymi na serwerze

## Konfiguracja
1. Pobierz i zainstaluj wymagane biblioteki.
2. Skonfiguruj bota, tworząc aplikację w [Discord Developer Portal](https://discord.com/developers/applications).
3. Skopiuj token bota i dodaj go do pliku `.env` programu.
4. Utwórz plik `.env` i dodaj następujące wartości:
   - `CONSUMER_KEY` (klucz uzyskany z usosa, instrukcja generowania znajduje się pod linkiem [https://apps.usos.edu.pl/developers/api/authorization/](https://apps.usos.edu.pl/developers/api/authorization/)),
   - `CONSUMER_SECRET` (secret uzyskany z usosa),
   - `TOKEN` (token bota),
   - `SERVER_ID` (id serwera Discorda)


## Funkcjonalności

- **Automatyczna weryfikacja**: Bot automatycznie przeprowadza nowych użytkowników przez proces weryfikacji.
- **Powiadomienia**: Bot informuje użytkowników o wyniku weryfikacji.
- **Komendy globalne**: Administrator ma możliwość jednym poleceniem wysłać przypomnienie o konieczności weryfikacji do wszystkich niezweryfikowanych użytkowników na serwerze
- **Automatyczna obsługa ticketów**: W momencie stworzenia ticketu przez użytkownika, bot sprawdza, czy jest on zweryfikowany. Na tej podstawie wysyła odpowiednią wiadomość.
- **Interakcje z użytkownikami na serwerze**: Bot posiada możliwość interakcji i użytkownikami na serwerze, np. poprzez wysłanie jednej z predefiniowanych wiadomości gdy wykryje, że ktoś wysłał wiadomość ze słowem "piwo" bądź jego synonimem.

## Autorzy

Autorzy: ximi36, kryreneus

## W przyszłości
- **Integracja z ChatemGPT**
- **Możliwość konfiguracji bota z poziomu pliku konfiguracyjnego, a nie kodu**
- **Łoptymalizacja w wekselu**


***Prace nad botem wciąż trwają, prosimy o cierpliwość. Ewentualne uwagi można kierować na adres mailowy spam@ximix.pl bądź spam@kryreneus.pl***
