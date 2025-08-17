// ─── gamify.js ───
// Simple gamification with localStorage

// RP thresholds for each level
const xpThresholds = [0, 100, 300, 600];
const levelNames   = ['Beginner', 'Intermediate', 'Advanced', 'Master'];

const XP_KEY = 'roa_xp';

function getXP() {
  return parseInt(localStorage.getItem(XP_KEY)) || 0;
}
function setXP(v) {
  localStorage.setItem(XP_KEY, v);
}
function addXP(amount) {
  const newXp = getXP() + amount;
  setXP(newXp);
  updateXPUI();
}

// Determine current level index
function getLevelIndex() {
  const xp = getXP();
  for (let i = xpThresholds.length - 1; i >= 0; i--) {
    if (xp >= xpThresholds[i]) return i;
  }
  return 0;
}

function updateXPUI() {
  const xp      = getXP();
  const lvlIdx  = getLevelIndex();
  const lvlName = levelNames[lvlIdx];
  const nextXP  = xpThresholds[lvlIdx + 1] || xpThresholds[xpThresholds.length - 1];
  const prevXP  = xpThresholds[lvlIdx];
  const percent = nextXP > prevXP
    ? Math.min(((xp - prevXP) / (nextXP - prevXP)) * 100, 100)
    : 100;

  document.querySelectorAll('.level-name')
    .forEach(el => el.textContent = lvlName);
  document.querySelectorAll('.xp-value')
    .forEach(el => el.textContent = `${xp} RP`);
  document.querySelectorAll('.xp-bar-inner')
    .forEach(el => el.style.width = `${percent}%`);
}

// QUIZ DATA (example)
const quizData = {
  'Framing Basics': [
    { q: 'What primary bone do we frame against?', a: 'collar' },
    { q: 'True/false: Frames prevent posture breaks.', a: 'true' }
  ],
  // add more modules here...
};

function startQuiz(moduleTitle) {
  const questions = quizData[moduleTitle] || [];
  if (!questions.length) {
    alert('No quiz available yet for ' + moduleTitle);
    return;
  }
  let score = 0;
  questions.forEach(({q,a}) => {
    const ans = prompt(q);
    if (ans && ans.toLowerCase().includes(a.toLowerCase())) score++;
  });
  const earned = score * 20; // 20 RP per correct
  addXP(earned);
  alert(`You scored ${score}/${questions.length}. Earned ${earned} RP!`);
}

// Init on page load
document.addEventListener('DOMContentLoaded', updateXPUI);
