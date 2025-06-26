
// static/firebase.js

// Import required Firebase modules
import { initializeApp } from "https://www.gstatic.com/firebasejs/9.22.2/firebase-app.js";
import { getAuth } from "https://www.gstatic.com/firebasejs/9.22.2/firebase-auth.js";
import { getAnalytics } from "https://www.gstatic.com/firebasejs/9.22.2/firebase-analytics.js";

// Your Firebase configuration
const firebaseConfig = {
  apiKey: "AIzaSyD9HNA23tUhsvOd731tq5IwMklXStO_RUk",
  authDomain: "cfg1-7af89.firebaseapp.com",
  projectId: "cfg1-7af89",
  storageBucket: "cfg1-7af89.appspot.com",
  messagingSenderId: "212406362897",
  appId: "1:212406362897:web:b4a2242f13503282d462b0",
  measurementId: "G-QGM3N2MX1G"
};

// Initialize Firebase app and services
const app = initializeApp(firebaseConfig);
const analytics = getAnalytics(app);
const auth = getAuth(app);

// Export auth so app.js can use it
export { auth };
