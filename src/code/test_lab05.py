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
ex_name      ='lab05'
ex_functions =['conteggiovocali','triangolo','ternepitagoriche',"ternepitagoriche2"] 


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

La prima riga subito dopo la cornice di asterischi contiene:
- un punto . per ogni test riuscito
- un carattere F per ogni test fallito
- un carattere E per ogni test che non è stato possiblie eseguire
*********************************************************************
"""
badhelptext="""
ANNULLAMENTO DEI TEST AUTOMATICI:

Le verifiche automatiche non possono partire perché il file non
esiste, non è eseguibile, oppure non contiene tutte le soluzioni 
degli esercizi. 

Sistemate il file delle soluzioni e rieseguite i test.
*********************************************************************
"""
if errori_preliminari:
    print(badhelptext)
    sys.exit(-1)
else:
    print(goodhelptext)

from pprint import pformat


class TestLab05Conteggiovocali(unittest.TestCase):

    def errormsg(self,text,expected,result):
        if len(text)==0:
            messaggio = """

MOTIVO DEL FALLIMENTO:
    Le vocali nella stringa vuota sono {1}, e invece il programma 
    restituisce {2}"""
        else:
            messaggio = """

MOTIVO DEL FALLIMENTO:
    Le vocali nella stringa
    '{0}'
    sono {1}, e invece il programma restituisce {2}"""
        messaggio = messaggio.format(text,expected,result)
        return messaggio
    
    def test_stringa_vuota(self):
        text=''
        expected=0
        result=conteggiovocali(text)
        msg=self.errormsg(text,expected,result)
        self.assertEqual(expected,result,msg=msg)
    
    def test_stringa_rana(self):
        text='La rana in spagna'
        expected=6
        result=conteggiovocali(text)
        msg=self.errormsg(text,expected,result)
        self.assertEqual(expected,result,msg=msg)

    def test_maiuscoleminuscole(self):
        text='A quanto pare Anna ed Enrico non verranno a Imola.'
        expected=20
        result=conteggiovocali(text)
        msg=self.errormsg(text,expected,result)
        self.assertEqual(expected,result,msg=msg)

    def test_contare_tutte(self):
        text='AEIOUaeiouàèìòùÀÈÌÒÙ'
        expected=20
        result=conteggiovocali(text)
        msg=self.errormsg(text,expected,result)
        self.assertEqual(expected,result,msg=msg)

    def test_consonanti(self):
        text='fdhjkfhryrh'
        expected=0
        result=conteggiovocali(text)
        msg=self.errormsg(text,expected,result)
        self.assertEqual(expected,result,msg=msg)


    def test_conteggiovocali_strighe(self):
        data=1000
        messaggio = """

MOTIVO DEL FALLIMENTO:
    La funzione conteggiovocali su input {0} dovrebbe sollevare
    'TypeError' perché accetta solo stringhe come argomenti."""
        messaggio = messaggio.format(repr(data))
        with self.assertRaises(TypeError,msg=messaggio):
            conteggiovocali(data)

        
class TestLab05Triangoli(unittest.TestCase):

    zero    =''
    uno     ="*"
    due     =" *\n**"
    tre     ="  *\n **\n***"
    quattro ="   *\n  **\n ***\n****"
    cinque  ="    *\n   **\n  ***\n ****\n*****"
    
    def errormsg(self,h,expected,result):
        messaggio = """

