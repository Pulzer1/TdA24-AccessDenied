/** @type {import('tailwindcss').Config} */
module.exports = {
  darkMode: 'class',
  content:
  [
    "./templates/**/*.html",
    "./templates/index.html",
    "./templates/lecturer.html"
  ],
  theme: {
  extend: {
    colors: {
      jet: '#333333',
      prussianblue: '#00384D',
      skyblue: '#74C7D3',
      sunglow: '#FECB2E'
      },
    fontFamily:{
      lalezar: ['Lalezar', 'sans-serif'],
      opensans: ['Open Sans', 'sans-serif'],
    }
    },
  },
  plugins: [],
}

