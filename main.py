**********targil 1:
  
def isDictKeysAlpha(d):
    for k in dict_city.keys():
        if k.isalpha:
            continue
    return True
  
**********targil 2:
  
def popByValue(dict):
    etgar = []
    for k,v in list(dict.items()):
        if type(dict[k]) == int:
            etgar.append(dict[k])
            dict.pop(k)
    return etgar  
  
 **********targil 3:
  
 def compareDict(d1,d2):
    if d1 == d2:
        print(d1,d2)
        return True
    else:
        return False 

 **********targil 4:     
      
      
 def newDict(d1,d2):
    dict = {}
    if len(list1) != len(list2):
        return None
    for i in range(len(list1)):
        dict[list1[i]] = list2[i]
    return dict     
