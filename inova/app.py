from flask import Flask, render_template, request, redirect

app = Flask(__name__)

usuario = []

@app.route('/')
def home():
    return render_template('index.html', usuario=usuario)

@app.route('/pegar', methods=['POST'])
def get():
    email = request.form['email']
    matri = request.form['matricula']
    user = [email, matri]
    usuario.append(user)
    
    return redirect('/abono')

@app.route('/abono')
def abono():
    return render_template('abono.html')

if __name__ == '__main__':
    app.run(debug=True)
