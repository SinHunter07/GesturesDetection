
import React from 'react'

function Features() {
  return (
    <div>

      <section id="features" className="py-20 bg-blue-50">
        <div className="container mx-auto text-center">
          <h2 className="text-[#501A89] text-[40px] font-bold font-[sk]">Features</h2>
          <div className="mt-10 grid grid-cols-1 md:grid-cols-3 gap-10">
            <div className="feature p-6 bg-white rounded-lg shadow-md transition-all duration-500 ease-in-out hover:bg-[#501A89] hover:text-white">
              <h3 className="text-2xl font-semibold">Real-time Recognition</h3>
              <p className="mt-4 ">Instantly convert your sign language gestures to readable text.</p>
            </div>
            <div className="feature p-6 bg-white rounded-lg shadow-md transition-all duration-500 ease-in-out hover:bg-[#501A89] hover:text-white">
              <h3 className="text-2xl font-semibold">User-Friendly Interface</h3>
              <p className="mt-4">Easy to navigate with clear instructions for beginners and advanced users alike.</p>
            </div>
            <div className="feature p-6 bg-white rounded-lg shadow-md transition-all duration-500 ease-in-out hover:bg-[#501A89] hover:text-white">
              <h3 className="text-2xl font-semibold">Diverse Dataset Integration</h3>
              <p className="mt-4">Trained on an extensive dataset featuring signers from various regions and age groups, the system ensures inclusivity and robustness.</p>
            </div>
          </div>
        </div>
      </section>
    </div>
  )
}

export default Features;
