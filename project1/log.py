from flask import Flask
import logging

app = Flask(__name__)

logging.basicConfig(filename='log.log', level=logging.DEBUG, format='%(asctime)s %(levelname)s %(name)s %(threadName)s : %(message)s')
