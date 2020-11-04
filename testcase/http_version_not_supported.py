import sys
sys.path.append('../')
import config
import socket
from http.client import HTTPResponse

# use raw socket to modify http version
def run():
    # send http header
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((config.SERVER_ADDR, config.SERVER_PORT))
    request_header = 'GET / HTTP/0.1\r\nHost:{}\r\n\r\n'.format(config.SERVER_ADDR)
    client.send(request_header.encode())
   
    # read and parse http response
    http_response = HTTPResponse(client)
    http_response.begin()
    # 505 error is expected for invalid http version
    if http_response.status != 505:
        print('error: {}'.format(__file__))
        print('expected status: {}, actual status: {}'.format('505', str(http_response.status)))
