from rest_api import REST_API
from conf.conf_external_docker import testing_conf
from flask_cors import CORS
        
app = REST_API(testing_conf, __name__)
CORS(app)

if __name__ == '__main__':
    app.run(port=5001, debug=True)