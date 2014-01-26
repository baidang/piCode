from bluetooth import * 

# Create the client socket
client_socket = BluetoothSocket(RFCOMM)

client_socket.connect(("00:15:83:3D:0A:57",7))

client_socket.send("Hello, aRou!")

print "finished!"

client_socket.close()
