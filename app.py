from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__) #defining the Flask app.

class node:
    def __init__(self, data=None, next=None):
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

    
    def sortAlphaAscend(self, head=None):
        '''applying merge sort on the singly linked list to sort all the nodes alphabetically ascending in O(n*logn) time'''

        #base case when there are no nodes or there is 1 node, then the head is returned.
        if (head == None or head.next == None):
            return head
        
        #splitting the head into left and right partitions.
        leftPartition = head #initially the left partition is just the SLL itself.
        rightPartition = self.getMid(head) #intitally the right partition is just the middle node SLL.
        tempRight = rightPartition.next #the right partition is always after the middle node.
        rightPartition.next = None #The left partition is now finished. Since rightPartition aliases the head, then leftPartition changes.
        rightPartition = tempRight #restoring the right partition.

        leftPartition = self.sortAlphaAscend(leftPartition)  #recursively break down and sort the left half of the list.
        rightPartition = self.sortAlphaAscend(rightPartition) #recursively break down and sort the right half of the list.

        return self.mergeAlphaAscend(leftPartition, rightPartition) #the sorted list is the merging of the left and right halves of the list.

    def mergeAlphaAscend(self, left, right):
        '''helper function for merging both left and right partitions of the list. (ALPHABETICALLY ASCENDING)'''
        tail = node()
        tailCopy = tail #tail copy which points to the head of the tail node.

        #iterating the left and right SLL lists until one or both of the lists are null and addding them to tail based on alphabetical order.
        while(left != None and right != None):

            #getting first strings from the left and right SLL lists.
            leftStr = (left.data)
            rightStr = (right.data)

            #comparing both the leftStr and rightStr objects to be lowercase, regardless if they were initially uppercase.
            leftStr =  leftStr.lower()
            rightStr = rightStr.lower()

            #updating the tail SLL.
            if (leftStr >= rightStr):
                #right node should come before the left node.
                tail.next = right
                right = right.next #iterate the right node.
            else:
                tail.next = left
                left = left.next #iterate the left node.
            
            tail = tail.next #iterate the tail node so it always points to its tail.
            
        if left != None:
            tail.next = left
        
        if right != None:
            tail.next = right
        
        return tailCopy.next

    def sortAlphaDescend(self, head):
        '''applying merge sort on the singly linked list to sort all the nodes alphabetically descending in O(n*logn) time'''
    
        pass

    def sortPopularAscend(self, head):
        '''applying merge sort on the singly linked list to sort all the nodes by most popularity ascending in O(n*logn) time'''

        pass

    def sortPopularDescend(self, head):
        '''applying merge sort on the singly linked list to sort all the nodes by most popularity descending in O(n*logn) time'''

        pass

    def sortCompanyFoundAscend(self, head):
        '''applying merge sort on the singly linked list to sort all the nodes by company founded ascending in O(n*logn) time'''

        pass

    def sortCompanyFoundDescend(self, head):
        '''applying merge sort on the singly linked list to sort all the nodes by company founded descending in O(n*logn) time'''

        pass

    def mergeAlphaDescend(self, left, right):
        '''helper function for merging both left and right partitions of the list. (ALPHABETICALLY ASCENDING)'''
        pass

    def mergePopularDescend(self, left, right):
        '''helper function for merging both left and right partitions of the list. (POPULARITY DESCENDING)'''
        pass

    def mergePopularAscend(self, left, right):
        '''helper function for merging both left and right partitions of the list. (POPULARITY ASCENDING)'''
        pass

    def mergeCompanyFoundDescend(self, left, right):
        '''helper function for merging both left and right partitions of the list. (COMPANY FOUND DESCENDING)'''
        pass

    def mergeCompanyFoundAscend(self, left, right):
        '''helper function for merging both left and right partitions of the list. (COMPANY FOUND ASCENDING)'''
        pass

    def reverse(self):
        '''reverses the singly linked list.'''
        pass

    def getMid(self, head):
        ''' helper function for the merge sort. '''
        slow = head #initially the slow pointer is just the head.
        fast = head.next #initially the fast pointer is one iteration ahead of the slow pointer.

        while (fast != None and fast.next != None):
            slow = slow.next #slow pointer has iteration incremented by 1.
            fast = fast.next.next #fast pointer is always 2 iterations ahead of the slow pointer.
        
        #when the fast pointer is NULL or its next node is none, then slow has reached the middle of the given head.
        return slow

