"""open the data file and then return the data."""
from Bio import SeqIO
from rich.console import Console
from gcs import saver
import random

console = Console()
minSize_int = 24

def getCodingData(myFile_str, numOfSeqs_int, maxSize_int):
    """ function to open the datafile and pull the coding sequences. MaxSize_int = 1 means that there is no limit."""
    counter = 0
    # console.print(f"getCodingData() maxsize = {maxSize_int}")
    
    for gb_record in SeqIO.parse(open(myFile_str,"r"), "genbank") :
        # parse record for features information
        print(f" \t\t Coding Seqs from Name {gb_record.name}, number of features: {len(gb_record.features)}")
    seq_dic = {} # contain the location(key) with seq(values)
    for i in range(len(gb_record.features)):
        tmp = gb_record.features[i]
        if tmp.type == "source": # do not want the source or the whole seq. 
            # console.print(":poop:SOURCE!!")
            pass
        else: # all other types of features, not source
            if counter == numOfSeqs_int: break # limit the selection to the numOfSeqs_int
            location_str = str(tmp.location)
            start = tmp.location.start
            end = tmp.location.end
            if end - start > minSize_int:
                thisSeq_str = gb_record.seq[start:end] #full seq
            # thisSeq_str = thisSeq_str # regular length seq

                if maxSize_int == 0: # use natural length of coding seq
                    # print("Collection full length.")
                    thisSeq_str = thisSeq_str # shorten seq to maxsize
                    seq_dic[location_str] = thisSeq_str
                else:
                    seq_dic[location_str] = thisSeq_str[:maxSize_int]
                    # print("not full seq")
                counter += 1
    # print(seq_dic)
    return seq_dic
    # end of getCodingData()



def getNonCodingData(myFile_str,seq_dic, numberOfSeqs_int, maxSize_int):
    mySeq_str = ""
    
    for gb_record in SeqIO.parse(open(myFile_str,"r"), "genbank") :
        # parse record for features information
        print(f"\t\t NonCoding Seq from Name {gb_record.name}")#, number of features: {len(gb_record.features)}")
        # print(f"SEQ: {repr(gb_record.seq)}")
        mySeq_str = str(gb_record.seq)
    # console.print(f"seq : {type(mySeq_str)}")

    # Remove the known cds regions and the rest is non-coding sequence material
    for i in seq_dic:
        mySeq_str = mySeq_str.replace(str(seq_dic[i]),".")
    nonCodingSeq_dic = {}
    mySeq_str = mySeq_str.replace(".","") # full sequence of noncoding material
    # console.print(f" the sequence: {mySeq_str}")
    for n in range(numberOfSeqs_int): # choose n seqs

        #start of seq
        mySeqStart_int = random.randrange(0, len(mySeq_str) - (maxSize_int + minSize_int), 3)

        # end of seq
        mySeqEnd_int = random.randrange(mySeqStart_int, mySeqStart_int + maxSize_int, 3)

        thisSeq_str = mySeq_str[mySeqStart_int: mySeqEnd_int]
        nonCodingSeq_dic[n] = thisSeq_str

        # print(f"{n}; {mySeqStart_int}- {mySeqEnd_int} :: {thisSeq_str}")

    # console.print(f" noncoding: {nonCodingSeq_dic}")
    return nonCodingSeq_dic

#end of getNonCodingData()


