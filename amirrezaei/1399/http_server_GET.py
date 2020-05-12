from http.server import BaseHTTPRequestHandler
from urllib import parse


class GetHandler(BaseHTTPRequestHandler):

    def do_GET(self):
        parsed_path = parse.urlparse(self.path)
        massage_parts = open('CV.html', 'r', encoding='utf-8')
        massage_parts.readline()
        self.send_response(200)
        self.send_header('Content-Type',
                         'text/plain; charset=utf-8')
        self.end_headers()
        massage_parts.close()


if __name__ == '__main__':
    from http.server import HTTPServer
    server = HTTPServer(('localhost', 8002), GetHandler)
    print('Starting server, use <Ctrl-C> to stop')
    server.serve_forever()