let ejercicios = document.querySelectorAll(".ejercicio")
const ejercicio_pasosid= document.getElementById("ejercicio_pasosid")
const screen_ejercicio = document.querySelector(".screen-ejercicio")
console.table(screen_ejercicio)
ejercicios.forEach(element => {
    element.addEventListener("click", ()=>{
        console.table(element)
        divcerrado.classList.add("active")
        if (!element.children[0].checked){
            if (screen_ejercicio.childElementCount == 1){
                old_child= screen_ejercicio.children[0]
                screen_ejercicio.removeChild(old_child)
            }
            let ejer_clone = element.cloneNode(true)
            screen_ejercicio.appendChild(ejer_clone)
            // let pasos = ejer_clone.children[2]
            // let video = ejer_clone.children[3]
    
            // console.log(pasos)
            // console.log(video)
    
            // ejercicio_pasosid.appendChild(pasos)
            // pasos.classList.add("active")
            
            // ejercicio_videoid.appendChild(video)
            // video.classList.add("active")

            
        }
        
        
    })
})

// function desactiveDetalle() {
//     detalle.forEach(element => element.classList.remove("active"));
//   }