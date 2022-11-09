
let modal_plan_1 = document.getElementById("pop-up--first")
let modal_plan_2 = document.getElementById("pop-up--second")
let modal_plan_3 = document.getElementById("pop-up--third")

let button_next_modal_plan_1 = document.querySelector("#pop-up--first > #first_button")
let button_next_modal_plan_2 = document.querySelector(".container_buttons > #second_button")

button_next_modal_plan_2.onclick = ()=>{
    modal_plan_2.classList.add("active")
    modal_plan_3.classList.add("active")
}

button_next_modal_plan_2.nextElementSibling.onclick = () =>{
    modal_plan_2.classList.remove("active") // Display block
    modal_plan_1.classList.remove("active") //Display none
}



