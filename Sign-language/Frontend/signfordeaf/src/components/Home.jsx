import React from 'react'

function Home() {
  return (     
<div>
  <section id="home" className="bg-slate-200 p-2">
  <div className="container mx-auto flex justify-between items-center ">
      
      <div className="w-[50%] pr-8">
        <h1 className="text-[50px] font-[sk] text-[#501A89]">Artificial Intelligence</h1>
        <p className="text-[40px] text-slate-500 mt-4"> Supported Sign Language Translator System </p>
        <div className="mt-6">
          <p className="w-full mb-7 font-semibold text-[20px]">
          Our system empowers individuals with hearing impairments and those who struggle with literacy by enabling them to access information, services, and multimedia content in sign language—their native form of communication. Through advanced AI technology, we bridge the communication gap, providing seamless translation from sign language to text.
          </p>
          <a href="#features" className="bg-blue-500 text-white px-6 py-3 rounded-full text-xl hover:bg-blue-600">
            Learn More
          </a>
        </div>
      </div>
    <div className='flex items-center justify-center mt-20'>
      <img
        src='https://www.signfordeaf.com/static/img/reading-1_r.png'
        className=''
        alt="Main Image"
      />
      <img
        src='https://cdn01.signfordeaf.com/signfordeaf/reading-img-box-line-thick.png'
        className='absolute top-[24%] right-[40%]'
        alt="Box Line"
      />
      <img
        src='https://cdn01.signfordeaf.com/signfordeaf/reading-img-hand-icons.png'
        className='absolute top-[35%] right-[40%]'
        alt="Hand Icons"
      />
      <img
        src='https://cdn01.signfordeaf.com/signfordeaf/reading-img-box-line.png'
        className='absolute top-[46%] right-[40%]'
        alt="Box Line"
      />
      <img
        src='https://cdn01.signfordeaf.com/signfordeaf/reading-img-hands.png'
        className='absolute top-[30%] right-[5%] '
        alt="Hands"
      />
      <img
        src='https://cdn01.signfordeaf.com/signfordeaf/reading-img-box-line.png'
        className='absolute top-[56%] right-[4%]'
        alt="Box Line"
      />
     
    </div>

   

      
  
    </div>
  </section>
</div>
  )
}

export default Home;