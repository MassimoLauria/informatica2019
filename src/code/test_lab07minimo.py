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
ex_name      ='lab07minimo'
ex_functions =['posiz_minimo'] 


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
        result=posiz_minimo(lista_mod)
        msg=self.errormsgmodlista(lista_orig,lista_mod)
        self.assertEqual(lista_orig,lista_mod,msg=msg)
    
    def test_minimo_in_testa_con_start_0(self):
        lista_orig=[3, 6, 4, 4, 6, 5]
        lista_mod=lista_orig.copy()
        expected=0
        result=posiz_minimo(lista_mod, 0)
        msg=self.errormsg(lista_orig,expected,result)
        self.assertEqual(expected,result,msg=msg)

    def test_minimo_in_coda_senza_start(self):
        lista_orig=[3, 6, 4, 4, 6, 1]
        lista_mod=lista_orig.copy()
        expected=5
        result=posiz_minimo(lista_mod)
        msg=self.errormsg(lista_orig,expected,result)
        self.assertEqual(expected,result,msg=msg)
    
    def test_minimo_in_coda_con_start_0(self):
        lista_orig=[3, 6, 4, 4, 6, 1]
        lista_mod=lista_orig.copy()
        expected=5
        result=posiz_minimo(lista_mod, 0)
        msg=self.errormsg(lista_orig,expected,result)
        self.assertEqual(expected,result,msg=msg)

    def test_minimo_interno_senza_start(self):
        lista_orig=[3, 6, 1, 4, 6, 5]
        lista_mod=lista_orig.copy()
        expected=2
        result=posiz_minimo(lista_mod)
        msg=self.errormsg(lista_orig,expected,result)
        self.assertEqual(expected,result,msg=msg)
    
    def test_minimo_interno_con_start_0(self):
        lista_orig=[3, 6, 1, 4, 6, 5]
        lista_mod=lista_orig.copy()
        expected=2
        result=posiz_minimo(lista_mod, 1)
        msg=self.errormsg(lista_orig,expected,result)
        self.assertEqual(expected,result,msg=msg)

    def test_minimo_in_coda_senza_start(self):
        lista_orig=[-4, 6, 1, 4, 6, 1]
        lista_mod=lista_orig.copy()
        expected=0
        result=posiz_minimo(lista_mod)
        msg=self.errormsg(lista_orig,expected,result)
        self.assertEqual(expected,result,msg=msg)
    
    def test_minimo_in_coda_con_start_0(self):
        lista_orig=[-4, 6, 1, 4, 6, 1]
        lista_mod=lista_orig.copy()
        expected=2
        result=posiz_minimo(lista_mod, 1)
        msg=self.errormsg(lista_orig,expected,result)
        self.assertEqual(expected,result,msg=msg)

    def test_minimo_in_coda_con_start_ultimo(self):
        lista_orig=[-4, 6, 1, 4, 6, 7]
        lista_mod=lista_orig.copy()
        expected=5
        result=posiz_minimo(lista_mod, 5)
        msg=self.errormsg(lista_orig,expected,result)
        self.assertEqual(expected,result,msg=msg)

    def test_non_lista(self):
        lista_orig=45
        messaggio = """

MOTIVO DEL FALLIMENTO:
    La funzione posiz_minimo su input {0} dovrebbe sollevare
    'TypeError' perché accetta solo una lista come argomento."""
        messaggio = messaggio.format(repr(lista_orig))
        with self.assertRaises(TypeError,msg=messaggio):
            posiz_minimo(lista_orig)
       
    def test_lista_non_numerica(self):
        lista_orig=[23,"parola",12]
        messaggio = """

MOTIVO DEL FALLIMENTO:
    La funzione posiz_minimo su input {0} dovrebbe sollevare
    'TypeError' perché accetta solo una lista di numeri come argomento."""
        messaggio = messaggio.format(repr(lista_orig))
        with self.assertRaises(TypeError,msg=messaggio):
            posiz_minimo(lista_orig)
       
    def test_start_negativo(self):
        lista_orig=[23, 4, 12]
        messaggio = """

MOTIVO DEL FALLIMENTO:
    La funzione posiz_minimo su input {0} e {1} dovrebbe sollevare
    'ValueError' perché il valore del secondo argomento non può essere  negativo."""
        messaggio = messaggio.format(repr(lista_orig), repr(-4))
        with self.assertRaises(ValueError,msg=messaggio):
            posiz_minimo(lista_orig,-4)
       
    def test_start_negativo(self):
        lista_orig=[23, 4, 12]
        messaggio = """

MOTIVO DEL FALLIMENTO:
    La funzione posiz_minimo su input {0} e {1} dovrebbe sollevare
    'ValueError' perché il valore del secondo argomento deve essere minore della lunghezza della lista."""
        messaggio = messaggio.format(repr(lista_orig), repr(3))
        with self.assertRaises(ValueError,msg=messaggio):
            posiz_minimo(lista_orig, 3)
 

if __name__ == '__main__':
    unittest.main()
                              

    
