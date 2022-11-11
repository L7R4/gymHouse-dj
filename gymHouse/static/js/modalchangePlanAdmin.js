const boton_modal = document.querySelector("#button_modal_plan");
const modal_plan = document.getElementById("planmensual--pop-up")
const modal_plan_1 = document.getElementById("pop-up--first")
const modal_plan_2 = document.getElementById("pop-up--second")
const modal_plan_3 = document.getElementById("pop-up--third")
const close_modal = document.querySelector("#close_modal_plan")
const next = document.getElementById("first_button")
const second_button = document.getElementById("second_button")
const second_secondbutton = document.getElementById("second_secondbutton")

boton_modal.addEventListener("click",()=>{
    modal_plan.classList.add("active")
})
close_modal.addEventListener("click", ()=>{
    modal_plan.classList.remove("active")
})
next.addEventListener("click",()=>{
    modal_plan_1.classList.add("active")
    modal_plan_2.classList.add("active")
})

second_button.addEventListener("click", ()=>{
    modal_plan_2.classList.remove("active")
    modal_plan_3.classList.add("active")
})

second_secondbutton.addEventListener("click", ()=>{
    modal_plan_2.classList.remove("active")
    modal_plan_1.classList.remove("active")
})

