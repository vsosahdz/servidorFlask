from flask import Flask, request, jsonify
import numpy as np
from joblib import load

#Cargar el modelo
dt = load('modelo.joblib')

#Generar el servidor (Back-end)
servidorWeb = Flask(__name__)


@servidorWeb.route('/modelo', methods=['POST'])
def modelo():
    #Procesar datos de entrada 
    contenido = request.json
    print(contenido)
    datosEntrada = np.array([
            contenido['pH'],
            contenido['sulphates'],
            contenido['alcohol']
        ])
    #Utilizar el modelo
    resultado=dt.predict(datosEntrada.reshape(1,-1))
    #Regresar la salida del modelo
    return jsonify({"Resultado":str(resultado[0])})

if __name__ == '__main__':
    servidorWeb.run(debug=False,host='0.0.0.0',port='8082')
