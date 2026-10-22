const container = document.getElementById('container');
const registerBtn = document.getElementById('register');
const loginBtn = document.getElementById('login');

registerBtn.addEventListener('click', () => {
    container.classList.add("active");
});

loginBtn.addEventListener('click', () => {
    container.classList.remove("active");
});

// --- TAMBAHAN BARU ---
// Cari tombol Sign In di dalam form Login
// (Di HTML kamu, tombol Sign In ada di form kedua)
const signInFormButton = document.querySelector('.sign-in form button');

signInFormButton.addEventListener('click', (e) => {
    e.preventDefault(); // Mencegah form submit biasa
    // Redirect ke halaman dashboard
    window.location.href = "/dashboard";
});