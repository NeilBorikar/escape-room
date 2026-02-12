async function getHint() {
  const stage = document.getElementById("stageSelect").value;
  const box = document.getElementById("hintBox");

  if (!stage) {
    box.innerText = "Please select a stage first.";
    return;
  }

  try {
    const res = await fetch(`http://127.0.0.1:5000/hint/${stage}`, {
      method: "POST"
    });

    const data = await res.json();
    box.innerText = data.reply;

  } catch (err) {
    box.innerText = "The system is silent.";
  }
}
