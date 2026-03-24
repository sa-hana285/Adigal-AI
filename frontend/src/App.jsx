import React, { useState } from 'react';
import Header from './components/Header';
import ChatContainer from './components/ChatContainer';
import InputBox from './components/InputBox';
import Sidebar from './components/Sidebar';
import HeroIntro from './components/HeroIntro';
import ChatContainerWrapper from './components/ChatContainer'; // just in case, wait, only need one

export default function App() {

  const [messages, setMessages] = useState([
    {
      id: 1,
      text: "Vannakkam (Welcome). I am Adigal. Ask me about the Silappatikaram, the epic of the Anklet, and its poetic wisdom.",
      sender: 'bot',
      time: new Date().toLocaleTimeString([], { hour: '2-digit', minute: '2-digit' })
    }
  ]);
  const [loading, setLoading] = useState(false);
  const API_URL = import.meta.env.VITE_API_URL;
  const handleSendMessage = async (text) => {
    // 1. Add User Message
    const userMessage = {
      id: Date.now(),
      text,
      sender: 'user',
      time: new Date().toLocaleTimeString([], { hour: '2-digit', minute: '2-digit' })
    };
    setMessages((prev) => [...prev, userMessage]);
    setLoading(true);

    try {
  const response = await fetch(`${API_URL}/api/chat`, {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify({ query: text }),
  });

      if (response.ok) {
        const data = await response.json();
        addBotMessage(data.answer);
      } else {
        setTimeout(() => {
          simulateFallbackResponse(text);
          setLoading(false);
        }, 1500);
      }
    } catch (error) {
       setTimeout(() => {
         simulateFallbackResponse(text);
         setLoading(false);
       }, 1500);
    }
  };

  const simulateFallbackResponse = (query) => {
    const fallbackText = `⚠️ Unable to connect to Adigal AI server. Please try again later.`;
    addBotMessage(fallbackText);
  };

  const addBotMessage = (text) => {
    const botMessage = {
      id: Date.now() + 1,
      text,
      sender: 'bot',
      time: new Date().toLocaleTimeString([], { hour: '2-digit', minute: '2-digit' })
    };
    setMessages((prev) => [...prev, botMessage]);
    setLoading(false);
  };

  const isIntro = messages.length <= 1;

  return (
    <div className="h-screen w-screen bg-[#070102] flex font-sans overflow-hidden antialiased relative">
      {/* 🔮 Dynamic Mesh Background / Light Flares */}
      <div className="absolute top-[-20%] left-[-10%] w-[800px] h-[800px] rounded-full bg-gradient-to-br from-temple-red/20 to-transparent blur-[140px] pointer-events-none animate-pulse duration-10000" />
      <div className="absolute bottom-[-20%] right-[-10%] w-[800px] h-[800px] rounded-full bg-gradient-to-br from-heritage-gold/15 to-transparent blur-[140px] pointer-events-none animate-pulse duration-7000" />

      {/* 🌟 Floating Ember Particles */}
      <div className="absolute inset-0 pointer-events-none overflow-hidden">
        <div className="absolute w-1 h-1 bg-heritage-gold/60 rounded-full top-1/4 left-1/3 blur-[1px] animate-ping" />
        <div className="absolute w-1.5 h-1.5 bg-heritage-gold/40 rounded-full top-2/3 left-2/3 blur-[1px] animate-pulse" />
        <div className="absolute w-0.5 h-0.5 bg-white/80 rounded-full top-1/3 right-1/4 animate-bounce" style={{ animationDuration: '4s' }} />
      </div>

      {/* 🧭 Left Sidebar Navigation */}
      <Sidebar />

      {/* 🏛️ Main Workspace Panel */}
      <div className="flex-1 flex flex-col h-full pl-16 md:pl-20 relative z-10">
        <Header />
        
        {/* Main Content Node */}
        <div className="flex-1 overflow-y-auto custom-scrollbar flex flex-col">
          {isIntro ? (
            <HeroIntro onSendPrompt={handleSendMessage} />
          ) : (
            <div className="max-w-4xl w-full mx-auto px-4 md:px-8 py-6">
              <ChatContainer messages={messages} />
            </div>
          )}
        </div>
        
        {loading && (
          <div className="px-4 py-2 text-xs text-heritage-gold font-sans bg-black/30 backdrop-blur-md animate-pulse text-center border-t border-white/5">
            Adigal is meditating on your questions...
          </div>
        )}

        {/* Floating Input Deck Centered */}
        <div className="w-full max-w-3xl mx-auto px-4 pb-6 mt-auto">
          <InputBox onSend={handleSendMessage} loading={loading} />
        </div>
      </div>
    </div>
  );
}



