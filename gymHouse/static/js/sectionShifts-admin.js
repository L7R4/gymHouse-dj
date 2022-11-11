window.addEventListener('load', loadShifts)
window.addEventListener('resize', loadShifts)

/*Inicializacion*/
// document.getElementById('planmensual--pop-up').style.display='none';
document.getElementById("navigation--space").style.display='none';
document.getElementById("navigation").style.display='none';
/*------------------------------------------------------------------*/

function loadShifts(){
    const list = document.querySelectorAll(".list");

    if(screen.width > 800){
        document.getElementById("navigation--space").style.display='none';
        document.getElementById("navigation").style.display='none';
        list.forEach((item) =>
        item.addEventListener('click',activeLink));
        document.getElementById('change-plan').addEventListener('click', changeShift);
    } else {
        document.getElementById("navigation--space").style.display='block';
        document.getElementById("navigation").style.display='flex';
        list.forEach((item) =>
        item.addEventListener('click',activeLink));
        document.getElementById('change-plan').addEventListener('click', changeShift);
    }
    
}

/*Esto es para el nav celu*/
function activeLink() {
    const list = document.querySelectorAll('.list');
    list.forEach((item) =>
    item.classList.remove('active'));
    this.classList.add('active');
    event.preventDefault();
}

/*Funcionamiento del cambiar turno--------------------------------------------------*/
function changeShift(){
    /*Botones*/
    const popUp = document.getElementById('planmensual--pop-up')
    popUp.style.display='flex';
    const first = document.getElementById('pop-up--first');
    first.style.display='flex';
    const second = document.getElementById('pop-up--second');
    second.style.display='none';
    const third = document.getElementById('pop-up--third');
    third.style.display='none';

    /*Seleccionar Alumnos*/
    const selected = document.querySelector(".selected");
    const optionsContainer = document.querySelector(".options-container");

    const optionsList = document.querySelectorAll(".option");
    /*-------------------------------------------------------------------------*/

    /*Cerrar todo*/
    const xMark = document.querySelectorAll(".fa-xmark");
    xMark.forEach( mark => {
            mark.addEventListener('click', e => {
                popUp.style.display = 'none';
                first.style.display = 'none';
                second.style.display = 'none';
                third.style.display = 'none';
                optionsContainer.classList.remove("actived");
            })
    });

    /*Primer po-up---------------------------------------------------------------------------------*/ 
    document.getElementById('first_button').addEventListener('click', firstButton => {
            first.style.display = 'none';
            second.style.display = 'flex';
    });

    document.getElementById('first_secondbutton').addEventListener('click', firstSecondButton => {
            popUp.style.display = 'none';
            first.style.display = 'none';
            second.style.display = 'none';
            third.style.display = 'none';
            optionsContainer.classList.remove("actived");
    });

    /*Segundo po-up---------------------------------------------------------------------------------*/ 
    document.getElementById('second_button').addEventListener('click', firstButton => {
        second.style.display = 'none';
        third.style.display = 'flex';
    });

    document.getElementById('second_secondbutton').addEventListener('click', firstSecondButton => {
            second.style.display = 'none';
            first.style.display = 'flex';
    });


    /*-------------------------------------------------------------------*/

    /*Esto es para seleccionar el alumno*/

    selected.addEventListener("click", () => {
        optionsContainer.classList.toggle("actived");
    });

    optionsList.forEach(o => {
        o.addEventListener("click", () => {
            selected.innerHTML = o.querySelector("label").innerHTML;
            optionsContainer.classList.remove("actived");
        });
    });
    /*-------------------------------------------------------------------*/
    /*Esto es para seleccionar la hora*/
    const customNum = document.querySelectorAll('.custom-num');

    customNum.forEach( num => {

        const numInput = document.getElementById('num-imput');
        const arrUp = document.getElementById('arr-up');
        const arrDown = document.getElementById('arr-down');

        if(screen.width > 800){
            arrUp.addEventListener('click', () => {
                numInput.stepUp();
                checkMaxMin();
            });
    
            arrDown.addEventListener('click', () => {
                numInput.stepDown();
                checkMaxMin();
            });
        } else {
            arrUp.addEventListener('click', () => {
                numInput.stepDown();
                checkMaxMin();
            });
    
            arrDown.addEventListener('click', () => {
                numInput.stepUp();
                checkMaxMin();
            });
        }
        

        numInput.addEventListener('input', checkMaxMin);

        /*Esto es para seleccionar la hora*/
        function checkMaxMin(){
            const numInputValue = parseInt(numInput.value);
            const numInputMax = parseInt(numInput.max);
            const numInputMin = parseInt(numInput.min);

            if(screen.width > 800){
                if(numInputValue === numInputMax) {
                    numInput.style.marginRight = "auto";
                    numInput.style.marginLeft = "unset";
                    numInput.style.width = "40%";
                    arrUp.style.display = "none";
                    arrDown.style.display = "block";
                }else if (numInputValue === numInputMin) {
                    numInput.style.marginLeft = "auto";
                    numInput.style.marginRight = "unset";
                    numInput.style.width = "40%";
                    arrDown.style.display = "none";
                    arrUp.style.display = "block";
                }else {
                    arrUp.style.display = "block";
                    arrDown.style.display = "block";
                }
            } else {
                if(numInputValue === numInputMax) {
                    numInput.style.marginBottom = "unset";
                    numInput.style.marginTop= "auto";
                    numInput.style.height = "60%";
                    arrUp.style.display = "block";
                    arrUp.style.padding = "0 .5rem .5rem .5rem";
                    arrDown.style.display = "none";
                }else if (numInputValue === numInputMin) {
                    numInput.style.marginTop = "unset";
                    numInput.style.marginBottom = "auto";
                    numInput.style.height = "60%";
                    arrDown.style.display = "block";
                    arrDown.style.padding = ".5rem .5rem 0 .5rem";
                    arrUp.style.display = "none";
                }else {
                    arrUp.style.display = "block";
                    arrDown.style.display = "block";
                }
            }
            
        }
    });
    
    /*-------------------------------------------------------------------*/
}