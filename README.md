# JARVIS – Browser‑Based AI Assistant  

**JARVIS** is a lightweight, pure‑client web app that turns any modern web browser into a personal AI assistant. The entire application runs locally – no server, no build tools, no external dependencies. Just open `index.html` or serve the folder with a static HTTP server and start conversing.

![HTML5](https://img.shields.io/badge/HTML5-E34F26?style=flat-square&logo=html5&logoColor=white)  
![CSS3](https://img.shields.io/badge/CSS3-1572B6?style=flat-square&logo=css3&logoColor=white)  
![JavaScript](https://img.shields.io/badge/JavaScript-F7DF1E?style=flat-square&logo=javascript&logoColor=black)  
![License: MIT](https://img.shields.io/badge/License-MIT-blue?style=flat-square)  

---

## Quick Start

1. **Clone the repository**  
   ```bash  
   git clone https://github.com/shubhyagami/jarvis.git && cd jarvis  
   ```

2. **Open the app**  
   * Double‑click `index.html` in your file manager, or launch a local static server such as:  
     `python -m http.server`  (Python 3)  
     `npx serve`  (Node)  

3. **Grant microphone access** – a browser prompt will request permission.  

4. **Talk to JARVIS** – the default wake word is “Hey JARVIS”, but you can change it in `config.js`.  

---

## Supported Browsers

| Browser | Status | Notes |
|---------|--------|-------|
| Chrome  | ✔ | Recommended |
| Edge    | ✔ | Full feature set |
| Firefox | ✔ | Voice recognition may be less accurate |
| Safari  | ✔ | Some advanced features behave slightly differently |

---

## How It Works

1. The microphone captures audio.  
2. The [Web Speech API](https://developer.mozilla.org/en-US/docs/Web/API/Web_Speech_API) converts speech to text.  
3. A lightweight parser checks the transcription against a list of skills.  
4. If a skill matches, its module is executed and the result is spoken or displayed.  
5. If no skill matches, a fallback response is shown.  

All steps are asynchronous and event‑driven, keeping the UI responsive.

---

## Features

- **Instant voice recognition** – uses the browser’s built‑in Speech API.  
- **Zero‑setup** – launch from `index.html` or any static file server.  
- **Modular skill system** – drop a `*.js` file into `/skills` and it is auto‑registered.  
- **Retro‑futuristic UI** – neon‑style HUD with live audio waveforms.  
- **Highly configurable** – tweak `config.js` for wake word, colors, avatar, voice, and more.

---

## Customization

| Setting | File / Location | Example |
|---------|-----------------|--------|
| Wake word | `config.js` | `wakeWord: "Hey JARVIS"` |
| Color scheme | `config.js` | `primaryColor: "#0bd"` |
| Avatar image | `assets/avatars/` | Replace `avatar.png` |
| Speech feedback | UI settings button | Toggle “Speak response” |

---

## Extending – Adding a New Skill

1. Create a file in `/skills`, e.g. `skills/mySkill.js`.  
2. Export a `run(state, command)` function that returns a promise resolving to a string or an HTML element.

```javascript
    export function run(state, command) {
        // Perform work
        return Promise.resolve('Skill result');
    }
```

The module will load automatically on the next page load.

---

## Contributing

The project is open to pull requests. Please follow these steps:

1. Fork the repository.  
2. Create a feature branch (`git checkout -b feature/...`).  
3. Commit your changes and push to your fork.  
4. Open a pull request against the `main` branch.  

Before opening a PR, run the linter (if available) to ensure consistent code style.  

---

## Project Stats

- Lines of code: ~1,250 (HTML/CSS/JS)  
- Built‑in skills: 12  
- Recognized commands: 50+  
- Average response time: < 200 ms  

---

## Changelog

- **2026‑09‑03** – README cleanup, improved wording, added contributor guidance.  
- **2026‑08‑21** – Minor README tweaks, streamlined skill module exports.  
- **2026‑08‑06** – Added live weather command; fixed mobile UI overlap; reduced memory usage by 15 %.  

---

## License

MIT – see the `LICENSE` file.
