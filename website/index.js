let scale = {
  height: window.innerHeight / 1080,
  width: window.innerWidth / 1920,
  update: function () {
    scale.height = window.innerHeight / 1080;
    scale.width = window.innerWidth / 1920;
  }
}

function scalebar() {
  scale.update();
  console.log("Hi");
  document.documentElement.style.setProperty("--scale", (130 * scale.width).toString() + "%");
};
scalebar();
window.onresize = scalebar
let pageContent = document.getElementById("pageContent");
let homeButtonClick = function (e) {
  pageContent.style.setProperty("display", "flex");
}
let personalButtonClick = function (e) {
}
let projectsButtonClick = function (e) {
}
let contactButtonClick = function (e) {
}
document.getElementById("homeButton").addEventListener("click", homeButtonClick, false);
document.getElementById("personalButton").addEventListener("click", personalButtonClick, false);
document.getElementById("projectsButton").addEventListener("click", projectsButtonClick, false);
document.getElementById("contactButton").addEventListener("click", contactButtonClick, false);