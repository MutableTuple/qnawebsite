clr_1=Math.round(Math.random()*255);
clr_2=Math.round(Math.random()*255);
clr_3=Math.round(Math.random()*255);
// opacity=Math.random();
new_clr='rgb('+clr_1 +','+clr_2 +','+clr_3 +')';
document.getElementById("box").style.borderTop="10px solid "+new_clr;

// document.getElementById("btn").onclick=

// function(){
//     clr_1=Math.round(Math.random()*255);
//     clr_2=Math.round(Math.random()*255);
//     clr_3=Math.round(Math.random()*255);
// // opacity=Math.random();
//     new_clr='rgb('+clr_1 +','+clr_2 +','+clr_3 +')';
//     document.getElementById("box").style.borderTop="10px solid "+new_clr;
//     // document.getElementById("box").style.background=new_clr;


//     document.getElementById("box").style.transition="0.3s";
//     // document.getElementById("box").innerHTML=new_clr;

// }