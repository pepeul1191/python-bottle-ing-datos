#!/usr/bin/env python
# -*- coding: utf-8 -*-

from bottle import Bottle, template, HTTPResponse
from configs.helpers import menu

subapp = Bottle()
