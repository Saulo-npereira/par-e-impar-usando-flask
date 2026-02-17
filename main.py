from flask import Flask, render_template, request

app = Flask(__name__)

numerospares = []
numerosimpares = []
numeros1 = []
@app.route('/', methods = ['POST', 'GET'])
def numeros():
    numeros1.clear()
    numerospares.clear()
    numerosimpares.clear()
    if request.method == 'POST':
        numero = request.form['numero']
        numerostr = str(numero)
        for i in numerostr:
            if int(i) % 2 == 0:
                numerospares.append(i)
                numeros1.append(i + '- PAR')
            else:
                numerosimpares.append(i)
                numeros1.append(i + '- IMPAR')

        '''for i in numerostr:
            if int(i) % 2 == 0:
                print('a')
            else:
                print('b')'''
        return render_template('home.html', numerospares=numerospares,
                                numerosimpares=numerosimpares,
                                numeros1=numeros1
                                  )
        
    return render_template('home.html')

if __name__ == '__main__':
    app.run(debug=True)