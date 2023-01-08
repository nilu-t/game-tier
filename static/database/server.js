/**
 * Name: Nilushanth Thiruchelvam.
 * Date: January 3, 2022
 * 
 * This is the server side to query the GameTier database using Node.JS
 */

const express = require("express");
const body_parser = require("body-parser");
const mysql = require("mysql2");
const config = require("./config"); //module which contains the database configuration details such as user, host, password etc.

const app = express();

/** establish app listening on port */
const port = 3000;
app.listen(port, function(error){
    if(error) console.log(error)
    else console.log("App listening on port %d", port);
});

/** create mysql connection to database */
var con = mysql.createConnection({
    user: config.configObj.user,
    host: config.configObj.host,
    database: config.configObj.database,
    password: config.configObj.password
});

/** testing the mysql connection */
con.connect(function(error){
    if(error) console.log(error)
    else console.log(`successful connection to ${config.configObj.database} database.`);
});

/** iterating through an array of all companies provided by game tier.
 *  A route is created for that company.
 *  A get request is made to that route and a response is sent to it containing ALL game information from each game company.
 */
var allCompanies = ["Tencent", "Rare", "Zynga", "Square Enix Holdings Co. Ltd", "Nexon Co. Ltd", "BioWare", "id Software", "Konami Holdings Corporations", 
"Blizzard Entertainment Inc", "LucasArts", "Sonic Team", "Bethesda Game Studios", "NCSOFT", "Insomniac Games Inc", "Bungie Inc", "Capcom Company Ltd", "Treasure Co. Ltd", "PopCap Games", 
"Level-5 Company", "Retro Studios", "ZeniMax Media Inc", "Gameloft", "Take-Two Interactive Software Inc", "Infinity Ward", "Naughty Dog", "Sega Games Co. Ltd", "Valve Corporation", 
"Sony", "Microsoft", "Bandai Namco", "Ubisoft", "Rockstar Games", "Epic Games", "Activision Blizzard", "Electronic Arts", "Nintendo", "Mojang"];

for(let i = 0; i < allCompanies.length; i++){
    let route = `/${allCompanies[i].split(" ").join("%20")}`;
    //console.log(route);
    app.get(route, function(req, res){
        let tableName = `${allCompanies[i].toLowerCase().split(" ").join("_").split(".").join("").split("-").join("_")}`;
        let stmt = "SELECT * FROM " + tableName;

        //special case for electronic arts which has 3 seperate tables due to a large database of video games.
        if(allCompanies[i] === "Electronic Arts"){
            stmt = "SELECT * FROM ea_games";
        }

        con.query(stmt, function(error, result,fields){
            if(error) console.log(error)
            else{
                let allData = "";

                result.forEach(function(item){
                    allData = allData + JSON.stringify(item) + "\n";
                });
                res.send(allData);
            }
        });
    });

}

