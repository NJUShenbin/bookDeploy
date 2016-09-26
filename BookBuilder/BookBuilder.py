from BookBuilder.BuildState import BuildState
from BookBuilder.HangUpBuild import HangUpBuild
import os
import threading

class BookBuilder:
    # __responseBody = None
    __repoTuple = None
    __buildState = None
    __hang = None

    def __init__(self,repoTuple):
        self.__repoTuple = repoTuple
        self.__buildState = BuildState()
        self.__hang = HangUpBuild()

    def match(self,responseBody):
        return responseBody["repository"]["url"] == self.__repoTuple[0]

    def getBuildState(self):
        return self.__buildState.getState()

    def build(self,responseBody):
        if self.__buildState.isBuilding():
            self.__hang.hangUp()
            return "busy"

        t = threading.Thread(target=self.__buildBook, args=(responseBody,))
        t.start()
        return "OK"

    def __buildBook(self, body):
        self.__buildState.building()

        gitUrl = self.__repoTuple[0]
        deployDir = self.__repoTuple[1]

        self.__excuteBuildShell(gitUrl,deployDir)

        while self.__hang.hasHangUp():
            print("something hangup,build again")
            self.__hang.noHangUp()
            self.__excuteBuildShell(gitUrl, deployDir)

        self.__buildState.finish(body["repository"]["name"])

    def __excuteBuildShell(self,gitUrl,deployDir):
        repoName = gitUrl[gitUrl.rindex("/")+1:]

        if deployDir[0] == '/':
            deployDir = deployDir[1:]
        os.system("sh deployHtml.sh "+gitUrl+" "+repoName+" "+deployDir)