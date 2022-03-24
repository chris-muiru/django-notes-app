let btnMenu = document.getElementById('btn-menu');
let divLinks = document.getElementById('div-links');

const setDivState=()=>{
    if(divLinks.style.display==""){ 
        divLinks.style.display="block";
    }
    else if(divLinks.style.display=="block"){
        divLinks.style.display="none"
    }

}

btnMenu.addEventListener('click',setDivState)