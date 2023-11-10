import os

from flask import Flask, request, render_template, make_response
# from flask_migrate import Migrate
# from flask_sqlalchemy import SQLAlchemy
import redis
from redis_lib import RedisRecord
import logging
from logging import handlers
# from prometheus_flask_exporter import PrometheusMetrics
import time
import json

APP = Flask(__name__)
# metrics = PrometheusMetrics(APP)


# APP.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# APP.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://orcaadmin12:orca123!@docker.for.mac.host.internal/orca'


# DB = SQLAlchemy(APP)


# MIGRATE = Migrate(APP, DB)


# from models import *


# Redis Setup 1234

# redis_pool = redis.ConnectionPool(
#     host="docker.for.mac.host.internal",
#     port=6379,
#     db=0
# )
# APP.redis_client = redis.Redis(connection_pool=redis_pool)


# logging setup

console_handler = logging.StreamHandler()
console_handler.setLevel(logging.CRITICAL)
console_handler_formatter = logging.Formatter(
    '[%(asctime)s] [%(levelname)-8s] [%(name)s:%(lineno)s] -- %(message)s'
)
console_handler.setFormatter(console_handler_formatter)
APP.logger.addHandler(console_handler)


# @APP.route('/')
# def view_registered_guests():
#     redis_obj = RedisRecord()
#     guests_count = redis_obj.get_value() or 0
#     is_redis_record = "This record is fetched from redis"
#     guests = Guest.query.all()
#     is_redis_record = 'This record is not fetched from redis'
#     redis_obj.set_value(len(guests))
#     return render_template('guest_list.html', guests=guests, guests_count=int(guests_count))


# @APP.route('/register', methods = ['GET'])
# def view_registration_form():
#     return render_template('guest_registration.html')


# @APP.route('/register', methods = ['POST'] )
# def register_guest():
#     name = request.form.get('name')
#     email = request.form.get('email')
#     partysize = request.form.get('partysize')
#     if not partysize or partysize=='':
#         partysize = 2

#     guest = Guest(name, email, partysize)
#     DB.session.add(guest)
#     DB.session.commit()

#     redis_obj = RedisRecord()
#     redis_obj.clear_sent()

#     return render_template('guest_confirmation.html',
#         name=name, email=email, partysize=partysize)

@APP.route('/health')
# @metrics.gauge('in_progress', 'Long running requests in progress')
def health_check():
    print ("Health check is running")
    APP.logger.info("Health check is running")
    message_value = 'I am fine app1. How are you?'
    return make_response(json.dumps({"message": message_value}), 200)



@APP.route('/var')
# @metrics.gauge('in_progress', 'Long running requests in progress1.')
def var():
    health_text = os.environ.get('health_text')
    service_nickname = os.environ.get('service_key')
    file_name = os.environ.get('FILE_NAME')
    print ("Health check is running")
    APP.logger.info("Health check is running ")
    message_value = 'I am fine app. How are you {}?. My nickname is {}. File name is {}'.format(health_text, service_nickname, file_name)
    return make_response(json.dumps({"message": message_value}), 200)


@APP.route('/')
# @metrics.summary('requests_by_status', 'Request latencies by status',
#                  labels={'status': lambda r: r.status_code})
def view_registered_guests():
    guests_count = 0
    return render_template('guest_list.html', guests=[], guests_count=int(guests_count))


@APP.route('/register', methods = ['GET'])
# @metrics.summary('requests_by_path', 'Request latencies by status.',
#                  labels={'status': lambda r: r.path})
def view_registration_form():
    try:
        print ("Ping Redis")
    except Exception as err:
        print ("Error {err} in connecting redis".format(err=err))
        APP.logger.error("Error {err} in connecting redis".format(err=err))
    return render_template('guest_registration.html')


@APP.route('/register', methods = ['POST'])
def register_guest():
    name = request.form.get('name')
    email = request.form.get('email')
    partysize = request.form.get('partysize')
    if not partysize or partysize=='':
        partysize = 1

    # guest = Guest(name, email, partysize)
    # DB.session.add(guest)
    # DB.session.commit()

    redis_obj = RedisRecord()
    current_count = redis_obj.get_value() or 0
    redis_obj.clear_sent()
    redis_obj.set_value(int(current_count) + 1)

    return render_template('guest_confirmation.html',
        name=name, email=email, partysize=partysize)
