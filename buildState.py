import datetime

state = "no commit"
begin = datetime.datetime.now()
end = None


def building():
    global state,begin,end
    state="building"
    begin = datetime.datetime.now()

def finish(name):
    global state, begin, end
    end = datetime.datetime.now()
    seconds = (end-begin).seconds
    state=end.strftime("%Y-%m-%d %H:%M:%S")+" finish in %d,commit by %s"%(seconds,name)

def getState():
    global state, begin, end
    return state

def isBuilding():
    return (state=="building")