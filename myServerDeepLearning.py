from flask import Flask
from flask_cors import CORS, cross_origin
from flask import request

# khoi tao flask server backend
app = Flask(__name__)

# apply flask CORS
CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'


@app.route('/nhandienkhuonmat', methods=['POST', 'GET'])
@cross_origin(origins='*')
def uppercase_process():
    face = request.args.get('nhandienkhuonmat')
    tenNguoi = face_model.predict(face)
    return tenNguoi


#start Backend
if __name__ == '__main__':
    app.run(host='0.0.0.0', port='9999')
