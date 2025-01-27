from ORM import *
import sqlite3 as sql
import matplotlib.pyplot as plt

#by Kamil Stenzel

def addtoDB():

    conn = sql.connect("ksiegarnia.db")
    cur = conn.cursor()

    t=int(input('''
            1.Ksiazka
            2.Wypozyczenie
            3.Klient'''))

    if t == 1:

        try:
            data=cur.execute('''select max(ID_Ksiazki) from Ksiazki''')
            for i in data:
                id=i[0]+1
            k = Ksiazki(10, input("Podaj tytul"),
                        input("Podaj autora"),
                        input("Podaj wydawnictwo"),
                        input("Podaj rok wydania"),
                        input("Podaj gatunek"),
                        input("Podaj ilość stron"))

            sql_input = "insert into ksiazki values({0},'{1}','{2}','{3}',{4},'{5}',{6})".format(id, k.tytul, k.autor,
                                                                                                 k.wydawnictwo,
                                                                                                 k.rok_wydania,
                                                                                                 k.gatunek,
                                                                                                 k.ilosc_stron)
            cur.execute(sql_input)
            conn.commit()


        except Exception as e:
                print("Błąd SQL")
                conn.close()
                return None
    elif t == 2:
        try:
            data = cur.execute('''select max(ID_wypozyczenia) from Wypozyczenia''')
            for i in data:
                id = i[0]+1
            k = Wypozyczenia(id, input("Podaj id ksiazki"),input("Podaj id klienta"))
            sql_input="insert into ksiazki values({0},{1},{2})".format(id, k.ID_ksiazki,k.ID_klienta)
            cur.execute(sql_input)
            conn.commit()


        except Exception as e:
            print("Błąd SQL")
            conn.close()
            return None
    elif t == 3:
        try:
            data = cur.execute('''select max(ID_klienta) from Klienci''')
            for i in data:
                id = i[0]+1
            k = Klienci(id, input("Podaj imie"),input("Podaj nazwisko"),input("Podaj plec"))

            sql_input="insert into ksiazki values({0},{1},{2})".format(id, k.imie,k.nazwisko,k.plec)

            cur.execute(sql_input)
            conn.commit()


        except Exception as e:
            print("Błąd SQL")
            conn.close()
            return None

    conn.close()

def listToORM(list,type):



    if(type==1):

        k=[]

        for i in list:

            k.append(Ksiazki(i[0],i[1],i[2],i[3],i[4],i[5],[6]))

        return k

    if(type==2):

        k=[]

        for i in list:

            k.append(Wypozyczenia(i[0],i[1],i[2]))

        return k

    if(type==3):

        k=[]

        for i in list:

            k.append(Klienci(i[0],i[1],i[2],i[3]))

        return k


def main():



    conn = sql.connect("ksiegarnia.db")

    cur=conn.cursor()

   # ksiazki=listToORM(cur.execute("select * from Ksiazki"),1)

   # wyp=listToORM(cur.execute("select * from wypozyczenia"),2)

  #  klienci=listToORM(cur.execute("select * from klienci"), 3)



    run = True

    while run:
        c = int(input("""Menu:
                1. Ilość wypożyczonych książek z podziałem na ich gatunki
                2. Ilość posiadanych książek z podziałem na ich autorów
                3. Jaki procent osób wypożyczających książki stanowią kobiety a ile mężczyźni
                4. Najczęściej wypożyczane tytuły książek
                5. Wprowadź dane do bazy
                6. Koniec"""))

        x = []
        y = []

        if c == 1:

            try:
                data=cur.execute("select gatunek, count(gatunek) from wypozyczenia inner join ksiazki"
                                 " on wypozyczenia.id_ksiazki=ksiazki.id_ksiazki group by gatunek")
                for i in data:
                    x.append(i[0])
                    y.append(i[1])
                plt.bar(x, y)
                plt.show()
            except Exception as e:
                print("Błąd SQL")

        elif c == 2:
            try:
                data = cur.execute("select autor, count(autor) from ksiazki group by autor")
                for i in data:
                    x.append(i[0])
                    y.append(i[1])
                plt.bar(x, y)
                plt.show()
            except Exception as e:
                print("Błąd SQL")

        elif c == 3:
            try:
                data = cur.execute("select ((select 1.0*count(plec) from klienci where plec='Kobieta')/(1.0*count(plec))),"
                                   "((select 1.0*count(plec) from klienci where plec='Mezczyzna')/(1.0*count(plec)))"
                                   " from klienci")
                for i in data:
                    x = i[0]
                    y = i[1]
                x = int(100 * x)
                y = int(100 * y)
                percentage = [x,y]
                labels = ["Kobieta","Mezczyzna"]
                plt.pie(percentage,labels=labels)
                plt.show()
            except Exception as e:
                print("Błąd SQL")

        elif c == 4:
            try:
                data = cur.execute("select count(wypozyczenia.id_ksiazki),ksiazki.tytul from wypozyczenia"
                                   " inner join ksiazki on wypozyczenia.id_ksiazki=ksiazki.id_ksiazki"
                                   " group by ksiazki.id_ksiazki")
                for i in data:
                    x.append(i[1])
                    y.append(i[0])
                plt.bar(x, y)
                plt.show()
            except Exception as e:
                print("Błąd SQL")

        elif c == 5:
            addtoDB()
        else:
            run = False

    conn.close()
if __name__.endswith('__main__'):
    main()

