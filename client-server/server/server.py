from http.server import HTTPServer, BaseHTTPRequestHandler
import json

class PenManager:
    name = 'pen'
    pens[]

    def get_all_pens(self):
        return self.pens

    def add_pen(self, suffix):
        self.pens.append(cls.name + suffix)


class RequestHandler(BaseHTTPRequestHandler):
    def GET(self):
        self.send_response(200)
        self.end_headers()
        self.wfile.write(json.dumps(PenManager.get_all_pens()).encode())

    def POST(self):
        content_length = int(self.headers['Content-Length'])
        text_input = self.rfile.read(content_length).decode()
        new_pen = json.loads(text_input)['pen']
        PenManager.add_pen(new_pen)
        self.send_response(201)
        self.end_headers()
        self.wfile.write('Pen created')


def setup():
    PORT = 3001
    server_address = ('0.0.0.0', PORT)
    httpd = HTTPServer(server_address, RequestHandler)
    httpd.serve_forever()
    print('Server running at port: $1', PORT)