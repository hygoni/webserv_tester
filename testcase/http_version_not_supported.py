import sys
sys.path.append('../')
sys.path.append('../lib')
from send_request import send_request
import config
import socket
from http.client import HTTPResponse

# test rfc7230 section 2.6: Protocol Versioning

def run():
    print('testing {}...'.format(__file__))
    
    # send http header
    request_header = 'GET / HTTP/0.1\r\nHost:{}\r\n\r\n'.format(config.SERVER_ADDR)
   
    http_response = send_request(request_header)
    # 505 error is expected for invalid http version
    if http_response.status != 505 and http_response.status // 100 != 4:
        print('error: {}'.format(__file__))
        print('expected status: {}, actual status: {}'.format('505 or 4XX', str(http_response.status)))

if __name__ == '__main__':
    run()
