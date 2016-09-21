
class HangUpBuild:

    def __init__(self):
        self.hasHangUp = False

    def hangUp(self):
        self.hasHangUp = True

    def noHangUp(self):
        self.hasHangUp = False

    def hasHangUp(self):
        return self.hasHangUp

