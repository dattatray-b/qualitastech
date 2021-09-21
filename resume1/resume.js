const academics = document.querySelector('.academics')
const education = document.querySelector('.education')


if(education.style.display = "none"){
    academics.addEventListener( 'click' , () => {
        education.style.display = "inline"
    })
}

