
class HangUpBuild:

    def __init__(self):
        self.__hasHangUp = False

    def hangUp(self):
        self.__hasHangUp = True

    def noHangUp(self):
        self.__hasHangUp = False

    def hasHangUp(self):
        return self.__hasHangUp


