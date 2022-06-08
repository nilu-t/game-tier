from flask import Flask, render_template, request, redirect, url_for 
from sll import sll #importing the sll class from the sll.py file within the same directory.

app = Flask(__name__) #defining the Flask app.

#home page.
@app.route('/', methods=['GET','POST'])
def home():

    #creating the individual companies. The nodes are added in the "COMPANY_NAME", "DATE_FOUNDED", "COUNTRY DEVELOPED" format.
    mySll = sll()
    mySll.addFirst("Mojang", "05/2009", "Sweden")
    mySll.addFirst("Nintendo", "09/1889", "Japan")
    mySll.addFirst("Electronic Arts", "05/1982", "U.S")
    mySll.addFirst("Activision Blizzard", "07/2008", "U.S")
    mySll.addFirst("Epic Games", "01/1991", "U.S")
    mySll.addFirst("Rockstar Games", "12/1998", "U.S")
    mySll.addFirst("Ubisoft", "03/1986", "France")
    mySll.addFirst("Bandai Namco", "03/2006", "Japan")
    mySll.addFirst("Microsoft", "04/1975", "U.S")
    mySll.addFirst("Sony", "05/1946", "Japan")
    mySll.addFirst("Valve Corporation","08/1996", "U.S")
    mySll.addFirst("Sega Games Co. Ltd", "06/1960", "Japan")
    mySll.addFirst("Naughty Dog Inc", "09/1984", "U.S")
    mySll.addFirst("Infinity Ward", "NA/2002", "U.S")
    mySll.addFirst("Take-Two Interactive Software Inc", "09/1993", "U.S")
    mySll.addFirst("Gameloft", "12/1999", "France")
    mySll.addFirst("ZeniMax Media Inc", "05/1999", "U.S")
    mySll.addFirst("Retro Studios", "09/1998", "U.S")
    mySll.addFirst("Level-5 Company", "10/1998", "Japan")
    mySll.addFirst("PopCap Games", "07/2000", "U.S")
    mySll.addFirst("Treasure Co. Ltd", "06/1992", "Japan")
    mySll.addFirst("Capcom Company Ltd", "05/1979", "Japan")
    mySll.addFirst("Bungie Inc", "05/1991", "U.S")
    mySll.addFirst("Insomniac Games Inc", "02/1994", "U.S")
    mySll.addFirst("NCSOFT", "03/1997", "South Korea")
    mySll.addFirst("Bethesda Game Studios", "06/1986", "U.S")
    mySll.addFirst("Sonic Team", "NA/1991", "Japan")
    mySll.addFirst("LucasArts", "05/1982", "U.S")
    mySll.addFirst("Blizzard Entertainment Inc", "02/1991", "U.S")
    mySll.addFirst("Konami Holdings Corporations", "03/1969", "Japan")
    mySll.addFirst("id Software", "02/1991", "U.S")
    mySll.addFirst("BioWare", "02/1995", "Canada")
    mySll.addFirst("Nexon Co. Ltd", "12/1994", "South Korea")
    mySll.addFirst("Square Enix Holdings Co. Ltd", "04/2003", "Japan")
    mySll.addFirst("Zynga", "04/2007", "U.S")
    mySll.addFirst("Rare", "NA/1985", "U.K")

    allCompanies = ""
    extraContent = "" #stores additional content, such as dates founded, countries developed, etc. Each extra content will be wrapped in paranthesis.

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
                extraContent += "(" + sortedHead.companyFounded + "),"
                sortedHead = sortedHead.next

        elif("company_found_descend" in request.form):
            sortedHead = mySll.sortCompanyFoundDescend(mySll.head)

            #iterating through all the sorted node data to populate allCompanies variable.
            while(sortedHead != None):
                allCompanies += sortedHead.data + ","
                extraContent += "(" + sortedHead.companyFounded + "),"
                sortedHead = sortedHead.next

        elif("country_produced_ascend" in request.form):
            sortedHead = mySll.sortCountryDevelopedAscend(mySll.head)

            #iterating through all the sorted node data to populate allCompanies variable.
            while(sortedHead != None):
                allCompanies += sortedHead.data + ","
                extraContent += "(" + sortedHead.country + "),"
                sortedHead = sortedHead.next

        elif("country_produced_descend" in request.form):
            return "country_produced_descend"

        elif("top_grossing_descend" in request.form):
            return "top_grossing_descend"
        
        elif("top_grossing_ascend" in request.form):
            return "top_grossing_ascend"

        return redirect(url_for('sorted', allCompanies=allCompanies, extraContent=extraContent))

    if (request.method == 'GET'):
        while(mySll.head != None):
            allCompanies += mySll.head.data + ","
            mySll.head = mySll.head.next
        return render_template("game_company.html",  allCompanies=allCompanies)

#page for "sorting". String converter is specified to filter it from the URL. This page is mainly due to creating a new state. So, when the page is refreshed there will be no "confirm resubmission of form" dialog. 
@app.route('/sorted/<string:allCompanies>/')
@app.route('/sorted/<string:allCompanies>/<path:extraContent>/')
@app.route('/sorted/<string:allCompanies>/<string:extraContent>/')
def sorted(allCompanies, extraContent=None):
    print(extraContent)
    return render_template("game_company.html", allCompanies=allCompanies, extraContent=extraContent)

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