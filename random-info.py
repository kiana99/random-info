import time 
import csv
from faker import Faker
import random
import ipaddress
network = ipaddress.IPv4Network("192.168.0.0/22")
fake = Faker()
services=[1,3,5,None]
names = ['John', 'Sophia','Maria','Kim','Nelson','Patrick','Henderson','Son','Arnold','Salah']



with open('new.csv','w', newline='') as file:
    writer = csv.writer(file,delimiter=';')
    #writer.writerow(["id", "name", "service", "ip", "ts"])

    for i in range(1,1001):
        name = random.choice(names)
        service = random.choice(services)
        ip = random.choice(list(network.hosts()))
        ts = int(time.time())
        row = [name, service, ip, ts]

        writer.writerow(row)
        time.sleep(1)



        
