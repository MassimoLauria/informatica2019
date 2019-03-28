#!/usr/bin/env python3

"""Test preliminari per l'homework di Informatica@SEFA 2017/2019

Questo file contiene i test preliminari per il compito di
programmazione del corso di Informatica@SEFA dell'anno 2018/2019
disponibile all'indirizzo

   http://massimolauria.net/courses/infosefa2018/docs/esercizio2018.pdf

Questi test verificano che le soluzioni del compito siano state
impostate correttamente, ma il fatto di passare questi test non
garantisce in alcun modo che le soluzioni siano
effettivamente corrette.

"""


import importlib
import unittest
import sys
import os




ex_name      ='esercizio2018'
ex_functions =[
    "inverti","cesare",
    "isbooleansquare","isbooleanqueen","isqueen",
    "conteggiotesto","conteggiofile",
    "query1","query2","query3"
]

ex_dataset=['holmes.txt',
            'chinook_db.sqlite',
            'registro_automobilistico_db.sqlite']



# Importa le soluzioni degli esercizi
lab=None
try:
    lab=importlib.__import__(ex_name)
except Exception:
    msg="""ERROR: Problema col file {0}.py. Forse
    -- forse non è presente in questa cartella
    -- oppure contiene errori che non lo rendono eseguibile
    
    Prova ad eseguire '$ python3 {0}.py'""".format(ex_name)
    print(msg,file=sys.stderr)
    sys.exit(-1)

f_objects={}
for f_name in ex_functions:
    try:
        f_object = lab.__dict__[f_name]
        f_objects[f_name] = f_object
    except KeyError:
        msg="ESERCIZIO MANCANTE: Funzione {1} non presente in file {0}.py".format(ex_name,f_name)
        print(msg,file=sys.stderr)

# Caricale nel namespace
globals().update(f_objects)


# Controlla che ci siano tutti i file di dati per eseguire i test
for fn in ex_dataset:
    file_missing=False
    try:
        f=open(fn,'r')
    except FileNotFoundError:
        file_missing = True
        print("Manca il file {}".format(fn),file=sys.stderr)
if file_missing:
    print("Non posso eseguire i test: mancano alcuni file di dati.",file=sys.stderr)
    sys.exit(-1)


from pprint import pformat

class TestBase(unittest.TestCase):

    def verifyValue(self,
                    func,args,
                    expected=None,
                    postprocess=None,
                    message=None):

        result=func(*args)
        if postprocess is not None:
            result=postprocess(result)
        
        messaggio_errore = '''

PROBLEMA> La computazione

{0}({1})

produce

{2}

quando invece dovrebbe produrre:

{3}
'''
        if message is None:
            message = messaggio_errore
   
        message = message.format(func.__name__,
                                  ", ".join(repr(x) for x in args),
                                  pformat(result),
                                  pformat(expected))
        self.assertEqual(expected,result,msg=message)

    def verifyError(self,
                    func,args,
                    error,
                    reason=None,
                    message=None):

        
        messaggio_errore = '''

PROBLEMA> La computazione

{0}({1})

non solleva {2} come ci si aspetterebbe.
{3}        
'''
        if message is None:
            message = messaggio_errore
        if reason is None:
            reason =""
            
        message = message.format(func.__name__,
                                 ", ".join(repr(x) for x in args),
                                 error,
                                 reason)

        with self.assertRaises(error,msg=message):
            func(*args)






# Test Parte Stringhe

