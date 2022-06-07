let allCompanies = document.querySelector(".game_companies").innerHTML; //storing the current html text inside the .game_companies class.
document.querySelector(".game_companies").innerHTML = ""; //clearing out all the companies that was previously inside the .game_companies tag.
allCompanies = allCompanies.split(","); //array of split strings now returned.

console.log(allCompanies)
const gameDiv = document.querySelector(".game_companies"); 

let dateCounter = 0;

for(let i = 0; i < allCompanies.length; i++){
    const anchor = document.createElement("a"); //creating an anchor element.

    const currCompanyOrDate = allCompanies[i];

    if(currCompanyOrDate == "" || currCompanyOrDate === "None"){
        continue; //there is an empty company, which obviously should not have an element created for.
    }
    /*the date is date="MM/YYYY" format. So if date[0],date[1],date[3],date[4],date[5],date[6] are numbers and date[2] is not a number. Then a date is encountered.
     *Also, a date is encountered if MM = "NA" for month not applicable. So, the query "/YYYY" is being targetted. */
    else if(isNaN(currCompanyOrDate[2]) && !isNaN(currCompanyOrDate[3]) && !isNaN(currCompanyOrDate[4]) && !isNaN(currCompanyOrDate[5]) && !isNaN(currCompanyOrDate[6]) ){
        const companyNoDate = document.getElementById(allCompanies[dateCounter]);
        companyNoDate.innerHTML += " (" + currCompanyOrDate + ")";
        // console.log("DATE IS " + currCompanyOrDate + " FOR " + allCompanies[dateCounter])
        dateCounter++;
        continue;
    }
    anchor.setAttribute("href", "/" + currCompanyOrDate);
    anchor.innerHTML = currCompanyOrDate;

    anchor.setAttribute("draggable", "false"); //for each of the anchors made, the element cannot be dragged.
    anchor.setAttribute("id", currCompanyOrDate); //the anchor will have an id of the current company name.
    gameDiv.append(anchor);

} //end of for-loop

