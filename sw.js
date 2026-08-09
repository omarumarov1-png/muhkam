// sw.js — Muḥkam service worker.
//
// Cache-first for the app shell (so the installed PWA opens with zero
// network), plus runtime caching for course data and audio -- so a course
// the user has already opened while online keeps working offline, text,
// audio, and all. Deliberately never touches Firebase's own Auth/
// Firestore traffic -- auth.js already has its own offline handling for
// that, and caching an XHR here could serve stale auth state.
//
// Course JSON files and the TTS audio directories are NOT bulk-precached
// at install time -- combined they run into the hundreds of MB across all
// nine courses, and most learners only ever study one or two. Instead
// they're cached the first time they're actually fetched (runtime
// caching below), so only what someone has genuinely opened ends up
// stored on their device.
//
// CACHE_VERSION is bumped by hand alongside index.html's own asset
// versions on every deploy -- that's what forces every open tab to fetch
// a fresh shell and drop the old cache on its next activate.
const CACHE_VERSION = "1";
const SHELL_CACHE = `muhkam-shell-v${CACHE_VERSION}`;
const RUNTIME_CACHE = `muhkam-runtime-v${CACHE_VERSION}`;

const SHELL_URLS = [
  "./",
  "./index.html",
  "./style.css?v=1784552040",
  "./app.js?v=1786284289",
  "./auth.js?v=6",
  "./firebase-config.js?v=1",
  "./manifest.json?v=1",
  "./icons/apple-touch-icon-180.png?v=1",
  "./icons/favicon-32.png?v=1",
  "./icons/icon-192.png",
  "./icons/icon-512.png",
  "./icons/icon-maskable-192.png",
  "./icons/icon-maskable-512.png",
];

self.addEventListener("install", (event) => {
  event.waitUntil(
    caches.open(SHELL_CACHE)
      .then((cache) => cache.addAll(SHELL_URLS))
      .then(() => self.skipWaiting())
  );
});

self.addEventListener("activate", (event) => {
  event.waitUntil(
    caches.keys()
      .then((keys) => Promise.all(
        keys.filter((k) => k !== SHELL_CACHE && k !== RUNTIME_CACHE).map((k) => caches.delete(k))
      ))
      .then(() => self.clients.claim())
  );
});

async function shellCacheFirst(req) {
  const cache = await caches.open(SHELL_CACHE);
  const cached = await cache.match(req);
  if (cached) return cached;
  try {
    const res = await fetch(req);
    if (res.ok) cache.put(req, res.clone());
    return res;
  } catch (e) {
    return cached || Response.error();
  }
}

// Same-origin TTS audio: never changes once generated, so pure cache-first
// with no revalidation is safe and saves bandwidth on repeat plays.
async function cacheFirstNoRevalidate(req) {
  const cache = await caches.open(RUNTIME_CACHE);
  const cached = await cache.match(req);
  if (cached) return cached;
  try {
    const res = await fetch(req);
    if (res.ok) cache.put(req, res.clone());
    return res;
  } catch (e) {
    return Response.error();
  }
}

// Course JSON / audio manifests: answer instantly from cache once a course
// has been opened before, but always kick off a background refetch too so
// a later content update (a course getting expanded, an audio fix) still
// reaches a frequently-online learner without needing a full reinstall.
async function staleWhileRevalidate(req) {
  const cache = await caches.open(RUNTIME_CACHE);
  const cached = await cache.match(req);
  const network = fetch(req).then((res) => {
    if (res.ok) cache.put(req, res.clone());
    return res;
  }).catch(() => null);
  if (cached) return cached;
  const res = await network;
  return res || Response.error();
}

self.addEventListener("fetch", (event) => {
  const req = event.request;
  if (req.method !== "GET") return; // never intercept writes (Firestore, etc.)
  const url = new URL(req.url);

  if (url.origin !== self.location.origin) return; // third-party (fonts, Firebase SDK/Auth/Firestore): pass through untouched

  // Opening/reloading the app itself: always answer from the precached
  // shell first, so this works with the device genuinely offline.
  if (req.mode === "navigate") {
    event.respondWith(shellCacheFirst(new Request("./index.html")));
    return;
  }

  const path = url.pathname;
  if (path.includes("/data/audio-") && !path.endsWith("manifest.json")) {
    event.respondWith(cacheFirstNoRevalidate(req));
    return;
  }
  if (path.includes("/data/courses") || path.endsWith("manifest.json")) {
    event.respondWith(staleWhileRevalidate(req));
    return;
  }
  event.respondWith(shellCacheFirst(req));
});
