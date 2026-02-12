async function unlock() {
  const code = document.getElementById("codeInput").value;
  const msg = document.getElementById("msg");

  const res = await fetch("http://127.0.0.1:5000/unlock", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ code })
  });

  const data = await res.json();

  if (data.success) {
    msg.innerText = "Stage unlocked";
    setTimeout(() => {
      window.location.href = "index.html";
    }, 1200);
  } else {
    msg.innerText = "Incorrect code.";
  }
}
