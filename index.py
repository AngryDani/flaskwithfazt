from flask import Flask, render_template

app = Flask(__name__) # Inicializar Flash + confirmar que es el archivo principal, se guarda en la variable app (crear rutas del servidor + url)

# Crear una ruta con un decorador
@app.route('/') #creo una ruta para la página principal
def home():
    return render_template("home.html")

@app.route('/about') # Creando el ABOUT localhost:5000/about
def about():
    return "ABOUT: @ANGRYDANY"

# Creamos la carpeta templates para almacenar los documenetos html e importamos render_template













if __name__=="__main__":
    app.run()



