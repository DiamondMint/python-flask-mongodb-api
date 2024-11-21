from flask import Flask, render_template
from dotenv import load_dotenv
import os

from config.mongodb import mongo
from routes.dog import dog #Importamos todas las rutas(endpoints)

load_dotenv()

app = Flask(__name__) 

app.config['MONGO_URI'] = os.getenv('MONGO_URI') #debe coincidir con el nombre de nuestra variable de ambiente en .env
mongo.init_app(app) #obv le paso el obj de mi aplicación

@app.route('/')    
def index():
    return render_template('index.html')
app.register_blueprint(dog, url_prefix= '/dog')
#app.register_blueprint(dog, url_prefix= '/dog/breed/<breed_name>')

if __name__ == '__main__':
    app.run(debug=True) #Para cuand yo haga un cambio, el servidor se reinicie en automático
