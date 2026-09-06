# JARVIS – Browser‑Based AI Assistant

A lightweight, pure‑client web app that turns any modern browser into a voice‑controlled AI assistant.  
Everything runs *entirely in the browser* – no server, no build step, no external dependencies.

![HTML5](https://img.shields.io/badge/HTML5-E34F26?style=flat-square&logo=html5&logoColor=white)  
![CSS3](https://img.shields.io/badge/CSS3-1572B6?style=flat-square&logo=css3&logoColor=white)  
![JavaScript](https://img.shields.io/badge/JavaScript-F7DF1E?style=flat-square&logo=javascript&logoColor=black)  
![Supported Browsers](https://img.shields.io/badge/Supported-Chrome%20%7C%20Edge%20%7C%20Firefox%20%7C%20Safari-brightgreen)  
![GitHub stars](https://img.shields.io/github/stars/shubhyagami/jarvis.svg?style=flat-square)  
![GitHub repo size](https://img.shields.io/github/repo-size/shubhyagami/jarvis.svg?style=flat-square)  
![MIT license](https://img.shields.io/badge/License-MIT-blue?style=flat-square)

---

## Quick Start

```bash
git clone https://github.com/shubhyagami/jarvis.git
cd jarvis
```

Open `index.html` directly in any supported browser (Chrome ≥ 49, Edge ≥ 79, Firefox ≥ 52, Safari ≥ 10.1).  
For a local server:

```bash
# Python 3
python -m http.server

# Node.js (serve package)
npx serve
```

Grant microphone access when the page loads.  
Say the default wake word **“Hey JARVIS”** (or change it in `config.js`) and let the assistant respond.

---

## Features

- **Zero‑setup** – run directly from `index.html` or any static host.
- **Built‑in voice recognition & synthesis** – uses the Web Speech API; no external libraries.
- **Modular skill system** – drop a `*.js` file into `/skills` and it registers automatically.
- **Neon HUD & live waveform** – visual feedback of microphone activity.
- **Fully configurable** – edit `config.js` for wake word, colors, avatar, voice, etc.
- **Client‑side only** – no server‑side code or build process.

---

## Browser Support

| Feature | Minimum supported browser |
|---------|----------------------------|
| Web Speech API (recognition + synthesis) | Chrome ≥ 49, Edge ≥ 79, Firefox ≥ 52, Safari ≥ 10.1 |
| Audio context (waveform) | Same as above |
| Promises & async/await | All modern browsers (IE 11+ not supported) |

Unsupported browsers will still show the UI but lack speech functionality.

---

## How It Works

1. **Capture audio** – the browser records microphone input.  
2. **Speech‑to‑text** – the Web Speech API transcribes speech to plain text.  
3. **Skill matching** – a lightweight parser checks the command against the skill list.  
4. **Execution** – a matching skill module runs, returning a string or an HTMLElement.  
5. **Fallback** – if no skill matches, a default response is shown.  

All steps are asynchronous, keeping the UI responsive.

---

## Customization

| Setting | File / Location | Example |
|---------|----------------|---------|
| Wake word | `config.js` | `wakeWord: "Hey JARVIS"` |
| Primary color | `config.js` | `primaryColor: "#0bd"` |
| Avatar image | `assets/avatars/` | Replace `avatar.png` |
| Voice feedback | UI settings button | Toggle “Speak response” |

---

## Adding a Skill

Create a JavaScript file in `skills/`, e.g. `skills/mySkill.js`, and export a `run(state, command)` function that returns a Promise resolving to a string or an HTMLElement.

```javascript
export function run(state, command) {
    // Your logic here
    return Promise.resolve('Skill result');
}
```

The module will be loaded automatically the next time the app starts.

---

## Contributing

1. Fork the repository.  
2. Create a feature branch: `git checkout -b feature/…`.  
3. Commit and push.  
4. Open a pull request against `main`.

If a linter is available, run it before submitting a PR to keep the code style consistent.

---

## Project Stats

- Lines of code (HTML/CSS/JS): ~1.3 k  
- Built‑in skills: 12  
- Recognized commands: 50+  
- Average response time: < 200 ms  

---

## Changelog

- **2026‑09‑04** – README cleanup, improved wording, added contribution guidance.  
- **2026‑09‑03** – Minor README tweaks, streamlined skill module exports.  
- **2026‑08‑21** – Added live weather command; fixed mobile UI overlap; reduced memory usage by 15 %.

---

## License

MIT – see the `LICENSE` file.
