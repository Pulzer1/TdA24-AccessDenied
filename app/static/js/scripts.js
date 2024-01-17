

document.addEventListener('DOMContentLoaded', (event) => {
    const savedTheme = localStorage.getItem('theme');
    const LocIcon = document.getElementById("location_icon");
    if (savedTheme === 'dark') {
        document.documentElement.classList.add('dark');
        document.getElementById('darkmode-toggle').checked = true;
        LocIcon.src = LocIcon.getAttribute("src-dark");
    } else {
        LocIcon.src = LocIcon.getAttribute("src-light");
    }
});

document.getElementById("darkmode-toggle").addEventListener('change', function() {
    const LogoImage = document.getElementById("logo-image");
    const LocIcon = document.getElementById("location_icon");
    if (this.checked) {
        document.documentElement.classList.add('dark');
        localStorage.setItem('theme', 'dark');
        LocIcon.src = LocIcon.getAttribute("src-dark");
    } else {
        document.documentElement.classList.remove('dark');
        localStorage.setItem('theme', 'light');
        LocIcon.src = LocIcon.getAttribute("src-light");
    }
});
