(() => {
  "use strict";

  const THEME_KEY = "muhkam-theme";
  const ACTIVE_COURSE_KEY = "muhkam-active-course";
  const DATA_VERSION = "1786269698";
  const MAX_MISSED = 150;
  const REVISION_SIZE = 20;
  const ADVANCE_DELAY_CORRECT = 900;
  const ADVANCE_DELAY_WRONG = 2000;

  // `group` drives the course-picker's two sections, and matches this
  // project's real distinction, not a cosmetic one: "established" is the
  // set of pre-existing courses; "underserved" is every course built from
  // scratch for a language mainstream apps don't teach. `accent` cycles
  // through a curated palette (see the --course-accent-* tokens in
  // style.css) purely so the picker's cards are visually distinguishable
  // at a glance -- it carries no other meaning.
  const COURSES = [
    { id: "arabic", file: "data/courses.json", legacyProgressKey: "muhkam-progress-v2", label: "Arabic — العربية", native: "العربية", en: "Arabic", flag: "العربية", group: "established", accent: "gold" },
    { id: "tajik", file: "data/courses-tajik.json", label: "Tajik — Тоҷикӣ", native: "Тоҷикӣ", en: "Tajik", flag: "Тоҷикӣ", group: "established", accent: "teal" },
    { id: "hebrew", file: "data/courses-hebrew.json", label: "Hebrew — עברית", native: "עברית", en: "Hebrew", flag: "עברית", group: "established", accent: "indigo" },
    { id: "kazakh", file: "data/courses-kazakh.json", label: "Kazakh — Қазақша", native: "Қазақша", en: "Kazakh", flag: "Қазақша", group: "established", accent: "sage" },
    { id: "chinese", file: "data/courses-chinese.json", label: "Chinese (Pinyin) — Zhōngwén", native: "Zhōngwén", en: "Chinese (Pinyin)", flag: "Zhōngwén", group: "established", accent: "rust" },
    { id: "uzbek", file: "data/courses-uzbek.json", audioManifest: "data/audio-uzbek/manifest.json", label: "Uzbek — Oʻzbekcha", native: "Oʻzbekcha", en: "Uzbek", flag: "Oʻzbekcha", group: "underserved", accent: "gold" },
    { id: "chechen", file: "data/courses-chechen.json", label: "Chechen — Нохчийн", native: "Нохчийн", en: "Chechen", flag: "Нохчийн", group: "underserved", accent: "maroon" },
    { id: "avar", file: "data/courses-avar.json", audioManifest: "data/audio-avar/manifest.json", label: "Avar — МагӀарул мацӏ", native: "МагӀарул мацӏ", en: "Avar", flag: "МагӀарул мацӏ", group: "underserved", accent: "teal" },
    { id: "ossetian", file: "data/courses-ossetian.json", label: "Ossetian — Ирон ӕвзаг", native: "Ирон ӕвзаг", en: "Ossetian", flag: "Ирон ӕвзаг", group: "underserved", accent: "indigo" },
    { id: "dari", file: "data/courses-dari.json", audioManifest: "data/audio-dari/manifest.json", label: "Dari — دری", native: "دری", en: "Dari", flag: "دری", group: "underserved", accent: "sage" },
    { id: "pashto", file: "data/courses-pashto.json", audioManifest: "data/audio-pashto/manifest.json", label: "Pashto — پښتو", native: "پښتو", en: "Pashto", flag: "پښتو", group: "underserved", accent: "rust" },
    { id: "turkmen", file: "data/courses-turkmen.json", audioManifest: "data/audio-turkmen/manifest.json", label: "Turkmen — Türkmençe", native: "Türkmençe", en: "Turkmen", flag: "Türkmençe", group: "underserved", accent: "maroon" },
  ];

  // iOS Safari keeps a tapped <button> focused, which makes the
  // button:focus-visible gold ring (meant for keyboard nav) stick around
  // on the last-tapped tile/option even though the user just touched it.
  // event.detail is 0 for a keyboard-triggered click and >=1 for a real
  // pointer/touch click, so this only blurs (removes the ring) on taps.
  document.addEventListener("click", e => {
    const btn = e.target.closest("button");
    if (btn && e.detail !== 0) btn.blur();
  });

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
  const THEME_CYCLE = ["light", "dark", "book"];
  function initTheme() {
    const stored = localStorage.getItem(THEME_KEY);
    if (THEME_CYCLE.includes(stored)) {
      document.documentElement.setAttribute("data-theme", stored);
    }
  }

  function currentEffectiveTheme() {
    const attr = document.documentElement.getAttribute("data-theme");
    if (THEME_CYCLE.includes(attr)) return attr;
    return window.matchMedia("(prefers-color-scheme: dark)").matches ? "dark" : "light";
  }

  function toggleTheme() {
    const cur = THEME_CYCLE.indexOf(currentEffectiveTheme());
    const next = THEME_CYCLE[(cur + 1) % THEME_CYCLE.length];
    document.documentElement.setAttribute("data-theme", next);
    localStorage.setItem(THEME_KEY, next);
  }

  // The app already works fully offline (course JSON + bundled audio are
  // both runtime-cached by the service worker) but never showed the user
  // whether they actually were offline -- this is the only UI surface for
  // that state.
  function wireOfflineIndicator() {
    const pill = document.getElementById("offlinePill");
    if (!pill) return;
    const update = () => pill.classList.toggle("hidden", navigator.onLine);
    window.addEventListener("online", update);
    window.addEventListener("offline", update);
    update();
  }

  // Pull-to-refresh on the roadmap only -- mid-lesson (session is non-null
  // the whole time a lesson/review is in progress) a stray downward drag
  // re-syncing and re-rendering out from under the learner would lose
  // their place, not help them. Same gesture/damping as Wird's port of
  // this same idea -- see the comment there for the full reasoning.
  function wirePullToRefresh() {
    const indicator = document.getElementById("pullIndicator");
    if (!indicator) return;
    const THRESHOLD = 68;
    let startY = null, pulling = false, refreshing = false;
    document.addEventListener("touchstart", e => {
      if (session !== null || window.scrollY > 0 || refreshing) { startY = null; return; }
      startY = e.touches[0].clientY;
      pulling = false;
    }, { passive: true });
    document.addEventListener("touchmove", e => {
      if (startY === null || refreshing) return;
      const dy = e.touches[0].clientY - startY;
      if (dy <= 0) { pulling = false; indicator.style.transform = ""; indicator.classList.remove("armed"); return; }
      if (window.scrollY > 0) return;
      pulling = true;
      const dist = Math.min(THRESHOLD * 1.6, dy * 0.5);
      indicator.style.transform = `translateY(${dist}px)`;
      indicator.classList.toggle("armed", dist >= THRESHOLD);
    }, { passive: true });
    document.addEventListener("touchend", async () => {
      if (!pulling) { startY = null; return; }
      pulling = false;
      const armed = indicator.classList.contains("armed");
      if (!armed) { indicator.style.transform = ""; startY = null; return; }
      refreshing = true;
      indicator.classList.add("spinning");
      indicator.style.transform = `translateY(${THRESHOLD}px)`;
      try { await syncFromCloud(); } catch (e) { /* offline or signed out -- pull-to-refresh just becomes a no-op */ }
      if (session === null) renderHome();
      indicator.classList.remove("spinning", "armed");
      indicator.style.transform = "";
      refreshing = false;
      startY = null;
    });
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
  // resume() is async; scheduling a tone via ctx.currentTime before it
  // actually resolves means the tone gets scheduled into a context that
  // isn't running yet and never actually plays. iOS suspends the context
  // again after any idle gap, so this bites every sound, not just the
  // first — callers must wait for the real resume before scheduling.
  let _lastAudioError = null;
  function withRunningAudioCtx(fn) {
    const ctx = getAudioCtx();
    if (!ctx) { _lastAudioError = "AudioContext unavailable"; return; }
    const run = () => {
      try { fn(ctx); _lastAudioError = null; }
      catch (e) { _lastAudioError = e.message || String(e); }
    };
    if (ctx.state === "suspended") ctx.resume().then(run).catch(e => { _lastAudioError = "resume failed: " + (e.message || e); });
    else run();
  }
  // Mobile browsers suspend AudioContext until a genuine user gesture
  // unlocks it; warm it up on the very first tap anywhere on the page so
  // the first real sound effect (an answer tap) isn't the one that's dropped.
  document.addEventListener("pointerdown", getAudioCtx, { once: true, passive: true });

  // iOS Safari leaves the speech engine "asleep" until it's spoken from
  // inside a real user gesture at least once; a silent, near-empty
  // utterance on the very first tap wakes it up so the first real answer
  // isn't the one that gets silently dropped.
  function warmSpeech() {
    if (!("speechSynthesis" in window)) return;
    try {
      const u = new SpeechSynthesisUtterance(" ");
      u.volume = 0;
      window.speechSynthesis.speak(u);
    } catch (e) { /* speech unavailable */ }
  }
  document.addEventListener("pointerdown", warmSpeech, { once: true, passive: true });

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
    withRunningAudioCtx(ctx => {
      playTone(ctx, 659.25, 0, 0.14, 0.16);
      playTone(ctx, 987.77, 0.08, 0.22, 0.14);
    });
  }

  function playIncorrectSound() {
    if (!soundEnabled) return;
    withRunningAudioCtx(ctx => {
      playTone(ctx, 207.65, 0, 0.24, 0.13);
      playTone(ctx, 174.61, 0.06, 0.3, 0.11);
    });
  }
  // No iOS Safari support at all (silently a no-op there); Android needs a
  // real user gesture, which every call site here already has (an answer
  // tap, a celebration triggered by one). Not gated on soundEnabled --
  // muting sound effects isn't the same preference as wanting no vibration.
  function haptic(pattern) {
    try { if (navigator.vibrate) navigator.vibrate(pattern); } catch (e) { /* unsupported or blocked -- silently skip */ }
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
    he: [
      /Carmit.*(Enhanced|Premium)/i,
      /Carmit/i,
      /Google עברית/i,
      /Microsoft (Asaf|Avri).*(Natural|Online)/i,
    ],
    kk: [],
    // Mandarin (mainland) voices are widely available across platforms,
    // unlike Tajik/Kazakh -- ranked by typical naturalness. `.lang` prefix
    // matching ("zh") already covers zh-CN/zh-TW/zh-HK; the name patterns
    // below specifically favour mainland/Mandarin voices over Cantonese or
    // Taiwanese ones where a device offers a choice.
    zh: [
      // Edge's neural voices (Natural/Online) are meaningfully more natural-
      // sounding than Chrome's older Google Mandarin voice or the classic
      // Windows/macOS voices below, so they're ranked first when present.
      /Microsoft Xiaoxiao.*(Natural|Online)/i,
      /Microsoft Yunxi.*(Natural|Online)/i,
      /Microsoft Xiaoyi.*(Natural|Online)/i,
      /Google 普通话（中国大陆）/i,
      /Tingting/i,
      /Ting-Ting/i,
      /Microsoft Huihui/i,
    ],
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
  // Many mobile browsers (Android Chrome especially, but also iOS Safari on
  // a cold load) return an empty voice list on the first synchronous
  // getVoices() call and never reliably fire onvoiceschanged (a long-standing
  // Chromium bug) — unlike most desktop browsers, where onvoiceschanged
  // alone is enough. Poll for up to ~9s after each course load as a
  // cross-platform fallback so voices that load in late still get picked
  // up instead of leaving TTS permanently silent on some devices.
  let _voicePollAttempts = 0;
  function voicesReady() {
    if (!_preferredVoiceEn) return false;
    if (course && course.lang === "tg") return !!(_preferredVoiceTarget || _preferredVoiceFa);
    return !!_preferredVoiceTarget;
  }
  function pollVoicesUntilFound() {
    if (!("speechSynthesis" in window)) return;
    refreshVoices();
    if (voicesReady() || _voicePollAttempts >= 30) return;
    _voicePollAttempts++;
    setTimeout(pollVoicesUntilFound, 300);
  }
  const SPEECH_RATE = 0.85;
  const SPEECH_RATE_SLOW = 0.55;
  let _currentUtterance = null;
  let _speakToken = 0;
  // Pre-generated audio (currently only Uzbek): text -> {file, voice}, loaded
  // from the active course's audioManifest path if it declares one. Some
  // languages here (Uzbek, and previously Kazakh/Tajik) have no usable
  // browser speechSynthesis voice at all, so without bundled audio their
  // target-language text would simply never be spoken -- see resolveSpeech().
  let audioManifest = {};
  let _currentBundledAudio = null;
  function playBundledAudio(entry, onEnd, onError) {
    if (_currentBundledAudio) { _currentBundledAudio.pause(); _currentBundledAudio = null; }
    // Directory derived from the ACTIVE course's own audioManifest path
    // (e.g. "data/audio-avar/manifest.json" -> "data/audio-avar/"), not
    // hardcoded to Uzbek -- this used to always point at data/audio-uzbek/
    // regardless of which course was active, so Avar's real bundled audio
    // (data/audio-avar/, a separate set of files) silently 404'd every
    // time and was never actually heard.
    const meta = COURSES.find(c => c.id === activeCourseId);
    const dir = (meta && meta.audioManifest) ? meta.audioManifest.replace(/manifest\.json$/, "") : "data/audio-uzbek/";
    const url = `${dir}${entry.file}`;
    const audio = new Audio(url);
    _currentBundledAudio = audio;
    let settled = false;
    let retried = false;
    // A failed load fires BOTH the play() promise rejection AND the
    // element's own 'error' event for the same failure -- same pattern
    // (and same real-world "plays sometimes, not others" symptom) already
    // found and fixed in Wird's playAudio(). This used to treat ANY
    // failure identically to a real completion (settle() either way),
    // silently -- a caller relying on onError (wireAudioStage's listening
    // exercise, which shows a diagnostic message) never found out a
    // bundled-audio file failed to load at all.
    let handledThisAttempt = false;
    const settle = () => { if (settled) return; settled = true; if (onEnd) onEnd(); };
    function retryPlay() {
      handledThisAttempt = false;
      audio.load();
      audio.play().catch(handleError);
    }
    function handleError() {
      if (_currentBundledAudio !== audio || settled || handledThisAttempt) return;
      handledThisAttempt = true;
      if (!retried) {
        retried = true;
        setTimeout(() => { if (_currentBundledAudio === audio && !settled) retryPlay(); }, 500);
        return;
      }
      settled = true;
      if (onError) onError("bundled-audio-failed");
      else if (onEnd) onEnd();
    }
    audio.addEventListener("ended", settle, { once: true });
    audio.addEventListener("error", handleError);
    audio.play().catch(handleError);
  }
  function speak(text, voice, onEnd, rate, onError) {
    if (!soundEnabled) { if (onEnd) onEnd(); return; }
    // Only the normal rate has a bundled recording -- slow replay falls
    // through to speechSynthesis (silently doing nothing if there's no
    // voice either, same as before bundled audio existed).
    const bundled = (!rate || rate === SPEECH_RATE) && audioManifest[text];
    if (bundled) {
      if (window.speechSynthesis && (window.speechSynthesis.speaking || window.speechSynthesis.pending)) {
        window.speechSynthesis.cancel();
      }
      playBundledAudio(bundled, onEnd, onError);
      return;
    }
    if (!("speechSynthesis" in window) || !voice) { if (onEnd) onEnd(); return; }
    const token = ++_speakToken;
    let settled = false;
    try {
      // Calling cancel() immediately before speak() is a well-known iOS
      // Safari trap: the following speak() can get silently dropped. Only
      // cancel when something is actually queued/playing.
      if (window.speechSynthesis.speaking || window.speechSynthesis.pending) {
        window.speechSynthesis.cancel();
      }
      const u = new SpeechSynthesisUtterance(text);
      u.lang = voice.lang;
      u.voice = voice;
      u.rate = rate || SPEECH_RATE;
      u.onend = () => { settled = true; if (onEnd) onEnd(); };
      u.onerror = e => {
        settled = true;
        if (onError) onError((e && e.error) || "unknown");
        if (onEnd) onEnd();
      };
      _currentUtterance = u; // keep a live reference — some browsers silently
      // drop speech if the utterance is garbage-collected before it plays
      window.speechSynthesis.speak(u);
      // Some Android builds silently drop an utterance entirely — no error
      // event, no end event, nothing ever plays. A watchdog distinguishes
      // that "silent drop" case from a real, still-loading voice so the UI
      // can say something more useful than nothing happening at all.
      // Scaled to the utterance's own estimated length (same estimate the
      // feedback timer bar already uses, which bakes in a 1s buffer) rather
      // than a flat 4s -- a affected device used to stall for a full 4
      // seconds after even a two-word answer; short utterances now recover
      // much faster, longer ones still get proportionally more room.
      setTimeout(() => {
        if (settled || token !== _speakToken) return;
        if (onError) onError("silent-timeout");
        if (onEnd) onEnd();
      }, Math.max(1500, speechDurationMs(text)));
    } catch (e) {
      if (onError) onError(e.message || String(e));
      if (onEnd) onEnd();
    }
  }
  // Resolves what to actually speak for a target-language answer: the real
  // target voice+text if one exists (Arabic, or a Tajik voice on the rare
  // device that has one), else a Farsi voice reading ex.farsi if both are
  // available, else nothing.
  function resolveSpeech(isEnglish, text, ex) {
    // One last synchronous re-scan in case the background poll gave up
    // before this particular device finished loading its voice list.
    if (!_preferredVoiceEn && !_preferredVoiceTarget && !_preferredVoiceFa) refreshVoices();
    if (isEnglish) return _preferredVoiceEn ? { text, voice: _preferredVoiceEn } : null;
    if (_preferredVoiceTarget) return { text, voice: _preferredVoiceTarget };
    // No browser voice for this target language -- bundled audio (Uzbek)
    // still counts as speakable even with voice: null, since speak() checks
    // the manifest before it ever looks at the voice argument.
    if (audioManifest[text]) return { text, voice: null };
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
  // Chinese displays pinyin only (no Hanzi shown to the learner anywhere),
  // but a zh-CN voice fed literal pinyin text generally won't pronounce it
  // as real Mandarin -- it needs the actual Hanzi. Exercises for this course
  // carry a hidden Hanzi twin of whatever field is on screen, consulted only
  // here/in the audio-stage helpers below, never rendered to the DOM.
  function hanziIfChinese(pinyinText, hanziText) {
    return (course.lang === "zh" && hanziText) || pinyinText;
  }
  // Always surface the target-language (Arabic/Tajik/Chinese) text, never
  // English — the whole point of the audio is reinforcing target
  // pronunciation. Which field holds that text depends on direction: when
  // the target language is the shown prompt (${lang}-en), speak the prompt;
  // when it's the expected answer (en-${lang}), speak that. Comprehension
  // questions have no target-language text tied to the specific answer, so
  // they get no audio.
  function targetLangText(ex) {
    if (ex.type === "comprehension") return null;
    const targetIsPrompt = ex.direction === `${course.lang}-en`;
    if (ex.type === "word-bank") {
      return targetIsPrompt
        ? hanziIfChinese(ex.prompt, ex.promptHanzi)
        : hanziIfChinese(ex.answer.join(" "), ex.answerHanzi);
    }
    return targetIsPrompt
      ? hanziIfChinese(ex.prompt, ex.promptHanzi)
      : hanziIfChinese(ex.options[ex.answerIndex], ex.optionsHanzi && ex.optionsHanzi[ex.answerIndex]);
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

  // Merge, not overwrite: this ran as a flat overwrite for a while, which
  // meant every boot while signed in pulled whatever was in the cloud and
  // silently replaced local progress with it outright -- including
  // progress made THIS session that just hadn't reached the 800ms debounced
  // push yet (completing an exercise, then reloading or closing the tab
  // quickly, before it caught up), and any real progress made on a device
  // that had gone a while without syncing. Same reasoning as Wird's card
  // merge: keep whichever side represents more actual study investment,
  // never pick a side wholesale.
  function mergeProgress(local, remote) {
    if (!local) return remote;
    if (!remote) return local;
    const union = (a, b) => Array.from(new Set([...(a || []), ...(b || [])]));
    // toDateString() (e.g. "Mon Aug 09 2026") puts the weekday first, so
    // comparing those strings directly is not chronological order -- parse
    // back to real Date objects to find which side is actually more recent.
    const localTime = local.lastActiveDate ? new Date(local.lastActiveDate).getTime() : 0;
    const remoteTime = remote.lastActiveDate ? new Date(remote.lastActiveDate).getTime() : 0;
    // Base is remote-then-local (so any field neither of the two blocks
    // below knows about -- e.g. migratedSplitIdsV1, or anything added
    // later -- survives the merge instead of silently vanishing, with
    // local's own copy of it preferred when both sides have one) --
    // MAX_MISSED-capped 6 fields below then override with the real merge.
    return Object.assign({}, remote, local, {
      xp: Math.max(local.xp || 0, remote.xp || 0),
      streak: Math.max(local.streak || 0, remote.streak || 0),
      lastActiveDate: remoteTime > localTime ? remote.lastActiveDate : local.lastActiveDate,
      completedLessons: union(local.completedLessons, remote.completedLessons),
      // capped queue -- union first so nothing genuinely unresolved on
      // either side is lost, then trim from the front (oldest) same as
      // the live eviction in afterAnswer().
      missedBank: union(local.missedBank, remote.missedBank).slice(-MAX_MISSED),
      wordHoard: union(local.wordHoard, remote.wordHoard),
      celebratedLevels: union(local.celebratedLevels, remote.celebratedLevels),
    });
  }

  // Returns the number of courses written, or throws on invalid/unreadable input.
  function applyProgressPayload(payload) {
    if (!payload || typeof payload.courses !== "object") throw new Error("Not a valid sync payload");
    let count = 0;
    Object.keys(payload.courses).forEach(courseId => {
      let localCourse = null;
      try { localCourse = JSON.parse(localStorage.getItem(progressKeyFor(courseId)) || "null"); } catch (e) { /* corrupt local -- remote wins for this course */ }
      const merged = mergeProgress(localCourse, payload.courses[courseId]);
      localStorage.setItem(progressKeyFor(courseId), JSON.stringify(merged));
      count++;
    });
    return count;
  }

  const STREAK_MILESTONES = [3, 7, 14, 30, 50, 100, 200, 365];
  function updateStreakOnCompletion() {
    const today = new Date().toDateString();
    if (progress.lastActiveDate !== today) {
      const yesterday = new Date(Date.now() - 86400000).toDateString();
      progress.streak = progress.lastActiveDate === yesterday ? progress.streak + 1 : 1;
      progress.lastActiveDate = today;
      // The lastActiveDate guard above only lets this branch run once per
      // real calendar day, and streak either increments by exactly 1 or
      // resets to 1 -- so hitting an exact milestone value only ever
      // happens once per streak run, no separate "already shown" flag needed.
      if (STREAK_MILESTONES.includes(progress.streak)) showStreakMilestoneToast(progress.streak);
    }
    saveProgress();
  }
  // A brief, self-dismissing toast rather than a full modal -- a streak
  // milestone is a nice nudge, not something that should block the flow
  // back to the roadmap the way a level-complete celebration does.
  function showStreakMilestoneToast(days) {
    const toast = document.createElement("div");
    toast.className = "streak-toast";
    toast.innerHTML = `<span class="streak-toast-flame">🔥</span><span class="streak-toast-text"><b>${days}-day streak!</b> Keep it going.</span>`;
    document.body.appendChild(toast);
    haptic([15, 30, 15]);
    requestAnimationFrame(() => toast.classList.add("show"));
    setTimeout(() => {
      toast.classList.remove("show");
      setTimeout(() => toast.remove(), 400);
    }, 3200);
  }

  // Animates every [data-count] element's textContent from 0 up to its
  // target integer -- purely decorative, so a reduced-motion preference
  // just snaps straight to the final value instead of skipping it.
  function animateCountUps(container) {
    const els = container.querySelectorAll("[data-count]");
    const reduce = window.matchMedia && window.matchMedia("(prefers-reduced-motion: reduce)").matches;
    els.forEach(el => {
      const target = Number(el.dataset.count) || 0;
      if (reduce || target === 0) { el.textContent = target; return; }
      const duration = Math.min(900, 250 + target * 12);
      const start = performance.now();
      function tick(now) {
        const p = Math.min(1, (now - start) / duration);
        const eased = 1 - Math.pow(1 - p, 3);
        el.textContent = Math.round(eased * target);
        if (p < 1) requestAnimationFrame(tick);
      }
      requestAnimationFrame(tick);
    });
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

  // Lessons with 25 exercises were split into shorter "-p1"/"-p2" parts
  // (12/13 exercises each), which changes their id. A learner's
  // completedLessons list still has the old, now-nonexistent ids, so every
  // one of those lessons silently reads as "not done" — worse, since this
  // course unlocks sequentially, everything after the first broken id also
  // reads as locked and the roadmap looks reset. This recovers it: any old
  // id that isn't in the current course but has a "-p1"/"-p2" descendant
  // gets replaced by that descendant, crediting the learner for what they
  // already finished. Runs once per course (flagged), then saves.
  function migrateSplitLessonIds() {
    if (progress.migratedSplitIdsV1) return;
    const allIds = new Set(flatLessons.map(l => l.id));
    const migrated = [];
    (progress.completedLessons || []).forEach(oldId => {
      if (allIds.has(oldId)) { migrated.push(oldId); return; }
      const p1 = `${oldId}-p1`, p2 = `${oldId}-p2`;
      if (allIds.has(p1)) migrated.push(p1);
      if (allIds.has(p2)) migrated.push(p2);
    });
    progress.completedLessons = Array.from(new Set(migrated));
    progress.migratedSplitIdsV1 = true;
    saveProgress();
  }

  // ---------- boot ----------
  async function loadCourseData(courseId) {
    const meta = COURSES.find(c => c.id === courseId) || COURSES[0];
    const bust = `v=${DATA_VERSION}`;
    const withVersion = url => url + (url.includes("?") ? "&" : "?") + bust;
    const [res, manifestRes] = await Promise.all([
      fetch(withVersion(meta.file), { cache: "no-cache" }),
      meta.audioManifest ? fetch(withVersion(meta.audioManifest), { cache: "no-cache" }).catch(() => null) : Promise.resolve(null),
    ]);
    if (!res.ok) throw new Error("Failed to load course data");
    const data = await res.json();
    course = data.course;
    course.id = meta.id;
    if (manifestRes && manifestRes.ok) {
      try { audioManifest = await manifestRes.json(); } catch (e) { audioManifest = {}; }
    } else {
      audioManifest = {};
    }
    _voicePollAttempts = 0;
    pollVoicesUntilFound();

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
    const courseToggleLabel = document.getElementById("courseToggleLabel");
    if (courseToggleLabel) courseToggleLabel.textContent = course.flag || course.languageName || course.id;
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
    migrateSplitLessonIds();
    refreshTopStats();
    renderHome();
  }

  // Pulls the cloud copy and merges it into local progress for every
  // course. Shared by boot() (runs once automatically) and the "Sync now"
  // button, which exists because a device only ever auto-pulls once, at
  // boot -- progress made on another device afterward never shows up here
  // until either a full reload or an explicit manual sync.
  async function syncFromCloud() {
    if (!(window.CloudSync && window.CloudSync.user)) return { found: false };
    const remote = await window.CloudSync.pullProgress();
    let found = false, lessonsInCloud = 0;
    if (remote && remote.courses) {
      found = true;
      lessonsInCloud = Object.keys(remote.courses)
        .reduce((n, id) => n + ((remote.courses[id].completedLessons || []).length), 0);
      applyProgressPayload(remote);
      progress = loadProgress();
    }
    // Always push the merged result back up, not only when the cloud had
    // nothing at all. A cloud document can exist with a courses object
    // that's empty or missing this course entirely (e.g. a push from this
    // account genuinely never landed) -- pulling alone would silently
    // leave that gap in place until the next lesson happens to trigger a
    // save, which is exactly the state a "Sync now" tap is supposed to fix
    // immediately.
    //
    // Awaited (not fire-and-forget): a caller reporting "uploaded" to the
    // user needs that to mean the write actually happened, not just that
    // it was scheduled -- the previous version said "uploaded too" the
    // instant the debounced write was queued, which could show success
    // right before that same write silently failed 800ms later.
    await window.CloudSync.pushProgressNow(buildProgressPayload());
    return { found, lessonsInCloud };
  }

  async function boot() {
    await loadCourseData(activeCourseId);
    progress = loadProgress();
    if (window.CloudSync && window.CloudSync.user) {
      try { await syncFromCloud(); } catch (e) { /* offline — continue with local progress */ }
    }
    migrateSplitLessonIds();
    refreshTopStats();
    updateSoundToggleUI();
    renderHome();
    wireGlobalUi();
  }

  // Reads a course's saved progress straight from localStorage without
  // switching to it or loading its (potentially uncached) course JSON --
  // the course picker needs this for every course at once just to render,
  // so it has to stay cheap. Returns null for a course that's never been
  // opened (no progress key written yet) so the caller can show "Not
  // started" instead of a misleading "0 lessons".
  function readCourseStats(courseId) {
    try {
      const raw = localStorage.getItem(progressKeyFor(courseId));
      if (!raw) return null;
      const p = JSON.parse(raw);
      const lessonsDone = (p.completedLessons || []).length;
      if (lessonsDone === 0 && !(p.xp > 0)) return null;
      return { lessonsDone, streak: p.streak || 0, xp: p.xp || 0 };
    } catch (e) {
      return null; // corrupt entry for that course -- treat as not started
    }
  }

  const COURSE_SECTIONS = [
    { group: "established", title: "Languages" },
    { group: "underserved", title: "Underserved Languages" },
  ];

  function courseCardHtml(meta) {
    const s = meta.id === activeCourseId ? { lessonsDone: progress.completedLessons.length, streak: progress.streak, xp: progress.xp } : readCourseStats(meta.id);
    const statsHtml = s
      ? `<span class="course-card-stats">
          <span class="course-card-pill">${s.lessonsDone} lesson${s.lessonsDone === 1 ? "" : "s"}</span>
          <span class="course-card-pill">${s.xp} XP</span>
          ${s.streak > 0 ? `<span class="course-card-pill course-card-pill--streak">${s.streak}🔥</span>` : ""}
        </span>`
      : `<span class="course-card-empty">Not started — tap to begin</span>`;
    return `
      <button class="course-card course-card--${meta.accent} ${meta.id === activeCourseId ? "active" : ""}" data-course="${meta.id}">
        <span class="course-card-native" dir="auto">${meta.native}</span>
        <span class="course-card-en">${meta.en}</span>
        ${statsHtml}
      </button>
    `;
  }

  function renderCoursePicker() {
    const list = document.getElementById("courseList");
    list.innerHTML = COURSE_SECTIONS.map(sec => {
      const courses = COURSES.filter(c => c.group === sec.group);
      if (!courses.length) return "";
      return `
        <section class="course-section">
          <h4 class="course-section-title">${sec.title}</h4>
          <div class="course-grid">${courses.map(courseCardHtml).join("")}</div>
        </section>
      `;
    }).join("");
    list.querySelectorAll(".course-card").forEach(btn => {
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
    // Disabled for now -- navigator.onLine was flagging false positives.
    // wireOfflineIndicator();
    wirePullToRefresh();
    const testSoundBtn = document.getElementById("testSoundBtn");
    if (testSoundBtn) {
      testSoundBtn.addEventListener("click", () => {
        playCorrectSound();
        setTimeout(() => {
          const diagEl = document.getElementById("audioDiagnostic");
          if (!diagEl) return;
          if (_lastAudioError) {
            diagEl.textContent = `Playback error: ${_lastAudioError}`;
            return;
          }
          // On iPhone/iPad, the physical silent switch mutes generated sound
          // effects like this one (a real iOS behavior, not a bug) — but not
          // spoken audio, which is why voice playback still works either way.
          diagEl.textContent = "If you didn't hear it: on iPhone/iPad, check the side silent-mode switch — it mutes short sound effects, though voice playback still works either way.";
        }, 250);
      });
    }

    const syncNowBtn = document.getElementById("syncNowBtn");
    const syncStatusEl = document.getElementById("syncStatus");
    if (syncNowBtn) {
      syncNowBtn.addEventListener("click", async () => {
        if (!(window.CloudSync && window.CloudSync.user)) {
          if (syncStatusEl) syncStatusEl.textContent = "Not signed in.";
          return;
        }
        syncNowBtn.disabled = true;
        if (syncStatusEl) syncStatusEl.textContent = "Syncing…";
        try {
          const result = await syncFromCloud();
          refreshTopStats();
          renderHome();
          if (syncStatusEl) {
            syncStatusEl.textContent = result.found
              ? `Synced — found ${result.lessonsInCloud} completed lesson(s) in the cloud; this device's progress was uploaded too.`
              : "The cloud had no saved progress for this account — this device's progress was uploaded.";
          }
        } catch (e) {
          // Show the real reason (e.g. Firestore's own error code, like
          // "permission-denied") instead of a generic guess -- a security
          // rules problem and a network blip look identical to the user
          // otherwise, and only one of them is fixed by "try again later".
          if (syncStatusEl) syncStatusEl.textContent = `Sync failed: ${(e && (e.code || e.message)) || "unknown error"}`;
        } finally {
          syncNowBtn.disabled = false;
        }
      });
    }

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
      // Starts at height:0 -- growGrowthWaveform() below animates each bar
      // up to its real data-h shortly after mount, using the height
      // transition .waveform .bar already has for its progress-color
      // change, just triggered on mount instead.
      html += `<div class="bar${i < filled ? " filled" : ""}" data-h="${h}" style="height:0"></div>`;
    }
    return html;
  }
  // Staggers each bar's grow-in so the waveform sweeps up left-to-right
  // rather than popping in all at once. Skipped under reduced-motion --
  // bars just render at their real height immediately in that case, since
  // the inline height:0 from waveformBars() would otherwise leave them
  // permanently flat.
  function growWaveform(container) {
    const bars = container.querySelectorAll(".waveform .bar");
    const reduce = window.matchMedia && window.matchMedia("(prefers-reduced-motion: reduce)").matches;
    bars.forEach((bar, i) => {
      if (reduce) { bar.style.height = bar.dataset.h + "px"; return; }
      setTimeout(() => { bar.style.height = bar.dataset.h + "px"; }, 20 + i * 22);
    });
  }

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

  // Scoped to the roadmap and the lesson-summary screen only -- the actual
  // per-exercise re-renders inside a lesson happen every ~1-2 seconds and
  // already have their own feedback-state animation, so fading the whole
  // screen on every one of those would be noisy rather than smooth.
  function applyScreenFadeIn() {
    screenEl.classList.remove("screen-fade-in");
    void screenEl.offsetWidth;
    screenEl.classList.add("screen-fade-in");
  }

  // currentColor so each icon automatically matches its node's own state
  // color (ink-soft when locked, maroon when unlocked, the paper tone when
  // done-on-gold-fill) without needing a separate CSS rule per state.
  const TRAIL_ICON_LOCK = `<svg viewBox="0 0 24 24" width="19" height="19" aria-hidden="true"><rect x="5" y="11" width="14" height="9" rx="2.2" fill="none" stroke="currentColor" stroke-width="1.8"/><path d="M8 11V7.6a4 4 0 018 0V11" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round"/></svg>`;
  const TRAIL_ICON_CHECK = `<svg viewBox="0 0 24 24" width="23" height="23" aria-hidden="true"><path d="M5 12.5l4.3 4.3L19 7" fill="none" stroke="currentColor" stroke-width="2.6" stroke-linecap="round" stroke-linejoin="round"/></svg>`;
  const TRAIL_ICON_FLAG = `<svg viewBox="0 0 24 24" width="22" height="22" aria-hidden="true"><path d="M6.5 3v18" stroke="currentColor" stroke-width="1.8" stroke-linecap="round"/><path d="M6.5 4.2h10.5l-2.8 3.8 2.8 3.8H6.5z" fill="currentColor" opacity="0.9"/></svg>`;
  const TRAIL_ICON_TROPHY = `<svg viewBox="0 0 24 24" width="14" height="14" aria-hidden="true" style="vertical-align:-2px"><path d="M7 4h10v4a5 5 0 01-10 0V4z" fill="none" stroke="currentColor" stroke-width="1.6"/><path d="M7 5H4v1.5A3.5 3.5 0 007.5 10M17 5h3v1.5A3.5 3.5 0 0116.5 10" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round"/><path d="M12 12.5v3M9 19h6M10 19c-.3-1.5-.3-2.3 0-3.5M14 19c.3-1.5.3-2.3 0-3.5" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round"/></svg>`;

  // A book, not a game board: instead of a path of circles to climb, the
  // level opens on a "continue reading" hero for wherever you actually
  // are, with the rest of the chapter laid out below as a real table of
  // contents -- numbered, titled, a status mark per row, nothing to
  // navigate along. Replaces the old circle-and-rail trail entirely.
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

    // Every completed level gets its one-time confetti celebration (see
    // checkLevelComplete/showLevelCompleteCelebration), but that moment
    // passes and progress.celebratedLevels was never shown anywhere again
    // afterward -- no way to look back at what you'd actually finished.
    const trophyLevels = (progress.celebratedLevels || [])
      .map(id => course.levels.find(lv => lv.id === id))
      .filter(Boolean);

    let currentLesson = null;
    for (const lesson of levelLessons) {
      const flatIndex = flatLessons.indexOf(lesson);
      const done = progress.completedLessons.includes(lesson.id);
      if (!done && isLessonUnlocked(flatIndex)) { currentLesson = lesson; break; }
    }

    let heroHtml = "";
    if (currentLesson) {
      heroHtml = `
        <div class="chapter-hero">
          <div class="chapter-hero-eyebrow">Continue where you left off</div>
          <div class="chapter-hero-main">
            <div class="chapter-hero-num">${currentLesson.number}</div>
            <div class="chapter-hero-text">
              <h3>${currentLesson.title}</h3>
              ${currentLesson.titleNative ? `<span class="chapter-hero-native" dir="auto">${currentLesson.titleNative}</span>` : ""}
            </div>
          </div>
          <button class="btn btn-primary btn-block" id="heroStartBtn" data-lesson="${currentLesson.id}">Begin Lesson</button>
        </div>
      `;
    } else if (levelComplete) {
      heroHtml = `
        <div class="chapter-hero chapter-hero--complete">
          <div class="chapter-hero-eyebrow">Chapter complete</div>
          <div class="chapter-hero-main">
            <div class="chapter-hero-num">${TRAIL_ICON_FLAG}</div>
            <div class="chapter-hero-text">
              <h3>Every lesson here is finished.</h3>
              ${nextLevel ? `<span class="chapter-hero-native">Onward to ${nextLevel.cefr} — ${nextLevel.label}</span>` : `<span class="chapter-hero-native">More chapters are on the way.</span>`}
            </div>
          </div>
          ${nextLevel ? `<button class="btn btn-primary btn-block" id="heroNextLevelBtn">Start ${nextLevel.cefr}</button>` : ""}
        </div>
      `;
    }

    const indexRowsHtml = levelLessons.map(lesson => {
      const flatIndex = flatLessons.indexOf(lesson);
      const unlocked = isLessonUnlocked(flatIndex);
      const done = progress.completedLessons.includes(lesson.id);
      const isCurrent = !!currentLesson && lesson.id === currentLesson.id;
      const stateClass = done ? "done" : isCurrent ? "current" : unlocked ? "unlocked" : "locked";
      const status = done ? TRAIL_ICON_CHECK : isCurrent ? `<span class="index-dot"></span>` : !unlocked ? TRAIL_ICON_LOCK : "";
      return `
        <button class="chapter-index-row ${stateClass}" data-lesson="${lesson.id}" ${unlocked ? "" : "disabled"}>
          <span class="index-num">${lesson.number}</span>
          <span class="index-text"><span class="index-title">${lesson.title}</span><span class="index-native" dir="auto">${lesson.titleNative || ""}</span></span>
          <span class="index-status">${status}</span>
        </button>
      `;
    }).join("");

    screenEl.innerHTML = `
      <div class="level-progress-card">
        <div class="waveform">${waveformBars(overallPct)}</div>
        <div class="level-progress-info">
          <div class="pct"><b data-count="${overallPct}">0</b>%</div>
          <div class="label">Overall progress</div>
          <div class="count">${doneLessons} / ${totalLessons} lessons</div>
        </div>
      </div>
      ${trophyLevels.length ? `
        <div class="level-trophies">
          ${trophyLevels.map(lv => `<button class="level-trophy" data-level="${lv.id}" title="${lv.label}${lv.labelNative ? ` · ${lv.labelNative}` : ""} — completed">${TRAIL_ICON_TROPHY} ${lv.cefr}</button>`).join("")}
        </div>
      ` : ""}
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
        : `${heroHtml}
           <div class="chapter-index-wrap">
             <div class="chapter-index-label">Full index &middot; ${level.cefr}</div>
             <div class="chapter-index">${indexRowsHtml}</div>
           </div>`
      }
    `;
    applyScreenFadeIn();
    growWaveform(screenEl);
    animateCountUps(screenEl);

    document.querySelectorAll(".level-trophy").forEach(btn => {
      btn.addEventListener("click", () => { currentLevelId = btn.dataset.level; renderLevelRoadmap(); });
    });
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
    const heroNextLevelBtn = document.getElementById("heroNextLevelBtn");
    if (heroNextLevelBtn) {
      heroNextLevelBtn.addEventListener("click", () => {
        if (!nextLevel) return;
        currentLevelId = nextLevel.id;
        renderLevelRoadmap();
      });
    }
    const heroStartBtn = document.getElementById("heroStartBtn");
    if (heroStartBtn) {
      heroStartBtn.addEventListener("click", () => {
        const lesson = flatLessons.find(l => l.id === heroStartBtn.dataset.lesson);
        if (lesson) startLesson(lesson);
      });
    }
    screenEl.querySelectorAll(".chapter-index-row:not(:disabled)").forEach(row => {
      row.addEventListener("click", () => {
        const lesson = flatLessons.find(l => l.id === row.dataset.lesson);
        if (lesson) startLesson(lesson);
      });
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
    if (_passagePlaying) {
      _passageToken++;
      window.speechSynthesis.cancel();
      _passagePlaying = false;
    }
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
      if (_passagePlaying) { _passageToken++; window.speechSynthesis.cancel(); _passagePlaying = false; }
      session = null;
      renderHome();
    });
  }

  // The global 1-4 number-key shortcut (picks the Nth .options .option --
  // see wireGlobalUi's keydown handler) had no visible hint anywhere.
  // Hidden on touch-only devices via the same hover:hover+pointer:fine
  // gate Wird uses for its own arrow-key hint.
  function kbdHintHtml() {
    return `<div class="kbd-hint"><kbd>1</kbd><kbd>2</kbd><kbd>3</kbd><kbd>4</kbd> to pick &nbsp;&middot;&nbsp; <kbd>&crarr;</kbd> to continue</div>`;
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
    const rows = lesson.readingPassage.paragraphs.map((p, i) => `
      <div class="passage-line" data-line="${i}">
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
        <div class="passage-controls">
          <button class="translit-toggle" id="passageToggle">Show English</button>
          <button class="passage-listen-btn" id="passageListenBtn" title="Listen to the passage" aria-label="Listen to the passage">🔊 Listen</button>
        </div>
        <p class="audio-diag hidden" id="passageAudioDiag"></p>
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

  let _passagePlaying = false;
  let _passageToken = 0;
  // iOS/Safari's SpeechSynthesis can fire onend/onerror twice — or early —
  // for the same utterance, and calling speak() again while the previous
  // one is still technically "speaking" can silently cut it off. A plain
  // recursive onend->speak() chain is therefore not reliable for reading
  // several paragraphs in strict order: duplicate/early events double-
  // advance the index and paragraphs end up skipped or overlapping.
  // Fix: a session token invalidates any callback from a stopped/replaced
  // chain, a per-step "already advanced" guard absorbs duplicate end
  // events, and a small gap between utterances avoids WebKit's glitch
  // when speak() is called immediately from inside another onend.
  function wirePassageListen() {
    const btn = document.getElementById("passageListenBtn");
    if (!btn) return;
    const diagEl = document.getElementById("passageAudioDiag");
    const lesson = currentExercise()._sourceLesson || session.lesson;
    if (!lesson.readingPassage) return;
    const paragraphs = lesson.readingPassage.paragraphs;
    const lineEls = Array.from(document.querySelectorAll(".passage-line"));
    btn.addEventListener("click", () => {
      if (_passagePlaying) {
        _passageToken++;
        window.speechSynthesis.cancel();
        _passagePlaying = false;
        btn.textContent = "🔊 Listen";
        lineEls.forEach(l => l.classList.remove("speaking"));
        return;
      }
      // Reading passages are shown in the target language (Arabic/Tajik) —
      // the audio must match, so this speaks .native with the course's own
      // target-language voice, not the English translation with an English
      // voice. (Tajik has no usable TTS voice at all — a known, accepted
      // platform limitation — so _preferredVoiceTarget stays null there and
      // the button simply does nothing, same as everywhere else in the app.)
      // One last synchronous re-scan in case the background poll gave up
      // before this particular device finished loading its voice list.
      if (!_preferredVoiceTarget) refreshVoices();
      if (!_preferredVoiceTarget) { showAudioDiag(diagEl, "no-voice"); return; }
      if (!soundEnabled) return;
      if (diagEl) diagEl.classList.add("hidden");
      window.speechSynthesis.cancel();
      _passagePlaying = true;
      btn.textContent = "⏹ Stop";
      const token = ++_passageToken;
      let i = 0;
      function step() {
        if (token !== _passageToken || i >= paragraphs.length) {
          if (token === _passageToken) { _passagePlaying = false; btn.textContent = "🔊 Listen"; }
          lineEls.forEach(l => l.classList.remove("speaking"));
          return;
        }
        lineEls.forEach(l => l.classList.remove("speaking"));
        if (lineEls[i]) lineEls[i].classList.add("speaking");
        // Chinese displays pinyin-only text in .native (no Hanzi shown to
        // the learner), but a zh-CN voice needs real Hanzi to pronounce
        // Mandarin correctly -- fall back to a parallel hidden field.
        const speakText = (course.lang === "zh" && paragraphs[i].nativeHanzi) || paragraphs[i].native;
        const u = new SpeechSynthesisUtterance(speakText);
        u.lang = _preferredVoiceTarget.lang;
        u.voice = _preferredVoiceTarget;
        u.rate = SPEECH_RATE;
        let advanced = false;
        function advance() {
          if (advanced || token !== _passageToken) return;
          advanced = true;
          i++;
          setTimeout(step, 150);
        }
        u.onend = advance;
        u.onerror = e => {
          if (i === 0) showAudioDiag(diagEl, (e && e.error) || "unknown");
          advance();
        };
        window.speechSynthesis.speak(u);
        // Same silent-drop watchdog as speak(): some Android builds never
        // fire onend/onerror at all when playback fails, so the passage
        // would otherwise just hang on the first line forever. Scaled to
        // this paragraph's own estimated length (same fix speak() already
        // got in "Scale the speechSynthesis silent-drop watchdog to the
        // utterance's own length instead of a flat 4s") -- this second,
        // independent implementation never got that same fix, so any
        // paragraph whose real speech took longer than a flat 4s had its
        // watchdog fire mid-sentence: it force-advanced the line index and
        // the "speaking" highlight to the NEXT paragraph while THIS one's
        // utterance was still actually playing (nothing here calls
        // .cancel() before the next speak()), so the highlighted line and
        // the audio you actually heard fell out of sync -- exactly the
        // "the highlight doesn't always work" symptom.
        setTimeout(() => {
          if (advanced || token !== _passageToken) return;
          if (i === 0) showAudioDiag(diagEl, "silent-timeout");
          advance();
        }, Math.max(1500, speechDurationMs(speakText)));
      }
      step();
    });
  }

  function grammarPanel() {
    const lesson = currentExercise()._sourceLesson || session.lesson;
    const topic = lesson.topicId && course.grammarTopics[lesson.topicId];
    if (!topic) return "";
    return `
      <details class="grammar-panel">
        <summary>Grammar note <span class="ar">${(course.uiStrings && course.uiStrings.grammarNote) || ""}</span></summary>
        <h4>${topic.title}</h4>
        <p class="grammar-pattern">${topic.pattern}</p>
        <p class="grammar-explanation">${topic.explanation}</p>
        <div class="fact-box">
          <span class="fact-label">Did you know? <span class="ar">${(course.uiStrings && course.uiStrings.didYouKnow) || ""}</span></span>
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
    if (ex.type === "listening") return renderListening(ex);
    if (ex.type === "listening-tap") return renderListeningTap(ex);
    if (ex.type === "fill-blank") return renderFillBlank(ex);
    if (ex.type === "matching") return renderMatching(ex);
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
    haptic(correct ? 12 : 35);
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
        ${kbdHintHtml()}
        <div id="feedbackSlot"></div>
      </div>
    `);
    wireTranslitToggle();
    wirePassageToggle();
    wirePassageListen();
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

  // ---- listening ----
  // A shared audio "stage": a big play button with pulsing rings that
  // animate only while the TTS is actually speaking (driven by speak()'s
  // real onEnd callback, not a fixed timer), plus a slow-motion (turtle)
  // replay for catching words you missed the first time.
  function audioStageHtml(big) {
    return `
      <div class="audio-stage${big ? " audio-stage-lg" : ""}">
        <button class="listen-play-btn" id="listenPlayBtn" type="button" aria-label="Listen">
          <span class="audio-rings"><span></span><span></span><span></span></span>
          <span class="audio-icon">🔊</span>
        </button>
        <button class="listen-slow-btn" id="listenSlowBtn" type="button" title="Slow" aria-label="Listen slowly">🐢</button>
      </div>
      <p class="audio-diag hidden" id="audioDiag"></p>
    `;
  }
  // Human-readable, actionable message per failure mode, so a device with
  // broken TTS shows something explainable instead of a button that just
  // silently does nothing.
  function audioDiagMessage(kind) {
    if (kind === "no-voice") {
      return "No Arabic voice found on this device. On Android: Settings → System → Languages & input → Text-to-speech output → (gear icon) → Install voice data → Arabic. Then reload this page.";
    }
    if (kind === "silent-timeout") {
      return "Nothing played. Your device lists an Arabic voice but its Text-to-Speech engine may not actually have the voice data installed — check Settings → Text-to-speech output → Install voice data.";
    }
    return `Playback error (${kind}). Try reloading the page, or check your phone's Text-to-Speech settings.`;
  }
  function showAudioDiag(el, kind) {
    if (!el) return;
    el.textContent = audioDiagMessage(kind);
    el.classList.remove("hidden");
  }
  function wireAudioStage(text) {
    const stage = document.querySelector(".audio-stage");
    const playBtn = document.getElementById("listenPlayBtn");
    const slowBtn = document.getElementById("listenSlowBtn");
    const diagEl = document.getElementById("audioDiag");
    function play(rate) {
      // One last synchronous re-scan in case the background poll gave up
      // before this particular device finished loading its voice list.
      if (!_preferredVoiceTarget) refreshVoices();
      // Bundled audio (Uzbek) is speakable even with no browser voice at
      // all -- speak() checks the manifest before it ever looks at the
      // voice argument, so only bail out here if neither exists.
      if (!_preferredVoiceTarget && !audioManifest[text]) { showAudioDiag(diagEl, "no-voice"); return; }
      if (diagEl) diagEl.classList.add("hidden");
      stage.classList.add("playing");
      speak(text, _preferredVoiceTarget, () => stage.classList.remove("playing"), rate,
        kind => showAudioDiag(diagEl, kind));
    }
    playBtn.addEventListener("click", () => play());
    slowBtn.addEventListener("click", () => play(SPEECH_RATE_SLOW));
    return play;
  }

  // Plays the target-language sentence and asks the learner to pick its
  // English meaning — multiple-choice rather than free-text, since typing
  // Arabic/Tajik script accurately isn't a reasonable ask for most learners.
  function renderListening(ex) {
    renderLessonChrome(`
      ${grammarPanel()}
      <div class="card">
        <p class="q-kicker">Listen and choose the meaning</p>
        ${audioStageHtml(true)}
        <button class="translit-toggle" id="listenRevealToggle">Show text</button>
        <p class="translit hidden" id="listenRevealText" dir="${course.dir}" lang="${course.lang}">${ex.native}</p>
        <div class="options">
          ${ex.options.map((opt, i) => `<button class="option" data-i="${i}">${opt}</button>`).join("")}
        </div>
        ${kbdHintHtml()}
        <div id="feedbackSlot"></div>
      </div>
    `);
    wireGrammarPanel();
    // Deliberately no autoplay: audio.play()/speechSynthesis.speak() called
    // from a setTimeout (i.e. outside the click that rendered this screen)
    // has no user gesture behind it, which iOS Safari in particular will
    // often silently refuse -- exactly the kind of "audio just doesn't
    // work" failure this app kept running into. The big audio-stage play
    // button is the real, reliable entry point; tapping it always works.
    wireAudioStage(hanziIfChinese(ex.native, ex.nativeHanzi));
    const revealToggle = document.getElementById("listenRevealToggle");
    revealToggle.addEventListener("click", () => {
      const t = document.getElementById("listenRevealText");
      t.classList.toggle("hidden");
      revealToggle.textContent = t.classList.contains("hidden") ? "Show text" : "Hide text";
    });

    const optionEls = Array.from(screenEl.querySelectorAll(".option"));
    optionEls.forEach(btn => {
      btn.addEventListener("click", () => {
        optionEls.forEach(b => b.disabled = true);
        const i = Number(btn.dataset.i);
        const correct = i === ex.answerIndex;
        btn.classList.add(correct ? "correct" : "incorrect");
        if (!correct) optionEls[ex.answerIndex].classList.add("correct");
        afterAnswer(correct);
        const fallback = correct ? ADVANCE_DELAY_CORRECT : ADVANCE_DELAY_WRONG;
        document.getElementById("feedbackSlot").innerHTML =
          renderFeedback(correct, `Correct answer: ${ex.options[ex.answerIndex]}`, { delay: fallback });
        scheduleAdvance(fallback);
      });
    });
  }

  // Hear the target-language sentence, then tap its own words (in the
  // target script) back into order — no text shown upfront. Unlike free
  // typing, tapping pre-existing tiles doesn't demand producing Arabic
  // script from scratch, just recognizing and sequencing what was heard.
  function renderListeningTap(ex) {
    const bank = shuffled(ex.answer.map((word, i) => ({ id: i, word })));
    const placedOrder = [];
    let evalTimer = null;

    renderLessonChrome(`
      ${grammarPanel()}
      <div class="card">
        <p class="q-kicker">Listen and tap the words in order</p>
        ${audioStageHtml(false)}
        <div class="bank-target" id="bankTarget"></div>
        <div class="bank-pool" id="bankPool">
          ${bank.map(t => `<button class="tile" data-id="${t.id}">${t.word}</button>`).join("")}
        </div>
        <div id="feedbackSlot"></div>
      </div>
    `);
    wireGrammarPanel();
    // No autoplay here either -- see the matching note in renderListening().
    wireAudioStage(hanziIfChinese(ex.native, ex.nativeHanzi));

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
      targetBtn.textContent = bank.find(t => t.id === id).word;
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
      const words = placedOrder.map(id => bank.find(t => t.id === id).word);
      const correct = words.length === ex.answer.length && words.every((w, i) => w === ex.answer[i]);
      poolTileEls.forEach(b => b.disabled = true);
      targetEl.querySelectorAll(".tile").forEach(b => b.disabled = true);
      afterAnswer(correct);
      const fallback = correct ? ADVANCE_DELAY_CORRECT : ADVANCE_DELAY_WRONG;
      document.getElementById("feedbackSlot").innerHTML =
        renderFeedback(correct, `Correct order: ${ex.answer.join(" ")}`, { delay: fallback });
      scheduleAdvance(fallback);
    }
  }

  // ---- fill in the blank ----
  // Blanks stay on the English side even for the Arabic/Tajik courses —
  // blanking a single word out of vocalized Arabic/Tajik script reliably
  // is much harder to get right mechanically than English, and the native
  // sentence is still shown in full for context.
  function renderFillBlank(ex) {
    const options = shuffled(ex.options.slice());
    renderLessonChrome(`
      ${grammarPanel()}
      <div class="card">
        <p class="q-kicker">Fill in the blank</p>
        <p class="prompt-native" dir="${course.dir}" lang="${course.lang}">${ex.native}</p>
        <div class="fill-blank-sentence">${ex.blankedEn}</div>
        <div class="options">
          ${options.map(opt => `<button class="option" data-word="${opt}">${opt}</button>`).join("")}
        </div>
        ${kbdHintHtml()}
        <div id="feedbackSlot"></div>
      </div>
    `);
    wireGrammarPanel();
    const optionEls = Array.from(screenEl.querySelectorAll(".option"));
    optionEls.forEach(btn => {
      btn.addEventListener("click", () => {
        optionEls.forEach(b => b.disabled = true);
        const correct = btn.dataset.word === ex.answer;
        btn.classList.add(correct ? "correct" : "incorrect");
        if (!correct) optionEls.find(b => b.dataset.word === ex.answer).classList.add("correct");
        afterAnswer(correct);
        const fallback = correct ? ADVANCE_DELAY_CORRECT : ADVANCE_DELAY_WRONG;
        document.getElementById("feedbackSlot").innerHTML =
          renderFeedback(correct, `Correct answer: ${ex.answer}`, { delay: fallback });
        scheduleAdvance(fallback);
      });
    });
  }

  // ---- matching pairs ----
  function renderMatching(ex) {
    const leftOrder = shuffled(ex.pairs.map((p, i) => i));
    const rightOrder = shuffled(ex.pairs.map((p, i) => i));
    renderLessonChrome(`
      <div class="card">
        <p class="q-kicker">Match the pairs</p>
        <div class="matching-grid">
          <div class="matching-col" id="matchLeft" dir="${course.dir}">
            ${leftOrder.map(i => `<button class="match-card" data-i="${i}" data-side="native" lang="${course.lang}">${ex.pairs[i].native}</button>`).join("")}
          </div>
          <div class="matching-col" id="matchRight">
            ${rightOrder.map(i => `<button class="match-card" data-i="${i}" data-side="en">${ex.pairs[i].en}</button>`).join("")}
          </div>
        </div>
      </div>
    `);
    let selectedLeft = null, selectedRight = null, matchedCount = 0, mistakes = 0;
    const total = ex.pairs.length;
    function tryMatch() {
      if (selectedLeft === null || selectedRight === null) return;
      const leftBtn = document.querySelector(`.match-card[data-side="native"][data-i="${selectedLeft}"]`);
      const rightBtn = document.querySelector(`.match-card[data-side="en"][data-i="${selectedRight}"]`);
      if (selectedLeft === selectedRight) {
        leftBtn.classList.add("matched");
        rightBtn.classList.add("matched");
        leftBtn.disabled = true;
        rightBtn.disabled = true;
        matchedCount++;
        if (matchedCount === total) {
          const correct = mistakes === 0;
          afterAnswer(correct);
          screenEl.insertAdjacentHTML("beforeend", renderFeedback(correct, "All pairs matched", { delay: correct ? ADVANCE_DELAY_CORRECT : ADVANCE_DELAY_WRONG }));
          scheduleAdvance(correct ? ADVANCE_DELAY_CORRECT : ADVANCE_DELAY_WRONG);
        }
      } else {
        mistakes++;
        [leftBtn, rightBtn].forEach(b => { b.classList.add("mismatch"); setTimeout(() => b.classList.remove("mismatch"), 350); });
      }
      selectedLeft = null; selectedRight = null;
      document.querySelectorAll(".match-card.selected").forEach(b => b.classList.remove("selected"));
    }
    document.querySelectorAll('.match-card[data-side="native"]').forEach(btn => {
      btn.addEventListener("click", () => {
        document.querySelectorAll('.match-card[data-side="native"]').forEach(b => b.classList.remove("selected"));
        btn.classList.add("selected");
        selectedLeft = Number(btn.dataset.i);
        tryMatch();
      });
    });
    document.querySelectorAll('.match-card[data-side="en"]').forEach(btn => {
      btn.addEventListener("click", () => {
        document.querySelectorAll('.match-card[data-side="en"]').forEach(b => b.classList.remove("selected"));
        btn.classList.add("selected");
        selectedRight = Number(btn.dataset.i);
        tryMatch();
      });
    });
  }

  // ---------- SUMMARY / FAIL ----------
  function renderSummary() {
    const perfect = session.mistakes === 0;
    const xpEarned = 10 + (perfect ? 5 : 0);
    // XP/streak/completedLessons are awarded as a side effect of
    // rendering, not from a single guarded call site -- renderExercise()
    // reaches this function every time its queue is empty, and while every
    // path that could plausibly call it twice for the same session (the
    // Enter-key skip-advance shortcut in particular) already appears
    // self-guarded by advanceTimer's own truthiness check, this flag makes
    // double-awarding structurally impossible regardless, rather than
    // relying on every future code path continuing to get that guard
    // right on its own.
    let justCompletedLevelId = null;
    if (!session.summarized) {
      session.summarized = true;
      progress.xp += xpEarned;
      if (session.mode === "lesson" && !progress.completedLessons.includes(session.lesson.id)) {
        progress.completedLessons.push(session.lesson.id);
        justCompletedLevelId = checkLevelComplete(session.lesson.levelId);
      }
      updateStreakOnCompletion();
      refreshTopStats();
    }

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
          <div class="stat-block"><span class="num">+<b data-count="${xpEarned}">0</b></span><span class="lbl">XP</span></div>
          <div class="stat-block"><span class="num"><b data-count="${session.mistakes}">0</b></span><span class="lbl">Mistakes</span></div>
          <div class="stat-block"><span class="num"><b data-count="${progress.streak}">0</b></span><span class="lbl">Day streak</span></div>
        </div>
        <button class="btn btn-primary" id="continueHome">Continue</button>
      </div>
    `;
    animateCountUps(screenEl);
    document.getElementById("continueHome").addEventListener("click", () => {
      session = null;
      renderHome();
    });
    if (justCompletedLevelId) showLevelCompleteCelebration(justCompletedLevelId);
  }

  // Fires once the first time every lesson in a level is completed (never
  // again for that level -- see progress.celebratedLevels below). Returns
  // the level's id if this lesson was genuinely the one that finished it,
  // so the caller can show the celebration overlay -- or null otherwise,
  // covering both "this level was already complete/celebrated" and "this
  // lesson wasn't the last one needed".
  function checkLevelComplete(levelId) {
    if (!levelId) return null;
    progress.celebratedLevels = progress.celebratedLevels || [];
    if (progress.celebratedLevels.includes(levelId)) return null;
    const levelLessons = flatLessons.filter(l => l.levelId === levelId);
    if (!levelLessons.length) return null;
    if (!levelLessons.every(l => progress.completedLessons.includes(l.id))) return null;
    progress.celebratedLevels.push(levelId);
    return levelId;
  }

  // Same one-shot canvas confetti approach as Wird's achievement overlay
  // (this app's sibling, same zero-dependency/no-build-step philosophy) --
  // ported rather than shared since the two apps don't share any code.
  function fireConfetti() {
    if (window.matchMedia && window.matchMedia("(prefers-reduced-motion: reduce)").matches) return;
    const canvas = document.createElement("canvas");
    canvas.className = "confetti-canvas";
    canvas.width = window.innerWidth;
    canvas.height = window.innerHeight;
    document.body.appendChild(canvas);
    const ctx = canvas.getContext("2d");
    if (!ctx) { canvas.remove(); return; }
    const colors = ["#b8901f", "#d6ac33", "#7a1f2b", "#2f6f63", "#6cc0ae"];
    const particles = Array.from({ length: 70 }, () => ({
      x: canvas.width / 2 + (Math.random() - 0.5) * 140,
      y: canvas.height * 0.32 + (Math.random() - 0.5) * 40,
      vx: (Math.random() - 0.5) * 9,
      vy: -Math.random() * 9 - 4,
      size: 4 + Math.random() * 4,
      color: colors[Math.floor(Math.random() * colors.length)],
      rot: Math.random() * Math.PI * 2,
      vrot: (Math.random() - 0.5) * 0.3,
    }));
    const gravity = 0.28;
    const duration = 1700;
    const start = performance.now();
    function frame(now) {
      const elapsed = now - start;
      ctx.clearRect(0, 0, canvas.width, canvas.height);
      particles.forEach(p => {
        p.vy += gravity;
        p.x += p.vx;
        p.y += p.vy;
        p.rot += p.vrot;
        ctx.save();
        ctx.translate(p.x, p.y);
        ctx.rotate(p.rot);
        ctx.fillStyle = p.color;
        ctx.globalAlpha = Math.max(0, 1 - elapsed / duration);
        ctx.fillRect(-p.size / 2, -p.size / 2, p.size, p.size * 0.6);
        ctx.restore();
      });
      if (elapsed < duration) requestAnimationFrame(frame);
      else canvas.remove();
    }
    requestAnimationFrame(frame);
  }

  function showLevelCompleteCelebration(levelId) {
    const level = course.levels.find(lv => lv.id === levelId);
    if (!level) return;
    const modal = document.getElementById("levelCompleteModal");
    if (!modal) return;
    const levelLessons = flatLessons.filter(l => l.levelId === levelId);
    document.getElementById("levelCompleteBadge").textContent = level.cefr;
    document.getElementById("levelCompleteTitle").textContent = "Level Complete";
    document.getElementById("levelCompleteSub").textContent =
      `${level.label}${level.labelNative ? ` · ${level.labelNative}` : ""} — ${levelLessons.length} lessons, done.`;
    modal.classList.remove("hidden");
    fireConfetti();
    haptic([20, 40, 20, 40, 40]);
    const closeBtn = document.getElementById("levelCompleteCloseBtn");
    const close = () => modal.classList.add("hidden");
    closeBtn.onclick = close;
    modal.onclick = e => { if (e.target === modal) close(); };
  }

  window.__appReady = boot;
})();
