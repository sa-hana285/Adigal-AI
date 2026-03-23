import React from 'react';

export default function MessageBubble({ message }) {
  const isUser = message.sender === 'user';

  return (
    <div className={`flex ${isUser ? 'justify-end' : 'justify-start'} mb-6 animate-fadeIn px-2`}>
      <div
        className={`max-w-[85%] md:max-w-[75%] px-6 py-4 rounded-2xl shadow-md transition-all duration-300 hover:scale-[1.01] ${
          isUser
            ? 'bg-gradient-to-r from-[#B42331] to-[#E58026] text-white rounded-br-none font-sans font-medium shadow-[0_4px_12px_rgba(180,35,49,0.25)]'
            : 'bg-white border border-heritage-gold/20 text-[#2F060A] rounded-bl-none font-traditional shadow-sm'
        }`}
      >
        {!isUser && (
          <div className="flex items-center space-x-2 mb-2 border-b border-heritage-gold/10 pb-1.5">
            <span className="text-xs font-bold font-sans text-heritage-gold uppercase tracking-widest">
              Adigal
            </span>
            <div className="w-1.5 h-1.5 rounded-full bg-temple-red animate-pulse" />
          </div>
        )}
        
        <p className={`leading-relaxed text-base md:text-lg font-bold ${!isUser ? 'text-[#2F060A]' : 'text-white'}`}>
          {message.text}
        </p>





        
        <div className={`text-[9px] mt-1.5 flex ${isUser ? 'justify-end text-white/60' : 'justify-start text-gray-400 font-sans'}`}>
          {message.time}
        </div>
      </div>
    </div>
  );
}

