var e = document.getElementById("class");
var clsSelected = e.options[e.selectedIndex].text;

var f = document.getElementById("subject");
var subjSelected = f.options[f.selectedIndex].text;

function checkStudent(no) {
  var text;
  var ok;
  ok=true;
  
  if (isNaN(no) || no < 1) {
    text = "Class number is invalid";
	ok = false;
  } else if (no > 32) {
	text = "Class number does not exist";
	ok = false;
  } else {
	text  = "Class number is OK";
	document.getElementById("clsnocheck").style.color="green";
  }
  document.getElementById("clsnocheck").innerHTML = text;
  if (ok != false) {
    $("#subject").show();
    $("#cw").show();
    $("#jt").show();
    $("#exm").show();
    $("#submit").show();
  }
}

function checkScore(cw,jt,exm) {
  var x, y, z, text;
  var ok = true;
  
  if (isNaN(cw) || cw < 0 || cw > 101) {
    x = "Score is invalid";
	ok = false;
  } else {
	x = "Score is OK";
	document.getElementById("cwcheck").style.color="green";
  }
  document.getElementById("cwcheck").innerHTML = x;
  
  if (isNaN(jt) || jt < 0 || jt > 101) {
    y = "Score is invalid";
	ok = false;
  } else {
	y = "Score is OK";
	document.getElementById("jtcheck").style.color="green";
  }
  document.getElementById("jtcheck").innerHTML = y;
  
   
  if (isNaN(exm) || exm < 0 || exm > 101) {
    z = "Score is invalid";
	ok = false;
  } else {
	z = "Score is OK";
	document.getElementById("exmcheck").style.color="green";
  }
  document.getElementById("exmcheck").innerHTML = z;
  if (ok != false) {
    $("#submit").hide();
	$("#nextpage").show();
  }
}