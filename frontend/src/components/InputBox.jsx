import React, { useState } from 'react';

export default function InputBox({ onSend, loading }) {
  const [text, setText] = useState('');

  const handleSubmit = (e) => {
    e.preventDefault();
    if (text.trim() && !loading) {
      onSend(text);
      setText('');
    }
  };

  return (
    <form onSubmit={handleSubmit} className="p-4 bg-white/5 backdrop-blur-xl border border-white/10 rounded-2xl flex items-center space-x-3 shadow-[0_10px_40px_rgba(0,0,0,0.5)] relative z-10 w-full">
      <input

        type="text"
        value={text}
        onChange={(e) => setText(e.target.value)}
        placeholder={loading ? "Adigal is thinking..." : "Ask Adigal about Silappatikaram..."}
        disabled={loading}
        className="flex-1 px-4 py-3 border border-white/10 rounded-xl focus:outline-none focus:ring-1 focus:ring-[#E58026]/50 bg-white/5 backdrop-blur-sm text-[#FDFBF7] text-sm font-sans placeholder-gray-400 disabled:opacity-50 transition-all duration-200"
      />
      
      <button
        type="submit"
        disabled={loading || !text.trim()}
        className="p-3 bg-gradient-to-br from-[#B42331] to-[#E58026] hover:from-[#E58026] hover:to-[#B42331] text-white rounded-xl transition-all duration-300 disabled:opacity-50 shadow-md hover:shadow-[0_0_15px_rgba(229,128,38,0.4)] transform active:scale-95 flex items-center justify-center border border-white/10"
      >
        <svg xmlns="http://www.w3.org/2000/svg" className="h-5 w-5 transform rotate-45" fill="none" viewBox="0 0 24 24" stroke="currentColor">
          <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M12 19l9 2-9-18-9 18 9-2zm0 0v-8" />
        </svg>
      </button>
    </form>
  );
}


