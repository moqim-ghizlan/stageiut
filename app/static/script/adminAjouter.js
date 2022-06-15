document.addEventListener("DOMContentLoaded", () => {
    $('.toast').toast('show');


    setMarquesOnReady()
    setModelesByMarque("Audi");


    let option = document.querySelector("#marque");
     option.addEventListener("change", function () {
     setModelesByMarque(option.value);
 })
});

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


let fileInput = document.querySelector("#imagesToUpload")
let imageContainer = document.querySelector("#imagesPreview");
let numOfImgs = document.querySelector("#addArticleFormRightNbImagesText");

function preview(){
    let files = fileInput.files;
    for(let i=0; i<files.length; i++){
        let reader = new FileReader();
        reader.readAsDataURL(files[i]);
        reader.onload = function(){
            let div = document.createElement("div");
            let image = document.createElement("img");
            // let span = document.createElement("span");
            // // span.classList.add('add_article_form_right_reviewImages_span');
            // span.innerHTML = "&#10005;";
            image.src = reader.result;
            image.setAttribute("id", "img")
            div.appendChild(image);
            // div.appendChild(span);
            imageContainer.appendChild(div);
            numOfImgs.innerHTML = imageContainer.childElementCount + " Images ont été téléchargées";
            // span.addEventListener("click", deleteDiv());
        }
    }
}


function deleteDiv(){
    let fileInput = document.querySelector("#imagesToUpload")
    let files = fileInput.files;
    console.log("click")
    return function(){
        // for(let i = 0; i<files.length; i++){
        //     if(files[i].name == this.closest("#img").src.split("/").pop()){
        //         files.splice(i, 1);
        //     }
        // }
        imageContainer.removeChild(this);
        numOfImgs.innerHTML = imageContainer.childElementCount + " Images ont été téléchargées";

    }
}










