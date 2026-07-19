(() => {
  "use strict";

  const THEME_KEY = "muhkam-theme";
  const ACTIVE_COURSE_KEY = "muhkam-active-course";
  const MAX_MISSED = 150;
  const REVISION_SIZE = 20;
  const ADVANCE_DELAY_CORRECT = 900;
  const ADVANCE_DELAY_WRONG = 2000;

  const COURSES = [
    { id: "arabic", file: "data/courses.json", legacyProgressKey: "muhkam-progress-v2", label: "Arabic — العربية", flag: "العربية" },
    { id: "tajik", file: "data/courses-tajik.json", label: "Tajik — Тоҷикӣ", flag: "Тоҷикӣ" },
  ];

  const screenEl = document.getElementById("screen");
  const streakEl = document.getElementById("streakCount");
  const xpEl = document.getElementById("xpCount");
  const wordsEl = document.getElementById("wordsCount");
  const wordsStatEl = document.getElementById("wordsStat");
  const mistakesEl = document.getElementById("mistakesCount");
  const mistakesStatEl = document.getElementById("mistakesStat");
  const practiceEl = document.getElementById("practiceCount");
  const practiceStatEl = document.getElementById("practiceStat");
  const themeToggleEl = document.getElementById("themeToggle");
  const soundToggleEl = document.getElementById("soundToggle");
  const courseToggleEl = document.getElementById("courseToggle");
  const mobileMenuEl = document.getElementById("mobileMenu");
  const menuToggleBtnEl = document.getElementById("menuToggleBtn");
  const mobileMenuPanelEl = document.getElementById("mobileMenuPanel");
  const hoardModal = document.getElementById("hoardModal");
  const dialogueModal = document.getElementById("dialogueModal");
  const courseModal = document.getElementById("courseModal");

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
  // Mobile browsers suspend AudioContext until a genuine user gesture
  // unlocks it; warm it up on the very first tap anywhere on the page so
  // the first real sound effect (an answer tap) isn't the one that's dropped.
  document.addEventListener("pointerdown", getAudioCtx, { once: true, passive: true });

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

  // ---------- text-to-speech ----------
  // Free browser/OS voices only. English is universally available; Arabic
  // has decent free voices on most platforms (Chrome/Edge/macOS). No browser
  // or OS ships a real Tajik voice, so for Tajik we fall back to a Farsi
  // voice reading a hand-checked Farsi equivalent (Tajik and Iranian Farsi
  // are the same spoken language) — but only where that equivalent exists
  // in the data (`ex.farsi`); we never guess or mechanically transliterate,
  // since a wrong-sounding "approximation" would teach bad pronunciation.
  const VOICE_RANK_EN = [
    /Google US English/i,
    /Microsoft (Aria|Jenny|Emma).*(Natural|Online)/i,
    /Samantha/i,
    /Microsoft Zira/i,
    /Ava|Nicky|Zoe/i,
    /Microsoft (David|Mark)/i,
  ];
  const VOICE_RANK_BY_LANG = {
    ar: [
      /Google العربية/i,
      /Microsoft (Hamed|Naayf).*(Natural|Online)/i,
      /Majed/i,
      /Tarik/i,
    ],
    fa: [
      /Google فارسی/i,
      /Microsoft (Dilara|Farid).*(Natural|Online)/i,
      /Negar/i,
    ],
    tg: [],
  };
  let _voices = [];
  let _preferredVoiceEn = null;
  let _preferredVoiceTarget = null;
  let _preferredVoiceFa = null;
  function pickVoice(langPrefix, rankList) {
    const pool = _voices.filter(v => v.lang.toLowerCase().startsWith(langPrefix));
    for (const pattern of rankList) {
      const match = pool.find(v => pattern.test(v.name));
      if (match) return match;
    }
    return pool[0] || null;
  }
  function refreshVoices() {
    if (!("speechSynthesis" in window)) return;
    _voices = window.speechSynthesis.getVoices() || [];
    _preferredVoiceEn = pickVoice("en", VOICE_RANK_EN);
    _preferredVoiceTarget = course ? pickVoice(course.lang, VOICE_RANK_BY_LANG[course.lang] || []) : null;
    _preferredVoiceFa = course && course.lang === "tg" ? pickVoice("fa", VOICE_RANK_BY_LANG.fa) : null;
  }
  if ("speechSynthesis" in window) {
    // Don't call refreshVoices() here — `course` isn't assigned yet at this
    // point in module init (it's declared later with `let`, so referencing
    // it now would throw). loadCourseData() calls refreshVoices() once
    // course is actually set; this handler covers async voice-list loads.
    window.speechSynthesis.onvoiceschanged = refreshVoices;
  }
  const SPEECH_RATE = 0.85;
  function speak(text, voice, onEnd) {
    if (!soundEnabled || !("speechSynthesis" in window) || !voice) { if (onEnd) onEnd(); return; }
    try {
      window.speechSynthesis.cancel();
      const u = new SpeechSynthesisUtterance(text);
      u.lang = voice.lang;
      u.voice = voice;
      u.rate = SPEECH_RATE;
      if (onEnd) { u.onend = onEnd; u.onerror = onEnd; }
      window.speechSynthesis.speak(u);
    } catch (e) { if (onEnd) onEnd(); }
  }
  // Resolves what to actually speak for a target-language answer: the real
  // target voice+text if one exists (Arabic, or a Tajik voice on the rare
  // device that has one), else a Farsi voice reading ex.farsi if both are
  // available, else nothing.
  function resolveSpeech(isEnglish, text, ex) {
    if (isEnglish) return _preferredVoiceEn ? { text, voice: _preferredVoiceEn } : null;
    if (_preferredVoiceTarget) return { text, voice: _preferredVoiceTarget };
    if (ex && ex.farsi && _preferredVoiceFa) return { text: ex.farsi, voice: _preferredVoiceFa };
    return null;
  }
  // Estimate for the feedback timer bar's animation-duration only (cosmetic;
  // the actual advance is driven by the real TTS "end" event below).
  function speechDurationMs(text) {
    if (!text) return 0;
    const words = text.trim().split(/\s+/).filter(Boolean).length;
    return (words / (2.3 * SPEECH_RATE)) * 1000 + 1000;
  }
  function visualDelay(correct, spoken) {
    const base = correct ? ADVANCE_DELAY_CORRECT : ADVANCE_DELAY_WRONG;
    return Math.max(base, speechDurationMs(spoken && spoken.text));
  }
  // Advance the instant the spoken answer finishes playing — no estimate, no
  // added pause, synced exactly to the real TTS "end" event. Falls back to
  // the fixed delay only when there's nothing to speak or audio is off, so
  // the learner still gets a moment to read.
  function advanceAfterSpeech(spoken, fallbackDelay) {
    if (!spoken) { scheduleAdvance(fallbackDelay); return; }
    speak(spoken.text, spoken.voice, () => scheduleAdvance(0));
  }
  // Always surface the target-language (Arabic/Tajik) text, never English —
  // the whole point of the audio is reinforcing target pronunciation. Which
  // field holds that text depends on direction: when the target language is
  // the shown prompt (${lang}-en), speak the prompt; when it's the expected
  // answer (en-${lang}), speak that. Comprehension questions have no target-
  // language text tied to the specific answer, so they get no audio.
  function targetLangText(ex) {
    if (ex.type === "comprehension") return null;
    const targetIsPrompt = ex.direction === `${course.lang}-en`;
    if (ex.type === "word-bank") return targetIsPrompt ? ex.prompt : ex.answer.join(" ");
    return targetIsPrompt ? ex.prompt : ex.options[ex.answerIndex];
  }

  let course = null;
  let activeCourseId = localStorage.getItem(ACTIVE_COURSE_KEY) || COURSES[0].id;
  if (!COURSES.some(c => c.id === activeCourseId)) activeCourseId = COURSES[0].id;
  let flatLessons = []; // [{ ...lesson, levelId }] in course order
  let exerciseIndex = new Map(); // gid -> { lesson, exercise }

  let progress = null;
  let session = null; // active lesson/review session state
  let advanceTimer = null;
  let currentLevelId = null;

  function scheduleAdvance(delay) {
    advanceTimer = setTimeout(() => {
      advanceTimer = null;
      renderExercise();
    }, delay);
  }

  function cancelAdvance() {
    if (advanceTimer) { clearTimeout(advanceTimer); advanceTimer = null; }
  }

  // ---------- persistence ----------
  function progressKeyFor(courseId) {
    const meta = COURSES.find(c => c.id === courseId);
    return (meta && meta.legacyProgressKey) || `muhkam-progress-v2-${courseId}`;
  }

  function progressKey() {
    return progressKeyFor(activeCourseId);
  }

  function loadProgress() {
    try {
      const raw = localStorage.getItem(progressKey());
      if (raw) return JSON.parse(raw);
    } catch (e) { /* corrupt storage, fall through to defaults */ }
    return { xp: 0, streak: 0, lastActiveDate: null, completedLessons: [], missedBank: [], wordHoard: [] };
  }

  function saveProgress() {
    localStorage.setItem(progressKey(), JSON.stringify(progress));
    if (window.CloudSync && window.CloudSync.user) {
      window.CloudSync.pushProgress(buildProgressPayload());
    }
  }

  // ---------- cross-device sync (manual code + cloud) ----------
  function buildProgressPayload() {
    const courses = {};
    COURSES.forEach(meta => {
      const raw = localStorage.getItem(progressKeyFor(meta.id));
      if (raw) {
        try { courses[meta.id] = JSON.parse(raw); } catch (e) { /* skip corrupt entry */ }
      }
    });
    return { version: 1, exportedAt: new Date().toISOString(), courses };
  }

  // Returns the number of courses written, or throws on invalid/unreadable input.
  function applyProgressPayload(payload) {
    if (!payload || typeof payload.courses !== "object") throw new Error("Not a valid sync payload");
    let count = 0;
    Object.keys(payload.courses).forEach(courseId => {
      localStorage.setItem(progressKeyFor(courseId), JSON.stringify(payload.courses[courseId]));
      count++;
    });
    return count;
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
    mistakesEl.textContent = progress.missedBank.length;
    mistakesStatEl.classList.toggle("hidden", progress.missedBank.length === 0);
    const poolSize = revisionPool().length;
    practiceEl.textContent = poolSize;
    practiceStatEl.classList.toggle("hidden", poolSize === 0);
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

  function nativeTokens(s) {
    return s.trim().replace(/[.,!?;:،؟!""«»—–]/g, "").split(/\s+/).filter(Boolean);
  }

  function isLessonUnlocked(flatIndex) {
    if (flatIndex === 0) return true;
    return progress.completedLessons.includes(flatLessons[flatIndex - 1].id);
  }

  function harvestWords(ex) {
    let words = [];
    if (ex.type === "word-bank") words = ex.answer;
    else if (ex.type === "multiple-choice" && ex.direction === `${course.lang}-en`) {
      words = nativeTokens(ex.prompt);
    }
    let added = 0;
    words.forEach(w => {
      if (!progress.wordHoard.includes(w)) { progress.wordHoard.push(w); added++; }
    });
    if (added) refreshTopStats();
  }

  // ---------- boot ----------
  async function loadCourseData(courseId) {
    const meta = COURSES.find(c => c.id === courseId) || COURSES[0];
    const res = await fetch(meta.file);
    if (!res.ok) throw new Error("Failed to load course data");
    const data = await res.json();
    course = data.course;
    course.id = meta.id;
    refreshVoices();

    flatLessons = [];
    exerciseIndex = new Map();
    course.levels.forEach(level => {
      level.lessons.forEach(lesson => {
        flatLessons.push({ ...lesson, levelId: level.id });
        lesson.exercises.forEach((ex, i) => {
          exerciseIndex.set(`${lesson.id}:${i}`, { lesson, exercise: ex });
        });
      });
    });

    document.documentElement.style.setProperty("--font-native", course.fontNative || "var(--font-arabic)");
    document.title = `Muḥkam — ${course.title}`;
    courseToggleEl.textContent = course.flag || course.languageName || course.id;
    const hoardNativeLabel = document.getElementById("hoardNativeLabel");
    if (hoardNativeLabel) hoardNativeLabel.textContent = (course.uiStrings && course.uiStrings.wordHoard) || "";
  }

  async function switchCourse(courseId) {
    if (courseId === activeCourseId) return;
    cancelAdvance();
    session = null;
    activeCourseId = courseId;
    localStorage.setItem(ACTIVE_COURSE_KEY, courseId);
    currentLevelId = null;
    await loadCourseData(courseId);
    progress = loadProgress();
    refreshTopStats();
    renderHome();
  }

  async function boot() {
    await loadCourseData(activeCourseId);
    progress = loadProgress();
    if (window.CloudSync && window.CloudSync.user) {
      try {
        const remote = await window.CloudSync.pullProgress();
        if (remote && remote.courses) {
          applyProgressPayload(remote);
          progress = loadProgress();
        } else {
          window.CloudSync.pushProgress(buildProgressPayload());
        }
      } catch (e) { /* offline — continue with local progress */ }
    }
    refreshTopStats();
    updateSoundToggleUI();
    renderHome();
    wireGlobalUi();
  }

  function renderCoursePicker() {
    const list = document.getElementById("courseList");
    list.innerHTML = COURSES.map(meta => `
      <button class="course-option ${meta.id === activeCourseId ? "active" : ""}" data-course="${meta.id}">
        <span class="course-option-name">${meta.label}</span>
      </button>
    `).join("");
    list.querySelectorAll(".course-option").forEach(btn => {
      btn.addEventListener("click", async () => {
        const id = btn.dataset.course;
        courseModal.classList.add("hidden");
        await switchCourse(id);
      });
    });
  }

  function wireGlobalUi() {
    themeToggleEl.addEventListener("click", toggleTheme);
    soundToggleEl.addEventListener("click", toggleSound);

    courseToggleEl.addEventListener("click", () => {
      renderCoursePicker();
      courseModal.classList.remove("hidden");
    });
    document.getElementById("courseClose").addEventListener("click", () => {
      courseModal.classList.add("hidden");
    });
    courseModal.addEventListener("click", e => {
      if (e.target === courseModal) courseModal.classList.add("hidden");
    });

    wordsStatEl.addEventListener("click", () => {
      renderHoard();
      hoardModal.classList.remove("hidden");
    });

    mistakesStatEl.addEventListener("click", () => {
      if (progress.missedBank.length === 0) return;
      cancelAdvance();
      startReview();
    });

    practiceStatEl.addEventListener("click", () => {
      cancelAdvance();
      startRevision();
    });

    function closeMobileMenu() {
      mobileMenuPanelEl.classList.remove("open");
      menuToggleBtnEl.setAttribute("aria-expanded", "false");
    }
    menuToggleBtnEl.addEventListener("click", () => {
      const nowOpen = mobileMenuPanelEl.classList.toggle("open");
      menuToggleBtnEl.setAttribute("aria-expanded", String(nowOpen));
    });
    mobileMenuPanelEl.querySelectorAll("button").forEach(btn => {
      btn.addEventListener("click", closeMobileMenu);
    });
    document.addEventListener("click", e => {
      if (mobileMenuPanelEl.classList.contains("open") && !mobileMenuEl.contains(e.target)) {
        closeMobileMenu();
      }
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
      list.removeAttribute("dir");
      list.innerHTML = `<p class="hoard-empty">No words collected yet — answer exercises correctly to fill your hoard.</p>`;
      return;
    }
    list.setAttribute("dir", course.dir);
    list.innerHTML = progress.wordHoard.slice().reverse()
      .map(w => `<span class="hoard-word" dir="${course.dir}" lang="${course.lang}">${w}</span>`).join("");
  }

  function showDialogue(topic) {
    document.getElementById("dialogueTitle").innerHTML = `${topic.title}`;
    document.getElementById("dialogueList").innerHTML = topic.dialogue.map(turn => `
      <div class="dialogue-turn">
        <span class="dialogue-speaker">${turn.sp}</span>
        <p class="dialogue-native" dir="${course.dir}" lang="${course.lang}">${turn.native}</p>
        <p class="dialogue-en">${turn.en}</p>
      </div>
    `).join("");
    dialogueModal.classList.remove("hidden");
  }

  // ---------- HOME ----------
  function waveformBars(pct, count = 14) {
    const filled = Math.round((pct / 100) * count);
    let html = "";
    for (let i = 0; i < count; i++) {
      const h = 8 + Math.round(Math.sin((i / count) * Math.PI) * 22);
      html += `<div class="bar${i < filled ? " filled" : ""}" style="height:${h}px"></div>`;
    }
    return html;
  }

  // Real geometry of every lesson node, in the roadmap's own content-space
  // coordinates (i.e. unaffected by current scroll position) — the single
  // source of truth for both the connecting path and the jump buttons.
  // Deliberately never touches scrollHeight/scrollWidth: an absolutely
  // positioned SVG child can itself inflate a scrolling container's
  // scrollHeight once sized, which was silently corrupting both the path
  // (clipped/misdrawn) and the jump targets (overshooting into empty space).
  function roadmapNodePoints(roadmapEl) {
    const nodeEls = Array.from(roadmapEl.querySelectorAll(".roadmap-node, .roadmap-next-node"));
    const containerRect = roadmapEl.getBoundingClientRect();
    return nodeEls.map(n => {
      const r = n.getBoundingClientRect();
      return {
        x: r.left + r.width / 2 - containerRect.left + roadmapEl.scrollLeft,
        y: r.top + r.height / 2 - containerRect.top + roadmapEl.scrollTop,
        top: r.top - containerRect.top + roadmapEl.scrollTop,
        done: n.classList.contains("done"),
      };
    });
  }

  // Traces an actual road through the zigzagged lesson nodes — measured
  // from real layout rather than guessed from CSS, since the left/center/
  // right offsets are percentage-based and shift with container width.
  // The walked stretch (behind completed lessons) is a solid gradient line
  // brightening toward the peak; the road ahead is a soft dashed track —
  // together they read as progress climbing toward the summit.
  function drawRoadmapPath() {
    const roadmapEl = document.getElementById("roadmapEl");
    if (!roadmapEl) return;
    const points = roadmapNodePoints(roadmapEl);
    if (points.length < 2) return;
    function segmentPath(pts) {
      let d = `M ${pts[0].x} ${pts[0].y}`;
      for (let i = 1; i < pts.length; i++) {
        const prev = pts[i - 1], curr = pts[i];
        const midY = (prev.y + curr.y) / 2;
        d += ` C ${prev.x} ${midY}, ${curr.x} ${midY}, ${curr.x} ${curr.y}`;
      }
      return d;
    }
    let doneCount = 0;
    while (doneCount < points.length && points[doneCount].done) doneCount++;
    const walkedPts = points.slice(0, Math.min(doneCount + 1, points.length));
    const aheadPts = points.slice(Math.max(doneCount, 0));
    let svg = roadmapEl.querySelector(".roadmap-path-svg");
    if (!svg) {
      svg = document.createElementNS("http://www.w3.org/2000/svg", "svg");
      svg.setAttribute("class", "roadmap-path-svg");
      roadmapEl.insertBefore(svg, roadmapEl.firstChild);
    }
    const maxY = Math.max(...points.map(p => p.y)) + 60;
    svg.setAttribute("width", roadmapEl.clientWidth);
    svg.setAttribute("height", maxY);
    let inner = `<defs><linearGradient id="roadmapGrad" x1="0" y1="1" x2="0" y2="0">
      <stop offset="0%" stop-color="var(--maroon)"/><stop offset="100%" stop-color="var(--gold)"/>
    </linearGradient></defs>`;
    if (aheadPts.length >= 2) inner += `<path d="${segmentPath(aheadPts)}" fill="none" stroke="var(--paper-deep)" stroke-width="5" stroke-linecap="round" stroke-dasharray="2 13"/>`;
    if (walkedPts.length >= 2) inner += `<path d="${segmentPath(walkedPts)}" fill="none" stroke="url(#roadmapGrad)" stroke-width="6" stroke-linecap="round"/>`;
    svg.innerHTML = inner;
  }
  // Scrolls to the true topmost or bottommost lesson node — computed from
  // real node positions, not scrollHeight (see roadmapNodePoints above).
  function scrollRoadmapToEdge(edge) {
    const roadmapEl = document.getElementById("roadmapEl");
    if (!roadmapEl) return;
    const points = roadmapNodePoints(roadmapEl);
    if (!points.length) return;
    const tops = points.map(p => p.top);
    const targetY = edge === "top"
      ? Math.min(...tops) - 24
      : Math.max(...tops) - roadmapEl.clientHeight + 100;
    roadmapEl.scrollTo({ top: Math.max(0, targetY), behavior: "smooth" });
  }
  let _roadmapResizeQueued = false;
  window.addEventListener("resize", () => {
    if (_roadmapResizeQueued || !document.getElementById("roadmapEl")) return;
    _roadmapResizeQueued = true;
    requestAnimationFrame(() => { _roadmapResizeQueued = false; drawRoadmapPath(); });
  });

  // The level whose roadmap should show by default: the one containing the
  // first unlocked-but-not-yet-completed lesson (i.e. "where the user is"),
  // falling back to the first level with lessons.
  function pickDefaultLevel() {
    for (const level of course.levels) {
      const levelLessons = flatLessons.filter(l => l.levelId === level.id);
      if (!levelLessons.length) continue;
      const hasCurrent = levelLessons.some(l => !progress.completedLessons.includes(l.id) && isLessonUnlocked(flatLessons.indexOf(l)));
      if (hasCurrent) return level.id;
    }
    const firstBuilt = course.levels.find(lv => flatLessons.some(l => l.levelId === lv.id));
    return firstBuilt ? firstBuilt.id : course.levels[0].id;
  }

  function renderHome() {
    if (!currentLevelId || !course.levels.some(l => l.id === currentLevelId)) {
      currentLevelId = pickDefaultLevel();
    }
    renderLevelRoadmap();
  }

  // Each level gets its own roadmap: lessons as round nodes running bottom
  // (lesson 1) to top (last lesson), like climbing toward the level's peak.
  // Completing the level unlocks a "next level" node above the last lesson.
  function renderLevelRoadmap() {
    const totalLessons = flatLessons.length;
    const doneLessons = flatLessons.filter(l => progress.completedLessons.includes(l.id)).length;
    const overallPct = totalLessons ? Math.round((doneLessons / totalLessons) * 100) : 0;

    const level = course.levels.find(l => l.id === currentLevelId);
    const builtLevels = course.levels.filter(lv => flatLessons.some(l => l.levelId === lv.id));
    const builtIdx = builtLevels.findIndex(lv => lv.id === currentLevelId);
    const prevLevel = builtIdx > 0 ? builtLevels[builtIdx - 1] : null;
    const nextLevel = builtIdx >= 0 && builtIdx < builtLevels.length - 1 ? builtLevels[builtIdx + 1] : null;

    const levelLessons = flatLessons.filter(l => l.levelId === level.id);
    const levelDone = levelLessons.filter(l => progress.completedLessons.includes(l.id)).length;
    const levelComplete = levelLessons.length > 0 && levelDone === levelLessons.length;

    let nodesHtml = "";
    levelLessons.forEach((lesson, i) => {
      const flatIndex = flatLessons.indexOf(lesson);
      const unlocked = isLessonUnlocked(flatIndex);
      const done = progress.completedLessons.includes(lesson.id);
      const isCurrent = unlocked && !done;
      const offset = ["center", "left", "right"][i % 3];
      nodesHtml += `
        <div class="roadmap-row ${offset}">
          <button class="roadmap-node ${done ? "done" : unlocked ? "unlocked" : "locked"} ${isCurrent ? "current" : ""}" data-lesson="${lesson.id}" ${unlocked ? "" : "disabled"} aria-label="${lesson.title}">
            ${done ? "✓" : unlocked ? lesson.number : "🔒"}
          </button>
          <div class="roadmap-label"><span class="roadmap-label-en">${lesson.title}</span><span class="roadmap-label-native">${lesson.titleNative || ""}</span></div>
        </div>
      `;
    });
    if (levelComplete && nextLevel) {
      nodesHtml += `
        <div class="roadmap-row center">
          <button class="roadmap-next-node" id="nextLevelBtn" aria-label="Next level">🏁</button>
          <div class="roadmap-label"><span class="roadmap-label-en">Level complete!</span><span class="roadmap-label-native">Next: ${nextLevel.cefr}</span></div>
        </div>
      `;
    }

    screenEl.innerHTML = `
      <div class="level-progress-card">
        <div class="waveform">${waveformBars(overallPct)}</div>
        <div class="level-progress-info">
          <div class="pct">${overallPct}%</div>
          <div class="label">Overall progress</div>
          <div class="count">${doneLessons} / ${totalLessons} lessons</div>
        </div>
      </div>
      <div class="roadmap-header">
        <button class="roadmap-arrow" id="prevLevelBtn" ${prevLevel ? "" : "disabled"} aria-label="Previous level">‹</button>
        <div class="roadmap-level-info">
          <span class="level-badge">${level.cefr}</span>
          <h2>${level.label}${level.labelNative ? ` &middot; ${level.labelNative}` : ""}</h2>
          <span class="level-count">${levelLessons.length ? `${levelDone}/${levelLessons.length}` : "coming soon"}</span>
        </div>
        <button class="roadmap-arrow" id="nextLevelNavBtn" ${nextLevel ? "" : "disabled"} aria-label="Next level">›</button>
      </div>
      ${!levelLessons.length
        ? `<div class="level-locked-note">Lessons for ${level.cefr} are still being prepared and will appear here soon.</div>`
        : `<div class="roadmap-wrap">
            <div class="roadmap" id="roadmapEl">${nodesHtml}</div>
            <button class="roadmap-jump roadmap-jump-top" id="jumpTopBtn" title="Jump to top" aria-label="Jump to top">⇈</button>
            <button class="roadmap-jump roadmap-jump-bottom" id="jumpBottomBtn" title="Jump to first lesson" aria-label="Jump to first lesson">⇊</button>
           </div>`
      }
    `;

    const jumpTopBtn = document.getElementById("jumpTopBtn");
    const jumpBottomBtn = document.getElementById("jumpBottomBtn");
    if (jumpTopBtn) jumpTopBtn.addEventListener("click", () => scrollRoadmapToEdge("top"));
    if (jumpBottomBtn) jumpBottomBtn.addEventListener("click", () => scrollRoadmapToEdge("bottom"));

    document.getElementById("prevLevelBtn").addEventListener("click", () => {
      if (!prevLevel) return;
      currentLevelId = prevLevel.id;
      renderLevelRoadmap();
    });
    document.getElementById("nextLevelNavBtn").addEventListener("click", () => {
      if (!nextLevel) return;
      currentLevelId = nextLevel.id;
      renderLevelRoadmap();
    });
    const nextLevelBtn = document.getElementById("nextLevelBtn");
    if (nextLevelBtn) {
      nextLevelBtn.addEventListener("click", () => {
        if (!nextLevel) return;
        currentLevelId = nextLevel.id;
        renderLevelRoadmap();
      });
    }
    screenEl.querySelectorAll(".roadmap-node:not(.locked)").forEach(node => {
      node.addEventListener("click", () => {
        const lesson = flatLessons.find(l => l.id === node.dataset.lesson);
        if (lesson) startLesson(lesson);
      });
    });

    const target = screenEl.querySelector(".roadmap-node.current") || screenEl.querySelector(".roadmap-node.unlocked");
    requestAnimationFrame(() => {
      drawRoadmapPath();
      if (target) target.scrollIntoView({ block: "center", behavior: "auto" });
    });
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
      lesson: { id: "__review__", title: "Review Session", titleNative: (course.uiStrings && course.uiStrings.review) || "" },
      mode: "mistakes",
      queue: gids.map((gid, i) => buildQueueItem(exerciseIndex.get(gid).exercise, gid, i, exerciseIndex.get(gid).lesson)),
      total: gids.length,
      solved: new Set(),
      mistakes: 0,
      combo: 0,
    };
    renderExercise();
  }

  // Every exercise from already-completed lessons, available to draw from for
  // revision practice — used both to size the top-bar counter and to build
  // the shuffled subset a revision session actually plays.
  function revisionPool() {
    const completedLessons = flatLessons.filter(l => progress.completedLessons.includes(l.id));
    const pool = [];
    completedLessons.forEach(lesson => {
      lesson.exercises.forEach((ex, i) => pool.push({ gid: `${lesson.id}:${i}`, lesson }));
    });
    return pool;
  }

  // Pools every exercise from already-completed lessons, mixes them together
  // (not grouped by lesson or topic), and pulls a random shuffled subset.
  function startRevision() {
    const pool = revisionPool();
    if (pool.length === 0) return;
    const picked = shuffled(pool).slice(0, Math.min(REVISION_SIZE, pool.length));
    session = {
      lesson: { id: "__revision__", title: "Practice", titleNative: (course.uiStrings && course.uiStrings.revision) || "" },
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
    if (ex.type === "word-bank") return `Build the sentence in ${course.languageName || course.title}`;
    if (ex.type === "comprehension") return "Reading comprehension";
    return "Select the correct translation";
  }

  function promptBlock(ex) {
    if (ex.type === "comprehension") {
      return `<p class="prompt-en">${ex.question}</p>`;
    }
    if (ex.direction === `${course.lang}-en` && ex.type !== "word-bank") {
      const toggle = ex.translit
        ? `<button class="translit-toggle" id="translitToggle">Show transliteration</button>
           <p class="translit hidden" id="translitText">${ex.translit}</p>`
        : ex.farsi
        ? `<button class="translit-toggle" id="translitToggle">Show in Farsi</button>
           <p class="translit translit-fa hidden" id="translitText" dir="rtl" lang="fa">${ex.farsi}</p>`
        : "";
      return `<p class="prompt-native" dir="${course.dir}" lang="${course.lang}">${ex.prompt}</p>${toggle}`;
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
        <p class="passage-native" dir="${course.dir}" lang="${course.lang}">${p.native}</p>
        <p class="passage-en hidden">${p.en}</p>
      </div>
    `).join("");
    const context = lesson.readingPassage.context
      ? `<p class="context-note">${lesson.readingPassage.context}</p>` : "";
    return `
      <details class="passage-panel" open>
        <summary>${lesson.title}${lesson.titleNative ? ` <span class="ar">${lesson.titleNative}</span>` : ""}</summary>
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

  function renderFeedback(correct, correctText, opts) {
    const delay = (opts && opts.delay) || (correct ? ADVANCE_DELAY_CORRECT : ADVANCE_DELAY_WRONG);
    const showSpeak = !!(opts && opts.spoken);
    const farsi = opts && opts.farsiHint;
    return `
      <div class="feedback ${correct ? "correct" : "incorrect"}" role="status">
        ${showSpeak ? `<button class="speak-btn" id="feedbackSpeakBtn" title="Play pronunciation" aria-label="Play pronunciation">🔊</button>` : ""}
        <div class="feedback-text">
          <div class="title">${correct ? "Correct" : "Not quite"}</div>
          ${correct ? "" : `<div class="detail">${correctText}${farsi ? `<span class="farsi-hint" dir="rtl" lang="fa">${farsi}</span>` : ""}</div>`}
        </div>
        <div class="feedback-timer" style="animation-duration:${delay}ms"></div>
      </div>
    `;
  }
  function wireFeedbackReplay(spoken) {
    const btn = document.getElementById("feedbackSpeakBtn");
    if (btn) btn.addEventListener("click", () => speak(spoken.text, spoken.voice));
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
    refreshTopStats();
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
        const spokenText = targetLangText(ex);
        const spoken = spokenText ? resolveSpeech(false, spokenText, ex) : null;
        const fallback = correct ? ADVANCE_DELAY_CORRECT : ADVANCE_DELAY_WRONG;
        document.getElementById("feedbackSlot").innerHTML =
          renderFeedback(correct, `Correct answer: ${ex.options[ex.answerIndex]}`, { spoken, delay: visualDelay(correct, spoken), farsiHint: ex.farsi });
        if (spoken) wireFeedbackReplay(spoken);
        advanceAfterSpeech(spoken, fallback);
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
    targetEl.setAttribute("dir", course.dir);
    poolEl.setAttribute("dir", course.dir);
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
      const spokenText = targetLangText(ex);
      const spoken = spokenText ? resolveSpeech(false, spokenText, ex) : null;
      const fallback = correct ? ADVANCE_DELAY_CORRECT : ADVANCE_DELAY_WRONG;
      document.getElementById("feedbackSlot").innerHTML =
        renderFeedback(correct, `Correct order: ${ex.answer.join(" ")}`, { spoken, delay: visualDelay(correct, spoken), farsiHint: ex.farsi });
      if (spoken) wireFeedbackReplay(spoken);
      advanceAfterSpeech(spoken, fallback);
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
        <p>${session.lesson.title}${session.lesson.titleNative ? ` &middot; ${session.lesson.titleNative}` : ""}</p>
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

  window.__appReady = boot;
})();
