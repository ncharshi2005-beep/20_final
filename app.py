from http.server import SimpleHTTPRequestHandler, HTTPServer

class Calculator:
    def add(self, a, b):
        return a + b

class MyHandler(SimpleHTTPRequestHandler):
    def do_GET(self):
        calc = Calculator()
        result = calc.add(10, 5) # Example calculation
        
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        # Visual output for the browser
        display = f"<html><body><h1>Calculator Web App</h1><p>Result of 10 + 5 is: {result}</p></body></html>"
        self.wfile.write(display.encode())

if __name__ == "__main__":
    server = HTTPServer(("0.0.0.0", 5020), MyHandler)
    print("Server running on port 8080...")
    server.serve_forever()
