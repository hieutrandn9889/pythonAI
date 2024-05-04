from flask import Flask
from flask_cors import CORS, cross_origin
from flask import request
import tensorflow as tf


# khoi tao flask server backend
app = Flask(__name__)

# apply flask CORS
CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'


@app.route('/nhandienkhuonmat', methods=['POST', 'GET'])
@cross_origin(origins='*')
def nhandienkhuonmat_process():
    face_numbers = 0

    # đọc ảnh từ clent gởi lên
    face = request.form.get('facebase64')
    

    # result
    return "Số mặt là  = " + str(face_numbers)


#start Backend
if __name__ == '__main__':
    app.run(host='0.0.0.0', port='9999')
