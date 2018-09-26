// 根据id查找元素赋值给变量,用于操作html元素
var last_month = document.getElementById("last_month");
var next_month = document.getElementById("next_month");
var nowyear = document.getElementById("calendar_year");
var nowmonth = document.getElementById("calendar_month");
var week_days = document.getElementById('week_days');
var back_to_today = document.getElementById('back_to_today');
var day_num = document.getElementById('day_num');
var lunar_year = document.getElementById('lunar_year');
var lunar_date = document.getElementById('lunar_date');
var term_info = document.getElementById('term_info');

var month_name = ["1月","2月","3月","4月","5月","6月","7月","8月","9月","10月","11月","12月"];
var leap_year_month = [31,29,31,30,31,30,31,31,30,31,30,31];
var normal_year_month = [31,28,31,30,31,30,31,31,30,31,30,31];

var now_date = new Date();
var now_year = now_date.getFullYear();  // 几年
var now_month = now_date.getMonth();  // 几月
var now_day = now_date.getDate();  // 几号

// 某个月有多少天
function month_days(year,month){
	// 是否闰年
    var tmp1 = year % 4;
    var tmp2 = year % 100;
    var tmp3 = year % 400;
    if((tmp1 == 0 && tmp2 != 0) || (tmp3 == 0)){
        return (leap_year_month[month]);
    }else{
        return (normal_year_month[month]);
    }
}

// 某个月第一天是周几
function month_start_day(year,month){
	var start_day = new Date(year, month, 1);
	return (start_day.getDay());  // 周几
}

// 刷新并打印日历
function refreshdate(){	
	var monthdays = new Array(); //某月日列表
	var days = month_days(now_year, now_month);
	var first_day = month_start_day(now_year, now_month);
	// 某月日列表开头补空
	for(i=0;i<first_day;i++){
		monthdays.push('&nbsp&nbsp&nbsp');
	}
	// 某月日列表
	for(i=1;i<=days;i++){
		monthdays.push(i);
	}
	// 某月日列表末尾补空
	var len = monthdays.length;
	for(i=len;i<42;i++)
		monthdays.push('');
	
	// 农历信息
	// console.log(calendar.solar2lunar(now_year,now_month+1,now_day));
	// 对应年月日的农历信息
	var lunar = calendar.solar2lunar(now_year,now_month+1,now_day);
	var animal = lunar.Animal; // 生肖
	var gz_year = lunar.gzYear; // 干支年
	var gz_month = lunar.gzMonth; // 干支月
	var gz_day = lunar.gzDay; // 干支日
	var lunar_month = lunar.IMonthCn; // 农历月
	var lunar_day = lunar.IDayCn; // 农历日
	var term = lunar.Term; // 节气

	var i=0; // 计数
	var week_str = ""; // 周 行字符串
	var days_str = ""; // 日 单元格字符串

	//生成日历字符串
	for(r=0;r<=6;r++){
		days_str = "";
		for(now_month;(i+r)%8!=0;i++){
			if (monthdays[i] == new Date().getDate() && now_year == new Date().getFullYear() && now_month == new Date().getMonth()){
				days_str += "<td><button type='button' onclick='click_day("+now_year+","+now_month+","+monthdays[i]+")' id='todaybtn'>"+monthdays[i]+"</button></td>";
			}
			else{
				days_str += "<td><button type='button' onclick='click_day("+now_year+","+now_month+","+monthdays[i]+")' id='daybtn'>"+monthdays[i]+"</button></td>";}
		}
		week_str += "<tr>"+days_str+"</tr>";
	}

	// 把字符串写入html
	day_num.innerHTML = now_day;
	lunar_year.innerHTML = gz_year + "年 [" + animal + "年]";
	lunar_date.innerHTML = lunar_month + lunar_day;
	term_info.innerHTML = term;
	week_days.innerHTML = week_str;
	nowyear.innerHTML = now_year + '年';
	nowmonth.innerHTML = month_name[now_month];
}

