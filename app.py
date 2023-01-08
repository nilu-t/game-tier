from flask import Flask, render_template, request, redirect, url_for, abort
from sll import sll #importing the sll class from the sll.py file within the same directory.
import json
import requests


app = Flask(__name__) #defining the Flask app.

#sll object used for creating the individual companies. The nodes are added in the "COMPANY_NAME", "DATE_FOUNDED", "COUNTRY DEVELOPED" format.
mySll = sll()

#helper function to initialize all the game companies.
def initializeCompanies():

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
    mySll.addFirst("Naughty Dog", "09/1984", "U.S")
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
    mySll.addFirst("Tencent", "11/1998", "China")

#home page.
@app.route('/', methods=['GET','POST'])
def home():
    if(mySll.getHead() == None):
        initializeCompanies()

    allCompanies = ""
    extraContent = "" #stores additional content, such as dates founded, countries developed, etc. Each extra content will be wrapped in paranthesis.

    if (request.method == 'POST'):

        sortedHead = None

        if("alpha_ascend" in request.form):
            sortedHead = mySll.sortAlphaAscend(mySll.head)
            mySll.setHead(sortedHead) #The head of the SLL is now the sorted head.

            #iterating through all the sorted node data to populate allCompanies variable.
            while(sortedHead != None):
                allCompanies += sortedHead.data + ","
                sortedHead = sortedHead.next

        elif("alpha_descend" in request.form):
            sortedHead = mySll.sortAlphaDescend(mySll.head)
            mySll.setHead(sortedHead)

            #iterating through all the sorted node data to populate allCompanies variable.
            while(sortedHead != None):
                allCompanies += sortedHead.data + ","
                sortedHead = sortedHead.next
    
        elif("company_found_ascend" in request.form):
            sortedHead = mySll.sortCompanyFoundAscend(mySll.head)
            mySll.setHead(sortedHead)

            #iterating through all the sorted node data to populate allCompanies variable.
            while(sortedHead != None):
                allCompanies += sortedHead.data + ","
                extraContent += "(" + sortedHead.companyFounded + "),"
                sortedHead = sortedHead.next

        elif("company_found_descend" in request.form):
            sortedHead = mySll.sortCompanyFoundDescend(mySll.head)
            mySll.setHead(sortedHead)

            #iterating through all the sorted node data to populate allCompanies variable.
            while(sortedHead != None):
                allCompanies += sortedHead.data + ","
                extraContent += "(" + sortedHead.companyFounded + "),"
                sortedHead = sortedHead.next

        elif("country_produced_ascend" in request.form):
            sortedHead = mySll.sortCountryDevelopedAscend(mySll.head)
            mySll.setHead(sortedHead)

            #iterating through all the sorted node data to populate allCompanies variable.
            while(sortedHead != None):
                allCompanies += sortedHead.data + ","
                extraContent += "(" + sortedHead.country + "),"
                sortedHead = sortedHead.next

        elif("country_produced_descend" in request.form):
            sortedHead = mySll.sortCountryDevelopedDescend(mySll.head)
            mySll.setHead(sortedHead)

            #iterating through all the sorted node data to populate allCompanies variable.
            while(sortedHead != None):
                allCompanies += sortedHead.data + ","
                extraContent += "(" + sortedHead.country + "),"
                sortedHead = sortedHead.next

        elif("top_grossing_descend" in request.form):
            return "EEEEE"
        
        elif("top_grossing_ascend" in request.form):
            return "EEEEE"

        return redirect(url_for('sorted', allCompanies=allCompanies, extraContent=extraContent))

    if (request.method == 'GET'):
        sllHead = mySll.getHead()
        while(sllHead != None):
            allCompanies += sllHead.data + ","
            sllHead = sllHead.next
        return render_template("game_company.html",  allCompanies=allCompanies)

#page for "sorting". String converter is specified to filter it from the URL. This page is mainly due to creating a new state. So, when the page is refreshed there will be no "confirm resubmission of form" dialog. 
@app.route('/sorted/<string:allCompanies>/')
@app.route('/sorted/<string:allCompanies>/<path:extraContent>/')
@app.route('/sorted/<string:allCompanies>/<string:extraContent>/')
def sorted(allCompanies, extraContent=None):
    return render_template("game_company.html", allCompanies=allCompanies, extraContent=extraContent)

#In the game_company.js file, the href to the game company with the app route for "companyName" is made.
#this routes' page is displayed after the game company is clicked.
@app.route('/<string:companyName>', methods=['GET','POST'])
def gameCompany(companyName=None):

    tempSLL = mySll
    tempHead = tempSLL.getHead()

    companyFound = False

    while(tempHead != None ):
        if(companyName != tempHead.data):
            tempHead = tempHead.next 
            continue #skip to next iteration, the company name is not found.
        elif(companyName == tempHead.data):
            companyFound = True
            break #break out the loop the company is found
    
    if(companyFound):
        print(companyName)

        allGames = requests.get('http://127.0.0.1:3000/'+companyName).text
    
        return render_template("games.html", companyName=companyName, allGames=allGames)
    
    else:
        return abort(404, description="It seems you are trying to access a page which is not a current game company.\nIf you feel something is missing that should be here, contact me.")

#page to suggest a game to me.
@app.route('/suggest_game')
def suggestion():
    return "Have a suggestion for a game or game company not listed here ? <br> Feel free to reach out to me."

#page for a "wishlist" feature that allows users to save games they are interested in purchasing or playing in the future.
@app.route('/wish_list')
def wish_list():
    return "your wish list of favourite games you are interested in purchasing/playing in the future"

#page for a "trending" section which displays the most popular games in the industry as a whole.
@app.route('/trending_list')
def trending():
    return "your trending list of most popular games from all popular game companies available on Game-Tier"

