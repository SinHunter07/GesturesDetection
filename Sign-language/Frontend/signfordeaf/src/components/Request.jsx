import React from 'react'
import { FaArrowRight } from "react-icons/fa6";

function Request() {
  return (
    <div>
        <section id='request' className=" bg-white ">
    <div class="container mx-auto text-center">
      <h2 class="text-[40px] font-bold font-[sk] text-[#501A89]">Request a Demo</h2>
      <div className='flex mt-7'>

     
      <img src='https://www.signfordeaf.com/static/img/solution-5-5_r.png' className=''></img>
      <div className='flex-col'>
      <p className=' text-[#501A89] font-[sk] text-[30px] m-20'>
      Web Sign Language Plugin
      </p>
      <div className=' text-[#501A89] text-[17px] font-semibold flex m-20 gap-5'>
        <a href='http://localhost:8501/'>Request demo</a>
        <div className='text-[25px] cursor-pointer'> <FaArrowRight /></div>
      </div>
      </div>
      </div>
       
    </div>
    </section>
    </div>
  )
}

export default Request