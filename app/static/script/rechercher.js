



function divToForm(route){
    var div = document.getElementById("showHideOptionsDeContactesDiv")
    var form = document.createElement('form');
    form.setAttribute('action', 'route');
    form.setAttribute('method', 'post');
    form.innerHTML = div.innerHTML;

    div.parentNode.insertBefore(form, div);
    div.parentNode.removeChild(div);
}
