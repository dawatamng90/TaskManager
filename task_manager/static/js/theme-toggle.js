// // theme-toggle.js
// document.addEventListener("DOMContentLoaded", () => {
//   const themeToggle = document.getElementById("theme-toggle");
//   const darkTheme = document.getElementById("dark-theme");
//   const icon = themeToggle.querySelector("i");

//   themeToggle.addEventListener("click", () => {
//     darkTheme.disabled = !darkTheme.disabled;
//     if (darkTheme.disabled) {
//       icon.classList.remove("fa-moon");
//       icon.classList.add("fa-sun");
//     } else {
//       icon.classList.remove("fa-sun");
//       icon.classList.add("fa-moon");
//     }
//   });
// });

document.addEventListener("DOMContentLoaded", () => {
  const themeToggle = document.getElementById("theme-toggle");
  const darkTheme = document.getElementById("dark-theme");
  const icon = themeToggle.querySelector("i");

  // Check if a theme is saved in localStorage and apply it
  const savedTheme = localStorage.getItem("theme");
  if (savedTheme === "dark") {
    darkTheme.disabled = false; // Enable dark theme
    icon.classList.remove("fa-sun");
    icon.classList.add("fa-moon");
  } else {
    darkTheme.disabled = true; // Enable light theme
    icon.classList.remove("fa-moon");
    icon.classList.add("fa-sun");
  }

  // Toggle the theme when the button is clicked
  themeToggle.addEventListener("click", () => {
    darkTheme.disabled = !darkTheme.disabled;
    if (darkTheme.disabled) {
      icon.classList.remove("fa-moon");
      icon.classList.add("fa-sun");
      localStorage.setItem("theme", "light"); // Save light theme in localStorage
    } else {
      icon.classList.remove("fa-sun");
      icon.classList.add("fa-moon");
      localStorage.setItem("theme", "dark"); // Save dark theme in localStorage
    }
  });
});
