/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    "./src/**/*.{js,ts,jsx,tsx}", // JS/TS/React files
    "./src/styles/**/*.css"        // CSS files
  ],  
  theme: {
    extend: {
      colors: {
        'accent-primary': '#00a5bb',
        'white': '#fff',
        'black': '#000',
      }
    },
  },
  plugins: [],
}