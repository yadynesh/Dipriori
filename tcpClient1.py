"""
Created on Wed Feb  1 18:13:25 2017

@author: yadynesh
"""

import socket
import pandas as pd
import pickle as pickle
def Main():
    host = '127.0.0.1'
    port = 5000
    
    df = pd.Series([1,2,3],index = ['a','b','c'])
    
    s = socket.socket()
    s.connect((host,port))
    
    message = input("Enter\n")
    while message != 'q':
        s.send(pickle.dumps(df))
        data = s.recv(1024)
        print("Recieved from server"+str(data))
        message = input("Enter\n")
    s.close()

if __name__ == '__main__':
    Main()