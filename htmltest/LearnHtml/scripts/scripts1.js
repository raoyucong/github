window.onload = function () {

    let myTitle = document.querySelector('button');
    
    myTitle.onclick = function() {
        let titleString = myTitle.getAttribute('class');
        if(titleString === "title") {
            myTitle.innerHTML = "正在学习···";
        }else{
            myTitle.innerHTML = "正在学习";
        }
    }
    };