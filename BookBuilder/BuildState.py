import datetime

class BuildState:

    __state = "no commit"
    __begin = datetime.datetime.now()
    __end = None

    def building(self):
        self.__state = "building"
        self.__begin = datetime.datetime.now()

    def finish(self,name):
        self.__end = datetime.datetime.now()
        seconds = (self.__end - self.__begin).seconds
        self.__state= self.__end.strftime("%Y-%m-%d %H:%M:%S") + " finish in %d,commit by %s" % (seconds, name)

    def getState(self):
        return self.__state

    def isBuilding(self):
        return self.__state == "building"
