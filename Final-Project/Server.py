import http.server
import socketserver
import termcolor
from pathlib import Path
import json
from Seq1 import *
port = 8080
server = "rest.ensembl.org"
connection = http.client.HTTPConnection(server)
parameter = "?content-type=application/json"

socketserver.TCPServer.allow_reuse_address = True # Prevent-> "PORT ALREADY IN USE"

class TestHandler(http.server.BaseHTTPRequestHandler):

    def do_GET(self):
        termcolor.cprint(self.requestline, "green")

        req = self.requestline.split(" ")
        arguments = (req[1]).split("?")
        first_arg = arguments[0]

        contents = Path("Error.html").read_text()
        status = 404

        if first_arg == "/":
            contents = Path("list_species.html").read_text()
            contents += Path("info_karyotype.html").read_text()
            contents += Path("chromosome_length.html").read_text()
            contents += "<h2>Medium level services</h2>"
            contents += Path("gene_seq.html").read_text()
            contents += Path("gene_info.html").read_text()
            contents += Path("gene_calc.html").read_text()
            contents += Path("gene_list.html").read_text()

            status = 200

# ----------| BASIC LEVEL |----------

        elif "/listSpecies" in first_arg:
            status = 200

            contents = """<!DOCTYPE html>
                               <html lang="en">
                               <head>
                                   <meta charset="utf-8">
                                   <title>LIST OF SPECIES</title>
                               </head>
                               <body style="background-color: lightsteelblue;">"""

            endpoint = "info/species"

            second_arg = arguments[1]
            limit = second_arg.split("=")[1]

            try:
                connection.request("GET", endpoint + parameter)

            except ConnectionRefusedError:
                termcolor.cprint("ERROR! It was not possible to connect to the server.", "orange")
                exit()

            res = connection.getresponse()
            body = res.read().decode("utf-8")
            data_dict = json.loads(body)

            list_every_specie = []

            for key, value in data_dict.items():
                if key == "species":
                    for element in value:
                        for k, v in element.items():
                            if k == "display_name":
                                species = v

                                list_every_specie.append(species)

            contents += f"<p>The total number of species in ensembl is: {len(list_every_specie)}</p>"

            if limit != "":
                try:

                    limit = int(limit)
                    contents += f"<p>The limit you have selected is: {limit}</p>"

                    if limit == 0 or limit < 0 or limit > int(len(list_every_specie)):
                        status = 404
                        contents = f"""<!DOCTYPE html>
                                            <html lang = "en">
                                            <head>
                                                <meta charset = "utf-8">
                                                <title>OUT OF RANGE</title>
                                            </head>
                                            <body style="background-color: crimson;">
                                            <h1>ERROR!</h1>
                                            <p>The limit must be between 1 and {len(list_every_specie)}</p>"""

                    else:
                        contents += f"<h3>The species: </h3>"

                        list_species = list_every_specie[: limit]

                        for species in list_species:
                            contents += f"<p> - {species}</p>"

                except ValueError:
                    status = 404
                    contents = f"""<!DOCTYPE html>
                                        <html lang = "en">
                                        <head>
                                            <meta charset = "utf-8">
                                            <title>VALUE ERROR</title>
                                        </head>
                                        <body style="background-color: crimson;">
                                        <h1>ERROR!</h1>
                                        <p>The limit must be A NUMBER</p>"""

            else:
                contents += f"<h3>The species are: </h3>"

                for species in list_every_specie:
                    contents += f"<p> - {species}</p>"

            contents += f"""<a href="/">Main page</a>
                         </body></html>"""


        elif "/karyotype" in first_arg:
            status = 200

            contents = f"""<!DOCTYPE html>
                                <html lang = "en">
                                <head>
                                    <meta charset = "utf-8">
                                    <title>KARYOTYPE</title>
                                </head>
                                <body style="background-color: lightsteelblue;">"""

            endpoint = "/info/assembly/"

            second_arg = arguments[1]
            client_species = second_arg.split("=")[1]

            contents += f"<p>Karyotype of {client_species}</p>"

            endpoint += client_species

            try:
                connection.request("GET", endpoint + parameter)

            except ConnectionRefusedError:
                termcolor.cprint("ERROR! It was not possible to connect to the server.", "orange")
                exit()

            res = connection.getresponse()
            body = res.read().decode("utf-8")
            data_dict = json.loads(body)

            try:
                list_karyotype = list(data_dict["karyotype"])
                if list_karyotype != list():

                    for key, value in data_dict.items():
                        if key == "karyotype":
                            contents += f"<h3>The chromosomes:</h3>"
                            for chromosome in value:
                                if chromosome == "MT":
                                    pass
                                else:
                                    contents += f"<p> - {chromosome}</p>"

                else:
                    status = 404
                    contents = f"""<!DOCTYPE html>
                                        <html lang = "en">
                                        <head>
                                            <meta charset = "utf-8">
                                            <title>KARYOTYPE ERROR</title>
                                        </head>
                                        <body style="background-color: crimson;">
                                        <h1>ERROR!</h1>
                                        <p>Not a valid specie</p>"""

            except KeyError:
                status = 404
                contents = f"""<!DOCTYPE html>
                                    <html lang = "en">
                                    <head>
                                        <meta charset = "utf-8">
                                        <title>KARYOTYPE ERROR</title>
                                    </head>
                                    <body style="background-color: crimson;">
                                    <h1>ERROR!</h1>
                                    <p>Not a valid specie</p>"""

            contents += f"""<a href="/">Main page</a>
                                         </body></html>"""


        elif "/chromosomeLength" in first_arg:
            status = 200

            contents = """<!DOCTYPE html>
                               <html lang="en">
                               <head>
                                   <meta charset="utf-8">
                                   <title>CHROMOSOME LENGTH</title>
                               </head>
                               <body style="background-color: lightsteelblue;">"""

            endpoint = "/info/assembly/"

            second_arg = arguments[1]
            species = second_arg.split("&")[0].split("=")[1]
            chromosome = second_arg.split("&")[1].split("=")[1]

            endpoint += f"{species}/{chromosome}"

            try:
                connection.request("GET", endpoint + parameter)

            except ConnectionRefusedError:
                termcolor.cprint("ERROR! It was not possible to connect to the server.", "orange")
                exit()

            res = connection.getresponse()
            body = res.read().decode("utf-8")
            data_dict = json.loads(body)

            contents += f"<p>The selected species: {species}</p>"
            contents += f"<p>The selected chromosome: {chromosome}"

            length = None

            for key, value in data_dict.items():
                if key == "length":
                    length = value

            if length != None:
                contents += f"<h3>The length of the chromosome is:</h3><p>{length}</p>"

            else:
                status = 404
                contents = f"""<!DOCTYPE html>
                                        <html lang = "en">
                                        <head>
                                            <meta charset = "utf-8">
                                            <title>CHROMOSOME ERROR</title>
                                        </head>
                                        <body style="background-color: crimson;">
                                        <h1>ERROR!</h1>
                                        <p>Try again</p>"""

            contents += f"""<a href="/">Main page</a>
                                     </body></html>"""


