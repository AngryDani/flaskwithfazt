from flask import Flask, render_template

app = Flask(__name__) # Inicializar Flash + confirmar que es el archivo principal, se guarda en la variable app (crear rutas del servidor + url)

# Crear una ruta con un decorador
@app.route('/') #creo una ruta para la página principal
def home():
    return render_template("home.html") #el archivo html está en la carpeta "templates"

@app.route('/about') # Creando el ABOUT localhost:5000/about
def about():
    return render_template("about.html")

# Creamos la carpeta templates para almacenar los documenetos html e importamos render_template













if __name__=="__main__":
    app.run(debug= True) # para evitar estar reiniciando el servidor y ver los cambios en tiempo real agregamos el debug (modo de prueba)



