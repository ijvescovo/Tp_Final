from flask import Flask, render_template, request, redirect, url_for # type: ignore
from TpFinal import conectar_db, inicializar_bbdd, registrar_producto, buscar_producto, actualizar_producto, eliminar_producto, listar_productos

app = Flask(__name__)

@app.before_first_request
def setup():
    conexion = conectar_db()
    inicializar_bbdd(conexion)
    conexion.close()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        nombre = request.form['nombre']
        descripcion = request.form['descripcion']
        cantidad = int(request.form['cantidad'])
        precio = float(request.form['precio'])
        categoria = request.form['categoria']
        conexion = conectar_db()
        codigo = registrar_producto(conexion, nombre, descripcion, cantidad, precio, categoria)
        conexion.close()
        if codigo:
            return redirect(url_for('index'))
    return render_template('register.html')

@app.route('/search', methods=['GET', 'POST'])
def search():
    producto = None
    if request.method == 'POST':
        codigo = request.form['codigo']
        conexion = conectar_db()
        producto = buscar_producto(conexion, codigo)
        conexion.close()
    return render_template('search.html', producto=producto)

@app.route('/update', methods=['GET', 'POST'])
def update():
    if request.method == 'POST':
        codigo = request.form['codigo']
        nueva_cantidad = int(request.form['cantidad'])
        conexion = conectar_db()
        actualizado = actualizar_producto(conexion, codigo, nueva_cantidad)
        conexion.close()
        if actualizado:
            return redirect(url_for('index'))
    return render_template('update.html')

@app.route('/delete', methods=['GET', 'POST'])
def delete():
    if request.method == 'POST':
        codigo = request.form['codigo']
        conexion = conectar_db()
        eliminado = eliminar_producto(conexion, codigo)
        conexion.close()
        if eliminado:
            return redirect(url_for('index'))
    return render_template('delete.html')

@app.route('/list')
def list_products():
    conexion = conectar_db()
    productos = listar_productos(conexion)
    conexion.close()
    return render_template('list.html', productos=productos)

if __name__ == '__main__':
    app.run(debug=True)