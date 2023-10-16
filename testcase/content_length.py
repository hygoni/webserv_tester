import sys
sys.path.append('../')
sys.path.append('../lib')
from send_request import send_request
import config
import socket
from http.client import HTTPResponse

# test rfc7230 section 3.3.2: Content Length

def run():

	# invalid content length
	print("_____________________")
	print("invalid content length")
	length = '-1'
	request_header = 'GET / HTTP/1.1\r\nHost:{}\r\nContent-Length: {}\r\n\r\n'.format(config.SERVER_ADDR, length)
	send_request(request_header, 400, __file__)

	print("_____________________")
	print("invalid content length")
	length = '100000000000000000000000'
	request_header = 'GET / HTTP/1.1\r\nHost:{}\r\nContent-Length: {}\r\n\r\n'.format(config.SERVER_ADDR, length)
	send_request(request_header, 400, __file__)

	print("_____________________")
	print("invalid content length")
	length = 'NOTDIGIT'
	request_header = 'GET / HTTP/1.1\r\nHost:{}\r\nContent-Length: {}\r\n\r\n'.format(config.SERVER_ADDR, length)
	send_request(request_header, 400, __file__)

	# Content-Length with Transfer-Encoding
	# Transfer-Encoding overrides Content-Length
	print("_____________________")
	print("content length with Transfer-Encoding")
	request_header = 'GET / HTTP/1.1\r\nHost:{}\r\nContent-Length: 10000\r\nTransfer-Encoding: chunked\r\n\r\n0'.format(config.SERVER_ADDR)
	send_request(request_header, 200, __file__)

	# multiple Content-Length differing size
	print("_____________________")
	print("multiple Content-Length differing size")
	request_header = 'GET / HTTP/1.1\r\nHost:{}\r\nContent-Length: 1\r\nContent-Length: 0\r\n\r\n'.format(config.SERVER_ADDR)
	send_request(request_header, 400, __file__)

if __name__ == '__main__':
	run()
