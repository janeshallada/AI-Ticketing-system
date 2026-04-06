import React, { useEffect, useState } from "react";

function App() {
  const [tickets, setTickets] = useState([]);
  const [title, setTitle] = useState("");
  const [desc, setDesc] = useState("");

  const fetchTickets = async () => {
    const res = await fetch("http://127.0.0.1:8000/tickets/");
    const data = await res.json();
    setTickets(data);
  };

  useEffect(() => {
    fetchTickets();
  }, []);

  const createTicket = async () => {
    await fetch(`http://127.0.0.1:8000/tickets/?title=${title}&description=${desc}`, {
      method: "POST"
    });
    fetchTickets();
  };

  return (
    <div style={{ padding: 20 }}>
      <h1>AI Ticketing System</h1>

      <input placeholder="Title" value={title} onChange={(e) => setTitle(e.target.value)} />
      <input placeholder="Description" value={desc} onChange={(e) => setDesc(e.target.value)} />

      <button onClick={createTicket}>Create Ticket</button>

      {tickets.map((t) => (
        <div key={t.id}>
          <h3>{t.title}</h3>
          <p>{t.description}</p>
          <p>{t.status}</p>
        </div>
      ))}
    </div>
  );
}

export default App;
