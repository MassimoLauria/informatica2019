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
ex_name      ='lab06unione'
ex_functions =['unione'] 


#---------------------------------------------------
import importlib
import unittest
import sys
import os

# Stampa un'intestazione che descrive l'esercizio
lista_delle_funzioni="\n".join("  -"+f for f in ex_functions)
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
- una carattere F per ogni test fallito
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


class TestLab06Unione(unittest.TestCase):

    def errormsg(self,lista1,lista2,expected,result):
        messaggio = """

MOTIVO DEL FALLIMENTO:
    Il risultato sulle liste {0} e {1} dovrebbe essere {2}, invece il programma 
    restituisce {3}"""
        messaggio = messaggio.format(lista1,lista2,expected,result)
        return messaggio
    
    def test_liste_vuote(self):
        lista1=[]
        lista2=[]
        expected=[]
        result=unione(lista1,lista2)
        msg=self.errormsg(lista1,lista2,expected,result)
        self.assertEqual(expected,result,msg=msg)

    def test_lista_singleton(self):
        lista1=[5]
        lista2=[5]
        expected=[5]
        result=unione(lista1,lista2)
        msg=self.errormsg(lista1,lista2,expected,result)
        self.assertEqual(expected,result,msg=msg)

    def test_liste_disgiunte(self):
        lista1=[7, 1]
        lista2=[8, 12]
        expected=[7,1,8,12].sort()
        result=unione(lista1,lista2).sort()
        msg=self.errormsg(lista1,lista2,expected,result)
        self.assertEqual(expected,result,msg=msg)

    def test_liste_permutate(self):
        lista1=[8, 6, 4, 5, 2]
        lista2=[2, 5, 6, 4, 8]
        expected=[2, 5, 6, 4, 8].sort()
        result=unione(lista1,lista2).sort()
        msg=self.errormsg(lista1,lista2,expected,result)
        self.assertEqual(expected,result,msg=msg)

    def test_liste_qualsiasi(self):
        lista1=[8, 1, 4, 5, 2]
        lista2=[2, 5, 6, 4, 18]
        expected=[8, 1, 4, 5, 2, 6, 18].sort()
        result=unione(lista1,lista2).sort()
        msg=self.errormsg(lista1,lista2,expected,result)
        self.assertEqual(expected,result,msg=msg)

    def test_lista1_in_lista2(self):
        lista1=[8, 1, 4]
        lista2=[2, 4, 8, 18, 1]
        expected=[2, 4, 8, 18, 1].sort()
        result=unione(lista1,lista2).sort()
        msg=self.errormsg(lista1,lista2,expected,result)
        self.assertEqual(expected,result,msg=msg)

    def test_lista2_in_lista1(self):
        lista1=[2, 4, 8, 18, 1]
        lista2=[8, 1, 4]
        expected=[2, 4, 8, 18, 1].sort()
        result=unione(lista1,lista2).sort()
        msg=self.errormsg(lista1,lista2,expected,result)
        self.assertEqual(expected,result,msg=msg)

    def test_non_lista_prima(self):
        lista1=1000
        lista2=[8, 4]
        messaggio = """

MOTIVO DEL FALLIMENTO:
    La funzione unione su input {0} e {1} dovrebbe sollevare
    'TypeError' perché accetta solo liste come argomento."""
        messaggio = messaggio.format(repr(lista1),repr(lista2))
        with self.assertRaises(TypeError,msg=messaggio):
            unione(lista1,lista2)

    def test_non_lista_seconda(self):
        lista1=[8, 4]
        lista2=451
        messaggio = """

MOTIVO DEL FALLIMENTO:
    La funzione unione su input {0} e {1} dovrebbe sollevare
    'TypeError' perché accetta solo liste come argomento."""
        messaggio = messaggio.format(repr(lista1),repr(lista2))
        with self.assertRaises(TypeError,msg=messaggio):
            unione(lista1,lista2)


if __name__ == '__main__':
    unittest.main()
                              

    
