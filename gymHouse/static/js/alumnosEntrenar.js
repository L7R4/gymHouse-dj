let ejercicios = document.querySelectorAll(".ejercicio")
const ejercicio_pasosid= document.getElementById("ejercicio_pasosid")

ejercicios.forEach(element => {
    element.addEventListener("click", ()=>{
        console.table(element)
        divcerrado.classList.add("active")
        if (!element.children[0].checked){
            let ejer_clone = element.cloneNode(true)
    
            let pasos = ejer_clone.children[2]
            let video = ejer_clone.children[3]
    
            console.log(pasos)
            console.log(video)
    
            ejercicio_pasosid.appendChild(pasos)
            pasos.classList.add("active")
            
            ejercicio_videoid.appendChild(video)
            video.classList.add("active")

            ejercicio_pasosid.insertAdjacentElement('beforebegin', ejer_clone)
        }
        
        
    })
})

// function desactiveDetalle() {
//     detalle.forEach(element => element.classList.remove("active"));
//   }