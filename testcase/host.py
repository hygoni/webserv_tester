import sys
sys.path.append('../')
sys.path.append('../lib')
from send_request import send_request
import config
import socket
from http.client import HTTPResponse

# test rfc7230 section 5.4 Host

def run():
    print('testing {}...'.format(__file__))

    # no host
    request_header = 'GET / HTTP/1.1\r\n\r\n'
    http_response = send_request(request_header)
    if http_response.status != 400:
            print('error: {}'.format(__file__))
            print('expected status: {}, actual status: {}'.format('400', str(http_response.status)))

    # multiple host
    request_header = 'GET / HTTP/1.1\r\nHost: naver.com\r\nHost: hyeyoo.com\r\n\r\n'
    http_response = send_request(request_header)
    if http_response.status != 400:
            print('error: {}'.format(__file__))
            print('expected status: {}, actual status: {}'.format('400', str(http_response.status)))

    # multiple host 2
    request_header = 'GET / HTTP/1.1\r\nHost: {}\r\nHost: {}\r\n\r\n'.format(config.SERVER_ADDR, config.SERVER_ADDR)
    http_response = send_request(request_header)
    if http_response.status != 400:
            print('error: {}'.format(__file__))
            print('expected status: {}, actual status: {}'.format('400', str(http_response.status)))


    # invalid field value in host
    request_header = 'GET / HTTP/1.1\r\nHost: hyeyoo@hyeyoo.com\r\n\r\n'
    http_response = send_request(request_header)
    if http_response.status != 400:
            print('error: {}'.format(__file__))
            print('expected status: {}, actual status: {}'.format('400', str(http_response.status)))

if __name__ == '__main__':
    run()
