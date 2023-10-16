import sys
sys.path.append('../')
sys.path.append('../lib')
from send_request import send_request
import config
import socket
from http.client import HTTPResponse

# test rfc7230 section 5.4 Host

def run():

	# no host
	print("_____________________")
	print("no host")
	request_header = 'GET / HTTP/1.1\r\n\r\n'
	send_request(request_header, 400, __file__)

	# multiple host
	print("_____________________")
	print("multiple host")
	request_header = 'GET / HTTP/1.1\r\nHost: naver.com\r\nHost: hyeyoo.com\r\n\r\n'
	send_request(request_header, 400, __file__)

	# multiple host 2
	print("_____________________")
	print("multiple host")
	request_header = 'GET / HTTP/1.1\r\nHost: {}\r\nHost: {}\r\n\r\n'.format(config.SERVER_ADDR, config.SERVER_ADDR)
	send_request(request_header, 400, __file__)

	# invalid field value in host
	print("_____________________")
	print("invalid field value in host")
	request_header = 'GET / HTTP/1.1\r\nHost: hyeyoo@hyeyoo.com\r\n\r\n'
	send_request(request_header, 400, __file__)

if __name__ == '__main__':
	run()
