import React from 'react';

export default function HeroIntro({ onSendPrompt }) {
  const suggestions = [
    {
      title: "Who broke the Anklet?",
      desc: "Describe the pivotal scene where the royal jeweler accuses Kovalan falsly.",
      icon: "💍"
    },
    {
      title: "What happened in Madurai?",
      desc: "Explain the absolute rage of Kannagi burning down the Kingdom in justice.",
      icon: "🔥"
    },
    {
      title: "Who is Kovalan?",
      desc: "Detail the merchant's background and his relationship with Madhavi.",
      icon: "📜"
    },
    {
      title: "Summarize the Epic",
      desc: "Provide a quick overview of the 3 books (Chapters) of Silappatikaram.",
      icon: "📖"
    }
  ];

  return (
    <div className="flex-1 flex flex-col items-center justify-center px-4 md:px-6 relative z-10 max-w-4xl mx-auto text-center h-full">
      <div className="space-y-4 mb-12">
        <h1 className="text-4xl md:text-5xl lg:text-6xl font-black font-sans text-white tracking-tight leading-none">
          Vannakkam, <span className="text-gradient bg-gradient-to-r from-temple-red to-[#E58026] bg-clip-text text-transparent">Reader</span>
        </h1>
        <h2 className="text-xl md:text-2xl font-bold font-traditional text-white/90">
          What would you like to know about Silappatikaram today?
        </h2>
        <p className="text-sm text-white/60 max-w-lg mx-auto font-sans font-medium">
          Select one of the quick prompts below to begin exploring the ancient Tamil epic, or type your own question in the input bar.
        </p>
      </div>

      <div className="grid grid-cols-1 md:grid-cols-2 gap-4 w-full max-w-2xl px-4">
        {suggestions.map((item, index) => (
          <div
            key={index}
            onClick={() => onSendPrompt(item.desc)}
            className="p-5 bg-white/5 backdrop-blur-md border border-white/10 rounded-2xl cursor-pointer hover:bg-white/10 hover:border-white/20 transition-all duration-300 transform hover:scale-[1.02] flex flex-col items-start text-left group shadow-lg"
          >
            <div className="text-2xl mb-3 group-hover:scale-110 transition-transform duration-300">
              {item.icon}
            </div>
            <h3 className="text-base font-bold text-white mb-1 group-hover:text-[#E58026] transition-colors">
              {item.title}
            </h3>
            <p className="text-xs text-white/60 font-sans font-medium leading-relaxed">
              {item.desc}
            </p>
          </div>
        ))}
      </div>
    </div>
  );
}