#home page.
@app.route('/', methods=['GET','POST'])
def home():
    #creating the individual companies.
    mySll = sll()
    mySll.addFirst("Mojang")
    mySll.addFirst("Nintendo")
    mySll.addFirst("Electronic Arts")
    mySll.addFirst("Activision Blizzard")
    mySll.addFirst("Epic Games")
    mySll.addFirst("Rockstar Games")
    mySll.addFirst("Ubisoft")
    mySll.addFirst("Bandai Namco")
    mySll.addFirst("Microsoft")
    mySll.addFirst("Sony")
    mySll.addFirst("Valve Corporation")
    mySll.addFirst("Sega Games Co. Ltd")
    mySll.addFirst("Naughty Dog Inc")
    mySll.addFirst("Infinity Ward")
    mySll.addFirst("Take-Two Interactive Software Inc")
    mySll.addFirst("Gameloft")
    mySll.addFirst("ZeniMax Media Inc")
    mySll.addFirst("Retro Studios")
    mySll.addFirst("Level-5 Company")
    mySll.addFirst("PopCap Games")
    mySll.addFirst("Treasure Co. Ltd")
    mySll.addFirst("Capcom Company Ltd")
    mySll.addFirst("Bungie Inc")
    mySll.addFirst("Insomniac Games Inc")
    mySll.addFirst("NCSOFT")
    mySll.addFirst("Bethesda Game Studios")
    mySll.addFirst("Sonic Team")
    mySll.addFirst("LucasArts")
    mySll.addFirst("Blizzard Entertainment Inc")
    mySll.addFirst("Konami Holdings Corporations")
    mySll.addFirst("id Software")
    mySll.addFirst("BioWare")
    mySll.addFirst("Nexon Co. Ltd")

    allCompanies = ""

    if (request.method == 'POST'):
        sortedHead = mySll.sortAlphaAscend(mySll.head)

        while(sortedHead != None):
            allCompanies += sortedHead.data + "\n"
            sortedHead = sortedHead.next

        if("alpha_ascend" in request.form):
            return redirect(url_for('sorted', allCompanies=allCompanies))
        elif("alpha_descend" in request.form):
            return "alpha_descend"
        elif("company_found_descend" in request.form):
            return "company_found_descend"
        elif("company_found_ascend" in request.form):
            return "company_found_ascend"
        elif("popular_ascend" in request.form):
            return "popular_ascend"
        elif("popular_descend" in request.form):
            return "popular_descend"

    if (request.method == 'GET'):
        while(mySll.head != None):
            allCompanies += mySll.head.data + "\n"
            mySll.head = mySll.head.next
        return render_template("game_company.html",  allCompanies=allCompanies)

#page for "sorting". String converter is specified to filter it from the URL. This page is mainly due to creating a new state. So, when the page is refreshed there will be no "confirm resubmission of form" dialog. 
@app.route('/sorted/<string:allCompanies>')
def sorted(allCompanies):
    print(allCompanies)
    return render_template("game_company.html",  allCompanies=allCompanies)

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
    mySll.addFirst("Pokemon")
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

#nintendo -> pokemon games.
@app.route('/nintendo/pokemon')
def nintendo_pokemon():
    return "pokemon games"

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
def activision_blizzard():
    return "Activision Blizzard tier list"

#Microsoft
@app.route('/microsoft')
def microsoft():
    return "Microsoft tier list here"

#User page to suggest a game to me.
@app.route('/suggest_game')
def suggestion():
    return "Have a suggestion for a game or game company not listed here ? <br> Feel free to reach out to me."