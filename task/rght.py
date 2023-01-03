"""import csv

f = open("US_PROD_DBServers_Information_ForAzure_IPAddress (1).csv", "r", encoding="utf8")

fields=['Cluster Name and IP', 'Cluster IP 1', 'Cluster IP 2', 'Cluster IP 3', 'Cluster IP 4', 'Node1', 'Server IP 1', 'Node2', 'Server IP 2', 'Node3', 'Server IP 3', 'Node4', 'Server IP 4', 'Instancename', 'SQL IP1', 'SQL IP2', 'SQL IP3', 'SQL IP4', '', 'computer_name', 'cluster_name', 'private_ip_address', 'additional_private_ip_addresses']
PROD_DICT = csv.DictReader(f)
print(type(PROD_DICT))
Cluster=[]
nodes=[]
cluster_ip=[]
private_ip=[]
sql_ip=[]

#all data

def dimmyit(d1,d2,d3,d4,s1,s2,s3,s4,l):
    d1=rows[s1]
    d2=rows[s2]
    d3=rows[s3]
    d4=rows[s4]

    if d1!='':
        l.append(d1)
    if d2!='':
        l.append(d2)
    if d3!='':
        l.append(d3)
    if d4!='':
        l.append(d4)

    

for rows in PROD_DICT:
    #FOR CLUSTER NAME
    temp_c=rows['Cluster Name and IP']
    Cluster.append(temp_c)
    
    #FOR GETTING NODES
    dimmyit('n1','n2','n3','n4','Node1','Node2','Node3','Node4',nodes)
    
    
    #for clusterip
    dimmyit('cp1','cp2','cp3','cp4', 'Cluster IP 1', 'Cluster IP 2', 'Cluster IP 3', 'Cluster IP 4',cluster_ip)

    #for private_ip .ie all server ips
    dimmyit('sr1','sr2','sr3','sr4','Server IP 1', 'Server IP 2','Server IP 3', 'Server IP 4',private_ip)

    #for sql ip combined all sql ips
    dimmyit('sq1','sq2','sq3','sq4','SQL IP1', 'SQL IP2', 'SQL IP3', 'SQL IP4',sql_ip)


#all sql ips combined without gap
#-------------------------------print(sql_ip)

#all server ips ina list as private ip
#-------------------------print(private_ip)     
    
#clusterip all without gaps
#------------------------------print(cluster_ip)

#print(Cluster)
#print(nodes)
computer_name=nodes

#computer names without space
#--------------------------------print(computer_name)
cluster_list=[]
Cluster_dict={}
for i in Cluster:
    if i!='':
        name=i
        num=0
    num+=1
    Cluster_dict[name]=num    
       

#cluster name with numbers for times AS KEYS
#---------------------------print(Cluster_dict)
Cluster_name=[]
for i in Cluster_dict:
   Cluster_name.append(i)

#CLUSTER NAME ONLY
#---------------------print(Cluster_name)

for i in Cluster_name:
    siz=Cluster_dict[i]
    for j in range(0,siz):
        cluster_list.append(i)

print(cluster_list)

#COMPUTER NAMES =NAMES OF NODES

cluster name =   Cluster=[]
computername =   nodes=[]
clusterip    =    cluster_ip=[]
privateip    =    private_ip=[]
sql ip       =     sql_ip=[]


print(len (cluster_list))
print(len( nodes))
print(len(cluster_ip))
print(len(private_ip))
print(len(sql_ip))

columns=['cluster name','computer name','cluster ip','private ip','sql ip','all ip']
dum_dict={}
num_rows=len(cluster_list)
f_list=[]
print(num_rows)"""
"""for i in range(0,num_rows):
    dum_dict={'cluster name':Cluster[i],'computer name' : nodes[i],'cluster ip':    cluster_ip[i],'private ip' :private_ip[i],'sql ip' :sql_ip[i]}
    f_list.append(dum_dict)
print(f_list)
"""

import csv

flist=[]

f = open("inputfile.csv", "r", encoding="utf8")

fields=[]

field=['Cluster Name and IP', 'Cluster IP 1', 'Cluster IP 2', 'Cluster IP 3', 'Cluster IP 4', 'Node1', 'Server IP 1', 'Node2', 'Server IP 2', 'Node3', 'Server IP 3', 'Node4', 'Server IP 4', 'Instancename', 'SQL IP1', 'SQL IP2', 'SQL IP3', 'SQL IP4', '', 'computer_name', 'cluster_name', 'private_ip_address', 'additional_private_ip_addresses']

PROD_DICT = csv.DictReader(f)

print(type(PROD_DICT))

dr = csv.DictReader(f)

print(type(dr))

def emptr(l):
    
    for i in range(0,4):
        
        for j in l:
         if j=='':
            l.remove('')
def adder(l,s1,s2,s3,s4):
    
    for i in range(0,4):
        
        l.append(book_dict[s1])
        l.append(book_dict[s2])
        l.append(book_dict[s3])
        l.append(book_dict[s4])
        emptr(l)
    
for book_dict in dr:
    #print(book_dict)
    
    print("---------------------------------------------")
    
    cluster_n=book_dict['Cluster Name and IP']
    
    clus_ip=[]
    
    adder(clus_ip,'Cluster IP 1', 'Cluster IP 2', 'Cluster IP 3', 'Cluster IP 4')
    
    com_name=[]
    
    adder(com_name,'Node1', 'Node2', 'Node3', 'Node4')
    
    pri_ip=[]
    
    adder(pri_ip, 'Server IP 1', 'Server IP 2',  'Server IP 3','Server IP 4')
    
    sq_ip=[]
    
    adder(sq_ip,'SQL IP1', 'SQL IP2', 'SQL IP3', 'SQL IP4')
    
    print(cluster_n,len(clus_ip),len(com_name),len(sq_ip),len(pri_ip))
    
    allip=clus_ip+pri_ip+sq_ip
    
    #print(allip)
    
    dum_dict={}
    
    for i in range(0,len(clus_ip)):
    
        dum_dict={'cluster name':cluster_n,'computer name':com_name[i],'cluster ip':clus_ip[i],'private ip':pri_ip[i],'sql ip':sq_ip,'all ip':allip}
    
        print(dum_dict)
    
        flist.append(dum_dict)

print(flist)

fields = ['cluster name','computer name','cluster ip','private ip','sql ip','all ip'] 
    
filename = "task_data_m.csv"
     
with open(filename, 'w') as csvfile:  

    writer = csv.DictWriter(csvfile, fieldnames = fields)  

    writer.writeheader() 

    writer.writerows(flist) 


