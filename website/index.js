let scale = {
  height: window.innerHeight / 1080,
  width: window.innerWidth / 1920,
  update: function(){
    scale.height = window.innerHeight / 1080;
    scale.width = window.innerWidth / 1920;
  }
}
function scalebar() {
  scale.update();
  console.log("Hi");
  document.documentElement.style.setProperty("--resolutionBasedFontSize", (130 * scale.width).toString() + "%");
};
scalebar();
window.onresize = scalebar
let pageContent = document.getElementById("pageContent");
document.getElementById("homeButton").addEventListener("click",function(e){
  pageContent.innerHTML = "<img src='https://cheaphostings.net/html/tf/nick-berg/nick-berg/assets/img/me.png'>";
  pageContent.innerHTML += "<div><h1> Hello </h1></div>";
  pageContent.style.setProperty("display","flex");
},false);
document.getElementById("personalButton").addEventListener("click",function(e){
  pageContent.innerHTML = "Personal";
},false);
document.getElementById("projectsButton").addEventListener("click",function(e){
  pageContent.innerHTML = "Projects";
},false);
document.getElementById("contactButton").addEventListener("click",function(e){
  pageContent.innerHTML = "<h1> Contact me: </h1>";
  pageContent.innerHTML += "<div id='contactmeform'> Buisness Inqueries:<a href='mailto:dr.stroev@gmail.com?subject=Buisness%20Inqueries'>dr.stroev@gmail.com</a> </div>";
},false);  
