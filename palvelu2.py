# Tästä tulee palvelu

from wsgiref.simple_server import make_server

def app(environ, respond):
    respond('200 OK', [('Content-type', 'text/html; charset=utf-8')])
    yield "Hello w€rld😞!".encode('utf-8')
    polku = environ["PATH_INFO"]
    salanimi = polku.replace("a","aca").replace("i","hani")
    yield "<h1>Huomio</h1>".encode('utf-8')
    yield f"<p>Salainen nimesi on <b>{salanimi}</b></p>".encode('utf-8')
    yield "<form method=GET><input type=button value=paina></form>".encode("utf-8")
    #for key in environ:
    #    yield ("%s: %s\n" % (key, environ[key])).encode('utf-8')


if __name__ == '__main__':
    with make_server("localhost", 8000, app) as server: 
        server.serve_forever()

