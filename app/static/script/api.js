let option = document.querySelector("#searchbar-form__option__row__marque");
if (option) {
    option.addEventListener("change", function () {
        let marque = document.querySelector("#searchbar-form__option__row__marque").value;
        
        setModelesByMarque(marque);
    })
}




document.addEventListener("DOMContentLoaded", () => {
    let selectModele = document.querySelector("#searchbar-form__option__row__modeles");
    selectModele.innerHTML = "";
    let option = document.createElement("option");
    option.text = "Toutes les modèles";
    option.value = "all";
    selectModele.add(option);
    setMarques()});


async function setMarques(){
    let data = await fetch("/get-marques");
    finalData = await data.json();
    selectMarques = document.querySelector("#searchbar-form__option__row__marque");
    let option = document.createElement("option");
    option.text = "Toutes les marques";
    option.value = "all";
    selectMarques.add(option);
    for(let i=0; i<finalData.length; i++){
        option = document.createElement("option");
        option.text = finalData[i].marque;
        option.value = finalData[i].marque;
        selectMarques.add(option);
    }
}




async function setModelesByMarque(marque){
    let data = await fetch("/get-marques");
    finalData = await data.json();
    let selectModele = document.querySelector("#searchbar-form__option__row__modeles");
    selectModele.innerHTML = "";
    let option = document.createElement("option");
    option.text = "Toutes les modèles";
    option.value = "all";
    selectModele.add(option);
    for(let i=0; i<finalData.length; i++){
        if(finalData[i].marque == marque){
            for(let j=0; j<finalData[i].modeles.length; j++){
                option = document.createElement("option");
                option.text = finalData[i].modeles[j];
                option.value = finalData[i].modeles[j];
                selectModele.add(option);
            }
        }
    }
}