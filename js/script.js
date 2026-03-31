// Persistence using localStorage
const STORAGE_KEY = "portal_users";

function getUsers() {
    const users = localStorage.getItem(STORAGE_KEY);
    return users ? JSON.parse(users) : [];
}

function saveUser(user) {
    const users = getUsers();
    users.push(user);
    localStorage.setItem(STORAGE_KEY, JSON.stringify(users));
}

function showMessage(msg, isError = true) {
    const message = document.getElementById("message");
    if (!message) return;
    
    message.innerHTML = msg;
    message.className = isError ? "error" : "success";
    message.style.display = "block";
    
    message.style.opacity = "0";
    setTimeout(() => {
        message.style.transition = "opacity 0.4s ease";
        message.style.opacity = "1";
    }, 10);
}

function validateRegistration() {
    const name = document.getElementById("name").value.trim();
    const regno = document.getElementById("regno").value.trim();
    const email = document.getElementById("email").value.trim();
    const password = document.getElementById("password").value;
    const department = document.getElementById("department").value;
    const gender = document.getElementById("gender").value;

    const regnoPattern = /^\d{2}[A-Z]{3}\d{4}$/;
    const namePattern = /^[A-Za-z ]+$/;
    const passwordPattern = /^(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&]).{6,}$/;
    const emailPattern = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;

    if (!name || !regno || !email || !password || !department || !gender) {
        showMessage("All fields are mandatory!");
        return false;
    }

    if (!namePattern.test(name)) {
        showMessage("Name must contain only alphabets and spaces!");
        return false;
    }

    if (!regnoPattern.test(regno)) {
        showMessage("Register Number must be in format: 23MIS0146");
        return false;
    }

    if (!emailPattern.test(email)) {
        showMessage("Please enter a valid email address!");
        return false;
    }

    if (!passwordPattern.test(password)) {
        showMessage("Password must be at least 6 characters and include: 1 Uppercase, 1 Number, and 1 Special Character (@$!%*?&)");
        return false;
    }

    // Check if user already exists
    const users = getUsers();
    if (users.find(u => u.email === email)) {
        showMessage("Email already registered!");
        return false;
    }

    // Save user
    const newUser = { name, regno, email, password, department, gender };
    saveUser(newUser);

    showMessage("Student Registered Successfully! You can now login.", false);
    
    // Smooth transition to login
    setTimeout(() => {
        window.location.href = 'login.html';
    }, 2000);
    
    return false; 
}

function validateLogin() {
    const email = document.getElementById("email").value.trim();
    const password = document.getElementById("password").value;

    if (!email || !password) {
        showMessage("Please enter both email and password!");
        return false;
    }

    // Check localStorage
    const users = getUsers();
    const user = users.find(u => u.email === email && u.password === password);

    if (user) {
        showMessage(`Welcome back, ${user.name}! Login Successful.`, false);
        
        // Save current session
        localStorage.setItem('current_user', JSON.stringify(user));
        
        // Smoothly redirect
        setTimeout(() => {
            window.location.href = 'dashboard.html';
        }, 1500);
    } else {
        showMessage("Invalid credentials! Please register if you haven't.");
    }

    return false;
}
