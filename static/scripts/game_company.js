let allCompanies = document.querySelector(".game_companies").innerHTML; //storing the current html text inside the .game_companies class.
document.querySelector(".game_companies").innerHTML = ""; //clearing out anything that was previously inside the .game_companies tag.
allCompanies = allCompanies.split("\n"); //array of split strings now returned.

console.log(allCompanies)
const gameDiv = document.querySelector(".game_companies"); 

for(let i = 0; i < allCompanies.length; i++){
    const anchor = document.createElement("a"); //creating an anchor element.

    const currCompany = allCompanies[i];

    //switch case statement for adding anchor href attributes to each of the elements.
    switch(currCompany){
        case "Microsoft":
            anchor.setAttribute("href", "/microsoft");
            anchor.innerHTML = "Microsoft";
            break;
        
        case "Bandai Namco":
            anchor.setAttribute("href", "/bandai_namco");
            anchor.innerHTML = "Bandai Namco";
            break;
        
        case "Ubisoft":
            anchor.setAttribute("href", "/ubisoft");
            anchor.innerHTML = "Ubisoft";
            break;
        
        case "Epic Games":
            anchor.setAttribute("href", "/epic_games");
            anchor.innerHTML = "Epic Games";
            break;
        
        case "Activision Blizzard":
            anchor.setAttribute("href", "/activision_blizzard");
            anchor.innerHTML = "Activision Blizzard";
            break;

        case "Electronic Arts":
            anchor.setAttribute("href", "/electronic_arts");
            anchor.innerHTML = "Electronic Arts";
            break;
        
        case "Nintendo":
            anchor.setAttribute("href", "/nintendo");
            anchor.innerHTML = "Nintendo";
            break;
        
        case "Mojang":
            anchor.setAttribute("href", "/mojang");
            anchor.innerHTML = "Mojang";
            break;
        
        case "Sony":
            anchor.setAttribute("href", "/sony");
            anchor.innerHTML = "Sony";
            break;

        case "Rockstar Games":
            anchor.setAttribute("href", "/rockstar_games");
            anchor.innerHTML = "Rockstar Games";
            break;

        case "Valve Corporation":
            anchor.setAttribute("href", "/valve_corporation");
            anchor.innerHTML = "Valve Corporation";
            break;

        case "Sega Games Co. Ltd":
            anchor.setAttribute("href", "/sega_games");
            anchor.innerHTML = "Sega Games Co. Ltd";
            break;

        case "Naughty Dog Inc":
            anchor.setAttribute("href", "/naughty_dog");
            anchor.innerHTML = "Naughty Dog Inc";
            break;

         case "Infinity Ward":
            anchor.setAttribute("href", "/infinity_ward");
            anchor.innerHTML = "Infinity Ward";
            break;

        case "Take-Two Interactive Software Inc":
            anchor.setAttribute("href", "/take_two_interactive_software");
            anchor.innerHTML = "Take-Two Interactive Software Inc";
            break;

        case "Gameloft":
            anchor.setAttribute("href", "/gameloft");
            anchor.innerHTML = "Gameloft";
            break;
        
        case "ZeniMax Media Inc":
            anchor.setAttribute("href", "/zenimax_media");
            anchor.innerHTML = "ZeniMax Media Inc";
            break;

        case "Zynga":
            anchor.setAttribute("href", "/zynga");
            anchor.innerHTML = "Zynga";
            break;

        case "Retro Studios":
            anchor.setAttribute("href", "/retro_studios");
            anchor.innerHTML = "Retro Studios";
            break;
        
        case "Level-5 Company":
            anchor.setAttribute("href", "/level5");
            anchor.innerHTML = "Level-5 Company";
            break;

        case "PopCap Games":
            anchor.setAttribute("href", "/popcap_games");
            anchor.innerHTML = "PopCap Games";
            break;
        
        case "Treasure Co. Ltd":
            anchor.setAttribute("href", "/treasure");
            anchor.innerHTML = "Treasure Co. Ltd";
            break;

        case "Capcom Company Ltd":
            anchor.setAttribute("href", "/capcom_company");
            anchor.innerHTML = "Capcom Company Ltd";
            break;

        case "Bungie Inc":
            anchor.setAttribute("href", "/bungie");
            anchor.innerHTML = "Bungie Inc";
            break;

        case "Insomniac Games Inc":
            anchor.setAttribute("href", "/insomniac_games");
            anchor.innerHTML = "Insomniac Games Inc";
            break;
        
        case "NCSOFT":
            anchor.setAttribute("href", "/ncsoft");
            anchor.innerHTML = "NCSOFT";
            break;
        
        case "Bethesda Game Studios":
            anchor.setAttribute("href", "/bethesda_game_studios");
            anchor.innerHTML = "Bethesda Game Studios";
            break;

        case "Sonic Team":
            anchor.setAttribute("href", "/sonic_team");
            anchor.innerHTML = "Sonic Team";
            break;
        
        case "LucasArts":
            anchor.setAttribute("href", "/lucasarts");
            anchor.innerHTML = "LucasArts";
            break;

        case "Blizzard Entertainment Inc":
            anchor.setAttribute("href", "/blizzard_entertainment");
            anchor.innerHTML = "Blizzard Entertainment Inc";
            break;

        case "Konami Holdings Corporations":
            anchor.setAttribute("href", "/konami_holdings_corporations");
            anchor.innerHTML = "Konami Holdings Corporations";
            break;
        
        case "id Software":
            anchor.setAttribute("href", "/id_software");
            anchor.innerHTML = "id Software";
            break;

        case "BioWare":
            anchor.setAttribute("href", "/bioware");
            anchor.innerHTML = "BioWare";
            break;

        case "Nexon Co. Ltd":
            anchor.setAttribute("href", "/nexon");
            anchor.innerHTML = "Nexon Co. Ltd";
            break;

        default:
            continue; //if none of the cases match skip to the next iteration.
    }//end of switch statement.

    anchor.setAttribute("draggable", "false"); //for each of the anchors made, the element cannot be dragged.
    gameDiv.append(anchor);


} //end of for-loop

