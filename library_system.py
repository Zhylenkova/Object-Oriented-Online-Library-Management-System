import datetime
from typing import List, Optional

class Ksiazka:
    """
    Klasa reprezentująca książkę w bibliotece.
    """
    def __init__(self, tytul: str, autor: str, rok_wydania: int, ilosc_dostepnych: int, opis: str):
        self.tytul = tytul
        self.autor = autor
        self.rok_wydania = rok_wydania
        self.ilosc_dostepnych = ilosc_dostepnych
        self.opis = opis

    def zmniejsz_ilosc(self, sztuki: int = 1):
        """Zmniejsza liczbę dostępnych egzemplarzy po wypożyczeniu książki."""
        if self.ilosc_dostepnych >= sztuki:
            self.ilosc_dostepnych -= sztuki
        else:
            print(f"Błąd: Nie można zmniejszyć ilości książki '{self.tytul}'. Brak wystarczającej liczby egzemplarzy.")

    def zwieksz_ilosc(self, sztuki: int = 1):
        """Metoda pomocnicza do zwiększania ilości przy zwrocie."""
        self.ilosc_dostepnych += sztuki

    def sprawdz_dostepnosc(self) -> bool:
        """Zwraca informację o dostępności książki w bibliotece."""
        return self.ilosc_dostepnych > 0

    def __str__(self):
        return f"'{self.tytul}' - {self.autor} ({self.rok_wydania}) [Dostępne: {self.ilosc_dostepnych}]"


class Wypozyczenie:
    """
    Klasa reprezentująca pojedyncze wypożyczenie książki.
    """
    def __init__(self, ksiazka: 'Ksiazka', uzytkownik: 'Uzytkownik', data_wypozyczenia: datetime.date):
        self.ksiazka = ksiazka
        self.uzytkownik = uzytkownik
        self.data_wypozyczenia = data_wypozyczenia
        self.data_zwrotu = self.oblicz_termin_zwrotu()

    def oblicz_termin_zwrotu(self) -> datetime.date:
        """Oblicza termin zwrotu książki na podstawie daty wypożyczenia (domyślnie 14 dni)."""
        return self.data_wypozyczenia + datetime.timedelta(days=14)

    def __str__(self):
        return f"Wypożyczenie: {self.ksiazka.tytul} przez {self.uzytkownik.imie} {self.uzytkownik.nazwisko} (Zwrot do: {self.data_zwrotu})"


class Uzytkownik:
    """
    Klasa reprezentująca użytkownika biblioteki.
    """
    def __init__(self, imie: str, nazwisko: str, email: str):
        self.imie = imie
        self.nazwisko = nazwisko
        self.email = email
        self.wypozyczenia: List[Wypozyczenie] = []

    def dodaj_do_wypozyczenia(self, ksiazka: Ksiazka):
        """Dodaje książkę do listy wypożyczeń użytkownika."""
        if ksiazka.sprawdz_dostepnosc():
            ksiazka.zmniejsz_ilosc()
            nowe_wypozyczenie = Wypozyczenie(ksiazka, self, datetime.date.today())
            self.wypozyczenia.append(nowe_wypozyczenie)
            print(f"Sukces: Użytkownik {self.imie} wypożyczył '{ksiazka.tytul}'.")
        else:
            print(f"Porażka: Książka '{ksiazka.tytul}' jest niedostępna.")

    def zwroc_ksiazke(self, ksiazka: Ksiazka):
        """Zwraca książkę do biblioteki."""
        wypozyczenie_do_usuniecia = None
        for wyp in self.wypozyczenia:
            if wyp.ksiazka == ksiazka:
                wypozyczenie_do_usuniecia = wyp
                break
        
        if wypozyczenie_do_usuniecia:
            self.wypozyczenia.remove(wypozyczenie_do_usuniecia)
            ksiazka.zwieksz_ilosc()
            print(f"Sukces: Użytkownik {self.imie} zwrócił '{ksiazka.tytul}'.")
        else:
            print(f"Błąd: Użytkownik {self.imie} nie ma wypożyczonej książki '{ksiazka.tytul}'.")

    def __str__(self):
        return f"{self.imie} {self.nazwisko} ({self.email})"


