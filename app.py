from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__) #defining the Flask app.

class node:
    def __init__(self, data=None, companyFounded=None, next=None):
        '''constructor for the node'''
        self.data = data #data for the company names.
        self.next = next
        self.companyFounded = companyFounded

class sll:
    def __init__(self, head = None):
        '''constructor for the singly linked list.'''
        self.head = head

    def addFirst(self, data, companyFounded=None):
        '''this function adds a node to the front of the linked list.'''
        self.head = node(data, companyFounded, self.head) #adding the node to the front of the sll. 

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

    def sortAlphaDescend(self, head):
        '''applying merge sort on the singly linked list to sort all the nodes alphabetically descending in O(n*logn) time'''

        #base case if the head is empty or the head is one node only. In that case the head is returned.
        if(head == None or head.next == None):
            return head

        left = head #left is initally the pointer to the head node.
        right = self.getMid(head) #right is initially the pointer to the head node. 
        tempRight = right.next #the right list is one node right of the middle node. 
        right.next = None #the left partition occurs here. 
        right = tempRight

        left = self.sortAlphaDescend(left) #recursively break down and sort the left list.
        right = self.sortAlphaDescend(right) #recursively break down and sort the right list.

        return self.mergeAlphaDescend(left, right) #merge the left and right partitions.

    def sortCompanyFoundAscend(self, head):
        '''applying merge sort on the singly linked list to sort all the nodes by company founded ascending in O(n*logn) time'''
        
        #the base case, when there is not a node given or it is a single node. In that case the head is returned.
        if(head == None or head.next == None):
            return head
        
        left = head #left half of the list is initially the head.
        right = self.getMid(head) #right half of the list is initially the middle.
        tempRight = right.next #storing the actual right node which is to the right of the middle node.
        right.next = None #the left partition occurs because right list aliases the head.
        right = tempRight

        left = self.sortCompanyFoundAscend(left)
        right = self.sortCompanyFoundAscend(right)

        return self.mergeCompanyFoundAscend(left, right)

    def sortCompanyFoundDescend(self, head):
        '''applying merge sort on the singly linked list to sort all the nodes by company founded descending in O(n*logn) time'''

        pass

    def sortPopularAscend(self, head):
        '''applying merge sort on the singly linked list to sort all the nodes by most popularity ascending in O(n*logn) time'''

        pass

    def sortPopularDescend(self, head):
        '''applying merge sort on the singly linked list to sort all the nodes by most popularity descending in O(n*logn) time'''
        
        pass

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
                #right node should come after the left node.
                tail.next = left
                left = left.next #iterate the left node.
            
            tail = tail.next #iterate the tail node so it always points to its tail.
        
        #it's possible that the left list is not null and the right list is null. In that case, the tail appends the remaining left list.
        if left != None:
            tail.next = left
        
        #it's possible that the right list is not null and the left list is null. In that case, the tail appends the remaining right list.
        if right != None:
            tail.next = right
        
        return tailCopy.next

    def mergeAlphaDescend(self, left, right):
        '''helper function for merging both left and right partitions of the list. (ALPHABETICALLY ASCENDING)'''

        tail = node() #tail node, used for populating the merged data.
        tailCopy = tail #tailCopy node which points to the head of the tail node.

        while(left != None and right != None):
            
            leftData = left.data
            rightData = right.data

            leftData = leftData.lower() #making the left data str to be lowercase.
            rightData = rightData.lower() #making the right data str to be lowercase.

            if(leftData > rightData):
                tail.next = left #the left node should appear before the right node if the left data is greater.
                left = left.next #iterate the left node. 
            elif(leftData <= rightData):
                tail.next = right #the right node should appear before the left node if the right data is greater.
                right = right.next #iterate the right node.
            
            tail = tail.next #the tail MUST always be iterated in order to point to its tail.
        
        #the left list might not be null. In that case, the remaining left list is appended to the tail.
        if(left != None):
            tail.next = left
        #the right list might not be null. In that case, the remaining right list appended to the tail.
        if(right != None):
            tail.next = right

        return tailCopy.next

    def mergeCompanyFoundAscend(self, left, right):
        '''helper function for merging both left and right partitions of the list. (COMPANY FOUND ASCENDING)'''

        tail = node() #tail node which always points to its own tail.
        tailCopy = tail #tail copy which points to the head of the tail node.
        
        while(left != None and right != None):

            leftCompanyFounded = (left.companyFounded).split("/")
            rightCompanyFounded = (right.companyFounded).split("/")

            leftTempMonth = leftCompanyFounded[0]
            rightTempMonth = rightCompanyFounded[0]

            rightMonth = 0
            leftMonth = 0
        
            #if the temp months for either of the lists are "NA" then, numerically their months value are equivalent to 0, since it is unknown.
            #so when two different company years are the same but one has a month of "NA", then the company with "NA" month will always be less. Since this is ascending then this company will be before the second company.
            if(leftTempMonth[0] == 'N' and leftTempMonth[1] == 'A'):
                leftMonth = 0
            elif(rightTempMonth[0] == 'N' and rightTempMonth[1] != 'A'):
                rightMonth = 0
            #finding the numerical value of the left list month.
            elif(leftTempMonth[0] == '0' and leftTempMonth[1] != '0'):
                leftMonth = int(leftTempMonth[1])
            elif(leftTempMonth[0] != '0' and leftTempMonth[1] != '0'):
                leftMonth = int(leftTempMonth)
            #finding the numerical value of the right list month.
            elif(rightTempMonth[0] == '0' and rightTempMonth[1] != '0'):
                rightMonth = int(rightTempMonth[1])
            elif(rightTempMonth[0] != '0' and rightTempMonth[1] != '0'):
                rightMonth = int(rightTempMonth)

            #converting the string "year" values to integer.
            leftYear = int(leftCompanyFounded[1])
            rightYear = int(rightCompanyFounded[1])

            if( (leftYear > rightYear) ):
                #right node should come before the left node to be in ascending order. Since, right list date is less than or equal to left list date.
                tail.next = right
                right = right.next #iterate the right list.
            elif( ( leftYear < rightYear) ):
                #left node should come before the right node to be in ascending order. Since, left list date is less than or equal to right list date.
                tail.next = left
                left = left.next #iterate the left list.
            elif ( ( leftYear == rightYear) ):
                if(leftMonth > rightMonth ):
                    #right node should come before the left node to be in ascending order. Since, right month is less than or equal to left month.
                    tail.next = right
                    right = right.next #iterate the right list.
                if (leftMonth <= rightMonth):
                    #left node should come before the right node to be in ascending order. Since, left month is less than or equal to right month.
                    tail.next = left
                    left = left.next #iterate the left list.

            #iterate the tail node so it is always pointing to its tail.
            tail = tail.next

        #after the while loop, the left and right list can still remain (not null). In that case, the remaining lists are appended to the tail.
        if(left != None):
            tail.next = left
        
        if(right != None):
            tail.next = right

        return tailCopy.next

    def mergeCompanyFoundDescend(self, left, right):
        '''helper function for merging both left and right partitions of the list. (COMPANY FOUND DESCENDING)'''
        pass

    def mergePopularDescend(self, left, right):
        '''helper function for merging both left and right partitions of the list. (POPULARITY DESCENDING)'''
        pass

    def mergePopularAscend(self, left, right):
        '''helper function for merging both left and right partitions of the list. (POPULARITY ASCENDING)'''
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
    mySll.addFirst("Mojang", "05/2009")
    mySll.addFirst("Nintendo", "09/1889")
    mySll.addFirst("Electronic Arts", "05/1982")
    mySll.addFirst("Activision Blizzard", "07/2008")
    mySll.addFirst("Epic Games", "01/1991")
    mySll.addFirst("Rockstar Games", "12/1998")
    mySll.addFirst("Ubisoft", "03/1986")
    mySll.addFirst("Bandai Namco", "03/2006")
    mySll.addFirst("Microsoft", "04/1975")
    mySll.addFirst("Sony", "05/1946")
    mySll.addFirst("Valve Corporation","08/1996")
    mySll.addFirst("Sega Games Co. Ltd", "06/1960")
    mySll.addFirst("Naughty Dog Inc", "09/1984")
    mySll.addFirst("Infinity Ward", "NA/2002")
    mySll.addFirst("Take-Two Interactive Software Inc", "09/1993")
    mySll.addFirst("Gameloft", "12/1999")
    mySll.addFirst("ZeniMax Media Inc", "05/1999")
    mySll.addFirst("Retro Studios", "09/1998")
    mySll.addFirst("Level-5 Company", "10/1998")
    mySll.addFirst("PopCap Games", "07/2000")
    mySll.addFirst("Treasure Co. Ltd", "06/1992")
    mySll.addFirst("Capcom Company Ltd", "05/1979")
    mySll.addFirst("Bungie Inc", "05/1991")
    mySll.addFirst("Insomniac Games Inc", "02/1994")
    mySll.addFirst("NCSOFT", "03/1997")
    mySll.addFirst("Bethesda Game Studios", "06/1986")
    mySll.addFirst("Sonic Team", "NA/1991")
    mySll.addFirst("LucasArts", "05/1982")
    mySll.addFirst("Blizzard Entertainment Inc", "02/1991")
    mySll.addFirst("Konami Holdings Corporations", "03/1969")
    mySll.addFirst("id Software", "02/1991")
    mySll.addFirst("BioWare", "02/1995")
    mySll.addFirst("Nexon Co. Ltd", "12/1994")

    allCompanies = ""
    allFounded = ""

    if (request.method == 'POST'):

        sortedHead = None

        if("alpha_ascend" in request.form):
            sortedHead = mySll.sortAlphaAscend(mySll.head)

            #iterating through all the sorted node data to populate allCompanies variable.
            while(sortedHead != None):
                allCompanies += sortedHead.data + ","
                sortedHead = sortedHead.next

        elif("alpha_descend" in request.form):
            sortedHead = mySll.sortAlphaDescend(mySll.head)

            #iterating through all the sorted node data to populate allCompanies variable.
            while(sortedHead != None):
                allCompanies += sortedHead.data + ","
                sortedHead = sortedHead.next
    
        elif("company_found_ascend" in request.form):
            sortedHead = mySll.sortCompanyFoundAscend(mySll.head)

            #iterating through all the sorted node data to populate allCompanies variable.
            while(sortedHead != None):
                allCompanies += sortedHead.data + ","
                allFounded += sortedHead.companyFounded + ","
                sortedHead = sortedHead.next

        elif("company_found_descend" in request.form):
            return "company_found_descend"

        elif("popular_ascend" in request.form):
            return "popular_ascend"

        elif("popular_descend" in request.form):
            return "popular_descend"

        return redirect(url_for('sorted', allCompanies=allCompanies, allFounded=allFounded))

    if (request.method == 'GET'):
        while(mySll.head != None):
            allCompanies += mySll.head.data + ","
            mySll.head = mySll.head.next
        return render_template("game_company.html",  allCompanies=allCompanies)

#page for "sorting". String converter is specified to filter it from the URL. This page is mainly due to creating a new state. So, when the page is refreshed there will be no "confirm resubmission of form" dialog. 
@app.route('/sorted/<string:allCompanies>/')
@app.route('/sorted/<string:allCompanies>/<path:allFounded>/')
def sorted(allCompanies, allFounded=None):
    print(allFounded)
    return render_template("game_company.html", allCompanies=allCompanies, allFounded=allFounded)

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
@app.route('/activision . blizzard')
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