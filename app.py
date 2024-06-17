from flask import Flask
from flask_cors import CORS
from src import routes, config, services


def create_app():
    app = Flask(__name__)
    CORS(app)

    app = config.init_app(app)
    app = services.init_app(app)
    app = routes.init_app(app)

    return app


app = create_app()

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5001)
