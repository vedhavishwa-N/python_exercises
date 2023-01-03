import csv
flist=[]
f = open("inputfile.csv", "r", encoding="utf8")
fields=[]
#field=['Cluster Name and IP', 'Cluster IP 1', 'Cluster IP 2', 'Cluster IP 3', 'Cluster IP 4', 'Node1', 'Server IP 1', 'Node2', 'Server IP 2', 'Node3', 'Server IP 3', 'Node4', 'Server IP 4', 'Instancename', 'SQL IP1', 'SQL IP2', 'SQL IP3', 'SQL IP4', '', 'computer_name', 'cluster_name', 'private_ip_address', 'additional_private_ip_addresses']
#PROD_DICT = csv.DictReader(f)
# print(type(PROD_DICT))
dr = csv.DictReader(f)
print(type(dr))
def emptr(l):
    #for i in range(0,4):
        for j in l:
         if j=='':
            l.remove('')

for book_dict in dr:
    #print(book_dict)
    print("---------------------------------------------")
    cluster_n=book_dict['Cluster Name and IP']
    clus_ip=[]
    clus_ip.append(book_dict['Cluster IP 1'])
    clus_ip.append(book_dict['Cluster IP 2'])
    clus_ip.append(book_dict['Cluster IP 3'])
    clus_ip.append(book_dict['Cluster IP 4'])
    
    emptr(clus_ip)
    
    com_name=[]

    com_name.append(book_dict['Node1'])
    com_name.append(book_dict['Node2'])
    com_name.append(book_dict['Node3'])
    com_name.append(book_dict['Node4'])
    emptr(com_name)
    
    pri_ip=[]

    pri_ip.append(book_dict['Server IP 1'])
    pri_ip.append(book_dict['Server IP 2'])
    pri_ip.append(book_dict['Server IP 3'])
    pri_ip.append(book_dict['Server IP 4'])
    emptr(pri_ip)
    
    sq_ip=[]
    sq_ip.append(book_dict['SQL IP1'])
    sq_ip.append(book_dict['SQL IP2'])
    sq_ip.append(book_dict['SQL IP3'])
    sq_ip.append(book_dict['SQL IP4'])
    emptr(sq_ip)

    print(cluster_n,len(clus_ip),len(com_name),len(sq_ip),len(pri_ip))
    
    allip=clus_ip+pri_ip+sq_ip
    #print(allip)
    dum_dict={}

    ip_s=""
#sql ip as comma seperated value

    for i in sq_ip:
        
        ip_s+=" {} ,".format(i)
    ip_s= ip_s[:-1]
    
    all_l=""
#all ip as comma seperated val
    for j in allip:
        all_l+=" {} ,".format(j)
    all_l=all_l[:-1]

    for i in range(0,len(clus_ip)):
        dum_dict={'cluster name':cluster_n,'computer name':com_name[i],'cluster ip':clus_ip[i],'private ip':pri_ip[i],'sql ip':ip_s,'all ip':all_l}
        #print(dum_dict)
        flist.append(dum_dict)
#final list of dictionary 
print(flist)

print("completed")

fields = ['cluster name','computer name','cluster ip','private ip','sql ip','all ip'] 
    
filename = "task_final.csv"
     
with open(filename, 'w') as csvfile:  
    writer = csv.DictWriter(csvfile, fieldnames = fields)  
    writer.writeheader() 
    writer.writerows(flist) 



