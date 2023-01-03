/**
 * Name: Nilushanth Thiruchelvam.
 * Date: January 3, 2022
 * 
 * This is the server side to query the BudgetVisionApp database using Node.JS
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
    else console.log("successful connection to BudgetVisionApp database.");
});

/** create a route for all ea games from 2000 to 2009*/
app.get("/ea2000to2009", function(req, res){
    let stmt = "SELECT * FROM ea_games";
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








