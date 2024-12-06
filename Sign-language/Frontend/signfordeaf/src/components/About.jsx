

import React from 'react'

function About() {
  return (
    <div>
      <section id="about" className="py-20 bg-white">
        <div className="container mx-auto text-center">
          <h2 className="text-[40px] font-bold font-[sk] text-[#501A89] mb-5">About the Project</h2>

          <div className="flex">
            <img
              src="https://www.signfordeaf.com/static/img/solution-4_r.png"
              className=""
            />
            <p className=" text-[#501A89] text-[20px] px-4 font-normal mt-10">
            This project aims to create a system that recognizes and translates Non-Manual Features (NMFs) in Indian Sign Language (ISL), such as facial expressions, head movements, and body posture. By leveraging advanced machine learning models, it provides real-time text translations for ISL videos, bridging communication gaps for the deaf and hard-of-hearing community. The system focuses on accuracy, inclusivity, and user-friendly functionality, ensuring accessibility in both online and offline environments. It is designed to be adaptable for diverse users and continuously improves through user feedback and iterative refinement.
            </p>
          </div>
        </div>
      </section>
    </div>
  )
}

export default About
