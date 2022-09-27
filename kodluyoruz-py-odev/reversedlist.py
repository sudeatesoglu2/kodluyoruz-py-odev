x = [[1, 2], [3, 4], [5, 6, 7]]
otherl = []
def reversedlist(x):
    for i in x:
        if isinstance(i,list):
            reversedlist(i)
        else:
            otherl.append(i)
    return otherl[::-1]
print(reversedlist(x))