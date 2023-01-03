"""fjdbgjsanl"""

"""#ROUGH
import json
import datetime
def estimatecarbattery():
    f = open('travel.json')
    user_details = ['traveldetails']
    name = input("enter your name")
    phonenumber = eval(input("enter your mobile number"))
    currentbattery= eval(input("current battery percentage"))
    fullcharge= eval(input("fullchargecapacity"))
    totaldistance = eval(input("totaldistance"))
    distance_covered = eval(input("current distance"))
    started_at = datetime.datetime.now()
    started_at = started_at.strftime("%Y-%m-%d")
    new_users = {
            'name': name,
            'phone': phonenumber,
            'requiredbattery': [{
                'currentbattery': currentbattery,
                'fullcharge': fullcharge,
                'distance_covered': distance_covered,
                'started_at': started_at,
            }],
        }
    user_details.append(new_users)
    print(user_details)
    
    percentage= fullcharge/100
    remainingdistance= totaldistance - distance_covered
    remainingbattery =(remainingdistance/percentage)-currentbattery
    remainingdistance=totaldistance-distance_covered
    requiredbattery=remainingdistance*percentage
    print("batterycharge required to reach destination",remainingbattery)
    print("remainingdistance",remainingdistance,"km")
    return remainingbattery,remainingdistance,requiredbattery
"""

"""
def write_extracted(data):
    json_format = json.dumps(data, indent=3)
    print(json_format)
    y = open('travel.json', 'w')
    y.write(json_format)
    y.close()
data = estimatecarbattery()
print(estimatecarbattery())
print("the data for json")
print(data)

write_extracted(data)
"""
"""n = int(input("enter the number"))
if(n %2)!= 0 :
    print("it is Weird")
    if(n %2)==0  and n>2 and n<=5:
       print("It is not weird")
    if(n %2)==0  and n>6 and n <=20:
        print("It is weird")
    elif(n %2 )==0 and n >20:
        print("it is not weird")
from bottle import route, run, template

@route('/home')
def home():
    return """
"""While deploying IT resources on the cloud, 
    securing them against various threats and vulnerabilities 
    requires a deep understanding of the security models used 
    by Cloud Providers such as AWS and the approaches that 
    you can take and the tools you can use. Tivona helps clients 
    deploy their applications,servers and
     other resources securely on the cloud.
     
     http://localhost:8001/contacts
run(host='localhost', port=8001, reloader=True)
"""
"""sum=0
print("enter the number")
i=list(input())
for num in i:
    num=eval(num)
    sum=sum+num
print(sum)
"""
"""for num in range(20):
    if num%2==0 and num!=0:
        print("{} is even".format(num))
    elif num!=0:
        print("{} is odd".format(num))

num=5
if num%num==0 and num!=0:
        print("{} is even".format(num))
elif num!=0:
        print("{} is odd".format(num))"""

"""num=5
for x in range(1,num):
 if num%x!=0 and x!=1:
  print("{} is a not prime number".format(num))
 else:
    print("{} is a  prime number".format(num))
"""
"""dxfcjhhvi
jbjikb
kp"""
import pandas as pd
xml_f=pd.read_xml("org.xml")

print(xml_f)



