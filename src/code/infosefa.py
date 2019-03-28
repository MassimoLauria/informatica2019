#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Codice utile per le esercitazioni di Informatica@SEFA 2017/2018

Il modulo contiene alcune funzioni utili per le esercitazioni.
Verrà regolarmente esteso quindi controllate che non vi siano
aggiornamenti disponibili prima di usarlo.

Copyright (C) 2017  Massimo Lauria <massimo.lauria@uniroma1.it>
"""

   
import random

def numeriacaso(N,minimo,massimo,ordinati=False):
    """Produce una lista di numeri generati a caso.

    Produce una lista di N elementi, ognuno dei quali preso a caso
    (con uguale probabilità) tra tutti i numeri interi compresi tra
    'minimo' e 'massimo', estremi inclusi.

    Se N<0 o minimo>massimo la funzione solleva un ValueError.

    Se 'ordinati' è vero la lista restituita è ordinata.
    """
    if N<0:
        ValueError("Quantità negativa di numeri da generare.")
    if minimo>massimo:
        ValueError("L'intervallo dei valori non ha senso: minimo>massimo.")
    seq = [random.randint(minimo,massimo) for _ in range(N)]
    if ordinati:
        seq.sort()
    return seq

def bubblesort(seq):
    """Ordina la sequenza utilizzando bubblesort
    """
    end=len(seq)-1
    while end>0:
        last_swap = -1
        for i in range(0,end):
            if seq[i] > seq[i+1]:
                last_swap = i
                seq[i], seq[i+1] = seq[i+1],seq[i]
        end=last_swap


def argmin(seq,start,end):
    minimo = seq[start]
    indice = start
    for i in range(start+1,end+1):
        if seq[i] < minimo:
            minimo = seq[i]
            indice = i
    return minimo,indice

def insertionsort(seq):
    """Ordina la sequenza utilizzando insertionsort
    """    
    for i in range(0,len(seq)-1):
        
        val,pos = argmin(seq,i,len(seq)-1)
        
        for j in range(pos-1,i-1,-1):
            seq[j+1] = seq[j] 

        seq[i] = val

def merge(S,low,mid,high):
      a=low
      b=mid+1
      temp=[]
      # Inserisci in testa il più piccolo
      while a<=mid and b<=high:
          if S[a]<=S[b]:
              temp.append(S[a])
              a=a+1
          else:
              temp.append(S[b])
              b=b+1
      # Esattamente UNA sequenza è esaurita. Va aggiunta l'altra
      residuo = range(a,mid+1) if a<=mid else range(b,high+1)
      for i in residuo:
          temp.append(S[i])
      # Va tutto copiato su S[start:end+1]
      for i,value in enumerate(temp,start=low):
          S[i] = value


def mergesort(S,start=0,end=None):
    """Ordina la sequenza S[start:end+1] usando mergesort"""
    if end is None:
        end=len(S)-1
    if start>=end:
        return
    mid=(end+start)//2
    mergesort(S,start,mid)
    mergesort(S,mid+1,end)
    merge(S,start,mid,end)

def countingsort(seq,key=None):
    if len(seq)==0:
        return
    if key is None:
        key = lambda x:x
    # n operazioni
    a = min(key(x) for x in seq)
    b = max(key(x) for x in seq)
    # creazione dei contatori
    counter=[0]*(b-a+1)
    for x in seq:
        counter[key(x)-a] += 1
    # posizioni finali di memorizzazione
    posizioni=[0]*(b-a+1)
    for i in range(1,len(counter)):
        posizioni[i]=posizioni[i-1]+counter[i-1]
    # costruzione dell'output
    for x in seq[:]:
        seq[posizioni[key(x)-a]]=x
        posizioni[key(x)-a] += 1

def key0(x):
    return x & 255

def key1(x):
    return (x>>8) & 255

def key2(x):
    return (x>>16) & 255

def key3(x):
    return (x//(256*256*256)) & 255

def key10(x):
    return x & 65535

def key32(x):
    return (x>>16) & 65535

def radixsort4x8bit(seq):
    """Ordina una sequenza di numeri positivi di al massimo 32 bit
    """
    for my_key in [key0,key1,key2,key3]:
        countingsort(seq,key=my_key)

def radixsort2x16bit(seq):
    """Ordina una sequenza di numeri positivi di al massimo 32 bit
    """
    for my_key in [key10,key32]:
        countingsort(seq,key=my_key)


def ricerca_linee(nome_file,encoding,stringa):
    """Restituisce gli indici delle righe che contengono la stringa

    Cerca all'interno di nome_file, le righe che contengono 'stringa'
    e le restituisce.
    """
    with open(nome_file,encoding=encoding) as f:
        return [i for i,text in enumerate(f,start=1) if text.find(stringa)!=-1]
    
def ricerca(nome_file,encoding,stringa):
    """Mostra le linee del file che contengono la parola cercata
    """
    with open(nome_file,encoding=encoding) as f:
        for i,text in enumerate(f,start=1):
             if text.find(stringa)!=-1:
                 print("{: 4}: {}".format(i,text))
    

def gettxtfilenames():
    """Restituisce la lista dei nomi dei file *.txt nella cartella corrente
    """
    from os import listdir
    return [name for name in listdir() if name[-4:]=='.txt']


def conta_vocali(s):
    '''Conta le vocali non accentate in s'''
    s = s.lower()
    count = 0
    for v in 'aeiou':
        count += s.count(v)
    return count

def file_to_dict(name,enc):
    """Carica un dizionario da un file.

    Il file deve avere CHAIVE : INFO per ogni riga non vuota 
    """
    with open(name,encoding=enc,mode='r') as data:
        diz = {}
        for line in data.readlines():

            if len(line.strip())==0:
                continue
            
            l = line.split(":")
            if len(l) != 2:
                raise ValueError("Dati mal formattata da una riga non vuota")

            k,v = l[0].strip(),l[1].strip()
            diz[k] = v

        return diz


def words_in_str(s):
    """Restituisce la lista delle parole nella stringa

    Le parole sono tutte standardizzate al minuscolo
    """
    # trova i caratter non alfabetici
    noalpha=''
    for c in s:
        if not c.isalpha() and c not in noalpha:
            noalpha += c
    # sostituisce i caratteri non alfabetici con spazi
    for c in noalpha:
        s = s.replace(c,' ')
    return s.lower().split()

def words_in_file(fname,enc='utf-8'):
    """Restituisce la lista delle parole nella stringa

    Le parole sono tutte standardizzate al minuscolo
    """
    with open(fname,encoding=enc,mode='r') as data:
        return words_in_str(data.read())

def word_frequence(fname,ricerca,enc='utf-8'):
    """Restituisce un dizionario che a ogni parola nella lsita 'ricerca'
    associa la sua frequenza percentuale nel file 'fname', codificato
    in 'enc'
    """
    # lista delle parole nel file
    parole = words_in_file(fname,enc)

    frequenze = {}
    for word in ricerca:

        # la parola in 'word' occorre ... volte
        occorrenze = parole.count(word.lower())

        # percentuale, arrotondata
        freq = occorrenze*100 / len(parole)
        freq = round(freq,3)

        # memorizza nel dizionario
        frequenze[word] = freq

    return frequenze


def searchdocuments(fnames,ricerca,enc='utf-8'):
    """Ordina i file  in base al punteggio della ricerca
    
    Calcola la rilevanza di ogni file indicate, rispetto
    alla 'query' fatta
    
    """
    scores = []
    for fname in fnames:
        freqs = word_frequence(fname,ricerca,enc)
        score = round(sum(freqs.values()),3)
        scores.append((score,fname))
    scores.sort(reverse=True)
    for score,fname in scores:
        print(fname,score)
    


# Funzioni per il test
def testRisultato(nome,r_atteso,func,*args):
    """Verifica che func(*args) restituisca r_atteso

    Calcola func(*args) e verifica che il valore restituito sia uguale
    a r_accesso. Ad esempio func è la funzione sum, e args=[1,2,4,6],
    il test calcola sum(1,2,3,4).

    INPUT:
    - nome: nome del test
    - r_atteso: valore atteso dal test
    - func: funzione da testare
    - args: sequenza di argomenti da testare
    
    PRINT:
    Stampa GOOD o FAIL a seconda dell'esito del test

    OUTPUT:
    True o False a seconda dell'esito del test
    """
    try:
        res=func(*args)
    except BaseException as err:
        print("FAIL {}. Ottenuto errore {}".format(nome,err))
        return False

    if res==r_atteso:
        print("GOOD {}. Ottenuto {}".format(nome,res))
        return True
    else:
        print("FAIL {}. Ottenuto {} invece di {}".format(nome,res,r_atteso))
        return False

def testErrore(nome,e_atteso,func,*args):
    """Verifica che func(*args) sollevi l'errore e_atteso

    Calcola func(*args) e verifica la funzione sollevi un errore, ed
    in particolare l'errore e_atteso.

    INPUT:
    - nome: nome del test
    - e_atteso: valore atteso dal test
    - func: funzione da testare
    - args: sequenza di argomenti da testare
    
    PRINT:
    Stampa GOOD o FAIL a seconda dell'esito del test

    OUTPUT:
    True o False a seconda dell'esito del test
    """
    if not issubclass(e_atteso,BaseException):
        raise TypeError('Il tipo di errore da testare non è valido.')
    
    try:
        res=func(*args)
    except e_atteso:
        print("GOOD {}. Errore atteso {}".format(nome,e_atteso))
        return True
    except BaseException as err:
        print("FAIL {}. Errore {} invece di {}".format(nome,err,e_atteso))
        return False
    else:
        print("FAIL {}. Manca l'errore atteso {}".format(nome,e_atteso))
        return False
    