refreshdate();

// 根据月份设置背景图片
var image_list =['static/pic/calendar/spring.jpg','static/pic/calendar/summer.jpg','static/pic/calendar/autumn.jpg','static/pic/calendar/winter.jpg']
function season_picture(month){
	if (month == 2 || month == 3 || month == 4){
		document.getElementById('main').style.backgroundImage="url("+image_list[0]+")";
	}
	else if (month == 5 || month == 6 || month == 7) {
		document.getElementById('main').style.backgroundImage="url("+image_list[1]+")";
	}
	else if (month == 8 || month == 9 || month == 10) {
		document.getElementById('main').style.backgroundImage="url("+image_list[2]+")";
	}
	else if (month == 11 || month == 0 || month == 1) {
		document.getElementById('main').style.backgroundImage="url("+image_list[3]+")";
	}
}

season_picture(now_month);

// 点击日期更改日期信息
function click_day(year,month,day){
	if (day==null) {
		day= new Date().getDate();
	}
	lunar = calendar.solar2lunar(year,month+1,day);
    animal = lunar.Animal; // 生肖
	gz_year = lunar.gzYear; //
	lunar_month = lunar.IMonthCn; // 农历月
	lunar_day = lunar.IDayCn; // 农历日
	term = lunar.Term; // 节气

	lunar_year.innerHTML = gz_year + "年 [" + animal + "年]";
	lunar_date.innerHTML = lunar_month + lunar_day;
	term_info.innerHTML = term;
    day_num.innerHTML = day;
    // 弹出添加事件窗口
    document.getElementById('main').style.width='800px';
    document.getElementById('mybackground').style.width='1200px';
	document.getElementById('hide').style.display='block';
	// document.getElementById('event_window').style.display='block';
	function startTimeout(){
		var timer = setTimeout(function(){document.getElementById('event_window').style.display='block';},300);
	}
	startTimeout()
}

// 回到今日日历
back_to_today.onclick = function(e){
    e.preventDefault();
    now_month = now_date.getMonth();
    now_year = now_date.getFullYear();
    refreshdate();
    season_picture(now_month);
}

// 上个月
last_month.onclick = function(e){
    now_month--;
    if(now_month < 0){
        now_year--;
        now_month = 11;
    }
    season_picture(now_month);
    refreshdate();
}

// 下个月
next_month.onclick = function(e){
    now_month++;
    if(now_month > 11){
        now_month = 0;
        now_year++;
    }
    season_picture(now_month);
    refreshdate();
}

// 隐藏添加事件窗口
function hide_event(){
	document.getElementById('main').style.width='400px';
	document.getElementById('mybackground').style.width='800px';
	document.getElementById('hide').style.display='none';
	document.getElementById('event_window').style.display='none';
    season_picture(now_month);
}

// 移除备忘信息
function remove_event(sef){
 	var events_list = document.getElementById('events_list');
	var parent_id = sef.parentElement; //当前父元素的id
	events_list.removeChild(parent_id);
}

var event_count=1;
function newevent(msg){
	event_count++;
	var eventdiv = document.createElement('div');
	eventdiv.id=('event_count_'+event_count);
	eventdiv.innerHTML = "<p class='note'>信息:<br>"+msg+"</p><button class='dele' onclick='remove_event(this)'>删除</button>"
	return eventdiv;
}
function add_event(){
	// 获取textarea内容
	var msg = document.getElementById('input_txt').value;
	if (msg == '') {
		console.log('')
	} else {
	// 空格换行符转换为解释器可读的
	var msg = msg.replace(/\r\n/g,'<br/>').replace(/\n/g, '<br/>').replace(/\s/g, ' ');
	// 获取events_list元素进行操作
	var events_list = document.getElementById('events_list');
	var event_div = newevent(msg);
	events_list.appendChild(event_div);
	events_list.scrollTop = events_list.scrollHeight;
	}
}

