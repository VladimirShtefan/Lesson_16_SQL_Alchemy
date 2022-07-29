from app.configs.configs import DevConfig
from app.create_app import create_app

app = create_app(config=DevConfig)

if __name__ == '__main__':
    app.run(host='0.0.0.0')

