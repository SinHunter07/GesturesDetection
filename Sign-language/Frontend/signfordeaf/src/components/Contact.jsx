import React from 'react';

function Contact() {
  return (
    <div>
      <section id="contact" className="py-20 bg-slate-300 text-center">
        <p className="text-[40px] font-bold font-[sk] text-[#501A89]">Contact Us</p>
        <p className="text-[20px] font-[sk1] text-black">Any question or remarks? Just write us a message!</p>

        <div className="flex justify-center items-center space-x-12">
          <img
            src="https://www.signfordeaf.com/static/img/solution-2.png"
            className="m-20"
          />

<form className=" p-8 rounded-md w-full max-w-2xl">
        <div className="grid grid-cols-1 md:grid-cols-2 gap-6">
          <div>
            <label className="block text-sm font-medium text-gray-700">
              First Name
            </label>
            <input
              type="text"
              placeholder="First Name"
              className="mt-1 block w-full border border-gray-300 rounded-md p-2"required
            />
          </div>
          <div>
            <label className="block text-sm font-medium text-gray-700">
              Last Name
            </label>
            <input
              type="text"
              placeholder="Last Name"
              className="mt-1 block w-full border border-gray-300 rounded-md p-2"required
            />
          </div>

          <div>
            <label className="block text-sm font-medium text-gray-700">
              Email
            </label>
            <input
              type="email"
              placeholder="Email"
              className="mt-1 block w-full border border-gray-300 rounded-md p-2"required
            />
          </div>
          <div>
            <label className="block text-sm font-medium text-gray-700">
              Phone
            </label>
            <input
              type="text"
              placeholder="Phone"
              className="mt-1 block w-full border border-gray-300 rounded-md p-2"required
            />
          </div>
        </div>

        <div className="mt-6">
          <label className="block text-sm font-medium text-gray-700">
            Message
          </label>
          <textarea
            placeholder="Write your message..."required
            rows={4}
            className="mt-1 block w-full border border-gray-300 rounded-md p-2"
          ></textarea>
        </div>

        <div className="flex flex-col md:flex-row justify-between items-center mt-6">
          
          <div className="mb-4 md:mb-0">
            <div className="border p-4 rounded-md border-gray-300">
              <input type="checkbox" className="mr-2" />
              <span className="text-sm text-gray-600">I'm not a robot</span>
            </div>
          </div>

        
          <button
            type="submit"
            className="bg-black text-white px-6 py-2 rounded-md shadow-md hover:bg-gray-800"
          >
            Send Message
          </button>
        </div>
      </form>
        </div>
      </section>
    </div>
  );
}

export default Contact;
