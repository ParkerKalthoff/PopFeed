// Import the functions you need from the SDKs you need
import { initializeApp } from "firebase/app";
import { getAnalytics } from "firebase/analytics";
// TODO: Add SDKs for Firebase products that you want to use
// https://firebase.google.com/docs/web/setup#available-libraries

// Your web app's Firebase configuration
// For Firebase JS SDK v7.20.0 and later, measurementId is optional
const firebaseConfig = {
  apiKey: "AIzaSyCJZEM4XbTfckqHTyUlAhKV-CBR3ETDeq8",
  authDomain: "popfeed-d5afc.firebaseapp.com",
  projectId: "popfeed-d5afc",
  storageBucket: "popfeed-d5afc.appspot.com",
  messagingSenderId: "221837075040",
  appId: "1:221837075040:web:df4db09d1500be141a9905",
  measurementId: "G-VLLZ1YNXG4"
};

// Initialize Firebase
const app = initializeApp(firebaseConfig);
const analytics = getAnalytics(app);

