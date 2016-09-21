import sys
from flask import Flask,request,jsonify
import logging
import buildState
import time
import threading
import os
from HangUpBuild import HangUpBuild

app = Flask(__name__)
gitPath = "/root/bookDeploy/testDeployBook/"
hang = HangUpBuild()

@app.route('/commit',methods=["POST"])
def commit():

    if buildState.isBuilding():
        hang.hangUp()
        return "busy"

    t = threading.Thread(target=buildBook,args=("NJUShenbin",gitPath))
    t.start()
    return "OK"

def buildBook(name,gitPath):
    buildState.building()
    os.system("sh deployHtml.sh "+gitPath)

    while hang.hasHangUp():
        hang.noHangUp()
        os.system("sh deployHtml.sh " + gitPath)

    buildState.finish(name)

@app.route('/')
def home():
    return buildState.getState()

if __name__ == '__main__':
    # 如果没有其他参数就是debug模式运行,如果有参数就是生产环境运行
    if len(sys.argv) == 1:
        app.run(debug=True)
    else:
        app.run(host="0.0.0.0",port=10000)
