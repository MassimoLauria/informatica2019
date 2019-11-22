#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Copyright (C) 2019 by Massimo Lauria <massimo.lauria@uniroma1.it>

"""Test per gli esercizi di informatica

Questo è un template per costruire i test per gli esercizi e gli esami
del corso di informatica del Dipartimento di Scienze Statistiche.
"""

import importlib
import unittest
import sys
from collections import namedtuple

# Struttura dati per i casi di test
#
#   name   - nome del test
#   fname  - nome della funzione da testare
#   input  - tupla contenente gli argomenti della funzione per il test
#   result - valore atteso
#   error  - errore atteso
#   explanation - spiegazione dell'errore (opzionale)
#
#   almeno uno tra 'result' e 'error' deve essere non nullo.

Testcase = namedtuple('Testcase', 'name fname input result error explanation')
Testcase.__new__.__defaults__ = (None,) * len(Testcase._fields)

headertext = """
*********************************************************************
  Informatica {anno}

  Test per il programma: {file}.py
  Funzioni:
{functions}


RACCOMANDAZIONI:

anche se non capite tutte le informazioni prodotte da questo
programma, leggete quelle che capite perché vi possono aiutare nello
svolgimento degli esercizi.
"""

goodhelptext = """
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

badhelptext = """
ANNULLAMENTO DEI TEST AUTOMATICI:

Le verifiche automatiche non possono partire perché il file non
esiste, non è eseguibile, oppure non contiene tutte le soluzioni
degli esercizi.

Sistemate il file delle soluzioni e rieseguite i test.
**********************************************************************
"""


def load_solution_file(filename_woext, functions):

    # Stampa un'intestazione che descrive l'esercizio
    lista_delle_funzioni = "\n".join("  - "+f for f in functions)
    print(headertext.format(anno='2019/2020', file=filename_woext, functions=lista_delle_funzioni))


    errori_preliminari = False   # il file ha la giusta struttura?

    # Importa le soluzioni degli esercizi
    print("CONTROLLO PRELIMINARE DEL FILE {0}.py:".format(filename_woext))

    lab = None
    try:
        lab = importlib.__import__(filename_woext)
    except Exception:
        msg = """
        Problema a importare il file {0}.py:
        -- il file potrebbe non essere presente in questa cartella,
        -- oppure potrebbe contenere errori che lo rendono non eseguibile.

        Provate ad eseguire il comando 'python3 {0}.py' da terminale per
        avere più informazioni. """.format(filename_woext)
        print(msg)
        errori_preliminari = True
    else:
        # Carica nel namespace le funzioni definite
        f_objects = {}
        for f_name in functions:
            try:
                f_object = lab.__dict__[f_name]
                f_objects[f_name] = f_object
            except KeyError:
                msg = "    Esercizio mancante: la funzione {1} non è presente nel file {0}.py".format(filename_woext, f_name)
                print(msg)
                errori_preliminari = True
            else:
                msg = "    Esercizio trovato: la funzione {1} è presente in file {0}.py".format(filename_woext, f_name)
                print(msg)

            globals().update(f_objects)

    if errori_preliminari:
        print(badhelptext)
        sys.exit(-1)
    else:
        print(goodhelptext)



def error_msg(testcase, computed=None):
    messaggio1 = """

MOTIVO DEL FALLIMENTO del test '{0}' per la funzione '{1}':""".format(testcase.name, testcase.fname)

    if testcase.result is not None:
        messaggio2 = """
    Il risultato che è stato calcolato con i parametri {0} è {2}, mentre invece
    dovrebbe essere {1}""".format(repr(testcase.input), testcase.result, computed)

    elif testcase.error is not None:
        messaggio2 = """
    La funzione sui parametri {} dovrebbe sollevare '{}'""".format(repr(testcase.input), str(testcase.error))

    else:
        raise ValueError("Il test {} non contiene né il campo 'error' né il campo 'result'")

    if testcase.explanation is None:
        messaggio3 = ''
    else:
        messaggio3 = ", perché {}".format(testcase.explanation)

    return messaggio1+messaggio2+messaggio3


def generate_test_function(testcase):
    if testcase.result is not None:
        # Creation of the test method for computation
        def tmp_test_function(self):

            func = globals()[testcase.fname]

            computed = func(*testcase.input)   # executes the test

            msg = error_msg(testcase, computed)

            self.assertEqual(testcase.result, computed, msg=msg)

    elif testcase.error is not None:
        # Creation of the test method for error signaling
        def tmp_test_function(self):

            func = globals()[testcase.fname]
            msg = error_msg(testcase)

            with self.assertRaises(testcase.error, msg=msg):
                func(*testcase.input)   # executes the test
    else:
        raise ValueError("Il test {} non contiene né il campo 'error' né il campo 'result'")

    return tmp_test_function


def populate_test_class(testclass, testcases):
    for testcase in testcases:
        test_name = 'test_' + "".join(testcase.name.split())
        setattr(testclass, test_name, generate_test_function(testcase))


# ------------------------- INIZIA A SCRIVERE QUI --------------------------
class TestLab08SommaMat(unittest.TestCase):
    pass

somma_mat_tests = [
    Testcase(name="somma matrice 1 x 1", fname='somma_mat', input=([[3]], ), result=3),

    Testcase(name="somma matrice 3 x 2", fname='somma_mat', input=([[3, 1], [8, -2], [4, -5]],), result=9),

    Testcase(name="somma matrice 2 x 3", fname='somma_mat', input=([[3, 1, 5], [8, -2, -1]], ),  result=14),

    Testcase(name="lista non matrice",  fname='somma_mat', input=([3,4],), error=TypeError,
             explanation="una matrice è una lista di liste, non una lista di numeri"),

    Testcase(name="numero non matrice", fname='somma_mat', input=(4,),     error=TypeError,
             explanation="una matrice è una lista di liste, non un numero"),

    Testcase(name="matrice non numerica",
             fname='somma_mat',
             input=([[3, 5, 6], [3, "pippo", 6]],),
             error=TypeError,
             explanation="la matrice deve contenere solo numeri")
]


if __name__ == '__main__':

    load_solution_file('prova',['somma_mat'])

    populate_test_class(TestLab08SommaMat, somma_mat_tests)

    unittest.main()
