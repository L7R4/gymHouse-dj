const buttons_alumnos = document.querySelectorAll(".shifts_info--pupils")
const window_turno = document.querySelector(".classmates > .classmates_names")
const modal_turno = document.querySelector(".classmates")

buttons_alumnos.forEach(element => {
    element.addEventListener("click", ()=>{
        // desactiveElement()
        // element.classList.add("element_clicked")
        
        let list_clone = element.nextElementSibling.cloneNode(true);
        
        if (window_turno.children.length == 1) {
            let exist_child_ul = document.querySelector(".classmates_names > .alumnos")
            window_turno.removeChild(exist_child_ul)
            window_turno.appendChild(list_clone)
        } else {
            window_turno.appendChild(list_clone)
        }
        modal_turno.classList.add("active")
    })
});

window_turno_alumnos_close_admin.onclick = function() {
    modal_turno.classList.remove("active")
}

function desactiveElement() {
    buttons_alumnos.forEach(element => element.classList.remove("active"));
}