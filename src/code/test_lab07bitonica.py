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
ex_name      ='lab07bitonica'
ex_functions =['bitonica'] 


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
    La chiamata con parametro {0} dovrebbe restituire il valore {1}, invece
restituisce {2}"""
        messaggio = messaggio.format(lista,expected,result)
        return messaggio
    
    def errormsgmodlista(self,lista_orig,lista_mod):
        messaggio = """

MOTIVO DEL FALLIMENTO:
    La funzione non deve modificare la lista passata come argomento: riceve la lista {0}  e la modifica in {1}"""
        messaggio = messaggio.format(lista_orig,lista_mod)
        return messaggio
    
    def test_lista_immutata(self):
        lista_orig=[3, 6, 4, 4, 6, 5]
        lista_mod=lista_orig.copy()
        expected=0
        result=bitonica(lista_mod)
        msg=self.errormsgmodlista(lista_orig,lista_mod)
        self.assertEqual(lista_orig,lista_mod,msg=msg)
    
    def test_lista_vuota(self):
        lista_orig=[]
        lista_mod=lista_orig.copy()
        expected=False
        result=bitonica(lista_mod)
        msg=self.errormsg(lista_orig,expected,result)
        self.assertEqual(expected,result,msg=msg)

    def test_lista_unitaria(self):
        lista_orig=[3]
        lista_mod=lista_orig.copy()
        expected=False
        result=bitonica(lista_mod)
        msg=self.errormsg(lista_orig,expected,result)
        self.assertEqual(expected,result,msg=msg)
    
    def test_lista_lunghezza_due(self):
        lista_orig=[3, 6]
        lista_mod=lista_orig.copy()
        expected=False
        result=bitonica(lista_mod)
        msg=self.errormsg(lista_orig,expected,result)
        self.assertEqual(expected,result,msg=msg)

    def test_altra_lista_lunghezza_due(self):
        lista_orig=[12, 6]
        lista_mod=lista_orig.copy()
        expected=False
        result=bitonica(lista_mod)
        msg=self.errormsg(lista_orig,expected,result)
        self.assertEqual(expected,result,msg=msg)

    def test_lista_lunga_bitonica(self):
        lista_orig=[2, 4, 13, 34, 23]
        lista_mod=lista_orig.copy()
        expected=True
        result=bitonica(lista_mod)
        msg=self.errormsg(lista_orig,expected,result)
        self.assertEqual(expected,result,msg=msg)
    
    def test_lista_lunga_senza_coda(self):
        lista_orig=[2, 4, 13, 34]
        lista_mod=lista_orig.copy()
        expected=False
        result=bitonica(lista_mod)
        msg=self.errormsg(lista_orig,expected,result)
        self.assertEqual(expected,result,msg=msg)
    
    def test_lista_lunga_senza_testa(self):
        lista_orig=[234, 48, 33, 31, 23]
        lista_mod=lista_orig.copy()
        expected=False
        result=bitonica(lista_mod)
        msg=self.errormsg(lista_orig,expected,result)
        self.assertEqual(expected,result,msg=msg)
    
    def test_lista_con_testa_costante(self):
        lista_orig=[3, 6, 6, 8, 5]
        lista_mod=lista_orig.copy()
        expected=False
        result=bitonica(lista_mod)
        msg=self.errormsg(lista_orig,expected,result)
        self.assertEqual(expected,result,msg=msg)
    
    def test_lista_con_apice_costante(self):
        lista_orig=[3, 6, 8, 8, 5]
        lista_mod=lista_orig.copy()
        expected=False
        result=bitonica(lista_mod)
        msg=self.errormsg(lista_orig,expected,result)
        self.assertEqual(expected,result,msg=msg)
    
    def test_lista_con_coda_costante(self):
        lista_orig=[3, 6, 8, 5, 5, 4]
        lista_mod=lista_orig.copy()
        expected=False
        result=bitonica(lista_mod)
        msg=self.errormsg(lista_orig,expected,result)
        self.assertEqual(expected,result,msg=msg)
    
    def test_lista_non_bitonica(self):
        lista_orig=[9, 3, 6, 5, 8, 2, 7]
        lista_mod=lista_orig.copy()
        expected=False
        result=bitonica(lista_mod)
        msg=self.errormsg(lista_orig,expected,result)
        self.assertEqual(expected,result,msg=msg)
    
    def test_altra_lista_non_bitonica(self):
        lista_orig=[1, 3, 6, 5, 8, 2, 7, 2]
        lista_mod=lista_orig.copy()
        expected=False
        result=bitonica(lista_mod)
        msg=self.errormsg(lista_orig,expected,result)
        self.assertEqual(expected,result,msg=msg)
    
    def test_non_lista(self):
        lista_orig=45
        messaggio = """

MOTIVO DEL FALLIMENTO:
    La funzione bitonica su input {0} dovrebbe sollevare
    'TypeError' perché accetta solo una lista come argomento."""
        messaggio = messaggio.format(repr(lista_orig))
        with self.assertRaises(TypeError,msg=messaggio):
            bitonica(lista_orig)
       
    def test_lista_non_numerica(self):
        lista_orig=[23,"parola",12]
        messaggio = """

MOTIVO DEL FALLIMENTO:
    La funzione bitonica su input {0} dovrebbe sollevare
    'TypeError' perché accetta solo una lista di numeri come argomento."""
        messaggio = messaggio.format(repr(lista_orig))
        with self.assertRaises(TypeError,msg=messaggio):
            bitonica(lista_orig)
        

if __name__ == '__main__':
    unittest.main()
                              

    
