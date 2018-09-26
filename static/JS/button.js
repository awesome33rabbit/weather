
var nav1 = document.getElementById("wea");

var nav2 = document.getElementById("page2");
var nav3 = document.getElementById("wea_index");
var nav4 = document.getElementById("main");
var nav5 = document.getElementById("chartroom");

document.getElementById("button2").onclick = function() {

    if (nav2.style.visibility = 'hidden') {
        nav3.style.visibility = 'hidden';
        nav4.style.visibility = 'hidden';
        nav5.style.visibility = 'hidden';
        document.getElementById('mybackground').style.width='800px';
        setTimeout(function(){nav2.style.visibility = 'visible';},200);
        document.getElementById('event_window').style.display='none';
        document.getElementById('main').style.width='400px';
        document.getElementById('hide').style.display='none';

    } else { nav2.style.visibility = 'hidden';
            nav3.style.visibility = 'hidden';
            }
}

document.getElementById("button3").onclick = function() {

    if (nav3.style.visibility = 'hidden') {
        nav2.style.visibility = 'hidden';
        nav4.style.visibility = 'hidden';
        nav5.style.visibility = 'hidden';
        document.getElementById('mybackground').style.width='800px';
        setTimeout(function(){nav3.style.visibility = 'visible';},200);
        document.getElementById('event_window').style.display='none';
        document.getElementById('main').style.width='400px';
        document.getElementById('hide').style.display='none';

    } else { nav3.style.visibility = 'hidden';
             nav2.style.visibility = 'hidden'; }
}

document.getElementById("button4").onclick = function() {

    if (nav4.style.visibility = 'hidden') {
        nav2.style.visibility = 'hidden';
        nav3.style.visibility = 'hidden';
        nav5.style.visibility = 'hidden';
        document.getElementById('mybackground').style.width='800px';
        setTimeout(function(){nav4.style.visibility = 'visible';},200);

    } else { nav4.style.visibility = 'hidden';
             nav2.style.visibility = 'hidden'; }
}

document.getElementById("button5").onclick = function() {

    if (nav5.style.visibility = 'hidden') {
        nav2.style.visibility = 'hidden';
        nav3.style.visibility = 'hidden';
        nav4.style.visibility = 'hidden';
        document.getElementById('mybackground').style.width='800px';
        setTimeout(function(){nav5.style.visibility = 'visible';},200);
        document.getElementById('event_window').style.display='none';
        document.getElementById('main').style.width='400px';
        document.getElementById('hide').style.display='none';

    } else { nav4.style.visibility = 'hidden';
             nav2.style.visibility = 'hidden';
             nav3.style.visibility = 'hidden';
         }
}

document.getElementById("close2").onclick = function() {

    nav2.style.visibility = 'hidden';
    nav3.style.visibility = 'hidden';
    nav5.style.visibility = 'hidden';
    nav4.style.visibility = 'hidden';
    document.getElementById('mybackground').style.width='400px';

}

document.getElementById("close3").onclick = function() {

    nav3.style.visibility = 'hidden';
    nav4.style.visibility = 'hidden';
    nav2.style.visibility = 'hidden';
    nav5.style.visibility = 'hidden';
    document.getElementById('mybackground').style.width='400px';

}

document.getElementById("close4").onclick = function() {

    nav3.style.visibility = 'hidden';
    nav4.style.visibility = 'hidden';
    nav2.style.visibility = 'hidden';
    nav5.style.visibility = 'hidden';
    document.getElementById('main').style.width='400px';
    document.getElementById('mybackground').style.width='400px';
    document.getElementById('event_window').style.display='none';

}

document.getElementById("close5").onclick = function() {

    nav3.style.visibility = 'hidden';
    nav4.style.visibility = 'hidden';
    nav2.style.visibility = 'hidden';
    nav5.style.visibility = 'hidden';
    document.getElementById('mybackground').style.width='400px';
    document.getElementById('event_window').style.display='none';

}
//💛
