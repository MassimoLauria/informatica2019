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
    """Carica il file delle soluzioni

    Importa il modulo `filename_woext`, assumendo che sia nella
    cartella corrente, e da esse carica le funzioni elencate
    `functions` nel global namespace.

    Parameters
    ----------
    filename_woext : str
        Nome del modulo da caricare (senza estensione .py)

    functions: str or list(str)
        Lista di nomi di funzione da caricare nel modulo.
        Se l'argomento non è una lista ma una stringa, viene
        interpretata come una lista che contiene quel nome come
        unico elemento.

    """
    if not isinstance(filename_woext, str):
       print("ERRORE NEL FILE DI TEST: il nome del file delle soluzioni non è valido.")
       sys.exit(-1)

    if isinstance(functions,str):
        functions = [functions]

    for s in functions:
        if not isinstance(s, str):
            print("ERRORE NEL FILE DI TEST: il nome del file delle soluzioni non è valido.")
            sys.exit(-1)


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
        raise ValueError("Il test {} non contiene né il campo 'error' né il campo 'result'".format(testcase.name))

    if testcase.explanation is None:
        messaggio3 = ''
    else:
        messaggio3 = ", perché {}".format(testcase.explanation)

    return messaggio1+messaggio2+messaggio3


def generate_test_function(testcase, default_fname=None):

    if testcase.fname is not None:
        fname = testcase.fname
    elif default_fname is not None:
        fname = default_fname
    else:
        raise AttributeError("'{}' non contiene il campo 'fname', "
                             "né è specificato un valore predefinito.".format(testcase.name))

    if testcase.input is None:
        raise AttributeError("'{}' non contiene il campo 'input', che è necessario.".format(testcase.name))

    if testcase.result is not None and testcase.error is not None:
        raise AttributeError("'{}' contiene sia il campo 'result', sia il campo 'error'.".format(testcase.name))

    if testcase.result is not None:
        # Creation of the test method for computation
        def tmp_test_function(self):

            func = globals()[fname]

            computed = func(*testcase.input)   # executes the test

            msg = error_msg(testcase, computed)

            self.assertEqual(testcase.result, computed, msg=msg)

    elif testcase.error is not None:
        # Creation of the test method for error signaling
        def tmp_test_function(self):

            func = globals()[fname]
            msg = error_msg(testcase)

            with self.assertRaises(testcase.error, msg=msg):
                func(*testcase.input)   # executes the test
    else:
        raise ValueError("'{}' non contiene né il campo 'error' né il campo 'result'".format(testcase.name))

    return tmp_test_function


def populate_test_class(testclass, testcases, default_fname=None):
    """Aggiunge ad una classe un metodo per ogni test

    La suite di test di unità di Python esegue i test che
    corrispondono ai metodi test_* trovati nelle classi che ereditano
    da `unittest.TestCase`.

    Questa funzione converte una sequenza di record che rappresenta
    una batteria di test in metodi di di una classe.

    Parameters
    ----------
    testclass : class
        La classe su cui vengono caricati i metodi.

    testcases: list(Testcase)
        Lista dei casi di test da caricare.

    default_fname: str
        funzione da testare, quando non specificata dai casi di test.
        Se un caso di test non specifica il nome della funzione da
        testare, viene usato invece il nome predefinito. Se né il test
        né questo parametro indicano un nome di funzione, viene
        sollevato errore. (default: None)
    """

    errori_nei_test = []

    for i, testcase in enumerate(testcases, start=1):

        try:
            if testcase.name is None:
                raise AttributeError("il test non contiene il campo 'name', che è necessario".format(i))

            test_name = 'test_' + "".join(testcase.name.split())
            if hasattr(testclass, test_name):
                raise ValueError("nome del metodo di test '{}'" \
                                 " è duplicato nella classe '{}'".format(test_name, testclass.__name__))

            setattr(testclass,
                    test_name,
                    generate_test_function(testcase, default_fname=default_fname))

        except (ValueError, AttributeError) as err:
            errori_nei_test.append((i,err))

    if len(errori_nei_test)>0:
        print("ERRORE NEI CASI DI TEST:")
        for i,err in errori_nei_test:
            print("  [{}] - {}".format(i,err))
        sys.exit(-1)

# ------------------------- INIZIA A SCRIVERE QUI --------------------------

# Struttura dati 'Testcase' per i casi di test
#
#   name   - nome del test
#   fname  - nome della funzione da testare (opzionale, vedi sotto)
#   input  - tupla contenente gli argomenti della funzione per il test
#   result - valore atteso
#   error  - errore atteso
#   explanation - spiegazione dell'errore (opzionale)
#
#   REQUISITI:
#       - 'name' e 'input' sono campi necessari;
#       - 'fname' è necessario se non viene fornito un default in 'populate_test_class'
#       - deve essere presente esattamente uno dei campi 'result' e 'error';
#       - non ci possono essere due test con nomi uguali (a meno di spazi).


esercizio_file = 'lab09righecrescenti'
esercizio_funzione = 'num_righe_crescenti'

casi_di_test = [
    Testcase(name="nessuna riga",  input=([]), error=TypeError,
             explanation="la matrice deve avere almeno una riga"),

    Testcase(name="primo elemento non lista",
             input=([56, [3, 5, "pippo", 8, 6], [3]]),
             error=TypeError,
             explanation="il primo elemento della lista non è una lista"),

    Testcase(name="un elemento non lista",
             input=([[56], "pluto", [3]]),
             error=TypeError,
             explanation="un elemento della lista non è una lista"),
             
    Testcase(name="nessuna riga crescente", input=([[3,4,6,1], [2,8,3,4]],), result=0),

    Testcase(name="alcune righe negative", input=([[3,4,5,8,17], [1,2,3,4,10], [-5,-4,-3,-2,-1]],), result=3),

    Testcase(name="alcune righe non  strettamente crescenti", input=([[3,4,5,5,17], [1,2,3,4,4], [8, 4, -4, 6, 7], [10,20,30,40,50]],), result=1),

    Testcase(name="una colonna", input=([[6], [6], [8], [1]],), result=4),

    Testcase(name="due colonne", input=([[6,8], [6,10], [-4,-2], [0,1], [-5,-1], [8,-4]],), result=5)
]


class TestLabInformatica(unittest.TestCase):
    pass


if __name__ == '__main__':

    # Gli errori generati qui sono colpa del docente
    populate_test_class(TestLabInformatica,
                        casi_di_test,
                        default_fname=esercizio_funzione)

    # Importa le soluzioni degli studenti e segnala eventuali problemi
    load_solution_file(esercizio_file, esercizio_funzione)

    # Testa le soluzioni degli studenti e segnala eventuali errori
    unittest.main()
