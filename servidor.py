#importando as bibliotecas
import socket
import threading
import sys
import pickle

#classe servidor para criação do soquete
class Servidor():
  def __init__(self, host="localhost", port=3000):
    self.clientes = []
    self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    self.sock.bind((str(host), int(port)))
    self.sock.listen(10)
    self.sock.setblocking(False)

    aceptar = threading.Thread(target = self.Aceitar)
    processar = threading.Thread(target = self.Manipula)

    aceptar.daemon = True
    aceptar.start()

    processar.daemon = True
    processar.start()

#loop que manterá o thread principal ativo
    while True:
      msg = input("-> ")
      if msg.lower() == "sair":
        self.sock.close()
        sys.exit()
      else:
        pass
      
#função que permite enviar mensagens para todos os clientes conectados         
  def Enviar(self, msg, cliente):
    for c in self.clientes:
      try:
        if c != cliente:
          c.send(msg)
      except:
        self.clientes.remove(c)

#função que aceita as conexões e armazena no vetor cliente
  def Aceitar(self):
    print("ok")
    while True:
      try:
        conn, addr = self.sock.accept()
        conn.setblocking(False)
        self.clientes.append(conn)
      except:
        pass

#função que processa as conexões, e percorre em loop o vetor clientes, Para saber quando o cliente vai receber uma mensagem.
  def Manipula(self):
    print("...ok")
    while True:
      if len(self.clientes) > 0:
        for c in self.clientes:
          try:
            data = c.recv(1024)
            if data:
              self.Enviar(data, c)
          except:
            pass

s = Servidor()