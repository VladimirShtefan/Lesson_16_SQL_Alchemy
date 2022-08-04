import os

from app.create_app import app


if __name__ == '__main__':
    os.environ['FLASK_ENV'] = 'development'
    app.run(host='0.0.0.0')
