import sys
sys.path.append('../')
sys.path.append('../lib')
from send_request import send_request
import config
import socket
from http.client import HTTPResponse

# test rfc7230 section 3.2.4: Field Parsing

def run():
    request_headers = []
    expected_status = []

    # space between header-field and colon
    request_header = 'GET / HTTP/1.1\r\nHost :{}\r\n\r\n'.format(config.SERVER_ADDR)
    http_response = send_request(request_header)
    if http_response.status != 400:
            print('error: {}'.format(__file__))
            print('expected status: {}, actual status: {}'.format('400', str(http_response.status)))

    request_header = 'GET / HTTP/1.1\r\nHost:{}\r\nAccept-Language :hyeyoo\r\n\r\n'.format(config.SERVER_ADDR)
    http_response = send_request(request_header)
    if http_response.status != 400:
            print('error: {}'.format(__file__))
            print('expected status: {}, actual status: {}'.format('400', str(http_response.status)))

    # too long header
    # not necessarily 400, it can be 4XX
    long_text = 'A' * 10000000
    request_header = 'GET / HTTP/1.1\r\nHost:{}\r\nUser-Agent:{}\r\n\r\n'.format(config.SERVER_ADDR, long_text)
    http_response = send_request(request_header)
    if http_response.status / 100 != 4:
            print('error: {}'.format(__file__))
            print('expected status: {}, actual status: {}'.format('4XX', str(http_response.status)))

if __name__ == '__main__':
    run()