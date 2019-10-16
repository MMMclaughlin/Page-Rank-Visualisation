import gzip
from Bio import SeqIO

def uniprot_seqrecords(file_location):
    records=[]#store the data from the file in a list

    handle= gzip.open(file_location)#open file of data
    for record in SeqIO.parse(handle, "uniprot-xml"):
        records.append(record)#this gets all the data from the file and adds it to the end of the list

    return records # this returns the list of file data