class TestParteStringhe(TestBase):

    def test_invertierror(self):
        self.verifyError(inverti,[5],TypeError)

    def test_invertierror2(self):
        self.verifyError(inverti,[['aa','bb']],TypeError)
    
    def test_invertiex1(self):
        self.verifyValue(inverti,['abcdef'],expected='fedcba')

    def test_invertiex2(self):
        self.verifyValue(inverti,['123456789 abcdefghi'],expected='ihgfedcba 987654321')

    def test_invertiex3(self):
        self.verifyValue(inverti,[''],expected='')

    def test_invertiex4(self):
        self.verifyValue(inverti,['abacaba'],expected='abacaba')

    def test_cesareex1(self):
        self.verifyValue(cesare,("abcdefghijklmnopqrstuvwxyz",5),  expected="fghijklmnopqrstuvwxyzabcde")
    def test_cesareex2(self):
        self.verifyValue(cesare,("abcdefghijklmnopqrstuvwxyz",13), expected="nopqrstuvwxyzabcdefghijklm")
    def test_cesareex3(self):
        self.verifyValue(cesare,("abcdefghijklmnopqrstuvwxyz",0),  expected="abcdefghijklmnopqrstuvwxyz")
    def test_cesareex4(self):
        self.verifyValue(cesare,("abcdefghij 1234567890 ;/?/.<>àèéìòù ABCDEFGHIJ",7),  expected="hijklmnopq 1234567890 ;/?/.<>àèéìòù HIJKLMNOPQ" )
    def test_cesareex5(self):
        self.verifyValue(cesare,("abcdefghij 1234567890 ;/?/.<>àèéìòù ABCDEFGHIJ",19), expected="tuvwxyzabc 1234567890 ;/?/.<>àèéìòù TUVWXYZABC" )
    def test_cesareex6(self):
        self.verifyValue(cesare,("abcdefghij 1234567890 ;/?/.<>àèéìòù ABCDEFGHIJ",-1), expected="zabcdefghi 1234567890 ;/?/.<>àèéìòù ZABCDEFGHI" )

    def test_cesarechain(self):
        text= '''

PROBLEMA> La computazione

cesare(cesare(cesare({1},3),-5),2)

produce

{2}

quando invece dovrebbe produrre:

{3}
'''
        stringa='ksahfeghfjsagf'
        def cesarechain(stringa):
            return cesare(cesare(cesare(stringa,3),-5),2)
        self.verifyValue(cesarechain,(stringa,),
                         expected=stringa,
                         message=text)
 
 
# Test Parte Regine
class TestParteRegine(TestBase):


    def test_bsquare_small(self):
        self.verifyValue(isbooleansquare,([[True]],),expected=True)
        
    def test_bsquare_empty(self):
        self.verifyValue(isbooleansquare,([],),expected=False)

    def test_bsquare_positive(self):
        m=[[False,False,False,True ],
           [False,True, False,False],
           [False,False,False,False],
           [True ,False,False,False]]
        self.verifyValue(isbooleansquare,[m],expected=True)
            
    def test_bsquare_notsquared(self):
        m=[[False,True, False,False],
           [False,False,False,False],
           [True ,False,False,False]]
        self.verifyValue(isbooleansquare,[m],expected=False)

    def test_bsquare_notmatrix(self):
        m=[[False,True,False],
           [False,False],
           [True ,False,False]]
        self.verifyValue(isbooleansquare,[m],expected=False)

    def test_bsquare_notboolean(self):
        m=[[1,0,0],
           [0,0,1],
           [0,1,0]]
        self.verifyValue(isbooleansquare,[m],expected=False)

    def test_bsquare_invalid(self):
        self.verifyValue(isbooleansquare,["a matrix is not a matrix"],expected=False)


    def test_bqueen_invalid(self):
        self.verifyError(isbooleanqueen,["a matrix is not a matrix"],error=ValueError)

    def test_bqueen_notmatrix(self):
        m=[[False,True,False],
           [False,False],
           [True ,False,False]]
        self.verifyError(isbooleanqueen,[m],error=ValueError)


    def test_bqueen_small(self):
        self.verifyValue(isbooleanqueen,([[True]],),expected=True)

    def test_bqueen_true(self):
        M=[[False,False,False,True ],
           [False,True, False,False],
           [False,False,False,False],
           [False,False,True ,False]]
        self.verifyValue(isbooleanqueen,[M],expected=True)

    def test_bqueen_false(self):
        M=[[False,False,False,True ],
           [False,True, False,False],
           [False,False,False,False],
           [True ,False,False,False]]
        self.verifyValue(isbooleanqueen,[M],expected=False)


    def test_queen_bad(self):
        badone='''
        ...X
        ...   
        ....
        ..X.
        '''
        self.verifyError(isqueen,[badone],error=ValueError)

        
    def test_queen_ex1(self):
        ex1='''
        ...X
        .X..
        ....
        ..X.
        '''
        self.verifyValue(isqueen,[ex1],expected=True)

    def test_queen_ex2(self):
        ex2='''
        .X
        X.
        '''
        self.verifyValue(isqueen,[ex2],expected=False)
        
    def test_queen_ex3(self):
        ex3='''
        X......
        ..X....
        ....X..
        ......X
        .X.....
        ...X...
        .....X.
        '''
        self.verifyValue(isqueen,[ex3],expected=True)

    def test_queen_ex4(self):
        ex4='''
        X......
        ..X....
        ....X..
        .....X.
        .X.....
        ...X...
        ......X
        '''
        self.verifyValue(isqueen,[ex4],expected=False)
        
    def test_queen_ex5(self):
        ex5='''
        X....
        ..X..
        .....
        X....
        .X...
        '''
        self.verifyValue(isqueen,[ex5],expected=False)

