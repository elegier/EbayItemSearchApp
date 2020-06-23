from flask import Flask
from flask import request
from flask import redirect, url_for
import requests
from logging.config import dictConfig

app = Flask(__name__)

@app.route('/')
def index():
    return redirect(url_for('static', filename='hw6LandingPage.html'))

@app.route('/search', methods=['GET'])
def serve_request():
    queryParams = request.query_string
    
    url = "https://svcs.ebay.com/services/search/FindingService/v1?OPERATION-NAME=findItemsAdvanced&SERVICE-VERSION=1.0.0&SECURITY-APPNAME=ErnestLe-WebTechH-PRD-f2eba4255-d7cfb358&RESPONSE-DATA-FORMAT=JSON&REST-PAYLOAD&" + queryParams.decode("utf-8") ;
    
    app.logger.info('Navigating to: %s', url)
    
    r = requests.get(url)
    app.logger.info('=========== %s', r.text)
    
    return r.text

if __name__ == '__main__':
    # This is used when running locally only. When deploying to Google App
    # Engine, a webserver process such as Gunicorn will serve the app. This
    # can be configured by adding an `entrypoint` to app.yaml.
    app.run(host='127.0.0.1', port=8080, debug=True)
# [END gae_python38_app]