# Challenge time!
# We have mentioned that the data for the Adventure game could be organised in many
# different ways.  We've created another way for you.
# Your mission, if you choose to accept it, is to
# change the code to make it work.
# Below is the the complete program from the last video, but with the
# locations dictionary modified so that everything is in a single dictionary.
# N.B. Yes the code has some errors, thats what you need to fix!


locations = {0: "You are sitting in front of a computer learning Python",
             1: "You are standing at the end of a road before a small brick building",
             2: "You are at the top of a hill",
             3: "You are inside a building, a well house for a small stream",
             4: "You are in a valley beside a stream",
             5: "You are in the forest"}


#exits must be in a dictionary, not in a lists
exits = {0: {"Q": 0},
         1: {"W": 2, "E": 3, "N": 5, "S": 4, "Q": 0},
         2: {"N": 5, "Q": 0},
         3: {"W": 1, "Q": 0},
         4: {"N": 1, "W": 2, "Q": 0},
         5: {"W": 2, "S": 1, "Q": 0} }
         


namedExits = {1: {"2": 2, "3": 3, "5": 5, "4": 4},
              2: {"5": 5},
              3: {"1": 1},
              4: {"1": 1, "2": 2},
              5: {"2": 2, "1": 1}}

vocabulary = {"QUIT" : "Q",
              "NORTH" : "N",
              "SOUTH" : "S",
              "EAST" : "E",
              "WEST" : "W",
              "ROAD" : "1",
              "HILL": "2",
              "BUILDING": "3",
              "VALLEY": "4",
              "FOREST": "5"}


loc = 1

while True:

    availableExites =", ".join(exits[loc].keys()) # dodanie przecinkow do wartosci dostepnych wyjsc
 
    
    if loc == 0:
        break
    else:
        allExits = exits[loc].copy() 
        allExits.update(namedExits[loc])
        
    direction = input ("Dostepne wyjscia to: " + availableExites + " ").upper()
    print()
    
    #Usage of vocabulary dictionary in input
    if len(direction) > 1:        
        words = direction.split() #Znajduje kierunek w zdaniu
        for word in words:
            if word in vocabulary:
                direction = vocabulary[word]
                break
        
    
    if direction in allExits:
        loc = allExits[direction]
    else:
        print("Nie pojdziesz ")


