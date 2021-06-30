class Film:
    def __init__(self, name, year, director, estimate):
        self.name = name
        self.year = year
        self.director = director
        self.estimate = estimate
        self.rating = "none"
        self.closeness = 100
        self.place = 0
        self.isNewBetter = "dummy"

def inputFilm(filmList):
    filmList.append(
        Film(
            input("What is the name of the movie? \n"),
            input("What year was the movie produced? \n"),
            input("Who directed the movie? \n"),
            int(input("On a scale of 1 to 100, what is your estimation of the movie's quality: \n"))
        )
    )

def updatePlace(List):
    for i in range(len(List)):
        List[i].place = i + 1

def placeNew(List):
    for i in range(len(List) - 1):
        if List[i].isNewBetter is "y":
            movieToMove = List.pop(len(List) - 1)
            List.insert(i, movieToMove)
            return


def orderList(filmList):
    lastAdded = filmList[len(filmList) - 1]
    askAbout = []
    #If the list is small enough, I'll just have it ask me about all of them.
    if len(filmList) <= 10:                               
        for i in range(len(filmList) - 1):
            filmList[i].isNewBetter = "dummy"
            askAbout.append.filmList[i]
    #This is for identifing which films it should ask me about
    else:
        currentClosest = filmList[0]
        for i in range(len(filmList) - 1):
            filmList[i].isNewBetter = "dummy"
            filmList[i].closeness = abs(filmList[i].rating - lastAdded.estimate)
            if filmList[i].closeness < currentClosest.closeness:
                currentClosest = filmList[i]
        for i in range(len(filmList) - 1):
            if filmList[i].place < currentClosest.place + 5 and filmList[i].place > currentClosest.place - 5:
                askAbout.append.filmList[i]
    #After that's done, I do the asking...
    for i in range(len(askAbout)):
        askAbout[i].isNewBetter = input(str("Is " + lastAdded.name + " a better movie than " + askAbout[i].name + "? \n"))
            #...we scan for a movie judged worse...
        for y in range(len(filmList) - 1):
            if filmList[y].isNewBetter is "y":
                    #...and a movie judged better under it to move above it.
                for n in range(len(filmList) - 1):
                    if filmList[n] is "n" and filmList[n].place > filmList[y].place:
                        inOrder = inOrder - 1
                        movieToMove = filmList.pop(n)
                        filmList.insert(y-1, movieToMove)
                        updatePlace(filmList)
    placeNew(filmList)
    updatePlace(filmList)

def assignRanks(list):
    distance = 100/len(list)
    for i in range(len(list)):
        currentRating = 100 - (distance * [i+1])
        list[i].rating = currentRating

