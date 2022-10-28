window.addEventListener('load', loadNewsComplete)

function loadNewsComplete(){

    document.getElementById('fa-regular fa-heart').style.display='block';
    document.getElementById('fa-solid fa-heart').style.display='none';

    document.getElementById('fa-regular fa-heart').addEventListener('click', function(){
        document.getElementById('fa-regular fa-heart').style.display='none';
        document.getElementById('fa-solid fa-heart').style.display='block';
    })
    document.getElementById('fa-solid fa-heart').addEventListener('click', function(){
        document.getElementById('fa-solid fa-heart').style.display='none';
        document.getElementById('fa-regular fa-heart').style.display='block';
    })


    document.getElementById('fa-regular fa-comment').style.display='block';
    document.getElementById('fa-solid fa-comment').style.display='none';

    document.getElementById('fa-regular fa-comment').addEventListener('click', function(){
        document.getElementById('fa-regular fa-comment').style.display='none';
        document.getElementById('fa-solid fa-comment').style.display='block';
    })
    document.getElementById('fa-solid fa-comment').addEventListener('click', function(){
        document.getElementById('fa-solid fa-comment').style.display='none';
        document.getElementById('fa-regular fa-comment').style.display='block';
    })
}