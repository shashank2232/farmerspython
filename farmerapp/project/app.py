from flask import Flask
from extensions import db, migrate
from flask_cors import CORS 
from flask_jwt_extended import JWTManager

app = Flask(__name__)

CORS(app, resources={r"/*":{"origins":"http://localhost:4200"}})
app.config.from_object('config.Config')

db.init_app(app)
migrate.init_app(app, db)

jwt=JWTManager(app)


def register_blueprints(app):
    from views.user_view import user_blueprint
    from views.country_view import country_blueprint
    from views.schedule_view import schedule_blueprint
    from views.farm_view import farm_blueprint
    from views.farmer_view import farmer_blueprint

    app.register_blueprint(user_blueprint, url_prefix = '/user')
    app.register_blueprint(country_blueprint, url_prefix = '/country')
    app.register_blueprint(farmer_blueprint, url_prefix='/farmer')
    app.register_blueprint(farm_blueprint, url_prefix='/farm')
    app.register_blueprint(schedule_blueprint, url_prefix='/schedule')

register_blueprints(app)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)
