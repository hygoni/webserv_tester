import sys
sys.path.append('../')
sys.path.append('../lib')
from send_request import send_request
import config
import socket
from http.client import HTTPResponse

# test rfc7230 section 3.3.1: Request Line

def run():
    request_headers = []
    expected_status = []

    # multiple spaces
    request_header = 'GET  /  HTTP/1.1\r\nHost:{}\r\n\r\n'.format(config.SERVER_ADDR)
    http_response = send_request(request_header)
    if http_response.status != 400:
        print('error: {}'.format(__file__))
        print('expected status: {}, actual status: {}'.format('400', str(http_response.status)))

    # too long URI
    target = '/' + 'A' * (config.MAX_URI_LENGTH - 1)
    request_header = 'GET {} HTTP/1.1\r\nHost:{}\r\n\r\n'.format(target, config.SERVER_ADDR)
    http_response = send_request(request_header)
    if http_response.status != 414:
        print('error: {}'.format(__file__))
        print('expected status: {}, actual status: {}'.format('414', str(http_response.status)))

if __name__ == '__main__':
    run()
