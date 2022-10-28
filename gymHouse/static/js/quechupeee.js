let ejercicios = document.querySelectorAll(".ejercicio")
let form_child = document.querySelector(".ejercicio-pasos > form")
ejercicios.forEach(element => {
    element.addEventListener("click", ()=>{
        console.table(element)
        let title_element = element.parentElement.parentNode.children[0].children[0]
        let algo = element.getElementsByClassName(".imgejercicio")
        
        
        let title_element_clone = title_element.cloneNode(true)
        console.log(title_element_clone)
        let div_selec_clone = element.cloneNode(true)
        form_child.appendChild(title_element_clone)
        form_child.appendChild(div_selec_clone)
        if (condition) {
            
        }
    })

    
});