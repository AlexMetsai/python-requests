# Alexandros I. Metsai
# alexmetsai@gmail.com
# Serve a directory over HTTP

import http.server
import socketserver

PORT = 8000

handler = http.server.SimpleHTTPRequestHandler

with socketserver.TCPServer(("", PORT), handler) as httpd:
    print("Server started at localhost:" + str(PORT))
    httpd.serve_forever()
