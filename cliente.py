#Importando as bibliotecas
import socket
import threading
import sys
import pickle
#a biblioteca pickle nos permite serializar as mensagens para poder envie-os na forma de bytes.

#criação do soquete, e o thread para ler as mensagens 
class Cliente():
  def __init__(self, host="localhost", port=3000):
    self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    self.sock.connect((str(host), int(port)))

    msg_recv = threading.Thread(target = self.msg_recv)
    msg_recv.daemon = True
    msg_recv.start()

#ciclo que manterá o thread principal ativo, que permitirá escrever as mensagens.
    while True:
      msg = input("-> ")
      if msg.lower() != "sair":
        self.send_msg(msg)
      else:
        self.sock.close
        sys.exit()

#loop que ficara exibindo na tela as mensagens enviadas pelo servidor.
  def msg_recv(self):
    while True:
      try:
        data = self.sock.recv(1024)
        if data:
          print(pickle.loads(data))
      except:
        pass
#testaannndddooo
#função para enviar as mensagens
  def send_msg(self, msg):
    self.sock.send(pickle.dumps(msg))

c = Cliente()