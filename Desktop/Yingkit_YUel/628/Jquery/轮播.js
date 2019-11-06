var jsLis = document.getElementsByClassName('li');

var jsImg = document.getElementById('img');

var currentPage = 0;

var jsBox = document.getElementById('box');

var jsLeftBtn = document.getElementById('leftbt');
var jsRightBtn = document.getElementById('rightbt');

jsLis[0].style.backgroundColor = 'red';

var pTimer = setInterval(func, 1000);
function func() {
    currentPage++;
    if (currentPage == 7) {
        currentPage = 0;
    }

    jsImg.src = currentPage + '.jpeg';

    for (var i = 0; i < jsLis.length; i++) {
        jsLis[i].style.backgroundColor = '#aaa';
    }

    jsLis[currentPage].style.backgroundColor = 'red';
}

jsBox.addEventListener('mousemove', function () {
    clearInterval(pTimer);
    jsLeftBtn.style.display = 'block';
    jsRightBtn.style.display = 'block';
},false);

jsBox.addEventListener('mouseout', function () {
    pTimer = setInterval(func, 1000);

    jsLeftBtn.style.display = 'none';
    jsRightBtn.style.display = 'none';
}, false);

jsLeftBtn.addEventListener('mouseover', function () {
    jsLeftBtn.style.backgroundColor = 'rgba(0,0,0,0.6)';
}, false);

jsRightBtn.addEventListener('mouseover', function () {
    jsRightBtn.style.backgroundColor = 'rgba(0,0,0,0.6)';
}, false);

jsLeftBtn.addEventListener('mouseout', function () {
    jsLeftBtn.style.backgroundColor = 'rgba(0,0,0,0.2)';
}, false);

jsRightBtn.addEventListener('mouseout', function () {
    jsRightBtn.style.backgroundColor = 'rgba(0,0,0,0.2)';
}, false);

jsLeftBtn.addEventListener('click', function () {
    currentPage--;
    if(currentPage == -1) {
        currentPage = 7;
    }
    jsImg.src = currentPage + '.jpeg';

    for (var i = 0; i < jsLis.length; i++) {
        jsLis[i].style.backgroundColor = '#aaa';
    }

    jsLis[currentPage].style.backgroundColor = 'red';
}, false)

jsRightBtn.addEventListener('click', function () {
    currentPage++;

    if (currentPage == 7) {
        currentPage = 0;
    }

    jsImg.src = currentPage + '.jpeg';

    for (var i = 0; i < jsLis.length; i++) {
        jsLis[i].style.backgroundColor = '#aaa';
    }

    jsLis[currentPage].style.backgroundColor = 'red';
}, false)

for (var i = 0; i < jsLis.length; i++) {

    jsLis[i].onmouseover = function () {
        //当前元素节点的文本节点

        //在事件函数中，this代表对应的元素节点
        currentPage = parseInt(this.innerHTML) - 1;
        jsImg.src = currentPage + ".jpg";
        for (var i = 0; i < jsLis.length; i++) {
            jsLis[i].style.backgroundColor = "#aaa";
        }
        jsLis[currentPage].style.backgroundColor = "red";
    };
}

