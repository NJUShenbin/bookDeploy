import os
import sys
import threading

from HangUpBuild import HangUpBuild
from flask import Flask

from BookBuilder.BuildState import BuildState

app = Flask(__name__)
gitPath = "/root/bookDeploy/DocumentMakeMeHappy/"
hang = HangUpBuild()


@app.route('/commit',methods=["POST"])
def commit():
    # body = request.get_json(force=True)
    # print(body["repository"]["name"])
    # print(body["commits"][0]["author"]["username"])
    # return "hello world!"

    if BuildState.isBuilding():
        hang.hangUp()
        print("is busy , hang up")
        return "busy"

    t = threading.Thread(target=buildBook,args=("NJUShenbin",gitPath))
    t.start()
    return "OK"

def buildBook(name,gitPath):
    BuildState.building()
    os.system("sh deployHtml.sh "+gitPath)

    while hang.hasHangUp():
        print("something hangup,build again")
        hang.noHangUp()
        os.system("sh deployHtml.sh " + gitPath)

    BuildState.finish(name)

@app.route('/')
def home():
    return BuildState.getState()

if __name__ == '__main__':
    # 如果没有其他参数就是debug模式运行,如果有参数就是生产环境运行
    if len(sys.argv) == 1:
        app.run(debug=True)
    else:
        app.run(host="0.0.0.0",port=10000)
