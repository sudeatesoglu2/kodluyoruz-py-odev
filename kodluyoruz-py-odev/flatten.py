x = [[1,'a',['cat'],2],[[[3]],'dog'],4,5]
otherl = []
def flatten(x):
    for i in x:
        if isinstance(i,list):
            flatten(i)
        else:
            otherl.append(i)
flatten(x)
print(otherl)