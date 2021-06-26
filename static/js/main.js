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

function paymentToggle(id) {
  var x = document.getElementById(id);
  if (x.style.display === "none") {
    x.style.display = "block";
  } else {
    x.style.display = "none";
  }
}