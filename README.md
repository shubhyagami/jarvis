# JARVIS – Browser‑Based AI Assistant

**JARVIS** is a lightweight, pure‑client web app that turns a modern web browser into a personal AI assistant.  
The entire application runs locally – no server, no build tools, no external dependencies.  
Open `index.html` or serve the repository with any static HTTP server and start talking.

> **Quick remark**  
> You’ll need a browser that supports the [Web Speech API](https://developer.mozilla.org/en-US/docs/Web/API/Web_Speech_API).

![HTML5](https://img.shields.io/badge/HTML5-E34F26?style=flat-square&logo=html5&logoColor=white)
![CSS3](https://img.shields.io/badge/CSS3-1572B6?style=flat-square&logo=css3&logoColor=white)
![JavaScript](https://img.shields.io/badge/JavaScript-F7DF1E?style=flat-square&logo=javascript&logoColor=black)
![Browser Support](https://img.shields.io/badge/Supported-Chrome%20%7C%20Edge%20%7C%20Firefox%20%7C%20Safari-brightgreen)
![License](https://img.shields.io/badge/License-MIT-blue?style=flat-square)

---

## Getting Started

```bash
git clone https://github.com/shubhyagami/jarvis.git
cd jarvis
```

Open the app in your browser:

- Double‑click `index.html` in File Explorer, or
- Run a local static server:

```bash
python -m http.server   # Python 3
# or
npx serve               # Node
```

A browser prompt will ask for microphone permission.  
Speak the default wake word **“Hey JARVIS”** (changeable in `config.js`).  
The assistant will respond with spoken or on‑screen replies.

---

## Browser Support

| Browser | Status | Notes |
|---------|--------|-------|
| Chrome  | ✅ | Recommended |
| Edge    | ✅ | Full features |
| Firefox | ✅ | Speech recognition may be less accurate |
| Safari  | ✅ | Some advanced features differ slightly |

---

## How It Works

1. **Audio capture** – the browser’s microphone input is recorded.  
2. **Speech → text** – the Web Speech API converts it to plain text.  
3. **Skill matching** – a lightweight parser checks the command against the skill list.  
4. **Skill execution** – if a match is found, the corresponding module runs and returns a string or DOM element.  
5. **Fallback** – if no skill matches, a default response appears.

All steps run asynchronously, keeping the UI responsive.

---

## Features

- Built‑in voice recognition via the browser’s Speech API
- Zero‑setup: launch directly from `index.html` or any static server
- **Modular skill system** – drop a `*.js` file into `/skills` and it registers automatically
- Retro‑futuristic neon HUD with live audio waveform
- Fully configurable – edit `config.js` to adjust wake word, colors, avatar, voice, etc.

---

## Customization

| Setting | File / Location | Example |
|--------|----------------|---------|
| Wake word | `config.js` | `wakeWord: "Hey JARVIS"` |
| Color scheme | `config.js` | `primaryColor: "#0bd"` |
| Avatar image | `assets/avatars/` | Replace `avatar.png` |
| Speech feedback | UI settings button | Toggle “Speak response” |

---

## Adding a New Skill

1. Create a file in `skills/`, e.g. `skills/mySkill.js`.  
2. Export a `run(state, command)` function that returns a Promise resolving to a string or an HTMLElement.

```js
export function run(state, command) {
    // Your logic here
    return Promise.resolve('Skill result');
}
```

The module will load automatically on the next page load.

---

## Contributing

1. Fork the repository.  
2. Create a feature branch: `git checkout -b feature/...`.  
3. Commit your changes and push to your fork.  
4. Open a pull request against the `main` branch.

Run the linter (if available) before submitting a PR to maintain consistent code style.

---

## Project Stats

- Lines of code: ~1.3 k (HTML/CSS/JS)  
- Built‑in skills: 12  
- Recognized commands: 50+  
- Average response time: < 200 ms  

---

## Changelog

- **2026‑09‑03** – README cleanup, improved wording, added contributor guidance.  
- **2026‑08‑21** – Minor README tweaks, streamlined skill module exports.  
- **2026‑08‑06** – Added live weather command; fixed mobile UI overlap; reduced memory usage by 15 %.

---

## License

MIT – see the `LICENSE` file.
