# GetCodingSequences: a coding/non-coding sequence extractor from Genbank files.

### Oliver Bonham-Carter, [Allegheny College](https://allegheny.edu/)
### email: obonhamcarter@allegheny.edu

---
![logo](graphics/logo.png)
Figure 1. A GCS stands for _Get Coding Sequences_.
Genetic Music: Use your ears to study DNA!!

## Table of Contents

- [Description](#description)
- [Running the code](#running-the-code)
- [Command Summary](#command-summary)
- [Mechanism](#mechanism)
- [Future Work](#future-work)

## Description

Often, when you have a tool from Bioinformatics, sequences are the input. This program, **GCS** creates fasta files of the coding sequences (producing protein) of a GenBank file. In addition, the program also outputs the non-coding sequences (those that produce no-known protein) from the Genbank file. These sequences can then be used for research or to test new tools. 


![genbank record](graphics/genbankFile.png)
Figure 2. In a GenBank file, there are references for the coding regions. 

GCS works by locating the coding sequences from a GenBank file by finding their location references in the record, as shown in Figure 2. Then GCS locates the actual sequences using these starting and ending markers, and places this sequence data into fasta files. The noncoding regions are located by removing the coding regions from main sequence. The remaining sequence, from which all coding information has been removed, is the non-coding region. Sequences are then extracted from this body of non-coding genetic material. 

```
    numOfSeqs_int = 20
    maxSize_int = 400
```
Note: shown above, the size of the extracted sequences is 400 base-pairs but this value may be customized in main.py, along with the number of sequences to produce. 

by parsing their locations out of a GenBank record, as shown in Figure 2.
## Running the code

	 [--bighelp] This page, right?
	 [--opt S] Create a music scale
	 [--opt T] Create song: Twinkle-Twinkle Little Star
	 [--opt H] Create song: Happy Birthday
	 [--data ./data --file file.fasta] Load fasta file, convert dna to score
	 Setup with Poetry :  poetry install

     😀 USAGE: poetry run genmus --dir ./data/ --file mydata.fasta 

