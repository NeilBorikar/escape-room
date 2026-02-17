async function fetchTime() {
  const res = await fetch("https://tv5gc8z9-5000.inc1.devtunnels.ms//time");
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
