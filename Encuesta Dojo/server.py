from flask import Flask, render_template, request, session, redirect

app = Flask(__name__)
app.secret_key = 'mysecretkey'

@app.route("/", methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        session['nombre'] = request.form['nombre']
        session['ubicacion'] = request.form['ubicacion']
        session['lenguaje'] = request.form['lenguaje']
        session['comentario'] = request.form['comentario']
        return redirect('/result')
    return render_template('index1.html')

@app.route("/process", methods=['POST'])
def process():
    session['nombre'] = request.form['nombre']
    session['ubicacion'] = request.form['ubicacion']
    session['lenguaje'] = request.form['lenguaje']
    session['comentario'] = request.form['comentario']
    return redirect("/result")

@app.route("/result")
def result():
    nombre = session.get('nombre')
    ubicacion = session.get('ubicacion')
    lenguaje = session.get('lenguaje')
    comentario = session.get('comentario')
    return render_template('index2.html', nombre=nombre, ubicacion=ubicacion, lenguaje=lenguaje, comentario=comentario)



if __name__=="__main__":
    app.run(debug=True, port=5001)