document.addEventListener("scroll", () => {
    const header = document.querySelector(".bar-cont");
        
    if (window.scrollY > 1070){
        header.classList.add("scrolled")
    }else{
        header.classList.remove("scrolled")
        
    }
})