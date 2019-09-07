from flask import Flask
from config import Config
from redis import Redis
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import rq


app = Flask(__name__)
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0
app.config.from_object(Config)
app.config["MAIL_SERVER"] = "smtp.gmail.com"
app.config["MAIL_PORT"] = 465
app.config["MAIL_USE_SSL"] = True
app.config["MAIL_USERNAME"] = 'interventionsimulator@gmail.com'
app.config["MAIL_PASSWORD"] = 'conflict123'
db = SQLAlchemy(app)
migrate = Migrate(app, db)


from app import routes, models

app.redis = Redis.from_url(app.config['REDIS_URL'])
app.task_queue = rq.Queue('simulator', connection=app.redis)
app.task_queue = rq.Queue('full_simulator', connection=app.redis)
bootstrap = Bootstrap(app)

