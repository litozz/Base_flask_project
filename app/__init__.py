from flask import Flask
from config import config
 
def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config[config_name])


    @app.route('/')
    def index():
        #return render_template('index2.html')
        return 'Hola desde el index de la aplicacion'

    @app.route('/saludo')
    def saludo():
        #return render_template('saludo.html')
        return 'Hola desde la funcion saludo de la aplicacion'
     
    @app.route('/user/<username>')
    def user(username):
        #return render_template('user.html', username=username)
        return 'Hola desde la función user de la aplicacion, {}'.format(username)



    # Configuracion de los BluePrints
    from app.primerblueprint import primerblueprint
    app.register_blueprint(primerblueprint)
    
    return app