document.addEventListener("DOMContentLoaded", () => {
    let selectedMarque = document.querySelector("#seleceted_marque").textContent; 
    let selectedModele = document.querySelector("#seleceted_modele").textContent;
    setImagesNumber();
    setMarquesOnReady();
    setModeleOnReady(selectedMarque, selectedModele);
    let option = document.querySelector("#marque");
     option.addEventListener("change", function () {
     setModelesByMarque(option.value);
 })
});


async function setMarquesOnReady(){
    let marques = document.querySelector("#marque");
    let data = await fetch("/get-marques");
    finalData = await data.json();
    let selecetedMarque = document.getElementById('seleceted_marque').textContent;
    marques.innerHTML = "";
    for(let i=0; i<finalData.length; i++){
        let option = document.createElement("option");
        option.text = finalData[i].marque;
        option.value = finalData[i].marque;
        if(finalData[i].marque == selecetedMarque){
            option.selected = true;
        }
        marques.add(option);
    }
}




async function setModeleOnReady(marque, modele){
    let data = await fetch("/get-marques");
    finalData = await data.json();
    let modedle = document.querySelector("#modeles");
    modedle.innerHTML = "";
    for(let i=0; i<finalData.length; i++){
        if(finalData[i].marque == marque){
            for(let j=0; j<finalData[i].modeles.length; j++){
                option = document.createElement("option");
                option.text = finalData[i].modeles[j];
                option.value = finalData[i].modeles[j];
                if(option == modele){
                    option.selected = true;
                }
                modedle.add(option);
            }
        }
    }
}











function setImagesNumber(){
    let addArticleFormRightNbImagesText = document.querySelector("#addArticleFormRightNbImagesText");
    let images = document.querySelector("#imagesPreview");
    addArticleFormRightNbImagesText.innerHTML = images.childElementCount + " Images ont été télechargées";
}





async function setModelesByMarque(marque){
    let data = await fetch("/get-marques");
    finalData = await data.json();
    let selectModele = document.querySelector("#modeles");
    selectModele.innerHTML = "";
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






async function setMarques(){
    let data = await fetch("/get-marques");
    finalData = await data.json();
    selectMarques = document.querySelector("#searchbar-form__option__row__marque");
    let option = document.createElement("option");
    option.text = "Toutes les marques";
    option.value = "0";
    selectMarques.add(option);
    for(let i=0; i<finalData.length; i++){
        option = document.createElement("option");
        option.text = finalData[i].marque;
        option.value = finalData[i].marque;
        selectMarques.add(option);
    }
}



let fileInput = document.querySelector("#imagesToUpload")
let imageContainer = document.querySelector("#imagesPreview");
let numOfImgs = document.querySelector("#addArticleFormRightNbImagesText");

function preview(){
    let files = fileInput.files;
    for(let i=0; i<files.length; i++){
        console.log("entered the loop");
        let reader = new FileReader();
        reader.readAsDataURL(files[i]);
        reader.onload = function(){
            let div = document.createElement("div");
            console.log(div);
            let image = document.createElement("img");
            image.src = reader.result;
            image.setAttribute("id", "img")
            div.appendChild(image);
            imageContainer.appendChild(div);
            numOfImgs.innerHTML = imageContainer.childElementCount + " Images ont été téléchargées";
        }
    }
}