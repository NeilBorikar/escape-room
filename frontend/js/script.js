function typeAIMessage(text) {
  const terminal = document.getElementById("terminal");

  const line = document.createElement("div");
  line.className = "ai";
  terminal.appendChild(line);

  let i = 0;
  const speed = 30;

  const typing = setInterval(() => {
    line.textContent = "AI: " + text.slice(0, i);
    i++;
    terminal.scrollTop = terminal.scrollHeight;

    if (i > text.length) {
      clearInterval(typing);
    }
  }, speed);
}

async function askAI() {
  const input = document.getElementById("userInput").value;
  if (!input) return;

  const terminal = document.getElementById("terminal");
  terminal.innerHTML += `<div class="user">You: ${input}</div>`;
  document.getElementById("userInput").value = "";

  try {
    const res = await fetch("https://escape-room-yi58.onrender.com/ask", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ question: input })
    });

    const data = await res.json();
    typeAIMessage(data.reply);

  } catch (e) {
    typeAIMessage("The signal is weak. Try again.");
  }
}
