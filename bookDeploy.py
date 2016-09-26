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
    # if has para,the run as production
    if len(sys.argv) == 1:
        app.run(debug=True)
    else:
        app.run(host="0.0.0.0",port=10000)
