#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""*********************************************************************
  Informatica 2019/2020
  
  Casi di test per: {0}
  Funzioni:
{1}
  

RACCOMANDAZIONI:  

anche se non capite tutte le informazioni prodotte da questo
programma, leggete quelle che capite perché vi possono aiutare nello
svolgimento degli esercizi.
"""
ex_name      ='lab06sommaliste'
ex_functions =['somma_liste'] 


#---------------------------------------------------
import importlib
import unittest
import sys
import os

# Stampa un'intestazione che descrive l'esercizio
lista_delle_funzioni="\n".join("  - "+f for f in ex_functions)
print(__doc__.format(ex_name,lista_delle_funzioni))


errori_preliminari=False   # il file ha la giusta struttura?

# Importa le soluzioni degli esercizi
print("CONTROLLO PRELIMINARE DEL FILE {0}.py:".format(ex_name))

lab=None
try:
    lab=importlib.__import__(ex_name)
except Exception:
    msg="""
    Problema a importare il file {0}.py:
    -- il file potrebbe non essere presente in questa cartella,
    -- oppure potrebbe contenere errori che lo rendono non eseguibile.
    
    Provate ad eseguire il comando 'python3 {0}.py' da terminale per
    avere più informazioni. """.format(ex_name)
    print(msg)
    errori_preliminari = True
else:
    #Carica nel namespace le funzioni definite
    f_objects={}
    for f_name in ex_functions:
        try:
            f_object = lab.__dict__[f_name]
            f_objects[f_name] = f_object
        except KeyError:
            msg="    Esercizio mancante: la funzione {1} non è presente nel file {0}.py".format(ex_name,f_name)
            print(msg)
            errori_preliminari = True
        else:
            msg="    Esercizio trovato: la funzione {1} è presente in file {0}.py".format(ex_name,f_name)
            print(msg)
        globals().update(f_objects)


goodhelptext="""
INIZIO DEI TEST AUTOMATICI:

Il file delle soluzioni sembra avere la struttura corretta,
quindi i test avranno luogo.

La riga che rappresenta l'esito dei test contiene:
- un punto . per ogni test riuscito
- un carattere F per ogni test fallito
- un carattere E per ogni test che non è stato possibile eseguire
**********************************************************************
*******                     ESITO DEI TEST                     *******
**********************************************************************
"""
badhelptext="""
ANNULLAMENTO DEI TEST AUTOMATICI:

Le verifiche automatiche non possono partire perché il file non
esiste, non è eseguibile, oppure non contiene tutte le soluzioni 
degli esercizi. 

Sistemate il file delle soluzioni e rieseguite i test.
**********************************************************************
"""
if errori_preliminari:
    print(badhelptext)
    sys.exit(-1)
else:
    print(goodhelptext)

from pprint import pformat


class TestLab06SommaListe(unittest.TestCase):

    def errormsg(self,lista1,lista2,expected,result):
        messaggio = """

MOTIVO DEL FALLIMENTO:
    La somma delle liste {0} e {1} dovrebbe essere {2}, invece il programma 
    restituisce {3}"""
        messaggio = messaggio.format(lista1,lista2,expected,result)
        return messaggio
    
    def test_liste_vuota(self):
        lista1=[]
        lista2=[]
        expected=[]
        result=somma_liste(lista1,lista2)
        msg=self.errormsg(lista1,lista2,expected,result)
        self.assertEqual(expected,result,msg=msg)
    
    def test_liste_singleton(self):
        lista1=[5]
        lista2=[7]
        expected=[12]
        result=somma_liste(lista1,lista2)
        msg=self.errormsg(lista1,lista2,expected,result)
        self.assertEqual(expected,result,msg=msg)

    def test_liste_lunghe(self):
        lista1=[7, 1, 3, 4, -3]
        lista2=[4, 2, -2, -1, 8]
        expected=[11, 3, 1, 3, 5]
        result=somma_liste(lista1,lista2)
        msg=self.errormsg(lista1,lista2,expected,result)
        self.assertEqual(expected,result,msg=msg)

    def test_non_lista(self):
        lista1=1000
        lista2=[4, 2, -2, -1, 8]
        messaggio = """

MOTIVO DEL FALLIMENTO:
    La funzione somma_liste su input {0} e {1} dovrebbe sollevare
    'TypeError' perché accetta solo liste come argomento."""
        messaggio = messaggio.format(repr(lista1), repr(lista2))
        with self.assertRaises(TypeError,msg=messaggio):
            somma_liste(lista1, lista2)

    def test_liste_non_numeriche(self):
        lista1=[3, "pippo", 5]
        lista2=[2, 8, 9]
        messaggio = """

MOTIVO DEL FALLIMENTO:
    La funzione somma_liste su input {0} e {1} dovrebbe sollevare
    'TypeError' perché accetta solo liste contenenti numeri interi come argomento."""
        messaggio = messaggio.format(repr(lista1), repr(lista2))
        with self.assertRaises(TypeError,msg=messaggio):
            somma_liste(lista1, lista2)

    def test_liste_float(self):
        lista1=[3, -2.1, 5]
        lista2=[2, 8, 0]
        messaggio = """

MOTIVO DEL FALLIMENTO:
    La funzione somma_liste su input {0} e {1} dovrebbe sollevare
    'TypeError' perché accetta solo liste contenenti numeri interi come argomento."""
        messaggio = messaggio.format(repr(lista1), repr(lista2))
        with self.assertRaises(TypeError,msg=messaggio):
            somma_liste(lista1, lista2)

    def test_liste_lunghezza_diversa_1(self):
        lista1=[3, 4]
        lista2=[2, 8, 9]
        messaggio = """

MOTIVO DEL FALLIMENTO:
    La funzione somma_liste su input {0} e {1} dovrebbe sollevare
    'ValueError' perché accetta solo liste della stessa lunghezza."""
        messaggio = messaggio.format(repr(lista1), repr(lista2))
        with self.assertRaises(ValueError,msg=messaggio):
            somma_liste(lista1, lista2)

    def test_liste_lunghezza_diversa_2(self):
        lista1=[3, 4, 78]
        lista2=[2, 9]
        messaggio = """

MOTIVO DEL FALLIMENTO:
    La funzione somma_liste su input {0} e {1} dovrebbe sollevare
    'ValueError' perché accetta solo liste della stessa lunghezza."""
        messaggio = messaggio.format(repr(lista1), repr(lista2))
        with self.assertRaises(ValueError,msg=messaggio):
            somma_liste(lista1, lista2)

        

        
if __name__ == '__main__':
    unittest.main()
                              

    
