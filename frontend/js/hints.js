async function getHint() {
  const stage = document.getElementById("stageSelect").value;
  const box = document.getElementById("hintBox");

  if (!stage) {
    box.innerText = "Please select a stage first.";
    return;
  }

  try {
    const res = await fetch(`https://tv5gc8z9-5000.inc1.devtunnels.ms//hint/${stage}`, {
      method: "POST"
    });

    const data = await res.json();
    box.innerText = data.reply;

    if (data.hints_used !== undefined) {
      updateHintDots(data.hints_used);
    }

  } catch (err) {
    box.innerText = "The system is silent.";
  }
}

function updateHintDots(count) {
  const dots = document.querySelectorAll(".hint-dot");

  dots.forEach((dot, index) => {
    if (index < count) {
      dot.classList.add("active");
    } else {
      dot.classList.remove("active");
    }
  });
}