MOTIVO DEL FALLIMENTO:
    Il trinagolo di altezza {0} sarebbe 
{1}
    e non
{2}"""
        messaggio = messaggio.format(h,expected,result)
        return messaggio

    def test_altezza_zero(self):
        h=0
        expected=self.zero
        disegno=triangolo(h)
        msg=self.errormsg(h,'la stringa vuota \'\'',disegno)
        self.assertEqual(expected,disegno,msg=msg)

    def test_altezza_uno(self):
        h=1
        expected=self.uno
        disegno=triangolo(h)
        msg=self.errormsg(h,expected,disegno)
        self.assertEqual(expected,disegno,msg=msg)
    
    def test_altezza_due(self):
        h=2
        expected=self.due
        disegno=triangolo(h)
        msg=self.errormsg(h,expected,disegno)
        self.assertEqual(expected,disegno,msg=msg)
    
    def test_altezza_tre(self):
        h=3
        expected=self.tre
        disegno=triangolo(h)
        msg=self.errormsg(h,expected,disegno)
        self.assertEqual(expected,disegno,msg=msg)
    
    def test_altezza_quattro(self):
        h=4
        expected=self.quattro
        disegno=triangolo(h)
        msg=self.errormsg(h,expected,disegno)
        self.assertEqual(expected,disegno,msg=msg)
    
    def test_altezza_cinque(self):
        h=5
        expected=self.cinque
        disegno=triangolo(h)
        msg=self.errormsg(h,expected,disegno)
        self.assertEqual(expected,disegno,msg=msg)

    def test_triangolo_stringa(self):
        data='gatto'
        messaggio = """

MOTIVO DEL FALLIMENTO:
    La funzione triangolo su input {0} dovrebbe sollevare
    'TypeError' perché accetta solo interi non negativi come argomenti."""
        messaggio = messaggio.format(repr(data))
        with self.assertRaises(TypeError,msg=messaggio):
            triangolo(data)

    def test_triangolo_float(self):
        data=2.3
        messaggio = """

MOTIVO DEL FALLIMENTO:
    La funzione triangolo su input {0} dovrebbe sollevare
    'TypeError' perché accetta solo interi non negativi come argomenti."""
        messaggio = messaggio.format(repr(data))
        with self.assertRaises(TypeError,msg=messaggio):
            triangolo(data)

    def test_triangolo_negativo(self):
        data=-10
        messaggio = """

MOTIVO DEL FALLIMENTO:
    La funzione triangolo su input {0} dovrebbe sollevare
    'ValueError' perché accetta solo interi non negativi come argomenti."""
        messaggio = messaggio.format(repr(data))
        with self.assertRaises(ValueError,msg=messaggio):
            triangolo(data)


            
class TestLab05TernePitagoriche(unittest.TestCase):
    
    def errormsg(self,N,expected,result):
        messaggio = """

MOTIVO DEL FALLIMENTO:
    Le terne pitagoriche fino a {0} sono {1} ma il programma ne conta {2}."""
        messaggio = messaggio.format(N,expected,result)
        return messaggio

    def test_fino_a_1(self):
        N=1
        expected=0
        result=ternepitagoriche(N)
        msg=self.errormsg(N,expected,result)
        self.assertEqual(expected,result,msg=msg)

    def test_fino_a_3(self):
        N=3
        expected=0
        result=ternepitagoriche(N)
        msg=self.errormsg(N,expected,result)
        self.assertEqual(expected,result,msg=msg)

    def test_fino_a_5(self):
        N=5
        expected=1
        result=ternepitagoriche(N)
        msg=self.errormsg(N,expected,result)
        self.assertEqual(expected,result,msg=msg)

    def test_fino_a_10(self):
        N=10
        expected=2
        result=ternepitagoriche(N)
        msg=self.errormsg(N,expected,result)
        self.assertEqual(expected,result,msg=msg)

    def test_fino_a_15(self):
        N=15
        expected=4
        result=ternepitagoriche(N)
        msg=self.errormsg(N,expected,result)
        self.assertEqual(expected,result,msg=msg)

    def test_fino_a_20(self):
        N=20
        expected=6
        result=ternepitagoriche(N)
        msg=self.errormsg(N,expected,result)
        self.assertEqual(expected,result,msg=msg)

    def test_fino_a_30(self):
        N=30
        expected=11
        result=ternepitagoriche(N)
        msg=self.errormsg(N,expected,result)
        self.assertEqual(expected,result,msg=msg)

    def test_fino_a_40(self):
        N=40
        expected=16
        result=ternepitagoriche(N)
        msg=self.errormsg(N,expected,result)
        self.assertEqual(expected,result,msg=msg)

    def test_fino_a_50(self):
        N=50
        expected=20
        result=ternepitagoriche(N)
        msg=self.errormsg(N,expected,result)
        self.assertEqual(expected,result,msg=msg)


    def test_triple1_stringa(self):
        data='gatto'
        messaggio = """

