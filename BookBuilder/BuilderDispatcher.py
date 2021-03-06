from BookBuilder.BookBuilder import BookBuilder

class BuilderDispatcher:

    __repos=None
    __builders = []

    def __init__(self, repoConfig):
        self.__repos = repoConfig
        for config in repoConfig:
            self.__builders.append(BookBuilder(config))

    def dispatch(self,responseBody):
        for builder in self.__builders:
            if builder.match(responseBody):
                return builder.build(responseBody)

        #not match,dynamic genernate a bookBuilder
        url = responseBody["repository"]["url"]
        repoName = responseBody["repository"]["name"]
        config = (url,repoName)
        builder = BookBuilder(config)
        self.__builders.append(builder)
        return builder.build(responseBody)

    def getBuildStates(self):
        return [b.getBuildState() for b in self.__builders]