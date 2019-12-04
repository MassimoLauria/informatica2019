#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Codice utile per le dispense di Informatica 

Il modulo contiene alcune funzioni utili per le dispense, in
particolare contiene le implementazioni degli algoritmi visti
a lezione.

Verrà regolarmente esteso quindi controllate che non vi siano
aggiornamenti disponibili prima di usarlo.

Copyright (C) 2017, 2018, 2019  Massimo Lauria <massimo.lauria@uniroma1.it>
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


def mcd(a, b):
    "Calcola il massimo comun divisore di due interi non negativi."
    if not isinstance(a,int) or not isinstance(b,int):
        raise TypeError("La funzione mcd accetta solo argomenti interi.")
    
    if a < 0 or b < 0:
        raise ValueError("La funzione mcd accetta solo argomenti non negativi.")

    a, b = max(a,b), min(a,b)
    while b > 0 :
        a, b = b, a % b
    return a


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

def insertionsort(L):
    """Ordina la lista utilizzando insertion sort
    """    
    for i in range(1,len(L)):

        x   = L[i]    # salvo il valore da inserire
        pos = i       # posizione di inserimento

        while pos > 0 and L[pos-1] > x:
            L[pos] = L[pos-1]   #sposto a destra L[pos-1]
            pos = pos -1
       
        L[pos] = x
        
        
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

def qsort_partition(S, start, end):
    # sceglie una posizione random per il pivot
    pivot_pos = random.randint(start, end)
    pivot = S[pivot_pos]
    # scambia il pivot con l'elemento di testa
    S[start], S[pivot_pos] = S[pivot_pos], S[start]
    i = start+1
    j = end
    # scansione della lista dall'inizio (pivot escluso) verso il centro
    # e dalla fine verso il centro
    while i<j:
        while i<j and S[i] < pivot:  # cerca un elemento grande da sx verso centro
            i += 1
        while i<j and S[j] >= pivot: # cerca un elemento piccolo da dx verso centro
            j -= 1
        if i<j:  # se ha trovato una coppia da scambiare la scambia
            S[i], S[j] = S[j], S[i]

    # se i ha scavallato tra gli elementi grandi, allora l'ultimo
    # elemento piccolo (da scambiare col pivot) è in posizione i-1,
    # altrimenti è in posizione i
    if S[i] >= pivot:
        i -= 1
    S[start], S[i] = S[i], S[start] # posiziona il pivot al centro
    return i

def quicksort(S, start=0, end=None):
    if end is None:
        end = len(S)-1
    if start>=end:
        return
    pivot_pos = qsort_partition(S, start, end)
    quicksort(S, start, pivot_pos - 1)
    quicksort(S, pivot_pos+1, end)


          
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

