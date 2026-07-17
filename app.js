(() => {
  "use strict";

  const STORAGE_KEY = "muhkam-progress-v2";
  const THEME_KEY = "muhkam-theme";
  const MAX_MISSED = 150;
  const REVISION_SIZE = 20;
  const ADVANCE_DELAY_CORRECT = 900;
  const ADVANCE_DELAY_WRONG = 2000;

  const screenEl = document.getElementById("screen");
  const streakEl = document.getElementById("streakCount");
  const xpEl = document.getElementById("xpCount");
  const wordsEl = document.getElementById("wordsCount");
  const wordsStatEl = document.getElementById("wordsStat");
  const themeToggleEl = document.getElementById("themeToggle");
  const soundToggleEl = document.getElementById("soundToggle");
  const hoardModal = document.getElementById("hoardModal");
  const dialogueModal = document.getElementById("dialogueModal");

  // ---------- theme ----------
  function initTheme() {
    const stored = localStorage.getItem(THEME_KEY);
    if (stored === "light" || stored === "dark") {
      document.documentElement.setAttribute("data-theme", stored);
    }
  }

  function currentEffectiveTheme() {
    const attr = document.documentElement.getAttribute("data-theme");
    if (attr === "light" || attr === "dark") return attr;
    return window.matchMedia("(prefers-color-scheme: dark)").matches ? "dark" : "light";
  }

  function toggleTheme() {
    const next = currentEffectiveTheme() === "dark" ? "light" : "dark";
    document.documentElement.setAttribute("data-theme", next);
    localStorage.setItem(THEME_KEY, next);
  }

  initTheme();

  // ---------- sound ----------
  const SOUND_KEY = "muhkam-sound";
  let soundEnabled = localStorage.getItem(SOUND_KEY) !== "off";
  let audioCtx = null;

  function updateSoundToggleUI() {
    soundToggleEl.classList.toggle("muted", !soundEnabled);
  }

  function toggleSound() {
    soundEnabled = !soundEnabled;
    localStorage.setItem(SOUND_KEY, soundEnabled ? "on" : "off");
    updateSoundToggleUI();
  }

  function getAudioCtx() {
    if (!audioCtx) {
      const Ctx = window.AudioContext || window.webkitAudioContext;
      if (!Ctx) return null;
      audioCtx = new Ctx();
    }
    if (audioCtx.state === "suspended") audioCtx.resume();
    return audioCtx;
  }

  function playTone(ctx, freq, startOffset, duration, gainPeak) {
    const osc = ctx.createOscillator();
    const gain = ctx.createGain();
    osc.type = "sine";
    osc.frequency.value = freq;
    const t0 = ctx.currentTime + startOffset;
    gain.gain.setValueAtTime(0.0001, t0);
    gain.gain.exponentialRampToValueAtTime(gainPeak, t0 + 0.02);
    gain.gain.exponentialRampToValueAtTime(0.0001, t0 + duration);
    osc.connect(gain);
    gain.connect(ctx.destination);
    osc.start(t0);
    osc.stop(t0 + duration + 0.03);
  }

  function playCorrectSound() {
    if (!soundEnabled) return;
    const ctx = getAudioCtx();
    if (!ctx) return;
    playTone(ctx, 659.25, 0, 0.14, 0.16);
    playTone(ctx, 987.77, 0.08, 0.22, 0.14);
  }

  function playIncorrectSound() {
    if (!soundEnabled) return;
    const ctx = getAudioCtx();
    if (!ctx) return;
    playTone(ctx, 207.65, 0, 0.24, 0.13);
    playTone(ctx, 174.61, 0.06, 0.3, 0.11);
  }

  let course = null;
  let flatLessons = []; // [{ ...lesson, levelId }] in course order
  let exerciseIndex = new Map(); // gid -> { lesson, exercise }

  let progress = loadProgress();
  let session = null; // active lesson/review session state
  let advanceTimer = null;

  function scheduleAdvance(correct) {
    const delay = correct ? ADVANCE_DELAY_CORRECT : ADVANCE_DELAY_WRONG;
    advanceTimer = setTimeout(() => {
      advanceTimer = null;
      renderExercise();
    }, delay);
  }

  function cancelAdvance() {
    if (advanceTimer) { clearTimeout(advanceTimer); advanceTimer = null; }
  }

  // ---------- persistence ----------
  function loadProgress() {
    try {
      const raw = localStorage.getItem(STORAGE_KEY);
      if (raw) return JSON.parse(raw);
    } catch (e) { /* corrupt storage, fall through to defaults */ }
    return { xp: 0, streak: 0, lastActiveDate: null, completedLessons: [], missedBank: [], wordHoard: [] };
  }

  function saveProgress() {
    localStorage.setItem(STORAGE_KEY, JSON.stringify(progress));
  }

  function updateStreakOnCompletion() {
    const today = new Date().toDateString();
    if (progress.lastActiveDate !== today) {
      const yesterday = new Date(Date.now() - 86400000).toDateString();
      progress.streak = progress.lastActiveDate === yesterday ? progress.streak + 1 : 1;
      progress.lastActiveDate = today;
    }
    saveProgress();
  }

  function refreshTopStats() {
    streakEl.textContent = progress.streak;
    xpEl.textContent = progress.xp;
    wordsEl.textContent = progress.wordHoard.length;
  }

  // ---------- helpers ----------
  function shuffled(arr) {
    const a = arr.slice();
    for (let i = a.length - 1; i > 0; i--) {
      const j = Math.floor(Math.random() * (i + 1));
      [a[i], a[j]] = [a[j], a[i]];
    }
    return a;
  }

  function arabicTokens(s) {
    return s.trim().replace(/[.،؟!]/g, "").split(/\s+/).filter(Boolean);
  }

  function isLessonUnlocked(flatIndex) {
    if (flatIndex === 0) return true;
    return progress.completedLessons.includes(flatLessons[flatIndex - 1].id);
  }

  function harvestWords(ex) {
    let words = [];
    if (ex.type === "word-bank") words = ex.answer;
    else if (ex.type === "multiple-choice" && ex.direction === "ar-en") {
      words = arabicTokens(ex.prompt);
    }
    let added = 0;
    words.forEach(w => {
      if (!progress.wordHoard.includes(w)) { progress.wordHoard.push(w); added++; }
    });
    if (added) refreshTopStats();
  }

  // ---------- boot ----------
  async function boot() {
    const res = await fetch("data/courses.json");
    if (!res.ok) throw new Error("Failed to load course data");
    const data = await res.json();
    course = data.course;

    course.levels.forEach(level => {
      level.lessons.forEach(lesson => {
        flatLessons.push({ ...lesson, levelId: level.id });
        lesson.exercises.forEach((ex, i) => {
          exerciseIndex.set(`${lesson.id}:${i}`, { lesson, exercise: ex });
        });
      });
    });

    refreshTopStats();
    updateSoundToggleUI();
    renderHome();
    wireGlobalUi();
  }

  function wireGlobalUi() {
    themeToggleEl.addEventListener("click", toggleTheme);
    soundToggleEl.addEventListener("click", toggleSound);

    wordsStatEl.addEventListener("click", () => {
      renderHoard();
      hoardModal.classList.remove("hidden");
    });
    document.getElementById("hoardClose").addEventListener("click", () => {
      hoardModal.classList.add("hidden");
    });
    hoardModal.addEventListener("click", e => {
      if (e.target === hoardModal) hoardModal.classList.add("hidden");
    });

    document.getElementById("dialogueClose").addEventListener("click", () => {
      dialogueModal.classList.add("hidden");
    });
    dialogueModal.addEventListener("click", e => {
      if (e.target === dialogueModal) dialogueModal.classList.add("hidden");
    });

    document.addEventListener("keydown", e => {
      if (advanceTimer && e.key === "Enter") { e.preventDefault(); cancelAdvance(); renderExercise(); return; }
      if (/^[1-4]$/.test(e.key)) {
        const opts = Array.from(document.querySelectorAll(".options .option:not(:disabled)"));
        const opt = opts[Number(e.key) - 1];
        if (opt) opt.click();
      }
    });
  }

  function renderHoard() {
    const list = document.getElementById("hoardList");
    if (progress.wordHoard.length === 0) {
      list.innerHTML = `<p class="hoard-empty">No words collected yet — answer exercises correctly to fill your hoard.</p>`;
      return;
    }
    list.innerHTML = progress.wordHoard.slice().reverse()
      .map(w => `<span class="hoard-word" dir="rtl" lang="ar">${w}</span>`).join("");
  }

  function showDialogue(topic) {
    document.getElementById("dialogueTitle").innerHTML = `${topic.title}`;
    document.getElementById("dialogueList").innerHTML = topic.dialogue.map(turn => `
      <div class="dialogue-turn">
        <span class="dialogue-speaker">${turn.sp}</span>
        <p class="dialogue-ar" dir="rtl" lang="ar">${turn.ar}</p>
        <p class="dialogue-en">${turn.en}</p>
      </div>
    `).join("");
    dialogueModal.classList.remove("hidden");
  }

  // ---------- HOME ----------
  function renderHome() {
    const totalLessons = flatLessons.length;
    const doneCount = flatLessons.filter(l => progress.completedLessons.includes(l.id)).length;
    const pct = totalLessons ? Math.round((doneCount / totalLessons) * 100) : 0;

    const reviewCard = progress.missedBank.length > 0 ? `
      <button class="review-card" id="reviewBtn">
        <div>
          <div class="review-title">Review your mistakes</div>
          <div class="review-sub">${progress.missedBank.length} exercise${progress.missedBank.length === 1 ? "" : "s"} waiting &middot; مراجعة</div>
        </div>
        <span class="review-arrow" aria-hidden="true">&rarr;</span>
      </button>` : "";

    const revisionCard = doneCount > 0 ? `
      <button class="review-card revision-card" id="revisionBtn">
        <div>
          <div class="review-title">Random revision</div>
          <div class="review-sub">Old sentences, shuffled and mixed across topics &middot; تكرار عشوائي</div>
        </div>
        <span class="review-arrow" aria-hidden="true">&rarr;</span>
      </button>` : "";

    let flatCursor = -1;
    let openAssigned = false;
    const levelSections = course.levels.map(level => {
      const levelDone = level.lessons.filter(l => progress.completedLessons.includes(l.id)).length;
      const levelComplete = levelDone === level.lessons.length;
      const nodes = level.lessons.map(lesson => {
        flatCursor++;
        const idx = flatCursor;
        const unlocked = isLessonUnlocked(idx);
        const done = progress.completedLessons.includes(lesson.id);
        const stateClass = done ? "done" : unlocked ? "current" : "locked";
        const status = done ? "Complete" : unlocked ? "Start" : "Locked";
        return `
          <li class="path-node ${stateClass}" data-lesson="${lesson.id}">
            <div class="medallion">${done ? "&#10003;" : lesson.number}</div>
            <div class="node-card">
              <div>
                <div class="node-title">${lesson.title}<span class="ar">${lesson.titleAr}</span></div>
                <div class="node-desc">${lesson.description}</div>
              </div>
              <div class="node-status">${status}</div>
            </div>
          </li>`;
      }).join("");

      let open = false;
      if (!openAssigned && !levelComplete) { open = true; openAssigned = true; }

      return `
        <details class="level-section" ${open ? "open" : ""}>
          <summary class="level-header">
            <span class="level-badge">${level.cefr}</span>
            <div>
              <h2>${level.label}<span class="ar">${level.labelAr}</span></h2>
            </div>
            <span class="level-progress">${levelDone}/${level.lessons.length}</span>
          </summary>
          <ul class="path">${nodes}</ul>
        </details>
      `;
    }).join("");

    screenEl.innerHTML = `
      <section class="hero">
        <p class="eyebrow">Modern Standard Arabic &middot; A2 &rarr; C1</p>
        <h1>${course.title}</h1>
        <p class="ar-title">من الأساسيات إلى الفصحى المتقدّمة</p>
        <p class="lede">${course.subtitle}. Real sentences from day one, gradually shedding the vowel marks and the hand-holding as you climb.</p>
        <div class="progress-row">
          <div class="ring" data-pct="${pct}" style="--pct:${pct}"></div>
          <div class="progress-text">
            <span class="label">Course progress</span>
            <span class="value">${doneCount} / ${totalLessons} lessons</span>
          </div>
        </div>
      </section>
      ${reviewCard}
      ${revisionCard}
      ${levelSections}
    `;

    screenEl.querySelectorAll(".path-node:not(.locked)").forEach(node => {
      node.querySelector(".node-card").addEventListener("click", () => {
        const lessonId = node.dataset.lesson;
        startLesson(flatLessons.find(l => l.id === lessonId));
      });
    });

    const reviewBtn = document.getElementById("reviewBtn");
    if (reviewBtn) reviewBtn.addEventListener("click", startReview);

    const revisionBtn = document.getElementById("revisionBtn");
    if (revisionBtn) revisionBtn.addEventListener("click", startRevision);
  }

  // ---------- LESSON / REVIEW ----------
  function buildQueueItem(ex, gid, idx, sourceLesson) {
    return { ...ex, _idx: idx, _gid: gid, _sourceLesson: sourceLesson };
  }

  function startLesson(lesson) {
    session = {
      lesson,
      mode: "lesson",
      queue: lesson.exercises.map((ex, i) => buildQueueItem(ex, `${lesson.id}:${i}`, i, lesson)),
      total: lesson.exercises.length,
      solved: new Set(),
      mistakes: 0,
      combo: 0,
    };
    renderExercise();
  }

  function startReview() {
    const gids = progress.missedBank.filter(gid => exerciseIndex.has(gid));
    if (gids.length === 0) return;
    session = {
      lesson: { id: "__review__", title: "Review Session", titleAr: "مراجعة" },
      mode: "mistakes",
      queue: gids.map((gid, i) => buildQueueItem(exerciseIndex.get(gid).exercise, gid, i, exerciseIndex.get(gid).lesson)),
      total: gids.length,
      solved: new Set(),
      mistakes: 0,
      combo: 0,
    };
    renderExercise();
  }

  // Pools every exercise from already-completed lessons, mixes them together
  // (not grouped by lesson or topic), and pulls a random shuffled subset.
  function startRevision() {
    const completedLessons = flatLessons.filter(l => progress.completedLessons.includes(l.id));
    const pool = [];
    completedLessons.forEach(lesson => {
      lesson.exercises.forEach((ex, i) => pool.push({ gid: `${lesson.id}:${i}`, lesson }));
    });
    if (pool.length === 0) return;
    const picked = shuffled(pool).slice(0, Math.min(REVISION_SIZE, pool.length));
    session = {
      lesson: { id: "__revision__", title: "Random Revision", titleAr: "تكرار عشوائي" },
      mode: "revision",
      queue: picked.map((item, i) => buildQueueItem(exerciseIndex.get(item.gid).exercise, item.gid, i, item.lesson)),
      total: picked.length,
      solved: new Set(),
      mistakes: 0,
      combo: 0,
    };
    renderExercise();
  }

  function currentExercise() {
    return session.queue[0];
  }

  function renderLessonChrome(bodyHtml) {
    const pct = Math.round((session.solved.size / session.total) * 100);
    const combo = session.combo >= 2 ? `<span class="combo-badge">&times;${session.combo}</span>` : "";

    screenEl.innerHTML = `
      <div class="lesson-bar">
        <button class="exit-btn" id="exitBtn" aria-label="Exit lesson">&times;</button>
        <div class="progress-track"><div class="progress-fill" style="width:${pct}%"></div></div>
        ${combo}
        <span class="infinity-badge" title="Unlimited lives — wrong answers just come back around">&infin;</span>
      </div>
      ${bodyHtml}
    `;
    document.getElementById("exitBtn").addEventListener("click", () => {
      cancelAdvance();
      session = null;
      renderHome();
    });
  }

  function kicker(ex) {
    if (ex.type === "word-bank") return "Build the sentence in Arabic";
    if (ex.type === "comprehension") return "Reading comprehension";
    return "Select the correct translation";
  }

  function promptBlock(ex) {
    if (ex.type === "comprehension") {
      return `<p class="prompt-en">${ex.question}</p>`;
    }
    if (ex.direction === "ar-en" && ex.type !== "word-bank") {
      const toggle = ex.translit
        ? `<button class="translit-toggle" id="translitToggle">Show transliteration</button>
           <p class="translit hidden" id="translitText">${ex.translit}</p>`
        : "";
      return `<p class="prompt-ar" dir="rtl" lang="ar">${ex.prompt}</p>${toggle}`;
    }
    return `<p class="prompt-en">${ex.prompt}</p>`;
  }

  function wireTranslitToggle() {
    const btn = document.getElementById("translitToggle");
    if (!btn) return;
    btn.addEventListener("click", () => {
      const t = document.getElementById("translitText");
      t.classList.toggle("hidden");
      btn.textContent = t.classList.contains("hidden") ? "Show transliteration" : "Hide transliteration";
    });
  }

  function passagePanel() {
    const lesson = currentExercise()._sourceLesson || session.lesson;
    if (!lesson.readingPassage) return "";
    const rows = lesson.readingPassage.paragraphs.map(p => `
      <div class="passage-line">
        <p class="passage-ar" dir="rtl" lang="ar">${p.ar}</p>
        <p class="passage-en hidden">${p.en}</p>
      </div>
    `).join("");
    const context = lesson.readingPassage.context
      ? `<p class="context-note">${lesson.readingPassage.context}</p>` : "";
    return `
      <details class="passage-panel" open>
        <summary>${lesson.title} <span class="ar">${lesson.titleAr}</span></summary>
        ${context}
        <button class="translit-toggle" id="passageToggle">Show English</button>
        ${rows}
      </details>
    `;
  }

  function wirePassageToggle() {
    const btn = document.getElementById("passageToggle");
    if (!btn) return;
    btn.addEventListener("click", () => {
      const lines = document.querySelectorAll(".passage-en");
      const hide = !lines[0].classList.contains("hidden");
      lines.forEach(l => l.classList.toggle("hidden", hide));
      btn.textContent = hide ? "Show English" : "Hide English";
    });
  }

  function grammarPanel() {
    const lesson = currentExercise()._sourceLesson || session.lesson;
    const topic = lesson.topicId && course.grammarTopics[lesson.topicId];
    if (!topic) return "";
    return `
      <details class="grammar-panel">
        <summary>Grammar note <span class="ar">ملاحظة نحوية</span></summary>
        <h4>${topic.title}</h4>
        <p class="grammar-pattern">${topic.pattern}</p>
        <p class="grammar-explanation">${topic.explanation}</p>
        <div class="fact-box">
          <span class="fact-label">Did you know? <span class="ar">هل تعلم؟</span></span>
          <p>${topic.fact}</p>
        </div>
        <button class="btn btn-ghost btn-small" id="dialogueBtn">View example dialogue</button>
      </details>
    `;
  }

  function wireGrammarPanel() {
    const btn = document.getElementById("dialogueBtn");
    if (!btn) return;
    const lesson = currentExercise()._sourceLesson || session.lesson;
    const topic = course.grammarTopics[lesson.topicId];
    btn.addEventListener("click", () => showDialogue(topic));
  }

  function renderExercise() {
    if (session.queue.length === 0) return renderSummary();

    const ex = currentExercise();

    if (ex.type === "multiple-choice" || ex.type === "comprehension") return renderMultipleChoice(ex);
    if (ex.type === "word-bank") return renderWordBank(ex);
  }

  function renderFeedback(correct, correctText) {
    const delay = correct ? ADVANCE_DELAY_CORRECT : ADVANCE_DELAY_WRONG;
    return `
      <div class="feedback ${correct ? "correct" : "incorrect"}" role="status">
        <div class="feedback-text">
          <div class="title">${correct ? "Correct" : "Not quite"}</div>
          ${correct ? "" : `<div class="detail">${correctText}</div>`}
        </div>
        <div class="feedback-timer" style="animation-duration:${delay}ms"></div>
      </div>
    `;
  }

  function afterAnswer(correct) {
    const ex = currentExercise();
    correct ? playCorrectSound() : playIncorrectSound();
    if (correct) {
      session.solved.add(ex._idx);
      session.combo++;
      session.queue.shift();
      harvestWords(ex);
      const pos = progress.missedBank.indexOf(ex._gid);
      if (pos !== -1) progress.missedBank.splice(pos, 1);
    } else {
      session.mistakes++;
      session.combo = 0;
      if (!progress.missedBank.includes(ex._gid)) {
        progress.missedBank.push(ex._gid);
        if (progress.missedBank.length > MAX_MISSED) progress.missedBank.shift();
      }
      const [wrong] = session.queue.splice(0, 1);
      session.queue.push(wrong);
    }
    saveProgress();
  }

  // ---- multiple choice / comprehension ----
  function renderMultipleChoice(ex) {
    const options = ex.options.map((opt, i) =>
      `<button class="option" data-i="${i}">${opt}</button>`
    ).join("");

    renderLessonChrome(`
      ${ex.type === "comprehension" ? "" : grammarPanel()}
      <div class="card">
        <p class="q-kicker">${kicker(ex)}</p>
        ${ex.type === "comprehension" ? passagePanel() : ""}
        ${promptBlock(ex)}
        <div class="options">${options}</div>
        <div id="feedbackSlot"></div>
      </div>
    `);
    wireTranslitToggle();
    wirePassageToggle();
    wireGrammarPanel();

    const optionEls = Array.from(screenEl.querySelectorAll(".option"));
    optionEls.forEach(btn => {
      btn.addEventListener("click", () => {
        optionEls.forEach(b => b.disabled = true);
        const i = Number(btn.dataset.i);
        const correct = i === ex.answerIndex;
        btn.classList.add(correct ? "correct" : "incorrect");
        if (!correct) optionEls[ex.answerIndex].classList.add("correct");

        afterAnswer(correct);
        document.getElementById("feedbackSlot").innerHTML =
          renderFeedback(correct, `Correct answer: ${ex.options[ex.answerIndex]}`);
        scheduleAdvance(correct);
      });
    });
  }

  // ---- word bank ----
  // Pool tiles are rendered once in fixed positions and never reordered —
  // a tapped tile fades in place (space reserved) instead of the pool reflowing.
  function renderWordBank(ex) {
    const tiles = shuffled(ex.bank.map((word, i) => ({ id: i, word })));
    const placedOrder = [];
    let evalTimer = null;

    renderLessonChrome(`
      ${grammarPanel()}
      <div class="card">
        <p class="q-kicker">${kicker(ex)}</p>
        ${promptBlock(ex)}
        <div class="bank-target" id="bankTarget"></div>
        <div class="bank-pool" id="bankPool">
          ${tiles.map(t => `<button class="tile" data-id="${t.id}">${t.word}</button>`).join("")}
        </div>
        <div id="feedbackSlot"></div>
      </div>
    `);
    wireTranslitToggle();
    wireGrammarPanel();

    const targetEl = document.getElementById("bankTarget");
    const poolEl = document.getElementById("bankPool");
    const poolTileEls = new Map();

    poolEl.querySelectorAll(".tile").forEach(btn => {
      const id = Number(btn.dataset.id);
      poolTileEls.set(id, btn);
      btn.addEventListener("click", () => placeTile(id));
    });

    function placeTile(id) {
      const poolBtn = poolTileEls.get(id);
      if (poolBtn.disabled || poolBtn.classList.contains("tile-used")) return;
      poolBtn.classList.add("tile-used");
      placedOrder.push(id);

      const targetBtn = document.createElement("button");
      targetBtn.className = "tile placed tile-pop";
      targetBtn.dataset.id = id;
      targetBtn.textContent = tiles.find(t => t.id === id).word;
      targetBtn.addEventListener("click", () => removeTile(id, targetBtn));
      targetEl.appendChild(targetBtn);

      if (placedOrder.length === ex.answer.length) {
        evalTimer = setTimeout(evaluate, 320);
      }
    }

    function removeTile(id, targetBtn) {
      if (targetBtn.disabled) return;
      if (evalTimer) { clearTimeout(evalTimer); evalTimer = null; }
      const idx = placedOrder.indexOf(id);
      if (idx === -1) return;
      placedOrder.splice(idx, 1);
      targetBtn.classList.add("tile-remove");
      targetBtn.addEventListener("animationend", () => targetBtn.remove(), { once: true });
      poolTileEls.get(id).classList.remove("tile-used");
    }

    function evaluate() {
      const words = placedOrder.map(id => tiles.find(t => t.id === id).word);
      const correct = words.length === ex.answer.length && words.every((w, i) => w === ex.answer[i]);
      poolTileEls.forEach(b => b.disabled = true);
      targetEl.querySelectorAll(".tile").forEach(b => b.disabled = true);

      afterAnswer(correct);
      document.getElementById("feedbackSlot").innerHTML =
        renderFeedback(correct, `Correct order: ${ex.answer.join(" ")}`);
      scheduleAdvance(correct);
    }
  }

  // ---------- SUMMARY / FAIL ----------
  function renderSummary() {
    const perfect = session.mistakes === 0;
    const xpEarned = 10 + (perfect ? 5 : 0);
    progress.xp += xpEarned;
    if (session.mode === "lesson" && !progress.completedLessons.includes(session.lesson.id)) {
      progress.completedLessons.push(session.lesson.id);
    }
    updateStreakOnCompletion();
    refreshTopStats();

    const summaryTitle = perfect
      ? "Perfect run"
      : session.mode === "mistakes" ? "Review complete"
      : session.mode === "revision" ? "Revision complete"
      : "Lesson complete";

    screenEl.innerHTML = `
      <div class="summary">
        <svg class="medal" viewBox="0 0 32 32"><path d="M16 2 L18.5 13.5 L30 16 L18.5 18.5 L16 30 L13.5 18.5 L2 16 L13.5 13.5 Z" fill="var(--gold)"/></svg>
        <h2>${summaryTitle}</h2>
        <p>${session.lesson.title} &middot; ${session.lesson.titleAr}</p>
        <div class="summary-stats">
          <div class="stat-block"><span class="num">+${xpEarned}</span><span class="lbl">XP</span></div>
          <div class="stat-block"><span class="num">${session.mistakes}</span><span class="lbl">Mistakes</span></div>
          <div class="stat-block"><span class="num">${progress.streak}</span><span class="lbl">Day streak</span></div>
        </div>
        <button class="btn btn-primary" id="continueHome">Continue</button>
      </div>
    `;
    document.getElementById("continueHome").addEventListener("click", () => {
      session = null;
      renderHome();
    });
  }

  boot();
})();
