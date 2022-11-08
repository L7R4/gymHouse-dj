window.addEventListener('load', profile)
window.addEventListener('resize', loadProfile)

function profile(){
    if(screen.width > 800){
        document.getElementById('section-profile').style.display='none';
        document.getElementById('show-profile').addEventListener('click',show)  
    } else {
        document.getElementById('section-profile').style.display='block';
        loadProfile();
    }
    
}

function show(){
    if(document.getElementById('section-profile').style.display=='none'){
        document.getElementById('section-profile').style.display='block';
        loadProfile();
    } else {
        document.getElementById('section-profile').style.display='none';
    }
}

function loadProfile(){
    document.getElementById('eprofile').style.display='none';
    const list = document.querySelectorAll('.list');
    let btnEditProfile = document.getElementById('profile_data--button')
    btnEditProfile.addEventListener('click',animationEdit)
    if(screen.width > 800){
        document.getElementById("navigation--space").style.display='none';
        document.getElementById("navigation").style.display='none';
        list.forEach((item) =>
        item.addEventListener('click',activeLink))
        document.getElementById('show-profile').addEventListener('click',show)
    } else {
        document.getElementById('section-profile').style.display='block';
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



function animationEdit(){
    if (screen.width > 700){
        document.getElementById('show-profile').removeEventListener('click',show) 
        document.getElementById("perfil_bg--gradient").style.transition = 'all 1s';
        document.getElementById("profile").style.display='none';
        document.getElementById("navbar--fill").style.display='none';
        document.getElementById("perfil_bg--gradient").classList.replace("perfil_bg--gradient","bgfill--gradient");
        document.getElementById("perfil_bg").classList.replace("perfil_bg","bgfill");
        setTimeout(sectionEdit,1100); 
    } else {
        document.getElementById("profile").style.display='none';
        document.getElementById("navbar--fill").style.display='none';
        document.getElementById("perfil_bg--gradient").classList.replace("perfil_bg--gradient","bgfill--gradient");
        document.getElementById("perfil_bg").classList.replace("perfil_bg","bgfill");
        setTimeout(sectionEdit,0); 
        
    }
    
}

function sectionEdit(){
    outAnimation()
    document.getElementById("eprofile").style.display='grid';
    let btnSaveProfile = document.getElementById('eprofile_data--button-save')
    btnSaveProfile.addEventListener('click',getBack)

    document.getElementById("navigation--space").style.display='none';
    document.getElementById("navigation").style.display='none';
    
    document.getElementById('man').addEventListener('click', genderMan)
    document.getElementById('woman').addEventListener('click', genderWoman)
    document.getElementById('other').addEventListener('click', genderOther)

    

    /*Contraseña actual*/
    document.getElementById('solid-eye-slash-actual').style.display='block'
    document.getElementById('solid-eye-actual').style.display="none"
    document.getElementById('solid-eye-slash-actual').addEventListener('click', function() {
        document.getElementById('solid-eye-slash-actual').style.display='none'
        document.getElementById('solid-eye-actual').style.display='block'
        document.getElementById('actualPassword').type='text'})
    
    document.getElementById('solid-eye-actual').addEventListener('click', function() {
        document.getElementById('solid-eye-actual').style.display='none'
        document.getElementById('solid-eye-slash-actual').style.display='block'
        document.getElementById('actualPassword').type='password'})

    /*Contraseña nueva*/
    document.getElementById('solid-eye-slash-new').style.display='block'
    document.getElementById('solid-eye-new').style.display="none"
    document.getElementById('solid-eye-slash-new').addEventListener('click', function() {
        document.getElementById('solid-eye-slash-new').style.display='none'
        document.getElementById('solid-eye-new').style.display='block'
        document.getElementById('newPassword').type='text'})
    
    document.getElementById('solid-eye-new').addEventListener('click', function() {
        document.getElementById('solid-eye-new').style.display='none'
        document.getElementById('solid-eye-slash-new').style.display='block'
        document.getElementById('newPassword').type='password'})



    /*Confirmar contraseña nueva*/
    document.getElementById('solid-eye-slash-confirm').style.display='block'
    document.getElementById('solid-eye-confirm').style.display="none"
    document.getElementById('solid-eye-slash-confirm').addEventListener('click', function() {
        document.getElementById('solid-eye-slash-confirm').style.display='none'
        document.getElementById('solid-eye-confirm').style.display='block'
        document.getElementById('confirmPassword').type='text'})
    
    document.getElementById('solid-eye-confirm').addEventListener('click', function() {
        document.getElementById('solid-eye-confirm').style.display='none'
        document.getElementById('solid-eye-slash-confirm').style.display='block'
        document.getElementById('confirmPassword').type='password'})
}

function getBack(){
    document.getElementById("profile_data--button").disabled = true;
    document.getElementById("perfil_bg--gradient").classList.replace("bgfill--gradient","perfil_bg--gradient");
    document.getElementById("perfil_bg--gradient").style.transition = 'all 1s';
    document.getElementById("perfil_bg").classList.replace("bgfill","perfil_bg");
    document.getElementById("profile").style.display='flex';
    document.getElementById("navbar--fill").style.display='block';
    document.getElementById("eprofile").style.display='none';
    document.getElementById('show-profile').addEventListener('click',show)  
    if (screen.width <= 700){
        document.getElementById("navigation--space").style.display='block';
        document.getElementById("navigation").style.display='flex';
    }

    setTimeout(() => {
        document.getElementById("profile_data--button").disabled = false;
    }, 1100);
    setTimeout(outAnimation,1100);
}

function outAnimation(){
    document.getElementById("perfil_bg--gradient").style.transition = 'none';
}

function genderMan(){
    
    document.getElementById('gender_woman').classList.remove('gender_selected')
    document.getElementById('gender_other').classList.remove('gender_selected')
    document.getElementById('gender_man').classList.add('gender_selected')
}

function genderWoman(){
    
    document.getElementById('gender_man').classList.remove('gender_selected')
    document.getElementById('gender_other').classList.remove('gender_selected')
    document.getElementById('gender_woman').classList.add('gender_selected')
}

function genderOther(){
    
    document.getElementById('gender_man').classList.remove('gender_selected')
    document.getElementById('gender_woman').classList.remove('gender_selected')
    document.getElementById('gender_other').classList.add('gender_selected')
}