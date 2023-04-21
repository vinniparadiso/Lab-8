#Vinni, Benthany, Krista
#Number 1
def score(dict):
    list=[]
    for key in dict:
        if dict[key]<50:
            list.append(key)
    return list

dict1={"lily":30,"jack":68,"ryan":22,"beth":98,"kate":21}
print(score(dict1))
