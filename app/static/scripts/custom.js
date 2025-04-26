// Burger Menu
document.addEventListener("DOMContentLoaded", () => {
  const burger = document.querySelector(".navbar-burger");
  const menu = document.getElementById(burger.dataset.target);

  burger.addEventListener("click", () => {
    burger.classList.toggle("is-active");
    menu.classList.toggle("is-active");
  });
});

// Flash Message
document.addEventListener("DOMContentLoaded", function () {
  const flashMessages = document.querySelectorAll(".flash-message");

  flashMessages.forEach((msg) => {
    // After 3 seconds (3000ms), start fading
    setTimeout(() => {
      msg.style.transition = "opacity 0.8s ease-out";
      msg.style.opacity = "0";

      // Then after fade, remove it from the DOM
      setTimeout(() => {
        msg.remove();
      }, 800); // match the transition time
    }, 3000);
  });
});
