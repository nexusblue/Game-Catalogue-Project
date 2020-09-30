
def ShowCommandMenu():
    #Main User Screen
    print("---------------------------------------------------------------\n")
    print("                 Game Catalogue")
    print("                 Press 1 To add a game")
    print("                 Press 2 Delete a game")
    print("                 Press 3 Find a game")
    print("                 Press 4 Edit a game")
    print("                 Press 6 Print Game List and info")
    print("                 Press 5 Exit Catalogue\n")
    print("---------------------------------------------------------------")
    while True:
        try:
            userCommand =  int(input("\nPlease enter an interger command:"))
        except ValueError:
            print('\nError:Please enter a number \n')
        else:
            break
    return userCommand

def repeatCmd():
    runAgain = str(input("\nWould you like redo this command again(y/n)?"))
    while runAgain != "y" and runAgain!="n":
        runAgain = str(input("\nPlease enter a y/n ?\n"))
    return runAgain

def addGame(pGameList,pGameInfo):
    #TODO: put in a code that prevents dupes
     GameName = str(input("Please enter a name:"))
     GameGenre = str(input("Please enter a Genre:"))
     pGameList.append(GameName)
     pGameInfo.append({"Name":GameName,"Genre":GameGenre})

     runAgain = repeatCmd()
     if runAgain == "y":
        addGame(pGameInfo, pGameList)

def delGame(pGameInfo, pGameList):
    #might remove counter code for another way to remove from gameinfo
    if len(pGameList) == 0:
        print("\nThere are no more games.\n")
        return

    GameName = str(input("Please enter the name of the game you wish to delete:"))
    counter = 0
    for keyName in pGameInfo:
        if keyName["Name"] == GameName:
            #print("that game is in the list")
            pGameList.remove(GameName)
            GameGenre = pGameInfo
            pGameInfo.remove( pGameInfo[counter])
            break
        counter+=1

    runAgain = repeatCmd()
    if runAgain == "y":
        delGame(pGameInfo, pGameList)

def editGame(pGameInfo, pGameList):
    #might remove counter code for another way to remove from gameinfo
    if len(pGameList) == 0:
        print("\nThere are no more games.\n")
        return

    GameName = str(input("Please enter the name of the game you wish to edit:"))
    counter = 0
    for keyName in pGameInfo:
        if keyName["Name"] == GameName:
            editType = str(input("What do you wish to edit? (Name or Genre) "))
            while editType != "name" and editType != "genre" :
                editType = str(input("Please enter either Name or Genre to edit) "))

            if editType == "name":
                print("we are editing name")
            elif editType == "genre":
                print("we are editing genre")
            break
        counter+=1

    runAgain = repeatCmd()
    if runAgain == "y":
        editGame(pGameInfo, pGameList)

def findGame(pGameInfo, pGameList):
    if len(pGameList) == 0:
        print("\nThere are no more games.\n")
        return
    gameToFind = str(input("Please type the name of the game you wish to find?"))
    for keyName in pGameInfo:
        if keyName["Name"] == gameToFind:
            print("\nThat game is in the list!\n")
            break
    print("\nThat game is not int the list!\n")
    runAgain = repeatCmd()
    if runAgain == "y":
       findGame(pGameInfo, pGameList)
    return

def main():
    #Game Data
    GameList = ["Persona 5", "BOTW"]
    GameInfo = [
        {"Name":"Persona 5", "Genre":"RPG" },
        {"Name":"BOTW", "Genre":"Open World"} ]
    userCommand = 0

    while userCommand !=5:
        userCommand = ShowCommandMenu()
        print("\n",GameList,"\n",)
        for item in GameInfo:
            print("\n",item,"\n")

        if userCommand == 1:
            addGame(GameList,GameInfo)
        elif userCommand == 2:
            delGame(GameInfo, GameList)
        elif userCommand == 3:
            findGame(GameInfo, GameList)
        elif userCommand == 4:
            editGame(GameInfo, GameList)
        elif userCommand == 6:
            print(GameList)
            print(GameInfo)

    print("Exiting Program...")
     
main()

def testCode():

    GameList = ["Persona 5", "BOTW"]
    GameInfo = [
        {"Name":"Persona 5", "Genre":"RPG" },
        {"Name":"BOTW", "Genre":"Open World"} ]

    if GameInfo[0]["Name"] == "Persona 5":
        print(GameInfo[1]["Genre"])
    else:
        print("not in the list")


    for value in GameInfo:
        #print(GameInfo[x]["Name"])
        #GameInfoValue= GameInfo[value]
        #print(GameInfoValue)
        print(value["Name"])

#testCode()
###
#def DeadCode():
    #elif infoToFind == "Genre" or infoToFind == "genre":
    #GameGenre = str(input("Please enter a Genre:"))
    #if infoToFind == "Name" or infoToFind == "name":
        #SearchGameByName(pGameInfo, pGameList)
    #while infoToFind != "Name"  and infoToFind != "name":
         #infoToFind = str(input("Please enter either Genre or Name)?\n"))