MOTIVO DEL FALLIMENTO:
    La funzione ternepitagoriche su input {0} dovrebbe sollevare
    'TypeError' perché accetta solo interi come argomenti."""
        messaggio = messaggio.format(repr(data))
        with self.assertRaises(TypeError,msg=messaggio):
            ternepitagoriche(data)

    def test_triple1_stringa(self):
        data=1.3
        messaggio = """

MOTIVO DEL FALLIMENTO:
    La funzione ternepitagoriche su input {0} dovrebbe sollevare
    'TypeError' perché accetta solo interi come argomenti."""
        messaggio = messaggio.format(repr(data))
        with self.assertRaises(TypeError,msg=messaggio):
            ternepitagoriche(data)

        
class TestLab05TernePitagoriche2(unittest.TestCase):

    def errormsg(self,N,expected,result):
        messaggio = """

MOTIVO DEL FALLIMENTO:
    Le terne pitagoriche (senza divisori comuni) fino a {0} 
    sono {1} ma il programma ne conta {2}."""
        messaggio = messaggio.format(N,expected,result)
        return messaggio

    def test_fino_a_1(self):
        N=1
        expected=0
        result=ternepitagoriche2(N)
        msg=self.errormsg(N,expected,result)
        self.assertEqual(expected,result,msg=msg)

    def test_fino_a_3(self):
        N=3
        expected=0
        result=ternepitagoriche2(N)
        msg=self.errormsg(N,expected,result)
        self.assertEqual(expected,result,msg=msg)

    def test_fino_a_5(self):
        N=5
        expected=1
        result=ternepitagoriche2(N)
        msg=self.errormsg(N,expected,result)
        self.assertEqual(expected,result,msg=msg)

    def test_fino_a_10(self):
        N=10
        expected=1
        result=ternepitagoriche2(N)
        msg=self.errormsg(N,expected,result)
        self.assertEqual(expected,result,msg=msg)

    def test_fino_a_15(self):
        N=15
        expected=2
        result=ternepitagoriche2(N)
        msg=self.errormsg(N,expected,result)
        self.assertEqual(expected,result,msg=msg)

    def test_fino_a_20(self):
        N=20
        expected=3
        result=ternepitagoriche2(N)
        msg=self.errormsg(N,expected,result)
        self.assertEqual(expected,result,msg=msg)

    def test_fino_a_30(self):
        N=30
        expected=5
        result=ternepitagoriche2(N)
        msg=self.errormsg(N,expected,result)
        self.assertEqual(expected,result,msg=msg)

    def test_fino_a_40(self):
        N=40
        expected=6
        result=ternepitagoriche2(N)
        msg=self.errormsg(N,expected,result)
        self.assertEqual(expected,result,msg=msg)

    def test_fino_a_50(self):
        N=50
        expected=7
        result=ternepitagoriche2(N)
        msg=self.errormsg(N,expected,result)
        self.assertEqual(expected,result,msg=msg)

    def test_terne2_stringa(self):
        data='gatto'
        messaggio = """

MOTIVO DEL FALLIMENTO:
    La funzione ternepitagoriche2 su input {0} dovrebbe sollevare
    'TypeError' perché accetta solo interi come argomenti."""
        messaggio = messaggio.format(repr(data))
        with self.assertRaises(TypeError,msg=messaggio):
            ternepitagoriche2(data)

    def test_terne2_stringa(self):
        data=1.3
        messaggio = """

MOTIVO DEL FALLIMENTO:
    La funzione ternepitagoriche2 su input {0} dovrebbe sollevare
    'TypeError' perché accetta solo interi come argomenti."""
        messaggio = messaggio.format(repr(data))
        with self.assertRaises(TypeError,msg=messaggio):
            ternepitagoriche2(data)

        
if __name__ == '__main__':
    unittest.main()
                              

    
