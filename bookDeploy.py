import sys
import ReposConfig
from flask import Flask,request
from BookBuilder.BuilderDispatcher import BuilderDispatcher

app = Flask(__name__)
dispatcher = BuilderDispatcher(ReposConfig.repos)

@app.route('/commit',methods=["POST"])
def commit():
    # body = request.get_json(force=True)
    # print(body["repository"]["name"])
    # print(body["commits"][0]["author"]["username"])
    # return "hello world!"
    body = request.get_json(force=True)
    return dispatcher.dispatch(body)

@app.route('/')
def home():
    states = dispatcher.getBuildStates()
    separator = "<br/>"
    return separator.join(states)

if __name__ == '__main__':
    # 如果没有其他参数就是debug模式运行,如果有参数就是生产环境运行
    if len(sys.argv) == 1:
        app.run(debug=True)
    else:
        app.run(host="0.0.0.0",port=10000)
