async function fetchTime() {
  const res = await fetch("http://127.0.0.1:5000//time");
  const data = await res.json();

  let t = data.time_left;
  let m = Math.floor(t / 60);
  let s = t % 60;

  document.getElementById("timer").innerText =
    `⏳ ${m}:${s.toString().padStart(2, "0")}`;

  if (t <= 0) {
    document.getElementById("timer").innerText = "⏳ TIME UP";
  }
}

setInterval(fetchTime, 1000);
fetchTime();
