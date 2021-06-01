function showSlidesAutomatic() {
  var i;
  var slides = document.getElementsByClassName("mySlidesAutomatic");
  for (i = 0; i < slides.length; i++) {
    slides[i].style.display = "none";
  }
  slideIndexAutomatic++;
  if (slideIndexAutomatic > slides.length) {slideIndexAutomatic = 1}
  slides[slideIndexAutomatic-1].style.display = "block";
  setTimeout(showSlidesAutomatic, 4000); // Change image every 2 seconds
}