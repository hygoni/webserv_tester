import sys
sys.path.append('../')
import config
import socket
from http.client import HTTPResponse

def send_request(request_header):
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((config.SERVER_ADDR, config.SERVER_PORT))
    client.send(request_header.encode())
    # read and parse http response
    http_response = HTTPResponse(client)
    http_response.begin()
    return http_response
