from flask import Flask

app = Flask(__name__) # Inicializar Flash + confirmar que es el archivo principal, se guarda en la variable app (crear rutas del servidor + url)

# Crear una ruta con un decorador
@app.route('/') #creo una ruta para la página principal
def home():
    return "Holiwis :D"


if __name__=="__main__":
    app.run()



