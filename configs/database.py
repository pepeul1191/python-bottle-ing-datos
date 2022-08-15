#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

load_dotenv()
engine = create_engine(os.getenv('DB'))
session_db = sessionmaker()
session_db.configure(bind=engine)