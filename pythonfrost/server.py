import socket
from router import routes, route, handle_request
import threading
from response import *

RED = "\033[31m"
BLUE = "\033[36m"
YELLOW = "\033[33m"
GREEN = "\033[32m"
MAGENTA = "\033[35m"
RESET = "\033[0m"

class Server:
    def __init__(self, host='127.0.0.1', port=8080):
        self.ip = host
        self.port = port
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_socket.bind((self.ip, self.port))
        self.server_socket.listen(5)

        print(f"\n{RED}Web server is up and running!{RESET}")
        print(f"{BLUE}You can access it on {YELLOW}http://{host}:{port}{RESET}")

        self.run()
        self.server_socket.close()



    def handle_client(self, client_socket):
        try:
            request = client_socket.recv(4096).decode('utf-8', errors='replace')
            if not request:
                return

            request_lines = request.splitlines()
            request_line = request_lines[0]
            method, path, version = request_line.split()

            headers = {}
            i = 1
            while i < len(request_lines) and request_lines[i]:
                if ":" in request_lines[i]:
                    key, value = request_lines[i].split(":", 1)
                    headers[key.strip()] = value.strip()
                i += 1

            content_length = int(headers.get("Content-Length", 0))
            body_bytes = b""
            if content_length > 0:
                body_bytes = request.split("\r\n\r\n", 1)[1].encode("utf-8")

            handler_result = handle_request(method, path, body_bytes)

            response = make_response(handler_result)
            client_socket.sendall(response)

        finally:
            client_socket.close()


    def run(self):
        while True:
            client_socket, client_address = self.server_socket.accept()
            print(f"\n\n{GREEN}New Connection: {MAGENTA}{client_address[0]}:{client_address[1]}{RESET}")
            
            threading.Thread(target=self.handle_client, args=(client_socket,)).start()