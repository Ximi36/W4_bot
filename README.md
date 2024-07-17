# Bot W4 do weryfikacji użytkowników na serwerze Discord

## Opis
Program służy do automatycznej weryfikacji użytkowników dołączających na serwer Discord. Umożliwia administratorom serwera łatwe i skuteczne zarządzanie nowymi członkami, zapewniając, że tylko zweryfikowane osoby mogą uzyskać pełny dostęp do serwera.

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
- Konto Discord z uprawnieniami administracyjnymi na serwerze

## Konfiguracja
1. Pobierz i zainstaluj bibliotekę `discord.py` za pomocą polecenia `pip install discord.py`.
2. Skonfiguruj bota, tworząc aplikację w [Discord Developer Portal](https://discord.com/developers/applications).
3. Skopiuj token bota i dodaj go do pliku .env programu.

## Funkcjonalności

- **Automatyczna weryfikacja**: Bot automatycznie przeprowadza nowych użytkowników przez proces weryfikacji.
- **Powiadomienia**: Bot informuje użytkowników o wyniku weryfikacji.
- **Komendy globalne**: Administrator ma możliwość jednym poleceniem wysłać przypomnienie o konieczności weryfikacji do wszystkich niezweryfikowanych użytkowników na serwerze 

## Autor

Autor: ximi36, kryreneus
