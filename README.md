# JARVIS – Browser‑Based AI Assistant

**JARVIS** is a lightweight, pure‑client web app that turns a modern web browser into a personal AI assistant.  
Everything runs locally – no server, no build step, no external dependencies.  
Open `index.html` or serve the repo with any static HTTP server and start talking.

> **Prerequisite**  
> A browser that supports the Web Speech API (Chrome, Edge, Firefox, Safari).

![HTML5](https://img.shields.io/badge/HTML5-E34F26?style=flat-square&logo=html5&logoColor=white)
![CSS3](https://img.shields.io/badge/CSS3-1572B6?style=flat-square&logo=css3&logoColor=white)
![JavaScript](https://img.shields.io/badge/JavaScript-F7DF1E?style=flat-square&logo=javascript&logoColor=black)
![Browser Support](https://img.shields.io/badge/Supported-Chrome%20%7C%20Edge%20%7C%20Firefox%20%7C%20Safari-brightgreen)
![License](https://img.shields.io/badge/License-MIT-blue?style=flat-square)

---

## Getting Started

**Clone the repository**

```
git clone https://github.com/shubhyagami/jarvis.git
cd jarvis
```

**Open the app**

- Double‑click `index.html` in File Explorer, **or**
- Start a local static server:

```
python -m http.server   # Python 3
# or
npx serve              # Node.js
```

When the page loads the browser will request microphone access.  
Speak the wake word `Hey JARVIS` (changeable in `config.js`).  
The assistant will reply via speech and/or text on the screen.

---

## Browser Support

| Browser | Status | Notes |
|---------|--------|-------|
| Chrome  | ✅ | Recommended |
| Edge    | ✅ | Full features |
| Firefox | ✅ | Speech recognition may be less accurate |
| Safari  | ✅ | Some advanced features differ slightly |

> The app does not rely on any polyfills; older browsers will simply fail to provide speech recognition.

---

## How It Works

1. **Capture audio** – the browser’s microphone input is recorded.  
2. **Speech‑to‑text** – the Web Speech API converts it to plain text.  
3. **Skill matching** – a lightweight parser checks the command against the skill list.  
4. **Execution** – if a match is found, the corresponding module runs and returns a string or an HTMLElement.  
5. **Fallback** – if no skill matches, a default response appears.

All steps run asynchronously, keeping the UI responsive.

---

## Features

* Zero‑setup: launch directly from `index.html` or any static server.  
* Built‑in voice recognition via the browser’s Speech API.  
* Modular skill system – drop a `*.js` file into `/skills` and it registers automatically.  
* Neon HUD with live audio waveform.  
* Fully configurable – edit `config.js` to change wake word, colors, avatar, voice, etc.  
* No external dependencies – everything runs in the browser.

---

## Customization

| Setting        | Location                 | Example                              |
|----------------|--------------------------|-------------------------------------|
| Wake word      | `config.js`              | `wakeWord: "Hey JARVIS"`            |
| Color scheme   | `config.js`              | `primaryColor: "#0bd"`              |
| Avatar image   | `assets/avatars/`        | Replace `avatar.png`                |
| Speech feedback| UI settings button      | Toggle “Speak response”              |

---

## Adding a New Skill

1. Create a file in `skills/`, e.g. `skills/mySkill.js`.  
2. Export a `run(state, command)` function that returns a Promise resolving to a string or an HTMLElement.

```
export function run(state, command) {
    // Your logic here
    return Promise.resolve('Skill result');
}
```

The module will load automatically the next time the page is opened.

---

## Contributing

1. Fork the repo.  
2. Create a feature branch: `git checkout -b feature/...`.  
3. Commit and push your changes.  
4. Open a pull request against the `main` branch.

Run the linter (if available) before submitting a PR to keep the code style consistent.

---

## Project Stats

- Lines of code: ~1.3 k (HTML/CSS/JS)  
- Built‑in skills: 12  
- Recognized commands: 50+  
- Average response time: < 200 ms  

---

## Changelog

- **2026‑09‑04** – README cleanup, improved wording, added contributor guidance.  
- **2026‑09‑03** – Minor README tweaks, streamlined skill module exports.  
- **2026‑08‑21** – Added live weather command; fixed mobile UI overlap; reduced memory usage by 15 %.  

---

## License

MIT – see the `LICENSE` file.
