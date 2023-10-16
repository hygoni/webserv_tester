import sys
sys.path.append('../')
sys.path.append('../lib')
from send_request import send_request
import config
import socket
from http.client import HTTPResponse

# test rfc7230 section 3.2.4: Field Parsing

def run():

	# space between header-name and colon
	print("_____________________")
	print("space between header-name and colon:")
	request_header = 'GET / HTTP/1.1\r\nHost :{}\r\n\r\n'.format(config.SERVER_ADDR)
	send_request(request_header, 400, __file__)

	print("_____________________")
	print("space between header-name and colon:")
	request_header = 'GET / HTTP/1.1\r\nHost:{}\r\nAccept-Language :hyeyoo\r\n\r\n'.format(config.SERVER_ADDR)
	send_request(request_header, 400, __file__)

	# too long header
	# not necessarily 400, it can be 4XX
	print("_____________________")
	print("too long header:")
	long_text = 'A' * 1000000000
	request_header = 'GET / HTTP/1.1\r\nHost:{}\r\nUser-Agent:{}\r\n\r\n'.format(config.SERVER_ADDR, long_text)
	send_request(request_header, 400, __file__)

	# empty header name
	print("_____________________")
	print("empty header name:")
	request_header = 'GET / HTTP/1.1\r\nHost:{}\r\n:empty_name\r\n\r\n'.format(config.SERVER_ADDR)
	send_request(request_header, 400, __file__)

if __name__ == '__main__':
	run()
