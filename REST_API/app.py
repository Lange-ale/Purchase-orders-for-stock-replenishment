from rest_api import REST_API
from conf.conf import production_conf
from flask_cors import CORS
        
app = REST_API(production_conf, __name__)
CORS(app) # Enable CORS
