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
ex_name      ='lab06separa'
ex_functions =['separa_elementi'] 


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


class TestLab06SeparaElementi(unittest.TestCase):

    def errormsg(self,lista,expected,result):
        messaggio = """

MOTIVO DEL FALLIMENTO:
    Il risultato sulla lista {0} dovrebbe essere {1}, invece il programma 
    restituisce {2}"""
        messaggio = messaggio.format(lista,expected,result)
        return messaggio
    
    def test_lista_vuota(self):
        lista=[]
        expected=([],[])
        result=separa_elementi(lista)
        msg=self.errormsg(lista,expected,result)
        self.assertEqual(expected,result,msg=msg)

    def test_lista_singleton(self):
        lista=[5]
        expected=([],[5])
        result=separa_elementi(lista)
        msg=self.errormsg(lista,expected,result)
        self.assertEqual(expected,result,msg=msg)

    def test_lista_coppia(self):
        lista=[7, 1]
        expected=([7],[1])
        result=separa_elementi(lista)
        msg=self.errormsg(lista,expected,result)
        self.assertEqual(expected,result,msg=msg)

    def test_lista_lunga1(self):
        lista=[0.96, 0.2, 0.4, 0.1, 0.55, 0.03, 0.88]
        expected=( [0.96, 0.55, 0.88] , [0.2, 0.4, 0.1, 0.03] )
        result=separa_elementi(lista)
        msg=self.errormsg(lista,expected,result)
        self.assertEqual(expected,result,msg=msg)

    def test_lista_lunga2(self):
        lista=[0.2, 0.96, 0.4, 0.1, 0.55, 0.03, 0.88]
        expected=( [0.96, 0.55, 0.88] , [0.2, 0.4, 0.1, 0.03] )
        result=separa_elementi(lista)
        msg=self.errormsg(lista,expected,result)
        self.assertEqual(expected,result,msg=msg)

    def test_non_lista(self):
        lista=1000
        messaggio = """

MOTIVO DEL FALLIMENTO:
    La funzione separa_elementi su input {0} dovrebbe sollevare
    'TypeError' perché accetta solo liste come argomento."""
        messaggio = messaggio.format(repr(lista))
        with self.assertRaises(TypeError,msg=messaggio):
            separa_elementi(lista)

    def test_liste_non_numeriche(self):
        lista=[3, "pippo", 5]
        messaggio = """

MOTIVO DEL FALLIMENTO:
    La funzione separa_elementi su input {0} dovrebbe sollevare
    'TypeError' perché accetta solo una lista contenenti numeri come argomento."""
        messaggio = messaggio.format(repr(lista))
        with self.assertRaises(TypeError,msg=messaggio):
            separa_elementi(lista)


if __name__ == '__main__':
    unittest.main()
                              

    
