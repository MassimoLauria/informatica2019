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
import textwrap
from collections import namedtuple
from copy import deepcopy


class TcUndef:
    pass


Testcase = namedtuple(
    'Testcase', " name fname input "
    " result error inplace "
    " explanation")
Testcase.__new__.__defaults__ = (TcUndef, ) * len(Testcase._fields)

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
        print(
            "ERRORE NEL FILE DI TEST: il nome del file delle soluzioni non è valido."
        )
        sys.exit(-1)

    if isinstance(functions, str):
        functions = [functions]

    for s in functions:
        if not isinstance(s, str):
            print(
                "ERRORE NEL FILE DI TEST: il nome del file delle soluzioni non è valido."
            )
            sys.exit(-1)

    # Stampa un'intestazione che descrive l'esercizio
    lista_delle_funzioni = "\n".join("  - " + f for f in functions)
    print(
        headertext.format(anno='2019/2020',
                          file=filename_woext,
                          functions=lista_delle_funzioni))

    errori_preliminari = False  # il file ha la giusta struttura?

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
                msg = "    Esercizio mancante: la funzione {1} non è presente nel file {0}.py".format(
                    filename_woext, f_name)
                print(msg)
                errori_preliminari = True
            else:
                msg = "    Esercizio trovato: la funzione {1} è presente in file {0}.py".format(
                    filename_woext, f_name)
                print(msg)

            globals().update(f_objects)

    if errori_preliminari:
        print(badhelptext)
        sys.exit(-1)
    else:
        print(goodhelptext)


def error_msg(testcase, computed=TcUndef, backup=TcUndef):
    messaggio1 = """

MOTIVO DEL FALLIMENTO del test '{0}' per la funzione '{1}':""".format(
        testcase.name, testcase.fname)

    def C(x):
        if isinstance(x, str):
            return repr(x)
        else:
            return str(x)

    def print_params(params):
        res = '\n'.join('{}) {}'.format(i, C(x))
                        for i, x in enumerate(params, start=1))
        return textwrap.indent(res, '    ')

    if testcase.result is not TcUndef:
        messaggio2 = "PARAMETRI:\n{0}\n\n" \
                     "RISULTATO CORRETTO:{1}\n" \
                     "RISULTATO OTTENUTO:{2}\n".format(print_params(testcase.input),
                                                     C(testcase.result),
                                                     C(computed))

    elif testcase.inplace is not TcUndef:
        messaggio2 = """
    La funzione doveva modificare l'input {0} in {1}, e 
    invece ha prodotto {2}""".format(repr(backup), repr(testcase.inplace),
                                     repr(testcase.input))

    elif testcase.error is not TcUndef:
        messaggio2 = """
    La funzione sui parametri {} dovrebbe sollevare '{}'""".format(
            repr(testcase.input), str(testcase.error))

    else:
        raise ValueError(
            "Il test {} non contiene né 'error', né 'result', né 'inplace'".
            format(testcase.name))

    if testcase.explanation is TcUndef:
        messaggio3 = ''
    else:
        messaggio3 = "\nNOTA: {}".format(testcase.explanation)

    m = textwrap.indent(messaggio2 + messaggio3, '   ')
    return messaggio1 + "\n" + m


def generate_test_function(testcase):

    if testcase.fname is TcUndef:
        raise AttributeError("'{}' non contiene il campo 'fname', "
                             "che è necessario.".format(testcase.name))

    if testcase.input is TcUndef:
        raise AttributeError(
            "'{}' non contiene il campo 'input', che è necessario.".format(
                testcase.name))

    # Checking that only one field among 'result', 'error', 'inplace'
    # is defined.
    behaviours = 0
    if testcase.result is not TcUndef:
        behaviours += 1
    if testcase.error is not TcUndef:
        behaviours += 1
    if testcase.inplace is not TcUndef:
        behaviours += 1

    if behaviours != 1:
        raise AttributeError("'{}' deve avere esattamente un campo tra "
                             "'result', 'error', 'inplace'.".format(
                                 testcase.name))

    if testcase.result is not TcUndef:
        # Test whether result is correct
        def tmp_test_function(self):

            func = globals()[testcase.fname]
            computed = func(*testcase.input)  # executes the test
            msg = error_msg(testcase, computed)

            if testcase.result is None:
                self.assertIsNone(computed, msg=msg)
            else:
                self.assertEqual(testcase.result, computed, msg=msg)

    elif testcase.inplace is not TcUndef:
        # Test whether input was modified appropriately
        def tmp_test_function(self):

            func = globals()[testcase.fname]
            input_backup = deepcopy(testcase.input)
            func(*testcase.input)  # executes the test
            msg = error_msg(testcase, backup=input_backup)

            self.assertEqual(testcase.inplace, testcase.input, msg=msg)

    elif testcase.error is not TcUndef:
        # Test for error signaling
        def tmp_test_function(self):

            func = globals()[testcase.fname]
            msg = error_msg(testcase)

            with self.assertRaises(testcase.error, msg=msg):
                func(*testcase.input)  # executes the test
    else:
        raise RuntimeError("'{}' non saremmo dovuti arrivare qui!!!".format(
            testcase.name))

    return tmp_test_function


