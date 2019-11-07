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
ex_name      ='lab07crealista'
ex_functions =['crea_lista'] 


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

    def errormsg(self,a,b,expected,result):
        messaggio = """

MOTIVO DEL FALLIMENTO:
    La lista creata con parametri {0} e {1} dovrebbe essere {2}, invece il programma 
    restituisce {3}"""
        messaggio = messaggio.format(a,b,expected,result)
        return messaggio
    
    def test_lunghezza_zero(self):
        a=10
        b=0
        expected=[]
        result=crea_lista(a,b)
        msg=self.errormsg(a,b,expected,result)
        self.assertEqual(expected,result,msg=msg)
    
    def test_liste_lunghezza_uno(self):
        a=10
        b=1
        expected=[10]
        result=crea_lista(a,b)
        msg=self.errormsg(a,b,expected,result)
        self.assertEqual(expected,result,msg=msg)

    def test_lista_lunga(self):
        a=20
        b=5
        expected=[20,21,22,23,24]
        result=crea_lista(a,b)
        msg=self.errormsg(a,b,expected,result)
        self.assertEqual(expected,result,msg=msg)

    def test_primo_negativo(self):
        a=-4
        b=6
        expected=[-4,-3,-2,-1,0,1]
        result=crea_lista(a,b)
        msg=self.errormsg(a,b,expected,result)
        self.assertEqual(expected,result,msg=msg)

    def test_primo_non_numero(self):
        a="pippo"
        b=4
        messaggio = """

MOTIVO DEL FALLIMENTO:
    La funzione crea_lista su input {0} e {1} dovrebbe sollevare
    'TypeError' perché accetta solo numeri come argomenti."""
        messaggio = messaggio.format(repr(a), repr(b))
        with self.assertRaises(TypeError,msg=messaggio):
            crea_lista(a,b)

    def test_secondo_non_naturale(self):
        a=25
        b=-5
        messaggio = """

MOTIVO DEL FALLIMENTO:
    La funzione crea_lista su input {0} e {1} dovrebbe sollevare
    'ValueError' perché accetta solo liste contenenti numeri come argomento."""
        messaggio = messaggio.format(repr(a), repr(b))
        with self.assertRaises(ValueError,msg=messaggio):
            crea_lista(a,b)        

        
if __name__ == '__main__':
    unittest.main()
                              

    
