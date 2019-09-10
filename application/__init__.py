from flask import Flask
from config import Config
from redis import Redis
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import rq


application = Flask(__name__)
application.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0
application.config.from_object(Config)
application.config["MAIL_SERVER"] = "smtp.gmail.com"
application.config["MAIL_PORT"] = 465
application.config["MAIL_USE_SSL"] = True
application.config["MAIL_USERNAME"] = 'interventionsimulator@gmail.com'
application.config["MAIL_PASSWORD"] = 'conflict123'
db = SQLAlchemy(application)
migrate = Migrate(application, db)


from application import routes

application.redis = Redis.from_url(application.config['REDIS_URL'])
application.task_queue = rq.Queue('simulator', connection=application.redis)
application.task_queue = rq.Queue('full_simulator', connection=application.redis)
bootstrap = Bootstrap(application)

