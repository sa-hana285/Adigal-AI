import React from 'react';

export default function Header() {
  return (
    <header className="w-full bg-white/40 backdrop-blur-md border-b border-heritage-gold/15 py-5 px-6 flex flex-col items-center justify-center relative z-10 shadow-sm">
      {/* Decorative Ornate Arch/Divider Border Top - Vibrant Glow */}
      <div className="absolute top-0 left-0 right-0 h-[3px] bg-gradient-to-r from-temple-red via-heritage-gold to-temple-red shadow-sm" />

      <div className="flex items-center space-x-3">
        {/* Ornate Frame Dot Glowing */}
        <div className="w-2.5 h-2.5 rounded-full bg-temple-red shadow-sm animate-pulse" />
        
        <h1 className="text-4xl font-extrabold tracking-widest text-temple-red font-traditional select-none">
          Adigal.ai
        </h1>
        
        <div className="w-2.5 h-2.5 rounded-full bg-temple-red shadow-sm animate-pulse" />
      </div>

      
      <p className="text-[10px] uppercase tracking-[0.25em] text-heritage-gold mt-1.5 font-sans font-black text-center drop-shadow-sm">
        Understanding Tamil Classics through AI
      </p>
      
      {/* Elegantly Drawn Decorative Divider Line */}
      <div className="w-40 h-[1.5px] bg-gradient-to-r from-transparent via-heritage-gold directly to-transparent mt-3 opacity-60" />
    </header>
  );
}


