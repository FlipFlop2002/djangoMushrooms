let slideIndex = 0;
showSlide(slideIndex);

function nextSlide() {
  showSlide((slideIndex += 1));
}

function prevSlide() {
  showSlide((slideIndex -= 1));
}

function showSlide(index) {
  const slides = document
    .getElementsByClassName("slides")[0]
    .getElementsByTagName("img");

  if (index >= slides.length) {
    slideIndex = 0;
  }

  if (index < 0) {
    slideIndex = slides.length - 1;
  }

  for (let i = 0; i < slides.length; i++) {
    slides[i].style.display = "none";
  }

  slides[slideIndex].style.display = "flex";
  // slides[slideIndex].style.objectFit = "cover";
  // slides[slideIndex].style.objectFit = "cover";
  // slides[slideIndex].style.width = "100%";
  // slides[slideIndex].style.height = "100%";
}
