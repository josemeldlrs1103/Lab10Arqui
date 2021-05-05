from flask import Flask, jsonify, request, render_template
import requests
import time
import mysql.connector as mariadb
from datetime import datetime
#Conexión a MariaDB
MariaConnect=mariadb.connect(user='a725e7_baselab',password='Sanpabl0',database='db_a725e7_baselab',host='mysql5038.site4now.net')
MCursor=MariaConnect.cursor()
#Instancia aplicación flask
app = Flask(__name__)
#Variables globales
entrada = None
codigo = ''
entradaPi = ''
numeroPi = 0
total = 0

#LAB-10
@app.route('/', methods =["GET", "POST"])
def lab10():
    if request.method == "POST":
        global entrada, entradaPi
        entrada = request.form.get("entrada")
    return render_template("entrada.html", data=entradaPi)

@app.route('/lab10', methods =["GET", "POST"])
def lab10Pi():
    if request.method == "POST":
        resp = request.get_json()
        global entradaPi, entrada, total
        entradaPi = resp['pi']
        total = int(str(entradaPi), 2) - int(entrada)
        print(int(str(entradaPi), 2))
        print(entrada)
        print(total)
        if entrada is not None:
            extra = '0'
            aux = total
            if total >= 10:
                total = total - 10
                extra = '1'
            CodigosDisplay()
            return jsonify({'r': extra,'display': codigo,'total': aux}), 201
    return jsonify({ 'r': '0' }), 201

def CodigosDisplay():
    global codigo,total
    if total == 0:
        codigo = '1111110'
    if total == 1:
        codigo = '0110000'
    if total == 2:
        codigo = '1101101'
    if total == 3:
        codigo = '1111001'
    if total == 4:
        codigo = '0110011'
    if total == 5:
        codigo = '1011011'
    if total == 6:
        codigo = '1011111'
    if total == 7:
        codigo = '1110000'
    if total == 8:
        codigo = '1111111'
    if total == 9:
        codigo = '1110011'
    return

if __name__ =="__main__":
    app.run(host='0.0.0.0', port=8080)    