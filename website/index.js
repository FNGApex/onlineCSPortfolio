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
