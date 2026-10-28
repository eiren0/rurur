from http.server import BaseHTTPRequestHandler, HTTPServer
from sklearn.datasets import load_iris
from sklearn.neighbors import KNeighborsClassifier

iris = load_iris()
model = KNeighborsClassifier(n_neighbors=3)
model.fit(iris.data, iris.target)

class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        prediction = model.predict([[5.1, 3.5, 1.4, 0.2]])
        result = iris.target_names[prediction[0]]
        self.send_response(200)
        self.send_header("Content-type", "text/plain; charset=utf-8")
        self.end_headers()
        self.wfile.write(f"Модель определила класс цветка: {result}".encode("utf-8"))

HTTPServer(("0.0.0.0", 8000), Handler).serve_forever()
