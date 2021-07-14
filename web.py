from http.server import HTTPServer, BaseHTTPRequestHandler
import todo
import json


class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        print("Just received a GET request")
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()

        todos = todo.List()
        print(todos)


        sample_dataset = {
                            "id": "bigqueryproject:datasetname",
                            "datasetReference": {
                                "datasetId": "datasetname",
                                "projectId": "bigqueryproject"
                            }
                        }
        self.wfile.write(json.dumps([todos]).encode("utf-8"))



def run(server_class=HTTPServer, handler_class=BaseHTTPRequestHandler):
    server_address = ('', 8000)
    httpd = server_class(server_address, handler_class)
    httpd.serve_forever()

def main():
    print("hello world!")
    run(handler_class=SimpleHTTPRequestHandler)

if __name__ == "__main__":
    main()
