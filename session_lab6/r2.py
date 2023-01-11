from collections import Counter
list= [1, 5, '5', 5.0, 'a', 8, 8.0, 3, '3.9', 'B', 'b', 'B', 'B',  'z', 26]
result={}

# print(Counter(list))
for i in list:
    try:             
        if i.isalpha():
            if i.islower() and i not in result:
                result[i]=1
            elif i.islower() and i in result:
                result[i]+=1
            elif i.isupper():
                i=i.lower()
                if i.islower() and i not in result:
                    result[i]=1
                elif i.islower() and i in result:
                    result[i]+=1
    except:
        if i in result:
            result[i]+=1
        elif i is float:
            i=int(i)
            if i in result:
                result[i]+=1
        else:
            result[i]=1
print(result)
            



    
