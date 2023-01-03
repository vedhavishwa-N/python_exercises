import csv
flist=[]
f = open("inputf.csv", "r")
fields=[]
#field=['Cluster Name and IP', 'Cluster IP 1', 'Cluster IP 2', 'Cluster IP 3', 'Cluster IP 4', 'Node1', 'Server IP 1', 'Node2', 'Server IP 2', 'Node3', 'Server IP 3', 'Node4', 'Server IP 4', 'Instancename', 'SQL IP1', 'SQL IP2', 'SQL IP3', 'SQL IP4', '', 'computer_name', 'cluster_name', 'private_ip_address', 'additional_private_ip_addresses']
#PROD_DICT = csv.DictReader(f)
# print(type(PROD_DICT))
dr = csv.DictReader(f)
print(type(dr))
def emptr(l):
    for i in range(0,4):
        for j in l:
         if j=='':
            l.remove('')
    #print("-----",l)
all_sq=[]

check=[]
for b_d in dr:
    sq_ip=[]
    sq_ip.append(b_d['SQL IP1'])
    sq_ip.append(b_d['SQL IP2'])
    sq_ip.append(b_d['SQL IP3'])
    sq_ip.append(b_d['SQL IP4'])
    emptr(sq_ip)
    all_sq.append(sq_ip)
for i in all_sq:
    if i==[]:
        all_sq.remove(i)
# print(all_sq)




      

flg=0
f1 = open("inputf.csv", "r")
dr2= csv.DictReader(f1)

for book_dict in dr2:
    #print(book_dict)
    
    cluster_n=book_dict['Cluster Name and IP']
    if cluster_n:
      print("---------------------------------------------")  
    
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

    #   tip_s=''
    #   for i in temp_sq:
        
    #     tip_s+=" {} ,".format(i)
    #   tip_s= tip_s[:-1]

    #   all_ip=clus_ip+pri_ip+temp_sq
    #   all_l=''
    #   for j in all_ip:
    #     all_l+=" {} ,".format(j)
    #   all_l=all_l[:-1]
    #   f_all_ip=all_l
    #   #print(f_all_ip)

      for n in range(0,len(clus_ip)):
        temp_sq=all_sq[flg]
        print("----",temp_sq)

        
        
        tip_s=''
        for i in temp_sq:
        
            tip_s+=" {} ,".format(i)
            tip_s= tip_s[:-1]

        all_ip=clus_ip[n]+","+pri_ip[n]+","+tip_s
        print(all_ip)

        dum_dict={'cluster name':cluster_n,'computer name':com_name[n],'cluster ip':clus_ip[n],'private ip':pri_ip[n],'sql ip':tip_s,'all ip':all_ip}
        print(dum_dict)
        flg+=1
        flist.append(dum_dict)
      

#final list of dictionary 
print(flist)

print("completed")

fields = ['cluster name','computer name','cluster ip','private ip','sql ip','all ip'] 
    
filename = "task_completed.csv"
     
with open(filename, 'w') as csvfile:  
    writer = csv.DictWriter(csvfile, fieldnames = fields)  
    writer.writeheader() 
    writer.writerows(flist) 



    

#final list of dictionary 
# print(flist)

# print("completed")

# fields = ['cluster name','computer name','cluster ip','private ip','sql ip','all ip'] 
    
# filename = "task_final.csv"
     
# with open(filename, 'w') as csvfile:  
#     writer = csv.DictWriter(csvfile, fieldnames = fields)  
#     writer.writeheader() 
#     writer.writerows(flist) 
