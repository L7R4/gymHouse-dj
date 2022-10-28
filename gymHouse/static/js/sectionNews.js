window.addEventListener('load', loadNews)

window.addEventListener('resize', loadNews)

function loadNews(){
    
    if (screen.width > 800){
            document.querySelector(".wrapper").style.display='none';
            document.querySelector(".news_slider").style.display='inline-block';
            document.getElementById("navigation--space").style.display='none';
            document.getElementById("navigation").style.display='none';
            const container = document.querySelector(".news_slider");
            const cards = document.querySelector(".cards");

            /* keep track of user's mouse down and up*/ 
            let isPressedDown = false;
            /* x horizontal space of cursor from inner container */
            let cursorXSpace;

            container.addEventListener("mousedown", (e) => {
            isPressedDown = true;
            cursorXSpace = e.offsetX - cards.offsetLeft;
            container.style.cursor = "grabbing";
            });


            container.addEventListener("mouseup", () => {
                container.style.cursor = "grab";
            });

            window.addEventListener("mouseup", () => {
            isPressedDown = false;
            });

            container.addEventListener("mousemove", (e) => {
            if (!isPressedDown) return;
            e.preventDefault();
            cards.style.left = `${e.offsetX - cursorXSpace}px`;
            boundCards();
            });

            function boundCards() {
                const container_rect = container.getBoundingClientRect();
                const cards_rect = cards.getBoundingClientRect();
            
                if (parseInt(cards.style.left) > 0) {
                    cards.style.left = 0;
                } else if (cards_rect.right < container_rect.right) {
                    cards.style.left = `-${cards_rect.width - container_rect.width}px`;
                }
            }
        } 
    if (screen.width <= 800) {
            document.querySelector(".news_slider").style.display='none';
            document.querySelector(".wrapper").style.display='flex';
            const wrapper = document.querySelector('.wrapper')

            let pressed = false
            let startX = 0

            wrapper.addEventListener('mousedown', function (e) {
            pressed = true
            startX = e.clientX
            this.style.cursor = 'grabbing'
            })

            wrapper.addEventListener('mouseleave', function (e) {
            pressed = false
            })

            window.addEventListener('mouseup', function (e) {
            pressed = false
            wrapper.style.cursor = 'grab'
            })

            wrapper.addEventListener('mousemove', function (e) {
            if(!pressed) {
                return
            }

            this.scrollLeft += startX - e.clientX
            })

            const list = document.querySelectorAll('.list');
            document.getElementById("navigation--space").style.display='block';
            document.getElementById("navigation").style.display='flex';
            list.forEach((item) =>
            item.addEventListener('click',activeLink))

            function activeLink() {
                const list = document.querySelectorAll('.list');
                list.forEach((item) =>
                item.classList.remove('active'));
                this.classList.add('active');
                event.preventDefault();
            }
        }
    
}



