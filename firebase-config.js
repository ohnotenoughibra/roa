// ─── firebase-config.js ───
// ⚠️ Remove ALL import/ESM lines from this file!
//    It must be a plain script, loaded via a <script> tag in your HTML.

// Your Firebase project config ↓
const firebaseConfig = {
    apiKey: "AIzaSyAWbXYLgzy3716BnvED5PCDhSEmumMl9gI",
    authDomain: "roa2-88fd2.firebaseapp.com",
    projectId: "roa2-88fd2",
    storageBucket: "roa2-88fd2.appspot.com",      // note the “.appspot.com” here
    messagingSenderId: "1066048221414",
    appId: "1:1066048221414:web:3224e45ed85b040ceecb27",
    measurementId: "G-XX3TQMV74E"
  };
  
  // Initialize Firebase (v8 compat)
  firebase.initializeApp(firebaseConfig);
  