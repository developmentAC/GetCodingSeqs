#!/usr/bin/env python3
# -*- coding: utf-8 -*-

""" Program to play DNA input files."""

from gcs import launcher
from gcs import fileloader
from gcs import saver

from pathlib import Path

import typer

from rich.console import Console

cli = typer.Typer()
console = Console()

@cli.command()
def getArguments(
    bighelp: bool = False,
#    opt: str = "",
    # data_file: Path = typer.Option(...)
    data_file: Path = typer.Option(None),
    fullSeqs: bool = typer.Option(False)

    # dir: Path = typer.Option(None),
    # file: Path = typer.Option(None),
) -> str:
    """New get arguments function"""

    if bighelp == True:  # print up some extra help about how to start a virtual env
        launcher.helper()
        # gh.helper_extended()
        exit()

    if  data_file.is_file() == False:
        console.print("\t :bomb: Oh no! The data file does not exist!")
        raise typer.Abort()

    else:

        main(data_file, fullSeqs)    
        # myData_list = fileloader.getData(data_file)
        # console.print(f" main() :: openfile returned: {myData_list}")

        # Further processing; we need the DNA sequences of the coding
        # regions and some regions that are NOT coding regions
        # main(myData_list, data_file)         
    # end of getArguments()

def main(data_file, fullSeqs):
    """ Driver function of the program """
    console.print(f"maxsize = {fullSeqs}")

    console.print("\t [+] Getting Coding regions")

    numOfSeqs_int = 20
    maxSize_int = 400
    if fullSeqs == True:
        maxSize_int = 0

    myCodingData_dic = fileloader.getCodingData(data_file, numOfSeqs_int, maxSize_int)
    console.print(f" main() :: openfile returned: {myCodingData_dic}")
    # for i in myCodingData_dic: console.print(f"{i} :: {myCodingData_dic[i]} ")
    saver.saveCodingFile(myCodingData_dic, "C")

    console.print("\t [+] Getting nonCoding regions")
    # Use parameter to say how many seqs to prepare.

    maxSize_int = 400

    myNonCodingData_dic = fileloader.getNonCodingData(data_file,myCodingData_dic,numOfSeqs_int, maxSize_int) 
    # console.print(f" main() :: openfile returned: {myNonCodingData_dic}")
    saver.saveNonCodeFile(myNonCodingData_dic,"nC")
    console.print(":cake:")

    # end of main()

if __name__ == "__main__":
    getArguments(sys.argv[1:])
