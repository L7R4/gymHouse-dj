const list_comentarios = async () =>{
    try{
        const response = await fetch("./comments/")
        // console.log(response)
        const data = await response.json()
        console.log(data)
    }
    catch(error){
        console.log(error)
    }
}
window.addEventListener("load", async()=>{
    await list_comentarios();
})