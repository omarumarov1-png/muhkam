// sw.js — Muḥkam service worker.
//
// History: this used to be a KILL SWITCH. An earlier version cached the
// app shell CACHE-FIRST, including full page navigations, which meant a
// device that already had the worker installed could never see a new
// deploy no matter what index.html said -- the old worker served its own
// stale cached copy instead of ever asking the network. Editing
// index.html alone can't reach those devices, only a byte-changed sw.js
// can (the browser diffs sw.js independently of the page's own JS). That
// bug was bad enough to need a version of this file that just wiped every
// cache and unregistered itself on activate.
//
// This version fixes the actual root cause instead of just disabling
// caching: the app SHELL (the files below) is NETWORK-FIRST, falling back
// to cache only when the network request genuinely fails. That makes it
// structurally impossible to get trapped behind stale content while
// online -- a real network response always wins and gets re-cached. Cache
// is purely a last-resort fallback for genuine offline use, never a
// shortcut taken while a fresh copy is reachable. Same fix, same shape,
// as the sibling Wird app's sw.js (which hit this exact bug first).
//
// Course JSON (data/courses-*.json), audio manifests, and audio files
// (data/audio-*/**) are deliberately NOT touched by this file at all.
// Downloading those for offline use is explicit and user-controlled (a
// Downloads action per course), backed by an IndexedDB store in app.js
// (muhkam-offline-v1 / downloadCourse / cachedBlobUrlFor) -- not this
// blanket shell cache. Keeping this file's job narrow (shell only) is
// deliberate: it means a broken/partial course download can never be
// masked or shadowed by service-worker caching.

const CACHE_VERSION = "20260830"; // bump whenever a shell file changes; keep in lockstep with index.html's ?v= query strings
const CACHE_NAME = `muhkam-shell-${CACHE_VERSION}`;

const SHELL_FILES = [
  "./",
  "./index.html",
  "./app.js",
  "./style.css",
  "./auth.js",
  "./firebase-config.js",
  "./manifest.json",
  "./data/course-sizes.json",
];

const ICON_FILES = [
  "./icons/icon-192.png",
  "./icons/icon-512.png",
  "./icons/icon-maskable-192.png",
  "./icons/icon-maskable-512.png",
  "./icons/apple-touch-icon-180.png",
  "./icons/favicon-32.png",
];

self.addEventListener("install", (event) => {
  event.waitUntil(
    caches.open(CACHE_NAME).then((cache) =>
      cache.addAll([...SHELL_FILES, ...ICON_FILES]).catch(() => {
        // A single missing/failed asset shouldn't block installation --
        // the fetch handler below re-caches successful responses anyway,
        // so a partial pre-cache just means a slightly colder first
        // offline load, not a broken one.
      })
    ).then(() => self.skipWaiting())
  );
});

self.addEventListener("activate", (event) => {
  event.waitUntil(
    (async () => {
      const keys = await caches.keys();
      await Promise.all(
        keys.filter((k) => k.startsWith("muhkam-shell-") && k !== CACHE_NAME)
          .map((k) => caches.delete(k))
      );
      await self.clients.claim();
    })()
  );
});

function isShellRequest(url) {
  if (url.origin !== self.location.origin) return false;
  const path = url.pathname;
  return (
    SHELL_FILES.some((f) => path.endsWith(f.replace("./", "/"))) ||
    ICON_FILES.some((f) => path.endsWith(f.replace("./", "/"))) ||
    path === "/" || path.endsWith("/index.html")
  );
}

self.addEventListener("fetch", (event) => {
  const req = event.request;
  if (req.method !== "GET") return;

  let url;
  try { url = new URL(req.url); } catch (e) { return; }

  // Only the app shell + icons are handled here. Everything else (course
  // JSON, audio manifests, audio files, Firebase/Firestore, gstatic SDK
  // imports) is left completely alone and goes straight to the network
  // exactly as if this service worker didn't exist.
  if (!isShellRequest(url)) return;

  event.respondWith(
    (async () => {
      try {
        const fresh = await fetch(req);
        if (fresh && fresh.ok) {
          const cache = await caches.open(CACHE_NAME);
          cache.put(req, fresh.clone());
        }
        return fresh;
      } catch (err) {
        const cached = await caches.match(req, { ignoreSearch: true });
        if (cached) return cached;
        throw err;
      }
    })()
  );
});
