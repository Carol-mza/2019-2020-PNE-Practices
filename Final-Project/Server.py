import http.server
import socketserver
import termcolor
from pathlib import Path
import json

Port = 8080
server = "rest.ensembl.org"
connection = http.client.HTTPConnection(server)
parameter = "content-type=application/json"

socketserver.TCPServer.allow_reuse_address = True # Prevent-> "PORT ALREADY IN USE"

class TestHandler(http.server.BaseHTTPRequestHandler):

    def do_GET(self):
        termcolor.cprint(self.requestline, "green")

        req = self.requestline.split(" ")
        path = req[1]
        first_arg = path.split("?")[0]

        contents = Path("Error.html").read_text()
        status = 404

        try:

            if path == "/":
                contents = Path("list_species.html").read_text()
                contents += Path("info_karyotype.html").read_text()
                contents += Path("chromosome_length.html").read_text()
                status = 200

            if first_arg == "/listSpecies":
                contents = 



#----------| MAIN PROGRAM |----------

Handler = TestHandler

with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print("Serving at PORT:", port)

    try:
        httpd.serve_forever()

    except KeyboardInterrupt:
        print()
        termcolor.cprint("Server stopped by user!", "yellow")

        httpd.server_close()