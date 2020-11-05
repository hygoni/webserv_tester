import sys
sys.path.append('../')
sys.path.append('../lib')
from send_request import send_request
import config
import socket
from http.client import HTTPResponse

# test rfc7230 section 3.3.2: Content Length

def run():
    request_headers = []
    expected_status = []

    # invalid content length
    length = '-1'
    request_header = 'GET / HTTP/1.1\r\nHost:{}\r\nContent-Length: {}\r\n\r\n'.format(config.SERVER_ADDR, length)
    http_response = send_request(request_header)
    if http_response.status != 400:
            print('error: {}'.format(__file__))
            print('expected status: {}, actual status: {}'.format('400', str(http_response.status)))

    length = '100000000000000000000000'
    request_header = 'GET / HTTP/1.1\r\nHost:{}\r\nContent-Length: {}\r\n\r\n'.format(config.SERVER_ADDR, length)
    http_response = send_request(request_header)
    if http_response.status != 400:
            print('error: {}'.format(__file__))
            print('expected status: {}, actual status: {}'.format('400', str(http_response.status)))

    length = 'NOTDIGIT'
    request_headers.append('GET / HTTP/1.1\r\nHost:{}\r\nContent-Length: {}\r\n\r\n'.format(config.SERVER_ADDR, length))
    expected_status.append(400)

    # Content-Length with Transfer-Encoding
    length = '0'
    request_header = 'GET / HTTP/1.1\r\nHost:{}\r\nContent-Length: -1\r\nTransfer-Encoding: chunked\r\n\r\n0\r\n\r\n'.format(config.SERVER_ADDR, length)
    http_response = send_request(request_header)
    if http_response.status != 200:
            print('error: {}'.format(__file__))
            print('expected status: {}, actual status: {}'.format('200', str(http_response.status)))

if __name__ == '__main__':
    run()
