""" file to receive sequences and then save them somewhere as a fasta file."""
from rich.console import Console
import os

console = Console()
OUTPUTDIR_str = "0_out/"

def cleaner(in_str):
    """function to remove unnecessary chars in a string"""
    # console.print(":poop:")
    in_str = in_str.replace("(+)","").replace("(-)","").replace(":","_").replace("[","").replace("]","").replace("{","").replace("}","").replace(">","").replace(" ","-").replace("(","").replace(")","")
    return in_str
# end of cleaner()

def saveCodingFile(in_dic,name_str):
    """ Function to save the coding sequences individually as a fasta file."""
    # console.print("[+] Saving coding files ... ")

    tmp_dir = checkDataDir(OUTPUTDIR_str)
    tmp = ""
    for i in in_dic:
        try:
            tmp = cleaner(i)
        except AttributeError:
            pass
        fname_str = f"{OUTPUTDIR_str}{name_str}_{tmp}.fasta"
        try:
            f = open(fname_str,"w")
            toSave_str = f">{tmp}\n{in_dic[i]}"
            f.write(toSave_str)
            f.close()
            # console.print(f"\t :sparkles: File saved: {fname_str}")
        except Exception:
            console.print("\t Error saving file : {fname_str}")
            pass
# end of saveCodingFile()


def saveNonCodeFile(in_dic,name_str):
    """ function to save noncoding files"""
    console.print("[+] Saving non-coding files ... ")
    for i in in_dic:
        fname_str = f"{OUTPUTDIR_str}{name_str}_{i}.fasta"
        # console.print(f"fn = {fname_str}, i= {i}, seq = {in_dic[i]}")
        f = open(fname_str, "w")
        toSave_str = f">{name_str}\n{in_dic[i]}"
        f.write(toSave_str)
        f.close()
        # console.print(f"\t :sparkles: File saved: {fname_str}")
# end of saveFastaFile()

def checkDataDir(dir_str):
    # function to determine whether a data output directory exists.
    # if the directory does not exist, then it is automatically created

    try:
        os.makedirs(dir_str)
        # if MYOUTPUT_DIR doesn't exist, create directory
        return 1
    
    except OSError:
        # console.print("\t Error creating directory or directory already present ... ")
        return 0

# end of checkDataDir()
        
