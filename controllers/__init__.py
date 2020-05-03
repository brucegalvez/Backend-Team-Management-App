#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Módulos propios
from server import *
from logger import *
from utils.lastConnection import *
from utils.connection import Connection
from utils.environment import Environment
from utils.dictToString import DictToString
from utils.validate import Validate


# Librerias importadas
import datetime
from flask import request, jsonify
from flask_restx import Resource
from flask_bcrypt import generate_password_hash, check_password_hash
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity

connection = Connection()
config = Environment().settingsOptions()
dicttostr = DictToString()
validate = Validate()
getTime = GetTime()
