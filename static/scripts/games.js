
const allGamesText = document.querySelector("#all_games").textContent;
const allGamesArray = allGamesText.split("\n");

// remove the last element if it is an empty string
if (allGamesArray[allGamesArray.length - 1] === "") {
  allGamesArray.pop();
}

const allGamesDatabase = "[" + allGamesArray.join(",") + "]";

const allGamesJSON = JSON.parse(allGamesDatabase);

console.log(allGamesJSON) //log the entire database to the console. It is in JSON format.

//log the unique keys in the allGamesJSON object. Each key represents a table column name.
let keys = new Set()
for(let i = 0; i < allGamesJSON.length; i++){
    for(let key in allGamesJSON[i]){
        keys.add(key);
    }
}
console.log(keys)

//the all games table.
const allGamesTable = document.createElement("table");
allGamesTable.className = "all_games_table";

//all games table head.
const tableHead = document.createElement("thead");
const tableHeadRow = document.createElement("tr");

for (let key of keys){
    let tempHeadRow = `<th>${key}</th>`;
    tableHeadRow.insertAdjacentHTML("beforeend", tempHeadRow);
}

tableHead.appendChild(tableHeadRow);
allGamesTable.appendChild(tableHead);

//all games table body.
const tableBody = document.createElement("tbody");
allGamesJSON.forEach(function(game){
    let tableBodyRow = document.createElement("tr");
    for(let key in game){
        tableBodyRow.insertAdjacentHTML("beforeend", `<td>${game[key]}</td>`);
    }
    tableBody.appendChild(tableBodyRow);
});


allGamesTable.appendChild(tableBody);
const flexContainer = document.querySelector('.table_container');
flexContainer.appendChild(allGamesTable);