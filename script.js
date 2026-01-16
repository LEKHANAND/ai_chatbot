async function sendMessage() {
  const input = document.getElementById("userInput");
  const message = input.value;
  if (!message) return;

  const chat = document.getElementById("chat");
  chat.innerHTML += `<p><b>You:</b> ${message}</p>`;
  input.value = "";
try {
  // typing indicator
  chat.innerHTML += `<p><b>Bot:</b> typing...</p>`;

  const response = await fetch("https://ai-chatbot-v60r.onrender.com/chat", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ message })
  });

  const data = await response.json();

  // replace typing with reply
  chat.lastChild.innerHTML = `<b>Bot:</b> ${data.reply}`;

} catch (error) {
  // error handling
  chat.innerHTML += `<p><b>Bot:</b> Server not responding ❌</p>`;
}
