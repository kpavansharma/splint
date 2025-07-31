### `frontend/static/chat_ui.js`
javascript
async function sendChat() {
  const input = document.getElementById("user-input").value;
  const res = await fetch("/chat", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ prompt: input, session_id: "test-user" })
  });
  const data = await res.json();
  document.getElementById("chat").innerHTML += `<p><b>You:</b> ${input}</p>`;
  document.getElementById("chat").innerHTML += `<p><b>SPLint:</b> ${data.response}</p>`;
  document.getElementById("user-input").value = "";
}