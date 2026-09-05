# JARVIS – Browser‑Based AI Assistant
A lightweight, pure‑client web app that turns a modern browser into a personal AI assistant.  
Everything runs entirely in the browser – no server, no build step, no external dependencies.

![HTML5](https://img.shields.io/badge/HTML5-E34F26?style=flat-square&logo=html5&logoColor=white)  
![CSS3](https://img.shields.io/badge/CSS3-1572B6?style=flat-square&logo=css3&logoColor=white)  
![JavaScript](https://img.shields.io/badge/JavaScript-F7DF1E?style=flat-square&logo=javascript&logoColor=black)  
![Browser Support](https://img.shields.io/badge/Supported-Chrome%20%7C%20Edge%20%7C%20Firefox%20%7C%20Safari-brightgreen)  
![License](https://img.shields.io/badge/License-MIT-blue?style=flat-square)

---

## Quick Start

```bash
git clone https://github.com/shubhyagami/jarvis.git
cd jarvis
```

Open `index.html` in a supported browser (Chrome ≥ 49, Edge ≥ 79, Firefox ≥ 52, Safari ≥ 10.1).  
If you prefer a local server, run:

```bash
python -m http.server   # Python 3
```

or

```bash
npx serve              # Node.js
```

Grant microphone access when prompted.  
Speak the wake word (default `Hey JARVIS`) or change it in `config.js`.  
The assistant will reply by voice and/or text.

---

## Browser Prerequisites

- Web Speech API support:  
  - Chrome ≥ 49  
  - Edge ≥ 79  
  - Firefox ≥ 52  
  - Safari ≥ 10.1  
- No polyfills are needed; unsupported browsers simply lose speech recognition.

---

## How It Works

1. **Capture audio** – the browser records microphone input.  
2. **Speech‑to‑text** – Web Speech API converts it to plain text.  
3. **Skill matching** – a lightweight parser checks the command against the skill list.  
4. **Execution** – a matching module runs, returning a string or an HTMLElement.  
5. **Fallback** – if no skill matches, a default response is shown.  

All steps are asynchronous, keeping the UI responsive.

---

## Core Features

- **Zero setup** – launch directly from `index.html` or any static HTTP server.  
- **Built‑in voice recognition** – no external libraries.  
- **Modular skill system** – drop a `*.js` file into `/skills` and it registers automatically.  
- **Neon HUD** with a live audio waveform.  
- **Fully configurable** – tweak `config.js` for wake word, colors, avatar, voice, etc.  
- **Client‑side only** – no server‑side code or build process.

---

## Customization

| Feature          | File / Location       | Example Value                           |
|------------------|-----------------------|----------------------------------------|
| Wake word        | `config.js`           | `wakeWord: "Hey JARVIS"`               |
| Primary color    | `config.js`           | `primaryColor: "#0bd"`                 |
| Avatar image     | `assets/avatars/`      | Replace `avatar.png`                    |
| Voice feedback   | UI settings button     | Toggle “Speak response”                 |

---

## Adding a New Skill

1. Create a file in `skills/`, e.g. `skills/mySkill.js`.  
2. Export a `run(state, command)` function that returns a Promise resolving to a string or an HTMLElement.

```javascript
export function run(state, command) {
    // Your logic here
    return Promise.resolve('Skill result');
}
```

The module will load automatically the next time the app is opened.

---

## Contributing

1. Fork the repository.  
2. Create a feature branch: `git checkout -b feature/…`.  
3. Commit and push.  
4. Open a pull request against the `main` branch.  

If a linter is available, run it before submitting a PR to keep the code style consistent.

---

## Project Stats

- **Lines of code**: ~1.3 k (HTML/CSS/JS)  
- **Built‑in skills**: 12  
- **Recognized commands**: 50+  
- **Average response time**: < 200 ms  

---

## Changelog

- **2026‑09‑04** – README cleanup, improved wording, added contribution guidance.  
- **2026‑09‑03** – Minor README tweaks, streamlined skill module exports.  
- **2026‑08‑21** – Added live weather command; fixed mobile UI overlap; reduced memory usage by 15 %.

---

## License

MIT – see the `LICENSE` file.
