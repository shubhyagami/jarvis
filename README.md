# JARVIS – Browser‑Based AI Assistant

A lightweight, pure‑client web app that turns any modern browser into a voice‑controlled AI assistant.  
Everything runs **entirely in the browser** – no server, no build step, no external dependencies.

![HTML5](https://img.shields.io/badge/HTML5-E34F26?style=flat-square&logo=html5&logoColor=white)  
![CSS3](https://img.shields.io/badge/CSS3-1572B6?style=flat-square&logo=css3&logoColor=white)  
![JavaScript](https://img.shields.io/badge/JavaScript-F7DF1E?style=flat-square&logo=javascript&logoColor=black)  
![Supported](https://img.shields.io/badge/Supported-Chrome%20%7C%20Edge%20%7C%20Firefox%20%7C%20Safari-brightgreen)  
![GitHub stars](https://img.shields.io/github/stars/shubhyagami/jarvis.svg?style=flat-square)  
![Repo size](https://img.shields.io/github/repo-size/shubhyagami/jarvis.svg?style=flat-square)  
![License](https://img.shields.io/badge/License-MIT-blue?style=flat-square)

---

## Quick Start

```bash
git clone https://github.com/shubhyagami/jarvis.git
cd jarvis
```

Open `index.html` in any supported browser (Chrome ≥ 49, Edge ≥ 79, Firefox ≥ 52, Safari ≥ 10.1).  
Alternatively, serve it locally:

```bash
# Python 3
python -m http.server

# Node.js
npx serve
```

Grant microphone access when prompted.  
Say the default wake word **“Hey JARVIS”** (or change it in `config.js`) and watch the assistant respond.

---

## Features

- **Zero‑setup** – run directly from `index.html` or host on any static server.  
- **Web Speech** – built‑in voice recognition & synthesis using the native API.  
- **Modular skill system** – add new skills by dropping a `.js` file into `/skills`.  
- **Real‑time UI** – neon HUD and live waveform visualise microphone activity.  
- **Fully configurable** – edit `config.js` to change wake word, colours, avatar, voice, etc.  
- **Client‑side only** – no server‑side code or build process.

---

## Browser Support

| Feature | Minimum supported browser |
|---------|---------------------------|
| Web Speech API (recognition + synthesis) | Chrome ≥ 49, Edge ≥ 79, Firefox ≥ 52, Safari ≥ 10.1 |
| Audio context (waveform) | Same as above |
| Promises & async/await | All modern browsers (IE 11+ not supported) |

Unsupported browsers display the UI but lack speech functionality.

---

## How It Works

1. **Capture audio** – the browser records microphone input.  
2. **Speech‑to‑text** – the Web Speech API transcribes speech.  
3. **Skill matching** – a lightweight parser checks the command against available skills.  
4. **Execution** – a matching skill module runs, returning a string or an `HTMLElement`.  
5. **Fallback** – if no skill matches, a default response is shown.

All steps are asynchronous, keeping the UI responsive.

---

## Customization

| Setting | Location | Example |
|---------|----------|---------|
| Wake word | `config.js` | `wakeWord: "Hey JARVIS"` |
| Primary color | `config.js` | `primaryColor: "#0bd"` |
| Avatar image | `assets/avatars/` | Replace `avatar.png` |
| Voice feedback | UI settings button | Toggle “Speak response” |

---

## Adding a Skill

Create a file in `skills/`, e.g. `skills/mySkill.js`, and export a `run(state, command)` function that returns a `Promise` resolving to a string or an `HTMLElement`.

```javascript
export function run(state, command) {
    // Your logic here
    return Promise.resolve('Skill result');
}
```

The module will load automatically the next time the app starts.

---

## Contributing

1. Fork the repo.  
2. Create a feature branch: `git checkout -b feature/...`.  
3. Commit and push.  
4. Open a pull request against `main`.  
5. (Optional) Run the linter before submitting to keep the code style consistent.

---

## Project Stats

- **Lines of code**: ~1.3 k (HTML/CSS/JS)  
- **Built‑in skills**: 12  
- **Recognized commands**: 50+  
- **Average response time**: < 200 ms  

---

## Changelog

- **2026‑09‑07** – README cleanup, added contribution guidelines.  
- **2026‑09‑04** – Minor wording improvements.  
- **2026‑08‑21** – Added live weather command; fixed mobile UI overlap; reduced memory usage by 15 %.

---

## License

MIT – see the `LICENSE` file.
