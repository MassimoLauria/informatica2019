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
ex_name      ='lab07azzeranegativi'
ex_functions =['azzera_elementi_negativi'] 


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


class TestLab7(unittest.TestCase):

    def errormsg(self,lista,expected,result):
        messaggio = """

MOTIVO DEL FALLIMENTO:
    La chiamata con parametro {0} dovrebbe modificare il parametro rendendolo {1}, invece
    il programma lo rende {2}"""
        messaggio = messaggio.format(lista,expected,result)
        return messaggio
    
    def errormsgnull(self,lista):
        messaggio = """

MOTIVO DEL FALLIMENTO:
    La funzione non deve restituire nulla"""
        return messaggio
    
    def test_lunghezza_zero(self):
        lista_orig=[]
        lista_mod=lista_orig.copy()
        expected=[]
        azzera_elementi_negativi(lista_mod)
        msg=self.errormsg(lista_orig,expected,lista_mod)
        self.assertEqual(expected,lista_mod,msg=msg)
    
    def test_lunghezza_zero_return_null(self):
        lista_orig=[]
        lista_mod=lista_orig.copy()
        result=azzera_elementi_negativi(lista_mod)
        msg=self.errormsgnull(lista_orig)
        self.assertEqual(None,result,msg=msg)

    def test_lista_lunga_return_null(self):
        lista_orig=[2,3,-4,6]
        lista_mod=lista_orig.copy()
        result=azzera_elementi_negativi(lista_mod)
        msg=self.errormsgnull(lista_orig)
        self.assertEqual(None,result,msg=msg)

    def test_lista_un_elemento(self):
        lista_orig=[4]
        lista_mod=lista_orig.copy()
        expected=[4]
        azzera_elementi_negativi(lista_mod)
        msg=self.errormsg(lista_orig,expected,lista_mod)
        self.assertEqual(expected,lista_mod,msg=msg)

    def test_lista_un_elemento_negativo(self):
        lista_orig=[-22]
        lista_mod=lista_orig.copy()
        expected=[0]
        azzera_elementi_negativi(lista_mod)
        msg=self.errormsg(lista_orig,expected,lista_mod)
        self.assertEqual(expected,lista_mod,msg=msg)

    def test_lista_senza_negativi(self):
        lista_orig=[1, 4, 3, 2, 10]
        lista_mod=lista_orig.copy()
        expected=[1, 4, 3, 2, 10]
        azzera_elementi_negativi(lista_mod)
        msg=self.errormsg(lista_orig,expected,lista_mod)
        self.assertEqual(expected,lista_mod,msg=msg)

    def test_lista_con_negativo_in_testa(self):
        lista_orig=[-1, 4, -4, 2, 10]
        lista_mod=lista_orig.copy()
        expected=[0, 4, 0, 2, 10]
        azzera_elementi_negativi(lista_mod)
        msg=self.errormsg(lista_orig,expected,lista_mod)
        self.assertEqual(expected,lista_mod,msg=msg)

    def test_lista_con_negativo_in_coda(self):
        lista_orig=[-1, 4, -4, 2, -8]
        lista_mod=lista_orig.copy()
        expected=[0, 4, 0, 2, 0]
        azzera_elementi_negativi(lista_mod)
        msg=self.errormsg(lista_orig,expected,lista_mod)
        self.assertEqual(expected,lista_mod,msg=msg)

    def test_lista_tutta_negativi(self):
        lista_orig=[-43, -9, -45]
        lista_mod=lista_orig.copy()
        expected=[0, 0, 0]
        azzera_elementi_negativi(lista_mod)
        msg=self.errormsg(lista_orig,expected,lista_mod)
        self.assertEqual(expected,lista_mod,msg=msg)

    def test_non_lista(self):
        lista_orig=45
        messaggio = """

MOTIVO DEL FALLIMENTO:
    La funzione azzera_elementi_negativi su input {0} dovrebbe sollevare
    'TypeError' perché accetta solo una lista come argomento."""
        messaggio = messaggio.format(repr(lista_orig))
        with self.assertRaises(TypeError,msg=messaggio):
            azzera_elementi_negativi(lista_orig)
       
    def test_lista_non_numerica(self):
        lista_orig=[23,"parola",12]
        messaggio = """

MOTIVO DEL FALLIMENTO:
    La funzione azzera_elementi_negativi su input {0} dovrebbe sollevare
    'TypeError' perché accetta solo una lista di numeri come argomento."""
        messaggio = messaggio.format(repr(lista_orig))
        with self.assertRaises(TypeError,msg=messaggio):
            azzera_elementi_negativi(lista_orig)
       
if __name__ == '__main__':
    unittest.main()
                              

    