def set_default_fname(testcases, fname):
    """Imposta ``fname'' come nome della funzione, quando questo non è già presente."""
    for i in range(len(testcases)):
        tc = testcases[i]
        if tc.fname is TcUndef:
            testcases[i] = tc._replace(fname=fname)


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
            if testcase.name is TcUndef:
                raise AttributeError(
                    "il test non contiene il campo 'name', che è necessario".
                    format(i))

            test_name = 'test_' + "".join(testcase.name.split())
            if hasattr(testclass, test_name):
                raise ValueError("nome del metodo di test '{}' "
                                 "è duplicato nella classe '{}'".format(
                                     test_name, testclass.__name__))

            setattr(testclass, test_name, generate_test_function(testcase))

        except (ValueError, AttributeError) as err:
            errori_nei_test.append((i, err))

    if len(errori_nei_test) > 0:
        print("ERRORE NEI CASI DI TEST:")
        for i, err in errori_nei_test:
            print("  [{}] - {}".format(i, err))
        sys.exit(-1)


# ------------------------- INIZIA A SCRIVERE QUI --------------------------

# Struttura dati 'Testcase' per i casi di test
#
#   name    - nome del test
#   fname   - nome della funzione da testare (opzionale, vedi sotto)
#   input   - tupla contenente gli argomenti della funzione per il test
#   result  - valore atteso
#   error   - errore atteso
#   inplace - modifica attesa dell'input
#   explanation - spiegazione dell'errore (opzionale)
#
#   REQUISITI:
#       - 'name' e 'input' sono campi necessari;
#       - 'fname' è necessario se non settato con 'set_default_fname'
#       - deve essere presente esattamente uno 'result', 'error', e 'inplace';
#       - non ci possono essere due test con nomi uguali (a meno di spazi).

esercizio_file = 'lab11bordo'
esercizio_funzione = 'bordo_zero'

casi_di_test = [
    Testcase(name="esempio 1x1 pos", input=([[0]], ), result=True),
    Testcase(name="esempio 1x1 neg", input=([[1]], ), result=False),
    Testcase(name="esempio 1x3 pos", input=([[0, 0, 0]], ), result=True),
    Testcase(name="esempio 1x3 neg", input=([[0, 0, 1]], ), result=False),
    Testcase(name="esempio 3x1 pos", input=([[0], [0], [0]], ), result=True),
    Testcase(name="esempio 3x1 neg", input=([[0], [0], [1]], ), result=False),
    Testcase(name="esempio 2x2 pos", input=([[0, 0], [0, 0]], ), result=True),
    Testcase(name="esempio 2x2 neg", input=([[0, 0], [1, 0]], ), result=False),
    # Un po' più grandi
    Testcase(name="esempio 4x2 pos",
             input=([[0, 0], [0, 0], [0, 0], [0, 0]], ),
             result=True),
    Testcase(name="esempio 4x2 neg",
             input=([[0, 0], [0, 1], [2, 0], [0, 0]], ),
             result=False),
    Testcase(name="esempio 2x4 pos",
             input=([[0, 0, 0, 0], [0, 0, 0, 0]], ),
             result=True),
    Testcase(name="esempio 2x4 neg",
             input=([[0, 0, 0, 0], [0, 0, -1, 0]], ),
             result=False),
    Testcase(name="esempio 3x5 pos",
             input=([[0, 0, 0, 0, 0], [0, 3, -1, 0, 0], [0, 0, 0, 0, 0]], ),
             result=True),
    Testcase(name="esempio 3x5 neg",
             input=([[0, 0, 0, 0, 0], [-5, 3, -1, 1, 2], [4, 1, -3, 0, 0]], ),
             result=False),
    Testcase(name="esempio 5x6 pos",
             input=([[0, 0, 0, 0, 0, 0], [0, 1, 1, 1, 1,
                                          0], [0, 1, 1, 1, 1, 0],
                     [0, 1, 1, 1, 1, 0], [0, 0, 0, 0, 0, 0]], ),
             result=True),
    Testcase(name="esempio 5x6 neg T",
             input=([[0, 1, 1, 1, 1, 0], [0, 1, 1, 1, 1,
                                          0], [0, 1, 1, 1, 1, 0],
                     [0, 1, 1, 1, 1, 0], [0, 0, 0, 0, 0, 0]], ),
             result=False),
    Testcase(name="esempio 5x6 neg R",
             input=([[0, 0, 0, 0, 0, 0], [0, 1, 1, 1, 1,
                                          1], [0, 1, 1, 1, 1, 1],
                     [0, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0]], ),
             result=False),
    Testcase(name="esempio 5x6 neg B",
             input=([[0, 0, 0, 0, 0, 0], [0, 1, 1, 1, 1,
                                          0], [0, 1, 1, 1, 1, 0],
                     [0, 1, 1, 1, 1, 0], [0, 1, 1, 1, 1, 0]], ),
             result=False),
    Testcase(name="esempio 5x6 pos L",
             input=([[0, 0, 0, 0, 0, 0], [1, 1, 1, 1, 1,
                                          0], [1, 1, 1, 1, 1, 0],
                     [1, 1, 1, 1, 1, 0], [0, 0, 0, 0, 0, 0]], ),
             result=False),
    Testcase(name="esempio 4x4 pos",
             input=([[0, 0, 0, 0], [0, 7, 8, 0], [0, -1, 5, 0], [0, 0, 0,
                                                                 0]], ),
             result=True)
]


class TestLabInformatica(unittest.TestCase):
    pass


if __name__ == '__main__':

    # Inseriamo il nome della funzione di default, quando non presente
    set_default_fname(casi_di_test, esercizio_funzione)

    # Gli errori generati qui sono colpa del docente
    populate_test_class(TestLabInformatica, casi_di_test)

    # Importa le soluzioni degli studenti e segnala eventuali problemi
    load_solution_file(esercizio_file, esercizio_funzione)

    # Testa le soluzioni degli studenti e segnala eventuali errori
    unittest.main()
