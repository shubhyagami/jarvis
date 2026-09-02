# JARVIS – Browser‑Based AI Assistant

A lightweight, pure‑client web app that turns your browser into a conversational AI assistant.  
All of the logic runs in the browser – no server, no build tools, no external libraries.

> **Open** `index.html` in any recent desktop browser and start talking.  
> It uses the Web Speech API for voice input and the Web Speech Synthesis API for spoken responses.

---

## Quick Links

| | |
|---|---|
| **Source** | <https://github.com/shubhyagami/jarvis> |
| **License** | MIT |
| **Languages** | HTML, CSS, JavaScript |

---

## Features

- **Voice‑first** – Natural‑language input via the Web Speech API.  
- **Zero‑setup** – Just open `index.html` or serve the folder with any static server.  
- **Modular skill system** – Add or replace functionality by dropping a `.js` file into `/skills`.  
- **Customizable UI** – Change the wake word, color theme, avatar, and voice settings in `config.js`.  
- **Offline ready** – Works fully on an empty folder, once the browser has cached the assets.

---

## Supported Browsers

| Browser | Status | Notes |
|---------|--------|-------|
| Chrome | ✔ | Recommended |
| Edge | ✔ | Full feature set |
| Firefox | ✔ | Voice recognition may be less accurate |
| Safari | ✔ | Some animations may differ |

---

## Getting Started

```bash
# Clone the repo
git clone https://github.com/shubhyagami/jarvis.git
cd jarvis
```

1. **Open the app**  
   *Double‑click* `index.html` or run a simple static server, e.g.:

   ```bash
   python -m http.server 8000
   ```

2. **Grant microphone access** – The browser will prompt for microphone permission.

3. **Speak a command** – Say “Hey JARVIS” or a built‑in command such as “What’s the time?”

> **Tip**: In Chrome, the first call to the Speech API asks for permission each time you reload.  
> Persist the setting by clicking the lock icon → Microphone → `Allow`.

---

## Extending Skill Set

1. Create `myskill.js` in the `/skills` folder.
2. Export a `run(state, command)` function that returns a `Promise` resolving to a string or an HTML element.

```js
// /skills/myskill.js
export function run(state, command) {
  // Example: reply with the command length
  return Promise.resolve(`You said ${command.length} words.`);
}
```

3. Reload the page – the new skill is automatically registered.

---

## Configuration

Edit `config.js` to tweak:

- `wakeWord` – Any trigger phrase.  
- `theme` – `light` or `dark` (plus optional color).  
- `voice` – Enable or disable TTS.  
- `skillsDir` – Path to the skill folder.

```js
export const config = {
  wakeWord: /hey jarvis/i,
  theme: 'dark',
  voice: true,
  skillsDir: '/skills',
};
```

---

## Project Structure

```
jarvis/
├─ index.html          → Entry point
├─ style.css           → UI styling
├─ app.js              → Core logic
├─ config.js           → User‑adjustable settings
├─ /skills/            → Skill modules (auto‑loaded)
│  └─ hello.js
├─ /assets/
│  ├─ avatar.png
│  └─ sound.wav
└─ README.md
```

---

## Contributing

Pull requests are welcome.  
Please keep the code simple, avoid adding external dependencies, and update the README if you add new features.

---

## Changelog (excerpt)

- **2026‑09‑02** – Updated README, added example skill contract.  
- **2026‑08‑21** – Simplified skill export format.  
- **2026‑08‑06** – Added live weather command; fixed mobile UI overlap.

---

## License

MIT – see the [LICENSE](LICENSE) file.
