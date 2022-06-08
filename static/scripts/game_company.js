let allCompanies = document.querySelector(".game_companies").innerHTML; //storing the current html text inside the .game_companies class.
document.querySelector(".game_companies").innerHTML = ""; //clearing out all the companies that was previously inside the .game_companies tag.
allCompanies = allCompanies.split(","); //array of split strings now returned.

console.log(allCompanies)
const gameDiv = document.querySelector(".game_companies"); 

let contentCounter = 0;

for(let i = 0; i < allCompanies.length; i++){
    const anchor = document.createElement("a"); //creating an anchor element.

    const companyOrExtraContent = allCompanies[i];

    if(companyOrExtraContent == "" || companyOrExtraContent === "None"){
        continue; //there is an empty company, which obviously should not have an element created for.
    }
    /* "extra content" is wrapped in paranthesis. Extra content is appended to the company ASSUMING!!! iterations of all companies have already finished.  */
    else if(companyOrExtraContent[0] == "(" && companyOrExtraContent[companyOrExtraContent.length - 1] == ")"){
        const companyNoContent = document.getElementById(allCompanies[contentCounter]);
        companyNoContent.innerHTML += " " + companyOrExtraContent
        contentCounter++;
        continue;
    }
    anchor.setAttribute("href", "/" + companyOrExtraContent);
    anchor.innerHTML = companyOrExtraContent;

    anchor.setAttribute("draggable", "false"); //for each of the anchors made, the element cannot be dragged.
    anchor.setAttribute("id", companyOrExtraContent); //the anchor will have an id of the current company name.
    gameDiv.append(anchor);

} //end of for-loop

