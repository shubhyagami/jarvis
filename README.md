# JARVIS – Browser‑Based AI Assistant

A lightweight, pure‑client web app that turns any modern browser into a voice‑controlled AI assistant.  
Everything runs **exclusively in the browser** – no server, no build step, no external dependencies.

![HTML5](https://img.shields.io/badge/HTML5-E34F26?style=flat-square&logo=html5&logoColor=white)  
![CSS3](https://img.shields.io/badge/CSS3-1572B6?style=flat-square&logo=css3&logoColor=white)  
![JavaScript](https://img.shields.io/badge/JavaScript-F7DF1E?style=flat-square&logo=javascript&logoColor=black)  
![Supported Browsers](https://img.shields.io/badge/Supported-Chrome%20%7C%20Edge%20%7C%20Firefox%20%7C%20Safari-brightgreen)  
![GitHub stars](https://img.shields.io/github/stars/shubhyagami/jarvis.svg?style=flat-square)  
![Repo size](https://img.shields.io/github/repo-size/shubhyagami/jarvis.svg?style=flat-square)  
![License](https://img.shields.io/badge/License-MIT-blue?style=flat-square)

---

## Quick Start

```bash
git clone https://github.com/shubhyagami/jarvis.git
cd jarvis
```

Open `index.html` in a supported browser (Chrome ≥ 49, Edge ≥ 79, Firefox ≥ 52, Safari ≥ 10.1).  
If you prefer a local server, any of the following will work:

```bash
# Python 3
python -m http.server

# Node.js
npx serve
```

Allow microphone access, say the default wake word **“Hey JARVIS”** (or edit `config.js`), and the assistant will respond.

---

## Features

| Feature | What it gives you |
|---------|------------------|
| **Zero‑setup** | Run directly from `index.html` or host on any static server |
| **Web Speech API** | Native voice recognition and synthesis, no external services |
| **Modular skill system** | Add or remove skills by editing the `skills/` directory |
| **Live UI** | Neon HUD, animated waveform, friendly avatar |
| **Configurable** | Tweak wake word, colors, avatar, voice, etc. in `config.js` |

---

## Customisation

| Setting | File / Location | Example |
|---------|-----------------|---------|
| Wake word | `config.js` | `wakeWord: "Hey JARVIS"` |
| Primary color | `config.js` | `primaryColor: "#0bd"` |
| Avatar image | `assets/avatars/` | Replace `avatar.png` |
| Voice feedback | UI Settings | Toggle “Speak response” |

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

- ~1.3 k lines of HTML, CSS, and JavaScript  
- Built‑in skills: 12  
- Recognised commands: 50+ (see `skills/`)  
- Average response time: < 200 ms  

---

## Changelog

- **2026‑09‑07** – README cleanup, added contribution guidelines.  
- **2026‑09‑04** – Minor wording improvements.  
- **2026‑08‑21** – Added live weather command; fixed mobile UI overlap; reduced memory usage by 15 %.  

---

## License

MIT – see the `LICENSE` file.
