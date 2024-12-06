import React from 'react'

function Nav() {
  return (
    <div>
        <header className="py-5 fixed top-0 w-screen bg-white">
        <div className="container mx-auto flex items-center justify-between">
          <img src='https://cdn01.signfordeaf.com/signfordeaf/logo_en.png' className='w-[175px] h-[42px]'></img>
          <nav>
            <ul className="flex space-x-10 font-[sk1] text-[#501A89] font-bold">
              <li><a href="#home" className=" hover:text-blue-400">Home</a></li>
              <li><a href="#about" className=" hover:text-blue-400">About</a></li>
              <li><a href="#features" className=" hover:text-blue-400">Features</a></li>
              <li><a href="#request" className="hover:text-blue-400">Request a demo</a></li>
              <li><a href="#contact" className="hover:text-blue-400">Contact Us</a></li>
              
            </ul>
          </nav>
        </div>
      </header>
    </div>
  )
}

export default Nav