let ejercicios = document.querySelectorAll(".ejercicio")
const ejercicio_pasosid= document.getElementById("ejercicio_pasosid")

ejercicios.forEach(element => {
    element.addEventListener("click", ()=>{
        divcerrado.classList.add("active")
        let ejer_clone = element.cloneNode(true)
        ejercicio_pasosid.insertAdjacentElement('beforebegin', ejer_clone)
        // ejercicio_pasosid
    })
})