import socket #cris conexão, fecha conexão e escuta em uma determinada porta

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #ipv4 e tcp
client.settimeout(10)
try:
    client.connect(('127.0.0.1', 4466)) #parametro ip (dns) e porta
    client.send(b'oi\n') #enviar dados - colocar o 'b' na frente para transformar em byte se nao da erro
    pacotes_recebidos = client.recv(1024).decode() #receber dados - colocar o número de bytes
    print(pacotes_recebidos)
except Exception as error:
    print('Um erro ocorreu')
    print(error)