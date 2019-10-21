def average_len(record):#function to find average protein length
    totallength = 0#set total length
    for i in enumerate(record):#loop through the list
        totallength=totallength+len(i[1])#add the length of selected protein
    average=totallength/len(record)#creates average of total/quantity
    return average

def average_len_taxa(records,depth):
    #calculates the average length for the top level taxa
    record_by_taxa = {}
    print(depth)
    depth=int(depth)-1
    for r in records:
        taxa = r.annotations["taxonomy"]
        try:
            record_by_taxa.setdefault(taxa[depth], []).append(r)
        except IndexError:
            pass
    return {taxa:average_len(record) for (taxa, record) in record_by_taxa.items()}
