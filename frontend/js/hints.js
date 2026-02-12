async function getHint() {
  const stage = document.getElementById("stageSelect").value;
  const box = document.getElementById("hintBox");

  if (!stage) {
    box.innerText = "Please select a stage first.";
    return;
  }

  try {
    const res = await fetch(`https://escape-room-yi58.onrender.com/hint/${stage}`, {
      method: "POST"
    });

    const data = await res.json();
    box.innerText = data.reply;

  } catch (err) {
    box.innerText = "The system is silent.";
  }
}
