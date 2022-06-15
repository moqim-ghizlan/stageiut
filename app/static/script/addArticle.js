let option = document.querySelector("#marque");
option.addEventListener("change", function () {
    setModelesByMarque(option.value);
})




document.addEventListener("DOMContentLoaded", setMarquesOnReady());


async function setMarquesOnReady(){
    let selectModele = document.querySelector("#marque");
    let data = await fetch("/get-marques");
    finalData = await data.json();
    for(let i=0; i<finalData.length; i++){
        let option = document.createElement("option");
        option.text = finalData[i].marque;
        option.value = finalData[i].marque;
        selectModele.add(option);
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




async function setModelesByMarque(marque){
    let data = await fetch("/get-marques");
    finalData = await data.json();
    let selectModele = document.querySelector("#searchbar-form__option__row__modeles");
    selectModele.innerHTML = "";
    let option = document.createElement("option");
    option.text = "Toutes les modèles";
    option.value = "0";
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


let fileInput = document.querySelector("#imagesToUpload")
let imageContainer = document.querySelector("#imagesPreview");
let numOfImgs = document.querySelector("#addArticleFormRightNbImagesText");
for(let i=0; i<fileInput.files.length; i++){
    let div = document.createElement("div");
    let image = document.createElement("img");
    image.className = "imagePreview";
    image.src = URL.createObjectURL(fileInput.files[i]);
    div.appendChild(image);
    let span = document.createElement("span");
    span.className = "add_article_form_right_reviewImages_span";
    span.innerHTML = "&times;";
    div.appendChild(span);
    imageContainer.appendChild(div);
    span.addEventListener('click', function handleClick(event) {
        console.log('element clicked 🎉🎉🎉', event);
      });
}


numOfImgs.innerHTML = `${imageContainer.childElementCount} images ont été ajoutées`;

function delete_image(){
    
}

