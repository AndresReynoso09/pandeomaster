from flask import Flask, request, jsonify
import math

app = Flask(__name__)

@app.route('/calculate', methods=['POST'])
def calculate():
    try:
        data = request.json
        E_value = float(data.get('E_value'))
        I_value = float(data.get('I_value'))
        L_value = float(data.get('L_value'))

        P_cr = (math.pi ** 2 * E_value * I_value) / (L_value ** 2)

        calculation_procedure = f"P_cr = (π^2 * {E_value} * {I_value}) / ({L_value}^2)"
        result = f"Carga Axial Crítica (P_cr) = {P_cr:.2f} N"

        return jsonify({
            'procedure': calculation_procedure,
            'result': result
        }), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 400

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
