import asyncore                                                                                          
import socket                                                                                            
import logging
from logging.handlers import RotatingFileHandler
import os

host = ''
port1 = 22335
port2 = 11331
port3 = 33456
port4 = 22456                                                                             

#logging.getLogger("asyncore").setLevel(logging.DEBUG)

# создаем папку если его нет 
if not os.path.exists('logs'):
    try:
        os.mkdir('logs')
    except Exception as my_error:
        print(f"Ошибка: {my_error}") #debug

# устанавливаем стандартные параметры логирования
logging.basicConfig(
    filename='logs/socket-asyncore.log', 
    level=logging.INFO, 
    format=f'%(asctime)s %(levelname)s %(name)s %(threadName)s : %(message)s',
    datefmt='%d-%m-%Y %H:%M:%S'
)

class EchoHandler(asyncore.dispatcher_with_send):                                                        
    def handle_read(self):                                                                            
        data = self.recv(1024)                                                                    
        if data == "close":self.close()
        self.send(data)                                                              

class EchoServer(asyncore.dispatcher):                                                                    

    def __init__(self, host, port1):                                                                  
        asyncore.dispatcher.__init__(self)                                                        
        self.create_socket(socket.AF_INET, socket.SOCK_STREAM)                                    
        self.set_reuse_addr()                                                                    
        self.bind((host, port1))                                                                  
        self.listen(15)                                                                          

    def handle_accept(self):                                                                          
        pair = self.accept()                                                                      
        if pair is not None:                                                                      
            sock, addr = pair                                                                
            print ('conn', addr)
            handler = EchoHandler(sock)                                                      

server = EchoServer(host, port1) 
server2 = EchoServer(host, port2)                                                                         
server3 = EchoServer(host, port3)                                                                         
server4 = EchoServer(host, port4)                                                                         
asyncore.loop() 