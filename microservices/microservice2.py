from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/dados_ahur01')
def get_data():
    return {"data": "Dados do microservice ahu201"}

@app.route('/health')
def health_check():
    return jsonify({"status": "UP"}), 200

if __name__ == '__main__':
    app.run(port=5002)