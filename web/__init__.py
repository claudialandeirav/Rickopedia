# IMOPRTS
import os

from flask import Flask, render_template, url_for, redirect, request, session, send_file

def start_app():
    app = Flask(__name__, static_folder='static')
    app.secret_key='estoesunaclavesupersecreta'

    return app