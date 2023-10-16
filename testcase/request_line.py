import sys
sys.path.append('../')
sys.path.append('../lib')
from send_request import send_request
import config
import socket
from http.client import HTTPResponse

# test rfc7230 section 3.3.1: Request Line

def run():

	# multiple spaces
	print("_____________________")
	print("Multiple spaces:")
	request_header = 'GET  /  HTTP/1.1\r\nHost:{}\r\n\r\n'.format(config.SERVER_ADDR)
	send_request(request_header, 400, __file__)
	

	# too long URI
	print("_____________________")
	print("too long URI:")
	target = '/' + 'A' * (config.MAX_URI_LENGTH - 1)
	request_header = 'GET {} HTTP/1.1\r\nHost:{}\r\n\r\n'.format(target, config.SERVER_ADDR)
	send_request(request_header, 414, __file__)

if __name__ == '__main__':
	run()
