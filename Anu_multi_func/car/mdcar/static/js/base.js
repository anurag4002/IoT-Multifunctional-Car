function toggleDarkMode() {
    var body = document.body;
    var icon = document.getElementById("mode");
  
    body.classList.toggle("dark-mode");
  
    if (body.classList.contains("dark-mode")) {
      icon.classList.remove("fa-moon");
      icon.classList.add("fa-sun");
    } else {
      icon.classList.remove("fa-sun");
      icon.classList.add("fa-moon");
    }
  }
  