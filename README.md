# System Zarządzania Biblioteką Online

Projekt zaliczeniowy z przedmiotu **Analiza i projektowanie obiektowe**.
Temat: **System zarządzania biblioteką online w ujęciu obiektowym**.

## Opis Projektu

Celem projektu było odwzorowanie rzeczywistego procesu wypożyczania książek w bibliotece internetowej przy użyciu paradygmatu programowania obiektowego. System modeluje kluczowe podmioty takie jak książki, użytkownicy, wypożyczenia oraz sama biblioteka.

### Zaimplementowane Klasy

1.  **Książka (`Ksiazka`)**:
    *   Przechowuje informacje o tytule, autorze, roku wydania, dostępnej ilości i opisie.
    *   Umożliwia zarządzanie stanem magazynowym (zmniejszanie/zwiększanie ilości).
    *   Metody: `zmniejsz_ilosc`, `zwieksz_ilosc`, `sprawdz_dostepnosc`.

2.  **Użytkownik (`Uzytkownik`)**:
    *   Reprezentuje klienta biblioteki (imię, nazwisko, email).
    *   Posiada listę aktywnych wypożyczeń.
    *   Metody: `dodaj_do_wypozyczenia`, `zwroc_ksiazke`.

3.  **Wypożyczenie (`Wypozyczenie`)**:
    *   Rejestruje fakt wypożyczenia konkretnej książki przez konkretnego użytkownika.
    *   Automatycznie oblicza termin zwrotu (domyślnie 14 dni od daty wypożyczenia).
    *   Metody: `oblicz_termin_zwrotu`.

4.  **Biblioteka (`Biblioteka`)**:
    *   Główny zarządca systemu.
    *   Przechowuje rejestr wszystkich książek i użytkowników.
    *   Metody: `dodaj_ksiazke`, `rejestruj_uzytkownika`.

## Wymagania

*   Python 3.x
*   Brak zewnętrznych zależności (użyto tylko bibliotek standardowych: `datetime`, `typing`).

## Uruchomienie

Aby uruchomić system i zobaczyć przykładową demonstrację działania (dodawanie książek, rejestracja użytkowników, proces wypożyczania i zwrotu), należy uruchomić plik `library_system.py`:

```bash
python library_system.py
```

## Struktura Katalogu

*   `library_system.py` - Główny plik z implementacją klas i logiką demonstracyjną.
*   `README.md` - Dokumentacja projektu.
