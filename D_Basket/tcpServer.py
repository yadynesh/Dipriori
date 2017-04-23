# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import socket
import pandas as pd
import pickle as pickle
def Main():
    host = " "
    port = 53
    s = socket.socket()
    s.bind((host,port))
    print("Server started")
    while True:
        data1 = pd.Series();
        data2 = pd.Series();
        data5 = pd.Series();
        s.listen(1)
        print("Server listening")
        
        c1, addr1 = s.accept()
        print ("Connection from :"+str(addr1))
        c2, addr2 = s.accept()
        print ("Connection from :"+str(addr2))
        c3, addr3 = s.accept()
        print ("Connection from :"+str(addr3))
        
        
        data3 = c1.recv(5000000000)
        data1 = pickle.loads(data3)
        
        data4 = c2.recv(5000000000)
        data2 = pickle.loads(data4)
        
        data6 = c3.recv(5000000000)
        data5 = pickle.loads(data6)
        
        
        
        print(data1)
        print(data2)
        print(data5)
        
        global_item_set = (data1+data2+data5)/3
        global_frequent_item_set = global_item_set[global_item_set>=2000]
        
        print(global_frequent_item_set)
      
        c1.send(pickle.dumps(global_frequent_item_set))
        c2.send(pickle.dumps(global_frequent_item_set))
        c3.send(pickle.dumps(global_frequent_item_set))
    
    c1.close()
    c2.close()
    c3.close()
    
    
if __name__ == '__main__':
    Main()