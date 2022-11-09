const days = document.querySelectorAll(".day")

console.log(days)
days.forEach(e =>{
    value_day = e.children[1].value
    e.children[0].textContent = value_day.slice(0,3).toUpperCase()
    e.children[0].addEventListener("click", () =>{
        if (!e.classList.contains("select")) {
            e.classList.add("select")
            e.children[2].classList.add("select")
        }else{
            e.classList.remove("select")
            e.children[2].classList.remove("select")
        }
    })
})