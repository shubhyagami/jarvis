# JARVIS – Your Personal Browser‑Based AI Assistant  

![HTML5](https://img.shields.io/badge/HTML5-E34F26?style=flat-square&logo=html5&logoColor=white)  
![CSS3](https://img.shields.io/badge/CSS3-1572B6?style=flat-square&logo=css3&logoColor=white)  
![JavaScript](https://img.shields.io/badge/JavaScript-F7DF1E?style=flat-square&logo=javascript&logoColor=black)  
![License](https://img.shields.io/badge/license-MIT-blue?style=flat-square)  

JARVIS is a lightweight, pure‑client web app that turns your browser into a conversational AI assistant. Inspired by the Iron Man J.A.R.V.I.S., the entire application runs locally—no server, no build tools, no external dependencies. Open `index.html` and start interacting.

---

## Overview

A single‑page application built with vanilla HTML5, CSS3, and JavaScript. All processing occurs on the client side, making it ideal for offline use, quick prototyping, or educational demos. The assistant listens for voice commands through the Web Speech API, parses them into a simple command language, and runs one of many modular *skills* that you can add or modify yourself.

---

## Key Features

- **Voice recognition** – Natural‑language input powered by the Web Speech API.  
- **Zero‑setup** – Launch by opening `index.html` or serve the folder with any static HTTP server.  
- **Modular skill system** – Drop a `.js` file into `/skills` and the app registers it automatically.  
- **Retro‑futuristic UI** – Neon HUD with live audio‑waveform visualizations.  
- **Customizable** – Adjust wake word, color scheme, avatar, and response preferences via `config.js`.

---

## Getting Started

1. **Clone the repository**  
   `git clone https://github.com/shubhyagami/jarvis.git` &nbsp;&nbsp; ← then `cd jarvis`

2. **Launch the app**  
   - Double‑click `index.html` in your file explorer, **or**  
   - Start a simple static server, e.g. `python -m http.server`, in the project directory.

3. **Grant microphone permission** – The browser will request access to your microphone; allow it to enable voice commands.

4. **Start speaking** – Say “Hey JARVIS” or any supported command such as “What’s the time?”  

> **Tip**: On some browsers the voice recognition may ask for permission each time you reload. If that happens, click the lock icon in the address bar → Microphone → *Allow*.

---

## Supported Browsers

| Browser | Status | Notes |
|---------|--------|-------|
| Chrome | ✔ | Recommended |
| Microsoft Edge | ✔ | Full feature set |
| Firefox | ✔ | Voice recognition may be less accurate |
| Safari | ✔ | Advanced features may behave slightly differently |

---

## How It Works

```
User speaks → Microphone → Speech Recognition API → Command Parser →
   ├─ Skill matched? → Execute skill → Voice / visual output
   └─ No match → Fallback response → Voice / visual output
```

The pipeline is fully asynchronous and event‑driven, ensuring a responsive experience.

---

## Customization

- **Wake word** – Edit `config.js` to set any trigger phrase you prefer.  
- **Voice feedback** – Toggle spoken responses on or off using the settings icon in the UI.  
- **Add skills** – Create a new file in `/skills` that exports a function matching the skill contract. The app loads all such modules automatically at startup.

---

## Adding New Skills

1. Create a file `myskill.js` in `/skills`.  
2. Export a function that accepts the `state` object and returns a promise resolving to a string or a visual element.
3. The assistant will load it automatically on the next page load.

> **Skill contract example**  
> ```js
> export function run(state, command) {
>   // perform action
>   return Promise.resolve('Skill executed');
> }
> ```

---

## Project Statistics

| Metric | Value |
|--------|-------|
| Code (HTML/CSS/JS) | 1,250+ lines |
| Built‑in skills | 12 |
| Recognized commands | 50+ |
| Avg. response time | < 200 ms |
| Licensed under MIT | ✔ |

---

## Changelog

- **2026‑08‑21** – Cleaned up README formatting; streamlined skill module exports.  
- **2026‑08‑06** – Added live weather command; fixed mobile UI overlap in waveform animation; reduced memory usage by 15 %.  

---

## License

This project is licensed under the MIT License – see the [LICENSE](LICENSE) file for details.
