const buttons_alumnos = document.querySelectorAll(".shifts_info--pupils")
const window_turno = document.querySelector(".window_turno_alumnos > .alumnos_wrapper")


buttons_alumnos.forEach(element => {
    element.addEventListener("click", ()=>{
        // desactiveElement()
        // element.classList.add("element_clicked")
        
        let list_clone = element.nextElementSibling.cloneNode(true);
        
        if (window_turno.children.length == 1) {
            let exist_child_ul = document.querySelector(".alumnos_wrapper > .alumnos")
            window_turno.removeChild(exist_child_ul)
            window_turno.appendChild(list_clone)
        } else {
            window_turno.appendChild(list_clone)
        }
        window_turno_alumnos.classList.add("active")
    })
});

window_turno_alumnos_close.onclick = function() {
    window_turno_alumnos.classList.remove("active")
}

function desactiveElement() {
    buttons_alumnos.forEach(element => element.classList.remove("active"));
}