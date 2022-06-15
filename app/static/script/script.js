function hideShowContactes(){
    let showHideOptionDeContactesDiv = document.querySelector("#showHideOptionsDeContactesDiv");
    if(showHideOptionDeContactesDiv.style.display !== "none"){
        showHideOptionDeContactesDiv.style.display = "none"
    }else{
        showHideOptionDeContactesDiv.style.display = "flex";
    }
}

function myFunction() {
    var x = document.getElementById("myTopnav");
    if (x.className === "topnav") {
        x.className += " responsive";
    } else {
        x.className = "topnav";
    }
}

function showHideOptionDeRechercheDiv(){
    let showHideOptionDeRechercheDiv = document.querySelector("#showHideOptionDeRechercheDiv");
    if(showHideOptionDeRechercheDiv.style.display !== "none"){
        showHideOptionDeRechercheDiv.style.display = "none"
        }else{
            showHideOptionDeRechercheDiv.style.display = "block";
        }
    }