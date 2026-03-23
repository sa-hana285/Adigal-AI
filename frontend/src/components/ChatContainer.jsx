import React, { useEffect, useRef } from 'react';
import MessageBubble from './MessageBubble';

export default function ChatContainer({ messages }) {
  const containerRef = useRef(null);

  // Auto-scroll to bottom of view on new message
  useEffect(() => {
    if (containerRef.current) {
      containerRef.current.scrollTop = containerRef.current.scrollHeight;
    }
  }, [messages]);

  return (
    <div
      ref={containerRef}
      className="flex-1 overflow-y-auto p-4 space-y-2 custom-scrollbar bg-ivory-white/30 backdrop-blur-sm"
    >
      {messages.map((message) => (
        <MessageBubble key={message.id} message={message} />
      ))}
    </div>
  );
}