class Biblioteka:
    """
    Klasa reprezentująca bibliotekę zarządząjącą zasobami.
    """
    def __init__(self):
        self.ksiazki: List[Ksiazka] = []
        self.uzytkownicy: List[Uzytkownik] = []

    def dodaj_ksiazke(self, ksiazka: Ksiazka):
        """Dodaje nową książkę do biblioteki."""
        self.ksiazki.append(ksiazka)
        print(f"Biblioteka: Dodano książkę '{ksiazka.tytul}'.")

    def rejestruj_uzytkownika(self, uzytkownik: Uzytkownik):
        """Rejestruje nowego użytkownika w systemie."""
        self.uzytkownicy.append(uzytkownik)
        print(f"Biblioteka: Zarejestrowano użytkownika {uzytkownik.imie} {uzytkownik.nazwisko}.")

    def pokaz_ksiazki(self):
        print("\n--- Lista Książek w Bibliotece ---")
        for k in self.ksiazki:
            print(k)
        print("----------------------------------")

    def pokaz_uzytkownikow(self):
        print("\n--- Lista Użytkowników ---")
        for u in self.uzytkownicy:
            print(u)
        print("--------------------------")


# Demonstracja działania systemu
if __name__ == "__main__":
    print("=== SYSTEM ZARZĄDZANIA BIBLIOTEKĄ ONLINE ===")
    
    # Tworzenie biblioteki
    biblioteka = Biblioteka()

    # Tworzenie książek
    k1 = Ksiazka("Wiedźmin: Ostatnie Życzenie", "Andrzej Sapkowski", 1993, 3, "Zbiór opowiadań o Geralcie z Rivii.")
    k2 = Ksiazka("Pan Tadeusz", "Adam Mickiewicz", 1834, 1, "Epos narodowy.")
    k3 = Ksiazka("Czysty Kod", "Robert C. Martin", 2008, 0, "Podręcznik dobrego programowania.")

    # Dodawanie książek do biblioteki
    biblioteka.dodaj_ksiazke(k1)
    biblioteka.dodaj_ksiazke(k2)
    biblioteka.dodaj_ksiazke(k3)

    # Rejestracja użytkowników
    u1 = Uzytkownik("Jan", "Kowalski", "jan.kowalski@example.com")
    u2 = Uzytkownik("Anna", "Nowak", "anna.nowak@example.com")

    biblioteka.rejestruj_uzytkownika(u1)
    biblioteka.rejestruj_uzytkownika(u2)

    # Wyświetlenie stanu początkowego
    biblioteka.pokaz_ksiazki()

    # Wypożyczanie książek
    print("\n--- Rozpoczęcie Wypożyczeń ---")
    u1.dodaj_do_wypozyczenia(k1) # Sukces
    u1.dodaj_do_wypozyczenia(k3) # Porażka, brak egzemplarzy
    u2.dodaj_do_wypozyczenia(k1) # Sukces
    u2.dodaj_do_wypozyczenia(k2) # Sukces
    u2.dodaj_do_wypozyczenia(k2) # Porażka, ostatnia sztuka wzięta wyżej (jeśli system nie blokuje podwójnego wypożyczenia tej samej - ale tu blokuje stan magazynowy)
                                 # Zaraz, k2 ma 1 sztukę. U2 wziął ją linię wyżej. Więc druga próba powinna się nie udać.

    # Sprawdzenie stanu po wypożyczeniach
    biblioteka.pokaz_ksiazki()

    # Zwroty
    print("\n--- Zwroty Książek ---")
    u2.zwroc_ksiazke(k2)
    u1.zwroc_ksiazke(k3) # Błąd, nie ma jej

    # Stan końcowy
    biblioteka.pokaz_ksiazki()
