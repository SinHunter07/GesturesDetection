/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    "./index.html",
    "./src/**/*.{js,jsx,ts,tsx}", // This tells Tailwind to look at all JavaScript, JSX, TSX, and HTML files in the src folder
  ],
  theme: {
    extend: {},
  },
  plugins: [],
};
