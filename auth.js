// Sign Up
function signUp() {
    const email = document.getElementById("signupEmail").value;
    const password = document.getElementById("signupPassword").value;
  
    firebase.auth().createUserWithEmailAndPassword(email, password)
      .then(() => {
        alert("Account created!");
        window.location.href = "dashboard.html";
      })
      .catch(error => alert(error.message));
  }
  
  // Login
  function logIn() {
    const email = document.getElementById("loginEmail").value;
    const password = document.getElementById("loginPassword").value;
  
    firebase.auth().signInWithEmailAndPassword(email, password)
      .then(() => {
        alert("Logged in!");
        window.location.href = "dashboard.html";
      })
      .catch(error => alert(error.message));
  }
  
  // Optional: Logout
  function logOut() {
    firebase.auth().signOut().then(() => {
      window.location.href = "login.html";
    });
  }
  