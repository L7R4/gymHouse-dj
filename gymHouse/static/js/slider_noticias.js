const sliderContainer = document.getElementById('slider-container');
const slider = document.getElementById('slider');
const buttonLeft = document.getElementById('button-left');
const buttonRight = document.getElementById('button-right');

const sliderElements = document.querySelectorAll('.slider__element');
let itemCount = sliderElements.length;

const rootStyles = document.documentElement.style;
const firstElement_clon= slider.firstElementChild.cloneNode(true);
const lastElement_clon = slider.lastElementChild.cloneNode(true);


let slideCounter = 0;
let isInTransition = false;

const DIRECTION = {
  RIGHT: 'RIGHT',
  LEFT: 'LEFT'
};

slider.setAttribute("style","min-width:calc(100%/" + itemCount + ")");
tamañoSlider = slider.setAttribute("style","width:"+ itemCount*100 +"%");
sliderElements.forEach(function(image){
  image.setAttribute("style","width:calc(100%/" + itemCount + ")");
});

let operacion = 0;
let calcDisplaySlider = 100/itemCount;


const reorderSlide = () => {
  rootStyles.setProperty('--transition', 'none');
    if (slideCounter === sliderElements.length - 1) {
      slider.appendChild(slider.firstElementChild);
      operacion += (calcDisplaySlider);
      rootStyles.setProperty(
        '--slide-transform',
        `${operacion}%`
      );
      slideCounter--;
    } else if (slideCounter === 0) {
      slider.prepend(slider.lastElementChild);
      operacion += -(calcDisplaySlider);
      rootStyles.setProperty(
        '--slide-transform',
        `${operacion}%`
      );
      slideCounter++;
    }
    isInTransition = false;
  console.log(slideCounter)
  
};

const moveSlide = direction => {
  if (isInTransition) return;
  rootStyles.setProperty('--transition', 'transform 1s');
  isInTransition = true;
 
  if (direction === DIRECTION.LEFT) {
    operacion += (calcDisplaySlider);
    rootStyles.setProperty(
      '--slide-transform',
      `${operacion}%`
    );
    slideCounter--;
  } else if (direction === DIRECTION.RIGHT) {
    
    operacion += -(calcDisplaySlider);
    rootStyles.setProperty(
      '--slide-transform',
      `${operacion}%`
    );
    slideCounter++;
  }
};

//AUTOMATIZAR SLIDE
//let timerId=setInterval(()=>{moveSlide(DIRECTION.RIGHT);},6000);

buttonRight.addEventListener('click', () => moveSlide(DIRECTION.RIGHT));
buttonLeft.addEventListener('click', () => moveSlide(DIRECTION.LEFT));

slider.addEventListener('transitionend', reorderSlide);
reorderSlide()


//analizar que tengo hoy disponible del capital
//Estimar mis ingresos futuros de acuerdo al analisis de mercado
//jajajjajajjajaj escribia las notas de econ
//
//
//