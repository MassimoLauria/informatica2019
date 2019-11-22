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
ex_name      ='lab08somma'
ex_functions =['somma_mat'] 


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


class TestLab8(unittest.TestCase):

    def errormsg(self,m,expected,result):
        messaggio = """

MOTIVO DEL FALLIMENTO:
    Il risultato con parametro {0} dovrebbe essere {1}, invece il programma 
    restituisce {2}"""
        messaggio = messaggio.format(m,expected,result)
        return messaggio
    
    def test_mat_1_1(self):
        m=[[3]]
        expected=3
        result=somma_mat(m)
        msg=self.errormsg(m,expected,result)
        self.assertEqual(expected,result,msg=msg)
    
    def test_mat_3_per_2(self):
        m=[[3, 1], [8, -2], [4, -5]]
        expected=9
        result=somma_mat(m)
        msg=self.errormsg(m,expected,result)
        self.assertEqual(expected,result,msg=msg)

    def test_mat_2_per_3(self):
        m=[[3, 1, 5], [8, -2, -1]]
        expected=14
        result=somma_mat(m)
        msg=self.errormsg(m,expected,result)
        self.assertEqual(expected,result,msg=msg)

    def test_parametro_lista_non_matrice(self):
        m = [3,4]
        messaggio = """

MOTIVO DEL FALLIMENTO:
    La funzione somma_mat su input {0} dovrebbe sollevare
    'TypeError' perché accetta solo una matrice come argomento."""
        messaggio = messaggio.format(repr(m))
        with self.assertRaises(TypeError,msg=messaggio):
            somma_mat(m)

    def test_parametro_numero_non_matrice(self):
        m = 4
        messaggio = """

MOTIVO DEL FALLIMENTO:
    La funzione somma_mat su input {0} dovrebbe sollevare
    'TypeError' perché accetta solo una matrice come argomento."""
        messaggio = messaggio.format(repr(m))
        with self.assertRaises(TypeError,msg=messaggio):
            somma_mat(m)

    def test_matrice_non_numerica(self):
        m = [[3, 5, 6], [3, "pippo", 6]]
        messaggio = """

MOTIVO DEL FALLIMENTO:
    La funzione somma_mat su input {0} dovrebbe sollevare
    'TypeError' perché accetta solo una matrice di numeri come argomento."""
        messaggio = messaggio.format(repr(m))
        with self.assertRaises(TypeError,msg=messaggio):
            somma_mat(m)

        
if __name__ == '__main__':
    unittest.main()
                              

    
