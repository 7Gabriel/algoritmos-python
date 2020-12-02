
def find_duplicate(status_sequence):
    seq_list = list(status_sequence)
    return dict([[i,seq_list.count(i)] for i in seq_list if seq_list.count(i)>1])


print(find_duplicate("IITRCRV"))

