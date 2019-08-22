from flask import Flask
from config import Config
from redis import Redis
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import matplotlib
import rq


app = Flask(__name__)
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0
app.config.from_object(Config)
db = SQLAlchemy(app)
migrate = Migrate(app, db)


from app import routes, models

app.redis = Redis.from_url(app.config['REDIS_URL'])
app.task_queue = rq.Queue('simulator', connection=app.redis)
app.task_queue = rq.Queue('full_simulator', connection=app.redis)
bootstrap = Bootstrap(app)