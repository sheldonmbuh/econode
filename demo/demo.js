const scenes = {
  clear: { score: 0.92, age: 80 },
  occluded: { score: 0.42, age: 90 },
  stale: { score: 0.91, age: 450 },
};
const scene = document.querySelector("#scene");
const score = document.querySelector("#score");
const age = document.querySelector("#age");
const guidance = document.querySelector("#guidance");
const reason = document.querySelector("#reason");

function update() {
  const current = scenes[scene.value];
  const fresh = current.age <= 200;
  const confident = current.score >= 0.8;
  score.textContent = current.score.toFixed(2);
  age.textContent = `${current.age} ms`;
  guidance.textContent = fresh && confident ? "Show a review cue" : "Withhold the cue";
  if (!fresh) reason.textContent = "Wait for a current frame before showing guidance.";
  else if (!confident) reason.textContent = "Ask for a clearer view to reduce uncertainty.";
  else reason.textContent = "The input meets both illustrative thresholds.";
}

scene.addEventListener("change", update);
update();
