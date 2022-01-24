let scale = {
  height: window.innerHeight / 1080,
  width: window.innerWidth / 1920,
  update: function () {
    scale.height = window.innerHeight / 1080;
    scale.width = window.innerWidth / 1920;
  }
}
let lastKnownScrollPosition = 0;
let ticking = false;
let mainHeaderHeight = document.getElementById("mainHeader").style.getPropertyValue("height");
function scalebar() {
  scale.update();
  console.log("Hi");
  document.documentElement.style.setProperty("--scale", (130 * scale.width).toString() + "%");
};
scalebar();
window.onresize = scalebar;

let pageContent = document.getElementById("pageContent");

function homeButtonClick(e) {
  console.log(window.scrollY);
}

function personalButtonClick(e) {}

function projectsButtonClick(e) {}

function contactButtonClick(e) {}

document.getElementById("homeButton").addEventListener("click", homeButtonClick, false);
document.getElementById("personalButton").addEventListener("click", personalButtonClick, false);
document.getElementById("projectsButton").addEventListener("click", projectsButtonClick, false);
document.getElementById("contactButton").addEventListener("click", contactButtonClick, false);

function addPermaBar(){
  document.getElementById("mainHeader").style.maxHeight = "0px";
  document.getElementById("mainHeader").style.maxWidth = "0px";
  console.log("Hello");
}
function removePermaBar(){
  document.getElementById("mainHeader").style.maxHeight = "auto";
  document.getElementById("mainHeader").style.maxWidth = "auto";
  console.log("Goodbye");
}
document.addEventListener("scroll", function (e) {
  lastKnownScrollPosition = window.scrollY;

  if (!ticking) {
    if (lastKnownScrollPosition >= mainHeaderHeight) {
      window.requestAnimationFrame(addPermaBar);
      console.log(lastKnownScrollPosition);
      console.log(window.scrollY);
      console.log(document.getElementById("mainHeader").style.height);
    } else {
      window.requestAnimationFrame(removePermaBar);
    }
  }
});