# -----------| MEDIUM LEVEL |----------

        elif "/geneSeq" in first_arg:
            status = 200
            try:
                contents = f"""<!DOCTYPE html>
                                    <html lang = "en">
                                    <head>
                                        <meta charset = "utf-8">
                                        <title>GENE SEQUENCE</title>
                                    </head>
                                    <body style="background-color: lightsteelblue;">"""

                endpoint = "xrefs/symbol/homo_sapiens/"

                second_arg = arguments[1]
                gene = second_arg.split("=")[1]

                endpoint += gene

                contents += f"<p>The selected human gene: {gene}</p>"

                try:
                    connection.request("GET", endpoint + parameter)

                except ConnectionRefusedError:
                    termcolor.cprint("ERROR! It was not possible to connect to the server.", "orange")
                    exit()

                res = connection.getresponse()
                body = res.read().decode("utf-8")
                data_dict = json.loads(body)

                gene_id = data_dict[0]
                gene_id = gene_id["id"]

                endpoint_2 = f"sequence/id/{gene_id}"

                try:
                    connection.request("GET", endpoint_2 + parameter)

                except ConnectionRefusedError:
                    termcolor.cprint("ERROR! It was not possible to connect to the server.", "orange")
                    exit()

                res_2 = connection.getresponse()
                body_2 = res_2.read().decode("utf-8")
                data_dict_2 = json.loads(body_2)

                sequence = data_dict_2["seq"]

                contents += f"<h3>The sequence:</h3>"
                contents += f"<p>{sequence}</p>"


            except IndexError:
                status = 404
                contents = f"""<!DOCTYPE html>
                                    <html lang = "en">
                                    <head>
                                        <meta charset = "utf-8">
                                        <title>GENE ERROR</title>
                                    </head>
                                    <body style="background-color: crimson;">
                                    <h1>ERROR!</h1>
                                    <p>Sorry not a valid human gene</p>"""

            except KeyError:
                status = 404
                contents = f"""<!DOCTYPE html>
                                    <html lang = "en">
                                    <head>
                                        <meta charset = "utf-8">
                                        <title>GENE ERROR</title>
                                    </head>
                                    <body style="background-color: crimson;">
                                    <h1>ERROR!</h1>
                                    <p>Sorry not a valid human gene</p>"""

            contents += f"""<a href="/">Main page</a>
                                                </body></html>"""


        elif "/geneInfo" in first_arg:
            status = 200

            try:

                contents = f"""<!DOCTYPE html>
                                    <html lang = "en">
                                    <head>
                                        <meta charset = "utf-8">
                                        <title>GENE INFO</title>
                                    </head>
                                    <body style="background-color: lightsteelblue;">"""

                endpoint = "/xrefs/symbol/homo_sapiens/"

                second_arg = arguments[1]
                gene = second_arg.split("=")[1]

                endpoint += gene

                contents += f"<p>The selected human gene: {gene}</p>"

                try:
                    connection.request("GET", endpoint + parameter)

                except ConnectionRefusedError:
                    termcolor.cprint("ERROR! It was not possible to connect to the server.", "orange")
                    exit()

                res = connection.getresponse()
                body = res.read().decode("utf-8")
                data_dict = json.loads(body)

                gene_id = data_dict[0]
                gene_id = gene_id["id"]

                endpoint_2 = f"lookup/id/{gene_id}"

                try:
                    connection.request("GET", endpoint_2 + parameter)

                except ConnectionRefusedError:
                    termcolor.cprint("ERROR! It was not possible to connect to the server.", "orange")
                    exit()

                res_2 = connection.getresponse()
                body_2 = res_2.read().decode("utf-8")
                data_dict_2 = json.loads(body_2)

                contents += f"<h3>Information:</h3>"

                id = data_dict_2["id"]
                contents += f"<p>Id: {id}</p>"
                chromosome = data_dict_2["seq_region_name"]
                contents += f"Chromosome: {chromosome}</p>"

                start = data_dict_2["start"]
                contents += f"<p>Start of the gene: {start}</p>"
                end = data_dict_2["end"]
                contents += f"<p>End of the gene: {end}</p>"

                length = int(end) - int(start)
                contents += f"<p>The length: {length}</p>"

            except IndexError:
                status = 404
                contents = f"""<!DOCTYPE html>
                                    <html lang = "en">
                                    <head>
                                        <meta charset = "utf-8">
                                        <title>GENE ERROR</title>
                                    </head>
                                    <body style="background-color: crimson;">
                                    <h1>ERROR!</h1>
                                    <p>Not a valid human gene</p>"""

            except KeyError:
                status = 404
                contents = f"""<!DOCTYPE html>
                                    <html lang = "en">
                                    <head>
                                        <meta charset = "utf-8">
                                        <title>GENE ERROR</title>
                                    </head>
                                    <body style="background-color: crimson;">
                                    <h1>ERROR!</h1>
                                    <p>Not a valid human gene</p>"""

            contents += f"""<a href="/">Main page</a>
                                            </body></html>"""


        elif "geneCalc" in first_arg:
            status = 200

            try:
                contents = f"""<!DOCTYPE html>
                                    <html lang = "en">
                                    <head>
                                        <meta charset = "utf-8">
                                        <title>GENE CALCULATIONS</title>
                                    </head>
                                    <body style="background-color: lightsteelblue;">"""

                endpoint = "/xrefs/symbol/homo_sapiens/"

                second_arg = arguments[1]
                gene = second_arg.split("=")[1]

                endpoint += gene

                contents += f"<p>The selected human gene: {gene}</p>"

                try:
                    connection.request("GET", endpoint + parameter)

                except ConnectionRefusedError:
                    termcolor.cprint("ERROR! It was not possible to connect to the server.", "orange")
                    exit()

                res = connection.getresponse()
                body = res.read().decode("utf-8")
                data_dict = json.loads(body)

                gene_id = data_dict[0]
                gene_id = gene_id["id"]

                endpoint_2 = f"sequence/id/{gene_id}"

                try:
                    connection.request("GET", endpoint_2 + parameter)

                except ConnectionRefusedError:
                    termcolor.cprint("ERROR! It was not possible to connect to the server.", "orange")
                    exit()

                res_2 = connection.getresponse()
                body_2 = res_2.read().decode("utf-8")
                data_dict_2 = json.loads(body_2)

                contents += f"<h3>Calculations:</h3>"

                seq = Seq(data_dict_2["seq"]) # Now the sequence is of class Seq

                length = seq.len()
                contents += f"<p>Length: {length}"

                basis_dict = seq.count()

                for key, value in basis_dict.items():
                    contents += f"<p>{key}: {round((value / length) * 100, 2)}%</p>"

            except IndexError:
                status = 404
                contents = f"""<!DOCTYPE html>
                                    <html lang = "en">
                                    <head>
                                        <meta charset = "utf-8">
                                        <title>GENE ERROR</title>
                                    </head>
                                    <body style="background-color: crimson;">
                                    <h1>ERROR!</h1>
                                    <p>Not a valid human gene</p>"""

            except KeyError:
                status = 404
                contents = f"""<!DOCTYPE html>
                                    <html lang = "en">
                                    <head>
                                        <meta charset = "utf-8">
                                        <title>GENE ERROR</title>
                                    </head>
                                    <body style="background-color: crimson;">
                                    <h1>ERROR!</h1>
                                    <p>Not a valid human gene</p>"""

            contents += f"""<a href="/">Main page</a>
                                            </body></html>"""


        elif "/geneList" in first_arg:
            status = 200

            try:

                contents = f"""<!DOCTYPE html>
                                    <html lang = "en">
                                    <head>
                                        <meta charset = "utf-8">
                                        <title>GENE CALCULATIONS</title>
                                    </head>
                                    <body style="background-color: lightsteelblue;">"""

                endpoint = "overlap/region/human/"

                second_arg = arguments[1]
                chromosome = second_arg.split("&")[0].split("=")[1]
                start = second_arg.split("&")[1].split("=")[1]
                end = second_arg.split("&")[2].split("=")[1]

                contents += f"<p>The selected chromosome: {chromosome}</p>"
                contents += f"<p>The start: {start}</p>"
                contents += f"<p>The end: {end}</p>"

                endpoint += f"{chromosome}:{start}-{end}"
                parameter_2 = "?feature=gene;content-type=application/json"

                try:
                    connection.request("GET", endpoint + parameter_2)

                except ConnectionRefusedError:
                    termcolor.cprint("ERROR! It was not possible to connect to the server.", "orange")
                    exit()

                res = connection.getresponse()
                body = res.read().decode("utf-8")
                data_dict = json.loads(body)

                contents += f"<h3>List:</h3>"

                if len(data_dict) != 0:
                    for gene in data_dict:
                        contents += f"""<p> - {gene["external_name"]} </p>"""

                else:
                    status = 404
                    contents = f"""<!DOCTYPE html>
                                        <html lang = "en">
                                        <head>
                                            <meta charset = "utf-8">
                                            <title>REGION ERROR</title>
                                        </head>
                                        <body style="background-color: crimson;">
                                        <h1>ERROR!</h1>
                                        <p>Try again</p>"""
            except TypeError:
                status = 404
                contents = f"""<!DOCTYPE html>
                                    <html lang = "en">
                                    <head>
                                        <meta charset = "utf-8">
                                        <title>CHROMOSOME ERROR</title>
                                    </head>
                                    <body style="background-color: crimson;">
                                    <h1>ERROR!</h1>
                                    <p>Try again</p>"""

            contents += f"""<a href="/">Main page</a>
                                            </body></html>"""


            # Generating response
        self.send_response(status)
        self.send_header("Content-Type", "text/html")
        self.send_header("Content-Length", len(str.encode(contents)))
        self.end_headers()

        self.wfile.write(str.encode(contents))

        return



#----------| MAIN PROGRAM |----------

Handler = TestHandler

with socketserver.TCPServer(("", port), Handler) as httpd:
    print("Serving at PORT:", port)

    try:
        httpd.serve_forever()

    except KeyboardInterrupt:
        print()
        termcolor.cprint("Server stopped by user!", "yellow")

        httpd.server_close()