import sys
sys.path.append('../')
import config
import socket
from http.client import HTTPResponse

def send_request(request_header, target_status, file):
	try:
		client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		client.connect((config.SERVER_ADDR, config.SERVER_PORT))
		client.send(request_header.encode())
		# read and parse http response
		http_response = HTTPResponse(client)
		http_response.begin()
		if http_response.status != target_status:
			print(f"\033[31mError with request:\033[0m\n{request_header[:-4][:100]}\n in file: {format(file)}")
			print('Expected status: {}\nReceived status: {}'.format(str(target_status), str(http_response.status)))
		else:
			print("\033[35mSuccess\033[0m")
	except Exception as e:
		print("\033[31;1mError sending request:\033[0m")
		print(e);
