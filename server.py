print('Importing Libraries')
import os
from flask import Flask, render_template, request, make_response
from flask import flash, redirect, url_for, jsonify

from settings import * 
from helper_functions.util import *

from PIL import Image
from io import BytesIO

print('Done!\nSetting up the directories and the model structure...')