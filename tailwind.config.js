/** @type {import('tailwindcss').Config} */
module.exports = {
  darkMode: 'class',
  content:[
    "./templates/index.html",
    "./templates/lecturer.html",
    "./app/templates/lecturer.html",
    "../app/templates/lecturer.html",
    "../app/templates/index.html"
  ],
  safelist: [
    {
      pattern: /./ 
    },    ],
    
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

