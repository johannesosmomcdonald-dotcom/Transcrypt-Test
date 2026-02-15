from http.server import ThreadingHTTPServer, SimpleHTTPRequestHandler

SimpleHTTPRequestHandler.extensions_map.update({
    ".js": "text/javascript",
    ".mjs": "text/javascript",
})

ThreadingHTTPServer(("localhost", 8000), SimpleHTTPRequestHandler).serve_forever()