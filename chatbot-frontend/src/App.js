import React, { useState, useEffect, useRef } from "react";
import { marked } from "marked";

const GATLearnChat = () => {
  const [query, setQuery] = useState("");
  const [chatHistory, setChatHistory] = useState(() => {
    const saved = localStorage.getItem("gatLearnChatHistory");
    return saved ? JSON.parse(saved) : [];
  });
  const [loading, setLoading] = useState(false);
  const responseAreaRef = useRef(null);

  useEffect(() => {
    localStorage.setItem("gatLearnChatHistory", JSON.stringify(chatHistory));
  }, [chatHistory]);

  useEffect(() => {
    if (responseAreaRef.current) {
      responseAreaRef.current.scrollTop = responseAreaRef.current.scrollHeight;
    }
  }, [chatHistory]);

  const handleSubmit = async (e) => {
    e.preventDefault();
    const trimmedQuery = query.trim();
    if (!trimmedQuery) return;

    const newEntry = { question: trimmedQuery, answer: "" };
    setChatHistory([...chatHistory, newEntry]);
    setQuery("");
    setLoading(true);

    try {
      const response = await fetch("http://127.0.0.1:5000/query", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ query: trimmedQuery }),
      });
      const data = await response.json();
      const formatted = data.response.replace(/\r?\n/g, "\n").trim();
      if (response.ok) {
        setChatHistory((prev) => {
          const updated = [...prev];
          updated[updated.length - 1].answer = formatted;
          return updated;
        });
      } else {
        setChatHistory((prev) => {
          const updated = [...prev];
          updated[updated.length - 1].answer = `⚠️ ${formatted}`;
          return updated;
        });
      }
    } catch (error) {
      setChatHistory((prev) => {
        const updated = [...prev];
        updated[updated.length - 1].answer = `[Error] ${error.message}`;
        return updated;
      });
    } finally {
      setLoading(false);
    }
  };

  const selectHistoryItem = (index) => {
    setQuery(chatHistory[index].question);
  };

  const clearHistory = () => {
    localStorage.removeItem("gatLearnChatHistory");
    setChatHistory([]);
  };

  return (
    <div
      style={{
        display: "flex",
        height: "100vh",
        fontFamily: "'Segoe UI', Tahoma, Geneva, Verdana, sans-serif",
        backgroundColor: "#F3EBDD",
        color: "#333333",
      }}
    >
      {/* Sidebar */}
      <div
        style={{
          width: "300px",
          borderRight: "1px solid #ddd",
          backgroundColor: "#404B3A",
          color: "#FDF7ED",
          display: "flex",
          flexDirection: "column",
          padding: "15px",
        }}
      >
        <h2 style={{ textAlign: "center", fontSize: "18px", letterSpacing: "1px" }}>
          CHAT HISTORY
        </h2>
        <div style={{ overflowY: "auto", flexGrow: 1 }}>
          {chatHistory.length === 0 ? (
            <p style={{ textAlign: "center", color: "#ccc" }}>No chat history yet.</p>
          ) : (
            chatHistory.map((item, idx) => (
              <div
                key={idx}
                onClick={() => selectHistoryItem(idx)}
                style={{
                  padding: "8px 12px",
                  margin: "8px 0",
                  backgroundColor: idx === chatHistory.length - 1 ? "#6E765A" : "#585f49",
                  borderRadius: "6px",
                  cursor: "pointer",
                  whiteSpace: "nowrap",
                  overflow: "hidden",
                  textOverflow: "ellipsis",
                }}
              >
                {item.question}
              </div>
            ))
          )}
        </div>

        <button
          onClick={clearHistory}
          style={{
            marginTop: "15px",
            backgroundColor: "#6E765A",
            color: "#FDF7ED",
            border: "none",
            padding: "10px",
            borderRadius: "6px",
            cursor: "pointer",
            fontWeight: "600",
            fontSize: "14px",
          }}
        >
          🗑 Clear History
        </button>
      </div>

      {/* Main Chat Panel */}
      <div style={{ flexGrow: 1, display: "flex", flexDirection: "column" }}>
        {/* Header */}
        <header
          style={{
            backgroundColor: "#404B3A",
            padding: "25px 0",
            textAlign: "center",
            boxShadow: "0 3px 8px rgba(0, 0, 0, 0.3)",
          }}
        >
          <div
            style={{
              display: "inline-block",
              backgroundColor: "#6E765A",
              padding: "12px 30px",
              borderRadius: "12px",
              fontWeight: "800",
              fontSize: "28px",
              color: "#FDF7ED",
              letterSpacing: "6px",
              userSelect: "none",
            }}
          >
            GAT LEARN
          </div>
        </header>

        {/* Chat Area */}
        <div
          ref={responseAreaRef}
          style={{
            flexGrow: 1,
            overflowY: "auto",
            padding: "25px 30px",
            display: "flex",
            flexDirection: "column",
            gap: "18px",
            backgroundColor: "#E4EFDF",
          }}
        >
          {chatHistory.map((item, idx) => (
            <div key={idx} style={{ display: "flex", flexDirection: "column" }}>
              {/* Question */}
              <div
                style={{
                  alignSelf: "flex-start",
                  backgroundColor: "#FDF7ED",
                  color: "#4A5C38",
                  padding: "12px 18px",
                  borderRadius: "24px 24px 24px 4px",
                  maxWidth: "75%",
                  fontWeight: "600",
                  fontSize: "15px",
                  whiteSpace: "pre-wrap",
                  wordBreak: "break-word",
                }}
              >
                {item.question}
              </div>

              {/* Answer (Markdown-rendered) */}
              <div
                style={{
                  alignSelf: "flex-end",
                  backgroundColor: "#FDF7ED",
                  color: "#333333",
                  padding: "12px 18px",
                  borderRadius: "24px 24px 4px 24px",
                  maxWidth: "75%",
                  fontSize: "15px",
                  fontWeight: "500",
                  marginTop: "6px",
                  wordBreak: "break-word",
                }}
                dangerouslySetInnerHTML={{ __html: marked.parse(item.answer || "") }}
              />
            </div>
          ))}
        </div>

        {/* Input Box */}
        <form
          onSubmit={handleSubmit}
          style={{
            display: "flex",
            padding: "16px 24px",
            backgroundColor: "#F3EBDD",
            borderTop: "1px solid #ddd",
          }}
        >
          <input
            type="text"
            placeholder="Ask your question..."
            value={query}
            onChange={(e) => setQuery(e.target.value)}
            style={{
              flexGrow: 1,
              padding: "12px 18px",
              borderRadius: "30px",
              border: "1px solid #bbb",
              fontSize: "15px",
              backgroundColor: "#fff",
              color: "#333",
              outline: "none",
              fontFamily: "inherit",
            }}
            disabled={loading}
          />
          <button
            type="submit"
            disabled={loading}
            style={{
              marginLeft: "12px",
              padding: "12px 22px",
              borderRadius: "30px",
              border: "none",
              backgroundColor: loading ? "#aaa" : "#6E765A",
              color: "#FDF7ED",
              fontWeight: "600",
              fontSize: "15px",
              cursor: loading ? "not-allowed" : "pointer",
              transition: "background-color 0.3s ease",
            }}
          >
            Send
          </button>
        </form>
      </div>
    </div>
  );
};

export default GATLearnChat;
