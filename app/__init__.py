from flask import Flask
from flask_bootstrap import Bootstrap

app = Flask(__name__)
db = SQLAlchemy(app)
return app
