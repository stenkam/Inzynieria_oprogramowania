from ORM import *
import sqlite3 as sql
import matplotlib.pyplot as plt
import tkinter

def listToORM(list,type):

    '''
    Konwersja listy na obiekt ORM
    :param list - rekord bazy w formie listy:
    :param type - klasa z pliku ORM: 1-ksiazki 2-wypozyczenia 3-klienci
    :return:
    '''

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



    conn=sql.connect("ksiegarnia.db")

    cur=conn.cursor()

    ksiazki=listToORM(cur.execute("select * from Ksiazki"),1)

    wyp=listToORM(cur.execute("select * from wypozyczenia"),2)

    klienci=listToORM(cur.execute("select * from klienci"), 3)



    conn.close()



if __name__=="__main__":
    main()

