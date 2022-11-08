window.addEventListener('load', loadShifts)
window.addEventListener('resize', loadShifts)

function loadShifts(){
    const list = document.querySelectorAll('.list');
    if(screen.width > 800){
        document.getElementById("navigation--space").style.display='none';
        document.getElementById("navigation").style.display='none';
        list.forEach((item) =>
        item.addEventListener('click',activeLink))
    } else {
        document.getElementById("navigation--space").style.display='block';
        document.getElementById("navigation").style.display='flex';
        list.forEach((item) =>
        item.addEventListener('click',activeLink))
    }
}

function activeLink() {
    const list = document.querySelectorAll('.list');
    list.forEach((item) =>
    item.classList.remove('active'));
    this.classList.add('active');
    event.preventDefault();
}
