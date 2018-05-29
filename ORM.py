class Ksiazki:
    '''
	Id_Książki: klucz główny, INTEGER
	Tytuł: VARCHAR(10)
	Autor*: VARCHAR(40)
    *podawany w kolejności: Nazwisko i Imię oddzielone spacją
	Wydawnictwo: VARCHAR(30)
	Rok wydania- INTEGER(4)
	Gatunek*: CHAR(12)
	*tylko biografia, historyczna, horror, fantastyka, naukowa, kryminalna, przygodowa, inna
	Ilość stron: INTEGER(4)
    '''
    _gatunki=["biografia",
             "historyczna",
             "horror",
             "fantastyka",
             "naukowa",
             "kryminalna",
             "przygodowa",
             "inna"]

    def __init__(self,id,tytul,autor,wydawnictwo,rok_wydania,gatunek,ilosc_stron):

        self.ID_Ksiazki=id
        self.tytul=tytul
        self.autor=autor #Nazwisko imie  oddzielone spacją
        self.wydawnictwo=wydawnictwo
        try:
            self.rok_wydania=int(rok_wydania)
        except ValueError:
            self.rok_wydania=0
        if(gatunek not in self._gatunki):
            self.gatunek=self._gatunki[-1]
        else:
            self.gatunek=gatunek
        try:
            self.ilosc_stron=int(ilosc_stron)
        except ValueError:
            self.ilosc_stron=0




class Wypozyczenia:

    '''
	Id_wypożyczenia: klucz główny, INTEGER
	Id_Książki: klucz obcy, INTEGER
	Id_Klienta: klucz obcy, INTEGER
    '''

    def __init__(self,ID_wypozyczenia,ID_ksiazki,ID_klienta):
        self.ID_wypozyczenia=ID_wypozyczenia
        self.ID_ksiazki=ID_ksiazki
        self.ID_klienta=ID_klienta


class Klienci:

    _p=["Mezczyzna","Kobieta"]

    '''
	Id_Klienta: klucz główny, INTEGER
	Imie: VARCHAR(10)
	Nazwisko: VARCHAR(20)
	Płeć*: CHAR(8)
	*wybór tylko między kobieta/mężczyzna
    '''

    def __init__(self,ID_klienta,Imie,Nazwisko,Plec):

        self.ID_klienta=ID_klienta
        self.imie=Imie
        self.nazwisko=Nazwisko
        if Plec.capitalize() not in self._p:
            self.plec=None
        else:
            self.plec=Plec

