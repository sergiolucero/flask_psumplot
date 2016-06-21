#!/usr/local/bin/python2.7
# -*- coding: utf-8 -*-
from time import time
from flask import Flask, render_template
#########################################################
app = Flask(__name__)       # create and configure
#########################################################
def psum(p):
    return sum(pow(ix,-p) for ix in xrange(1,10000))
@app.route('/')
def start_page():
    psum_data = [(p,psum(p)) for p in xrange(10)]
    return render_template('psum_plot.html', data=psum_data)
#########################################################
if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
