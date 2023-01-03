"""the sql ip 1 in csv indicates the end of the iteration 
for rows so add something at the sqli p 1 cell 
after last row in csv file  
"""
import csv
f = open("inputf.csv", "r")
def emptr(l):
    for i in range(0,len(l)):
        for j in l:
         if j=='':
            l.remove('')
table= csv.DictReader(f)
flist,clus_ip,com_name,pri_ip,sq_ip1,sq_ip2,sq_ip3,sq_ip4,all_sq=[]
for rows in table:
    check=rows['Cluster Name and IP']
    if check !='':
        cluster_n=rows['Cluster Name and IP']
        clus_ip.append(rows['Cluster IP 1'])
        clus_ip.append(rows['Cluster IP 2'])
        clus_ip.append(rows['Cluster IP 3'])
        clus_ip.append(rows['Cluster IP 4'])
        emptr(clus_ip)
        com_name.append(rows['Node1'])
        com_name.append(rows['Node2'])
        com_name.append(rows['Node3'])
        com_name.append(rows['Node4'])
        emptr(com_name)
        pri_ip.append(rows['Server IP 1'])
        pri_ip.append(rows['Server IP 2'])
        pri_ip.append(rows['Server IP 3'])
        pri_ip.append(rows['Server IP 4'])
        emptr(pri_ip)
        sq_ip1.append(rows['SQL IP1'])
        sq_ip2.append(rows['SQL IP2'])
        sq_ip3.append(rows['SQL IP3'])
        sq_ip4.append(rows['SQL IP4'])
        emptr(sq_ip1)
        emptr(sq_ip2)
        emptr(sq_ip3)
        emptr(sq_ip4)
    else:
        sq_ip1.append(rows['SQL IP1'])
        sq_ip2.append(rows['SQL IP2'])
        sq_ip3.append(rows['SQL IP3'])
        sq_ip4.append(rows['SQL IP4'])
        emptr(sq_ip1)
        emptr(sq_ip2)
        emptr(sq_ip3)
        emptr(sq_ip4)
        if rows['SQL IP1']=='':

            all_sq.append(sq_ip1)
            all_sq.append(sq_ip2)
            all_sq.append(sq_ip3)
            all_sq.append(sq_ip4)
            for n in range(0,len(clus_ip)):
                temp_sq=all_sq[n]
                tip_s=''
                for i in temp_sq:
                    tip_s+="{},".format(i)
                tip_s= tip_s[:-1]
                all_ip=clus_ip[n]+","+pri_ip[n]+","+tip_s    
                dum_dict={'cluster name':cluster_n,'computer name':com_name[n],'cluster ip':clus_ip[n],'private ip':pri_ip[n],'sql ip':tip_s,'all ip':all_ip}
                flist.append(dum_dict)
            clus_ip,com_name,pri_ip,sq_ip1,sq_ip2,sq_ip3,sq_ip4,all_sq=[]
print("completed")
fields = ['cluster name','computer name','cluster ip','private ip','sql ip','all ip'] 
filename = "task_test1.csv"
with open(filename, 'w') as csvfile:  
    writer = csv.DictWriter(csvfile, fieldnames = fields)  
    writer.writeheader() 
    writer.writerows(flist) 

            

            



        
        
        
    
        
        
    



    
    
    

