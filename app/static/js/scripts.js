

document.addEventListener('DOMContentLoaded', (event) => {
    const savedTheme = localStorage.getItem('theme');
    if (savedTheme === 'dark') {
        document.documentElement.classList.add('dark');
        document.getElementById('darkmode-toggle').checked = true;
    }
});

document.getElementById("darkmode-toggle").addEventListener('change', function() {
    const LogoImage = document.getElementById("logo-image")
    if (this.checked) {
        document.documentElement.classList.add('dark');
        localStorage.setItem('theme', 'dark');
    } else {
        document.documentElement.classList.remove('dark');
        localStorage.setItem('theme', 'light');
    }
});
