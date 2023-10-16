import sys
sys.path.append('../')
sys.path.append('../lib')
from send_request import send_request
import config
import socket
from http.client import HTTPResponse

# test rfc7230 section 2.6: Protocol Versioning

def run():

	# send http header
	print("_____________________")
	print("http version 0.1:")
	request_header = 'GET / HTTP/0.1\r\nHost:{}\r\n\r\n'.format(config.SERVER_ADDR)
	send_request(request_header, 505, __file__)

if __name__ == '__main__':
	run()
