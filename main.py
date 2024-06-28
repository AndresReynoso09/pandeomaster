from flask import Flask, request, jsonify
from flask_cors import CORS
import math

app = Flask(__name__)
CORS(app)  # Permite solicitudes CORS desde cualquier origen

@app.route('/calcular', methods=['POST'])
def calcular_pandeo():
    try:
        data = request.json
        E = data.get('E')
        I = data.get('I')
        L = data.get('L')

        # Calcular la carga crítica de pandeo usando la fórmula de Euler
        carga_critica = (math.pi**2) * E * I / (L**2)

        return jsonify({'cargaCritica': carga_critica}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 400

@app.route('/', methods=['GET'])
def index():
    return "La aplicación PandeoMaster API está corriendo correctamente"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

