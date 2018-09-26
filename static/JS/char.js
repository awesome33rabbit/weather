document.getElementById("robot").focus();
var xmlHttp
function showHint(str)
{
    if (event.keyCode == 13)
    {
        addmsg(str);
    }
}

function Send(str)
{
    if (str.length == 0)
    {
        // document.getElementById("txtHint").innerHTML = "";
        return;
    }
    xmlHttp = GetXmlHttpObject()

    if (xmlHttp == null)
    {
        alert("您的浏览器不支持AJAX！");
        return;
    }

    var url = "http://www.tuling123.com/openapi/api?key=93b3134e1e894083b9505376461e0400";
    url = url + "&info=" + str;
    url = url + "&userid=awesome_rabbit";
    xmlHttp.onreadystatechange = stateChanged;
    xmlHttp.open("GET", url, true);
    xmlHttp.send(null);
    document.getElementById("robot").value = "";
}

function stateChanged()
{
    if (xmlHttp.readyState == 4)
    {
        var msg = eval('(' + xmlHttp.responseText + ')');
        console.log(msg.text);
        var tbody = document.getElementsByTagName('tbody')[7];
        console.log(tbody)
        var tr = document.createElement('tr');
        var td1 = document.createElement('td');
        var myMsg = document.createElement('td');
        var td3 = document.createElement('td');
        myMsg.setAttribute('class', 'return_msg')
        td1.setAttribute('class', 'png')
        myMsg.innerHTML = msg.text;
        td1.innerHTML = '<img src="static/2.png" alt="" width="25px" class="png">'
        tr.appendChild(td1);
        tr.appendChild(myMsg);
        tr.appendChild(td3);
        tbody.appendChild(tr)
        var div = document.getElementById("room_size");
        div.scrollTop=div.scrollHeight;
    }
}

function GetXmlHttpObject()
{
    var xmlHttp = null;
    try
    {
        // Firefox, Opera 8.0+, Safari
        xmlHttp = new XMLHttpRequest();
    } catch (e)
    {
        // Internet Explorer
        try
        {
            xmlHttp = new ActiveXObject("Msxml2.XMLHTTP");
        } catch (e)
        {
            xmlHttp = new ActiveXObject("Microsoft.XMLHTTP");
        }
    }
    return xmlHttp;
}

function addmsg() {
    document.getElementById("robot").focus();
    var sendmsg = document.getElementById('robot').value;
    Send(sendmsg);
    var tbody = document.getElementsByTagName('tbody')[7];
    var tr = document.createElement('tr');
    var td1 = document.createElement('td');
    var myMsg = document.createElement('td');
    var td3 = document.createElement('td');
    myMsg.setAttribute('class', 'send_msg')
    td3.setAttribute('class', 'png')
    myMsg.innerHTML = sendmsg;
    td3.innerHTML = '<img src="static/2.png" alt="" width="25px" class="png">'
    tr.appendChild(td1);
    tr.appendChild(myMsg);
    tr.appendChild(td3);
    tbody.appendChild(tr)
    var div = document.getElementById("room_size");
    div.scrollTop=div.scrollHeight;
}