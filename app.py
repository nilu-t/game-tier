from flask import Flask, render_template

app = Flask(__name__) #defining the Flask app.

class node:
    def __init__(self, data, next=None):
        '''constructor for the node'''
        self.data = data
        self.next = next

class sll:
    def __init__(self, head = None):
        '''constructor for the singly linked list.'''
        self.head = head

    def addFirst(self, data):
        '''this function adds a node to the front of the linked list.'''
        self.head = node(data, self.head)

    def addLast(self, data):
        '''this function adds a node to the end of the linked list.'''
        #if the head is null then addFirst is called.
        if(self.head == None):
            self.addFirst(data)
        else:
            #traversing the sll to find the last element.
            currNode = self.head
            while(currNode.next != None):
                currNode = currNode.next
            
            #now that the last element is found, its next node is the new node to be created.
            newNode = node(data)
            currNode.next = newNode

    def reverse():
        '''reverses the singly linked list.'''
        pass

#home page.
@app.route('/')
def home():

    #creating the individual companies.
    mySll = sll()
    mySll.addFirst("Mojang")
    mySll.addFirst("Nintendo")
    mySll.addFirst("Electronic Arts")
    mySll.addFirst("Activision Blizzard")
    mySll.addFirst("Epic Games")

    allCompanies = ""

    while(mySll.head != None):
        allCompanies += mySll.head.data + "\n"
        mySll.head = mySll.head.next

    return render_template("game_company.html", allCompanies=allCompanies)

#mojang
@app.route('/mojang')
def mojang():

    #creating the individual game nodes for the mojang singly linked list.
    mySll = sll()
    mySll.addFirst("Minecraft")
    mySll.addFirst("Minecraft Dungeons")
    mySll.addFirst("Caller's Bane")
    mySll.addFirst("Crown and Council")
    mySll.addFirst("Minecraft: Story Mode")
    mySll.addFirst("Minecraft: Pocket Edition")

    allGames = ""
    company = "Mojang"

    while(mySll.head != None):
        allGames += mySll.head.data + "\n"
        mySll.head = mySll.head.next

    return render_template("games.html", company=company, allGames=allGames)  


#nintendo
@app.route('/nintendo')
def nintendo():

    #creating the individual sub-game nodes for the nintendo singly linked list.
    mySll = sll()
    mySll.addFirst("Mario ")
    mySll.addFirst("Pokémon")
    mySll.addFirst("The legend of Zelda")

    allGames = ""
    company = "Nintendo"

    while(mySll.head != None):
        allGames += mySll.head.data + "\n"
        mySll.head = mySll.head.next
    return render_template("games.html", company=company, allGames=allGames)  

#nintendo -> mario games.
@app.route('/nintendo/mario')
def nintendo_mario():
    return "mario games"

#nintendo -> pokémon games.
@app.route('/nintendo/pokemon')
def nintendo_pokemon():
    return "pokémon games"

#nintendo -> zelda games.
@app.route('/nintendo/zelda')
def nintendo_zelda():
    return "The legend of Zelda games"

#EA
@app.route('/EA')
def electronic_arts():
    return "electronic arts (EA) tier list"

#Activision Blizzard
@app.route('/activision_blizzard')
def activision_bilizzard():
    return "Activision Blizzard tier list"

#User page to suggest a game to me.
@app.route('/suggest_game')
def suggestion():
    return "Have a suggestion for a game or game company not listed here ? <br> Feel free to reach out to me."