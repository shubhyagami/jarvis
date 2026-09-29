[K[2m  [2mmodel z-ai/glm-5.3-flash failed, trying next...[0m[0m
[K[2m  [2mmodel deepseek-ai/deepseek-v4.1-flash failed, trying next...[0m[0m
# JARVIS – Browser‑Based AI Assistant

JARVIS is a lightweight, pure‑client web application that turns a modern browser into a voice‑controlled AI assistant.  
All code runs **entirely in the browser** – no server, no build step, no external dependencies.

![HTML5](https://img.shields.io/badge/HTML5-E34F26?style=flat-square&logo=html5&logoColor=white)  
![CSS3](https://img.shields.io/badge/CSS3-1572B6?style=flat-square&logo=css3&logoColor=white)  
![JavaScript](https://img.shields.io/badge/JavaScript-F7DF1E?style=flat-square&logo=javascript&logoColor=black)  
![Supported Browsers](https://img.shields.io/badge/Supported-Chrome%20%7C%20Edge%20%7C%20Firefox%20%7C%20Safari-brightgreen)  
![GitHub stars](https://img.shields.io/github/stars/shubhyagami/jarvis?style=flat-square)  
![Repo size](https://img.shields.io/github/repo-size/shubhyagami/jarvis?style=flat-square)  
![License](https://img.shields.io/badge/License-MIT-blue?style=flat-square)

---

## Features

- **Zero‑setup** – open `index.html` or host it on any static server.  
- **Native Web Speech** – the browser handles all speech recognition & synthesis.  
- **Modular skill system** – add or remove functionality by adding JavaScript files to `skills/`.  
- **Live UI** – neon HUD, animated waveform, and an animated avatar.  
- **Fully configurable** – tweak wake word, colours, avatar, voice, and more in `config.js`.

---

## Getting Started

> Modern browsers require HTTPS for microphone access.  
> Running locally is simplest with a local server:  

```bash
git clone https://github.com/shubhyagami/jarvis.git
cd jarvis
python -m http.server   # or `npx serve`
```

Open the local URL in a modern browser, grant microphone permission, and say the wake word (default: **“Hey JARVIS”**).  
The wake word can be changed in `config.js`.

---

## How It Works

JARVIS listens for voice input via the Web Speech API. When the wake word is detected, the following spoken words are parsed as a command. The command is matched against the available skills located in `skills/`. The corresponding skill’s `run(state, command)` function is executed and its string or `HTMLElement` result is spoken or displayed.

Supported browsers: Chrome ≥ 49, Edge ≥ 79, Firefox ≥ 52, Safari ≥ 10.1.

---

## Configuration

| Setting          | File         | Example                               |
|------------------|--------------|---------------------------------------|
| Wake word        | `config.js` | `wakeWord: "Hey JARVIS"`              |
| Primary colour    | `config.js` | `primaryColor: "#0bd"`                |
| Avatar image     | `assets/avatars/` | Replace `avatar.png`                |
| Voice feedback   | UI Settings panel | Toggle “Speak response”             |

---

## Adding a New Skill

1. Create `skills/yourSkill.js`.  
2. Export a `run(state, command)` function that returns a promise resolved with a string or an `HTMLElement`.

```js
export function run(state, command) {
  // Your logic here
  return Promise.resolve('Skill result');
}
```

3. Reload the app; the new skill appears automatically.

---

## Contributing

1. Fork the repository.  
2. Checkout a feature branch: `git checkout -b feature/your-feature`.  
3. Commit, push, and open a pull request against `main`.  
4. Run the linter with `npm run lint` before submitting.

Pull requests that improve documentation, add new skills, or refactor existing code are welcome.

---

## Project Stats

- ~1.3 k lines of HTML, CSS, and JavaScript  
- 12 built‑in skills  
- 50 + recognised commands  
- Average response time < 200 ms  

---

## Changelog (excerpt)

| Date       | Change |
|------------|--------|
| 2026‑09‑07 | README cleanup, added contribution guidelines. |
| 2026‑09‑04 | Minor wording improvements. |
| 2026‑08‑21 | Added live weather command; fixed mobile UI overlap; reduced memory usage by 15 %. |

---

## License

MIT – see the `LICENSE` file.
