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
  pageContent.innerHTML = "Home";
},false);
document.getElementById("aboutmeButton").addEventListener("click",function(e){
  pageContent.innerHTML = "About Me";
},false);
document.getElementById("projectsButton").addEventListener("click",function(e){
  pageContent.innerHTML = "Projects";
},false);
document.getElementById("contactButton").addEventListener("click",function(e){
  pageContent.innerHTML = "Contact"
},false);