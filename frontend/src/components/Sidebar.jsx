import React from 'react';

export default function Sidebar() {
  return (
    <aside className="w-16 md:w-20 h-full fixed left-0 top-0 bg-[#0D0104]/80 backdrop-blur-2xl border-r border-white/10 flex flex-col items-center py-6 z-30 justify-between">
      {/* Top Section: Logo / App Trigger */}
      <div className="flex flex-col items-center space-y-6">
        <div className="w-10 h-10 rounded-xl bg-gradient-to-br from-temple-red to-[#E58026] flex items-center justify-center shadow-md hover:shadow-lg transition-all duration-300 cursor-pointer">
          <span className="text-white font-black text-xs">A</span>
        </div>
        
        <button className="w-10 h-10 rounded-full border border-white/10 flex items-center justify-center text-white/70 hover:bg-white/10 hover:text-white transition-all duration-200">
          <svg xmlns="http://www.w3.org/2000/svg" className="h-5 w-5" fill="none" viewBox="0 0 24 24" stroke="currentColor">
            <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M12 4v16m8-8H4" />
          </svg>
        </button>
      </div>

      {/* Middle Section: Navigation Icons */}
      <div className="flex flex-col items-center space-y-4 flex-1 justify-center">
        <button className="w-10 h-10 rounded-xl flex items-center justify-center text-white/70 hover:bg-white/5 hover:text-white transition-all">
          <svg xmlns="http://www.w3.org/2000/svg" className="h-5 w-5" fill="none" viewBox="0 0 24 24" stroke="currentColor">
            <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M3 12l2-2m0 0l7-7 7 7M5 10v10a1 1 0 001 1h3m10-11l2 2m-2-2v10a1 1 0 01-1 1h3m-6 0a1 1 0 001-1v-4a1 1 0 011-1h2a1 1 0 011 1v4a1 1 0 001 1m-6 0h6" />
          </svg>
        </button>
        <button className="w-10 h-10 rounded-xl flex items-center justify-center text-white/40 hover:bg-white/5 hover:text-white transition-all cursor-not-allowed">
          <svg xmlns="http://www.w3.org/2000/svg" className="h-5 w-5" fill="none" viewBox="0 0 24 24" stroke="currentColor">
            <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M21 21l-6-6m2-5a7 7 0 11-14 0 7 7 0 0114 0z" />
          </svg>
        </button>
        <button className="w-10 h-10 rounded-xl flex items-center justify-center text-white/40 hover:bg-white/5 hover:text-white transition-all cursor-not-allowed">
          <svg xmlns="http://www.w3.org/2000/svg" className="h-5 w-5" fill="none" viewBox="0 0 24 24" stroke="currentColor">
            <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M12 6.253v13m0-13C10.832 5.477 9.246 5 7.5 5S4.168 5.477 3 6.253v13C4.168 18.523 5.832 18 7.5 18s3.332.477 4.5 1.253m0-13C13.168 5.477 14.754 5 16.5 5s3.332.477 4.5 1.253v13C19.832 18.523 18.168 18 16.5 18s-3.332.477-4.5 1.253" />
          </svg>
        </button>
      </div>

      {/* Bottom Section: Profile Avatar */}
      <div className="flex flex-col items-center space-y-4">
        <button className="w-10 h-10 rounded-xl flex items-center justify-center text-white/40 hover:bg-white/5 hover:text-white transition-all cursor-not-allowed">
          <svg xmlns="http://www.w3.org/2000/svg" className="h-5 w-5" fill="none" viewBox="0 0 24 24" stroke="currentColor">
            <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M10.325 4.317c.426-1.756 2.924-1.756 3.35 0a1.724 1.724 0 002.573 1.066c1.543-.94 3.31.826 2.37 2.37a1.724 1.724 0 001.065 2.572c1.756.426 1.756 2.924 0 3.35a1.724 1.724 0 00-1.066 2.573c.94 1.543-.826 3.31-2.37 2.37a1.724 1.724 0 00-2.572 1.065c-.426 1.756-2.924 1.756-3.35 0a1.724 1.724 0 00-2.573-1.066c-1.543.94-3.31-.826-2.37-2.37a1.724 1.724 0 00-1.065-2.572c-1.756-.426-1.756-2.924 0-3.35a1.724 1.724 0 001.066-2.573c-.94-1.543.826-3.31 2.37-2.37.996.608 2.296.07 2.572-1.065z" />
            <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M15 12a3 3 0 11-6 0 3 3 0 016 0z" />
          </svg>
        </button>
        <div className="w-8 h-8 rounded-full bg-gradient-to-br from-heritage-gold to-[#E58026] flex items-center justify-center cursor-pointer shadow-sm">
          <span className="text-white font-bold text-xs">M</span>
        </div>
      </div>
    </aside>
  );
}
