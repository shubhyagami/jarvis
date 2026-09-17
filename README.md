# JARVIS – Browser‑Based AI Assistant  

A lightweight, pure‑client web app that turns any modern browser into a voice‑controlled AI assistant.  
Everything runs **exclusively in the browser** – no server, no build step, no external dependencies.  

[![HTML5](https://img.shields.io/badge/HTML5-E34F26?style=flat-square&logo=html5&logoColor=white)](https://developer.mozilla.org/en-US/docs/Web/HTML)  
[![CSS3](https://img.shields.io/badge/CSS3-1572B6?style=flat-square&logo=css3&logoColor=white)](https://developer.mozilla.org/en-US/docs/Web/CSS)  
[![JavaScript](https://img.shields.io/badge/JavaScript-F7DF1E?style=flat-square&logo=javascript&logoColor=black)](https://developer.mozilla.org/en-US/docs/Web/JavaScript)  
[![Supported Browsers](https://img.shields.io/badge/Supported-Chrome%20%7C%20Edge%20%7C%20Firefox%20%7C%20Safari-brightgreen)](https://developer.mozilla.org/en-US/docs/Web/API)  
[![GitHub stars](https://img.shields.io/github/stars/shubhyagami/jarvis.svg?style=flat-square)](https://github.com/shubhyagami/jarvis/stargazers)  
[![Repo size](https://img.shields.io/github/repo-size/shubhyagami/jarvis.svg?style=flat-square)](https://github.com/shubhyagami/jarvis)  
[![License](https://img.shields.io/badge/License-MIT-blue?style=flat-square)](./LICENSE)  

---

## Quick Start

```bash
git clone https://github.com/shubhyagami/jarvis.git
cd jarvis
```

Open `index.html` in a supported browser (Chrome ≥ 49, Edge ≥ 79, Firefox ≥ 52, Safari ≥ 10.1). If you prefer a local server, any of the following will work:

```bash
# Python 3
python -m http.server

# Node.js
npx serve
```

Allow microphone access, say the default wake word **“Hey JARVIS”** (or edit `config.js`), and the assistant will respond.

---

## Features

- **Zero‑setup** – run directly from `index.html` or host on any static server.  
- **Web Speech API** – native voice recognition and synthesis, no external services.  
- **Modular skill system** – add or remove skills by editing the `skills/` directory.  
- **Live UI** – neon HUD with an animated waveform and friendly avatar.  
- **Fully configurable** – tweak wake word, colors, avatar, voice, etc. in `config.js`.  

---

## Supported Browsers

| Feature | Minimum supported browser |
|---------|----------------------------|
| Web Speech API (recognition & synthesis) | Chrome ≥ 49, Edge ≥ 79, Firefox ≥ 52, Safari ≥ 10.1 |
| AudioContext (waveform) | Same as above |
| ES 2017 (Promises + async/await) | All current browsers |

If a browser does not support the necessary APIs, the UI loads but speech features are disabled.

---

## How It Works

1. **Audio capture** – the browser records from your microphone.  
2. **Speech‑to‑text** – the Web Speech API transcribes the voice.  
3. **Skill matching** – a simple parser checks the command against available skills.  
4. **Execution** – the matching skill module runs and returns a string or an `HTMLElement`.  
5. **Fallback** – if no skill matches, a default reply is shown.

All operations are asynchronous, keeping the UI responsive.

---

## Customisation

| Setting       | Location          | Example                      |
|---------------|-------------------|------------------------------|
| Wake word     | `config.js`       | `wakeWord: "Hey JARVIS"`    |
| Primary color | `config.js`      | `primaryColor: "#0bd"`       |
| Avatar image  | `assets/avatars/` | Replace `avatar.png`          |
| Voice feedback | UI Settings      | Toggle **Speak response**   |

---

## Adding a Skill

Create a file `skills/yourSkill.js` and export a `run(state, command)` function that resolves to a string or an `HTMLElement`:

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
2. Create a feature branch: `git checkout -b feature/...`.  
3. Commit and push.  
4. Open a pull request against `main`.  
5. Run the linter before submitting to keep the code style consistent.

---

## Project Stats

- Approx. 1.3 k lines of HTML, CSS, and JavaScript.  
- Built‑in skills: 12.  
- Recognised commands: 50+ (see `skills/`).  
- Average response time: < 200 ms.  

---

## Changelog

- **2026‑09‑07** – README cleanup, added contribution guidelines.  
- **2026‑09‑04** – Minor wording improvements.  
- **2026‑08‑21** – Added live weather command; fixed mobile UI overlap; reduced memory usage by 15 %.  

---

## License

MIT – see the `LICENSE` file.
