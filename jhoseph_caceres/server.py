from http.server import HTTPServer, SimpleHTTPRequestHandler

# Directorio donde se encuentran los archivos estáticos
static_dir = "assets/image/jose.jpg"

# Configuración del servidor
server_address = ("", 8000)  # Puerto en el que el servidor estará escuchando

# Crear el servidor HTTP
httpd = HTTPServer(server_address, SimpleHTTPRequestHandler)

# Configurar el directorio base para servir archivos estáticos
SimpleHTTPRequestHandler.directory = static_dir

# Iniciar el servidor
print("Servidor iniciado en http://localhost:8000/")
httpd.serve_forever()