# Test Parte Testo
class TestParteTesti(TestBase):


    def test_testo_ex1(self):
        self.verifyValue(conteggiotesto,('Casa caSa, casa gatto cane.',4),expected=2)

    def test_testo_ex2(self):
        self.verifyValue(conteggiotesto,('Casa caSa, casa gatto cane.',5),expected=1)

    def test_testo_ex3(self):
        self.verifyValue(conteggiotesto,('Casa caSa, casa gatto cane.',-3),expected=0)

    def test_testo_ex4(self):
        self.verifyValue(conteggiotesto,("Quanta legna taglia un taglia-legna, se vuol tagliare legna.",5),expected=1)

    def test_nofile(self):
        self.verifyError(conteggiofile,("nonesiste.txt",5,'latin1'),
                         error=FileNotFoundError,reason="La funzione non si è accorta che il file nonesiste.txt non è presente.")
        
    def test_holmes1(self):
        self.verifyValue(conteggiofile,("holmes.txt", 5,'utf-8-sig'), expected = 1134)
        
    def test_holmes2(self):
        self.verifyValue(conteggiofile,("holmes.txt",12,'utf-8-sig'), expected = 154)

    def test_holmes3(self):
        self.verifyValue(conteggiofile,("holmes.txt",16,'utf-8-sig'), expected = 1)



            
# Test Parte SQL
class TestParteSQL(TestBase):

    def test_query1error(self):
        self.verifyError(query1,['1'],TypeError)

    
    def test_query1empty(self):
        self.verifyValue(query1,[0],expected=[])

    def test_query1ex1(self):
        self.verifyValue(query1,[3],[('Ford',), ('Honda',)])
        
    def test_query1ex2(self):
        self.verifyValue(query1,[4],[('Piaggio',), ('Toyota',), ('Volkswagen',)])
        
    def test_query2point(self):
        def apoint(res):
            return res[3][2]
        text='''

PROBLEMA> La data nella quarta riga ottenuta con

query2()

è

{2}

quando invece dovrebbe essere:

{3}
'''
        self.verifyValue(query2,[],
                         expected='1994/5/21',
                         postprocess=apoint,
                         message=text)

    def test_query2ex1(self):
        def three(res):
            return res[:3]
        text='''

PROBLEMA> Le prime tre righe ottenute con

query2()

sono

{2}

quando invece dovrebbero essere:

{3}
'''
        self.verifyValue(query2,[],
                         expected=[('Bernocchi', 'Giuseppina', '1990/9/16'),
                                   ('Giovanolla', 'Filippo', '1993/11/30'),
                                   ('Spoldi', 'Diego', '1994/2/29')],
                         postprocess=three,
                         message=text)

    
    def test_query3ex1(self):
        self.verifyValue(query3,(120,300),[('Iron Maiden', 213), ('U2', 135)])

    def test_query3ex2(self):
                text='''

PROBLEMA> Il numero delle righe in 

{0}({1})

è

{2}

quando invece dovrebbe essere:

{3}
'''
                self.verifyValue(query3,(7,10),
                                 expected=14,
                                 postprocess=len,
                                 message=text)

    def test_query3reverse(self):
        self.verifyValue(query3,[10,7],expected=[])
        
    def test_query3error1(self):
        self.verifyError(query3,['a',3],TypeError)

    def test_query3error2(self):
        self.verifyError(query3,[1,'b'],TypeError)


        
if __name__ == '__main__':
    unittest.main()
                              
