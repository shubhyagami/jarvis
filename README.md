# JARVIS — Browser-Based Voice Assistant

JARVIS is a lightweight, fully client-side web app that turns a modern browser into a voice-controlled AI assistant. Everything runs in the browser: no backend, no build step, no external dependencies.

![HTML5](https://img.shields.io/badge/HTML5-E34F26?style=flat-square&logo=html5&logoColor=white) ![CSS3](https://img.shields.io/badge/CSS3-1572B6?style=flat-square&logo=css3&logoColor=white) ![JavaScript](https://img.shields.io/badge/JavaScript-F7DF1E?style=flat-square&logo=javascript&logoColor=black) ![Supported Browsers](https://img.shields.io/badge/Supported-Chrome%20%7C%20Edge%20%7C%20Firefox%20%7C%20Safari-brightgreen) ![GitHub stars](https://img.shields.io/github/stars/shubhyagami/jarvis?style=flat-square) ![Repo size](https://img.shields.io/github/repo-size/shubhyagami/jarvis?style=flat-square) ![License](https://img.shields.io/badge/License-MIT-blue?style=flat-square)

---

## Features

- **Zero setup** — open `index.html` directly or serve the folder with any static server.
- **Native Web Speech** — speech recognition and synthesis are handled by the browser itself.
- **Modular skill system** — add or remove functionality by dropping JavaScript files into `skills/`.
- **Live UI** — neon HUD, animated waveform, and an animated avatar.
- **Fully configurable** — wake word, colors, avatar, voice, and more are set in `config.js`.

## At a Glance

- ~1,300 lines of HTML, CSS, and JavaScript
- 12 built-in skills
- 50+ recognized commands
- Average response time under 200 ms

---

## Getting Started

> Modern browsers only allow microphone access on secure origins (HTTPS or `localhost`), so run the app through a local server:

```bash
git clone https://github.com/shubhyagami/jarvis.git
cd jarvis
python -m http.server   # or: npx serve
```

Open the printed URL (`http://localhost:8000`) in a modern browser, grant microphone permission, and say the wake word (default: **"Hey JARVIS"**). The wake word can be changed in `config.js`.

---

## How It Works

1. JARVIS listens for voice input via the Web Speech API.
2. Once the wake word is detected, the words that follow are treated as a command.
3. The command is matched against the available skills in `skills/`.
4. The matching skill's `run(state, command)` function executes, and its result (a string or an `HTMLElement`) is spoken and/or displayed.

**Supported browsers:** Chrome ≥ 49, Edge ≥ 79, Firefox ≥ 52, Safari ≥ 10.1.

---

## Configuration

| Setting          | Where                  | Example                        |
|------------------|------------------------|--------------------------------|
| Wake word        | `config.js`            | `wakeWord: "Hey JARVIS"`       |
| Primary color    | `config.js`            | `primaryColor: "#0bd"`         |
| Avatar image     | `assets/avatars/avatar.png` | Replace `avatar.png`      |
| Voice feedback   | UI settings panel      | Toggle "Speak response"        |

---

## Adding a New Skill

1. Create `skills/yourSkill.js`.
2. Export a `run(state, command)` function that resolves with a string or an `HTMLElement`:

```js
export function run(state, command) {
  // Your logic here
  return Promise.resolve("Skill result");
}
```

3. Reload the app — the new skill is picked up automatically.

---

## Contributing

1. Fork the repository.
2. Create a feature branch: `git checkout -b feature/your-feature`.
3. Commit and push, then open a pull request against `main`.
4. Run `npm run lint` before submitting.

Improvements to documentation, new skills, and refactors are all welcome.

---

## Changelog

| Date       | Change                                                                                    |
|------------|-------------------------------------------------------------------------------------------|
| 2026-10-02 | README rewritten and reorganized.                                                         |
| 2026-09-07 | README cleanup; added contribution guidelines.                                            |
| 2026-09-04 | Minor wording improvements.                                                               |
| 2026-08-21 | Added live weather command; fixed mobile UI overlap; reduced memory usage by 15%.        |

---

## License

Released under the [MIT License](LICENSE).
