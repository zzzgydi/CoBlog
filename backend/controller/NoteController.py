# -*- coding=utf-8 -*-
from flask import session, request, jsonify
from model.Enum import Status
from model.Result import Result
from manager import UserManager
from controller.Adaptor import Controller
import json