import socket

# Define the host as a tuple

HOST, PORT = "", 8080,
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.bind((HOST,PORT))
s.listen(True)

print("Serving HTTP on port %s.." %PORT);

while True:
    client_connection, client_address = s.accept();
    request = client_connection.recv(1024);  # Buffer Size
    print(request.decode("utf-8"));  # Display the HTTP request
    http_response = """/

HTTP/1.1 200 OK

Welcome to Group10 Website !
"""
    client_connection.sendall(bytes(http_response, "utf-8"))
    client_connection.close();
