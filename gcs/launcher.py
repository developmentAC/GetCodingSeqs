#!/usr/bin/env python3
# -*- coding: utf-8 -*-
""" This file contains code to facilitate loading files and running the program. """


DATE = "24 February 2023"
VERSION = "0.1.0"
AUTHOR = "Oliver Bonham-Carter"
AUTHORMAIL = "obonhamcarter@allegheny.edu"


from pathlib import Path
from rich.console import Console

import os, random, sys

THISPROG = sys.argv[0].replace("./", "")
WHATISTHIS_p1 = f"\n\t{THISPROG}: Gathers coding and non-coding genetic sequences (DNA) from Genbank files. \n\t These sequences may be used as data for other tools."
WHATISTHIS_p2 = (
    "\t Use option '-h' for more glorification about this amazing project!\n"
)

MYOUTPUT_DIR = "0_out/"  # all results are saved in this local directory

console = Console()

banner1_str = """
\t    ██████╗  ██████╗███████╗   
\t██╗██╔════╝ ██╔════╝██╔════╝██╗
\t╚═╝██║  ███╗██║     ███████╗╚═╝
\t██╗██║   ██║██║     ╚════██║██╗
\t╚═╝╚██████╔╝╚██████╗███████║╚═╝
\t    ╚═════╝  ╚═════╝╚══════╝   
"""

def displayBanner(displayCount_int):
    """ display banner with some randomly selected colour. The argument is the number of times 
    to make the display."""
    for i in range(displayCount_int):
        red_int   = random.choice(range(0,255))
        green_int = random.choice(range(0,255))
        blue_int  = random.choice(range(0,255))
        colStyle_str = f"rgb({red_int},{green_int},{blue_int})"
        console.print(banner1_str, style = colStyle_str)

# end of displayBanner()


# banner ref: https://manytools.org/hacker-tools/ascii-banner/


def helper():
    """Cheap and friendly online help; how to use the program"""
    displayBanner(1)  # print up one banner screen
    console.print(WHATISTHIS_p1)
    h_str1 = "\t" + DATE + " | version: " + VERSION
    h_str2 = "\t" + AUTHOR + "\n\tmail: " + AUTHORMAIL
    console.print("\t" + len(h_str2) * "-")
    console.print(h_str1)
    console.print("\t" + len(h_str2) * "-")
    console.print(h_str2)
    # print(h_str2)
    console.print("\t" + len(h_str2) * "-")
    console.print("\tOptions:")
    console.print(f"\t [+] --bighelp : This page, right?")
    console.print(f"\t [+] Produce reduced-sized sequences from a genbank file.")
    console.print(f"\t\t :smiley: poetry run {THISPROG} --data-file data/df.gb") 
    console.print(f"\t [+] Produce full-sized sequences from a genbank file")
    console.print(f"\t\t :smiley: poetry run {THISPROG} --data-file data/df.gb --fullseqs")

# end of helper()


def helper_extended():
    """Function to print up extra information for the user."""
    print("\n\t # --------------------------")
    print(f"\n\t You are to run {THISPROG} using poetry.")

    # end of helper_extended()



def checkDataDir(dir_str):
    # function to determine whether a data output directory exists.
    # if the directory doesnt exist, then it is created

    try:
        os.makedirs(dir_str)
        # if MYOUTPUT_DIR doesn't exist, create directory
        # printByPlatform("\t Creating :{}".format(dir_str))
        return 1

    except OSError:
        # printErrorByPlatform("\t Error creating directory or directory already present ... ")
        return 0
# end of checkDataDir()


def get_platformType():
    """Function to dermine the OS type."""
    platforms = {
        "darwin": "OSX",
        "win32": "Windows",
        "linux1": "Linux",
        "linux2": "Linux",
    }
    if sys.platform not in platforms:
        return sys.platform
    return platforms[sys.platform]
# end of get_platformType()


# # end of isFileConfirmed()
