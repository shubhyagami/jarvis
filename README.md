# JARVIS – Browser‑Based AI Assistant  

**JARVIS** is a lightweight, pure‑client web application that turns any web browser into a personal AI assistant. Inspired by Iron Man’s J.A.R.V.I.S., the entire app runs locally – no server, no build tools, no external dependencies. Just open `index.html` and start conversing.

![HTML5](https://img.shields.io/badge/HTML5-E34F26?style=flat-square&logo=html5&logoColor=white)  
![CSS3](https://img.shields.io/badge/CSS3-1572B6?style=flat-square&logo=css3&logoColor=white)  
![JavaScript](https://img.shields.io/badge/JavaScript-F7DF1E?style=flat-square&logo=javascript&logoColor=black)  
![License](https://img.shields.io/badge/license-MIT-blue?style=flat-square)

---

## Quick Start

1. **Clone the repo**  
   `git clone https://github.com/shubhyagami/jarvis.git && cd jarvis`

2. **Open the app**  
   *Double‑click `index.html`* or serve the folder with a static server such as  
   `python -m http.server` or `npx serve`.

3. **Grant microphone access** – A browser prompt will appear; allow it.

4. **Speak** – Use the default trigger “Hey JARVIS” (configurable) or any built‑in command like “What’s the time?”.

---

## Supported Browsers

| Browser | Support | Notes |
|---------|---------|-------|
| Chrome  | ✔ | Recommended |
| Edge    | ✔ | Full feature set |
| Firefox | ✔ | Voice recognition may be less accurate |
| Safari  | ✔ | Some advanced features behave slightly differently |

---

## How It Works

1. Microphone captures audio.  
2. Web Speech API turns speech into text.  
3. A lightweight command parser checks the text against a list of skill names.  
4. If a skill matches, its module is executed.  
5. The skill returns a string or an HTML element; the assistant speaks or displays the result.  
6. If no skill matches, a fallback response is shown.

The entire pipeline is asynchronous and event‑driven, keeping the UI responsive.

---

## Key Features

- **Voice recognition** – Uses the Web Speech API for natural‑language input.  
- **Zero‑setup** – Launch by opening `index.html` or any static server.  
- **Modular skill system** – Add a `*.js` file to `/skills` and the app auto‑registers it.  
- **Retro‑futuristic UI** – Neon HUD with live audio waveforms.  
- **Customizable** – Edit `config.js` to change wake word, colors, avatar, and voice settings.  

---

## Customization

| Setting | Where to change | Example |
|---------|-----------------|---------|
| Wake word | `config.js` | `wakeWord: "Hey JARVIS"` |
| Color scheme | `config.js` | `primaryColor: "#0bd"` |
| Avatar | `assets/avatars` | Replace `avatar.png` |
| Speech feedback | UI settings button | Toggle “Speak response” |

---

## Adding a New Skill

1. Create `skills/mySkill.js`.  
2. Export a function that accepts `state` and `command`.  
3. Return a promise that resolves to a string or an HTML element.  

**Skill contract example**  
```js
export function run(state, command) {
  // Perform work
  return Promise.resolve('Skill result');
}
```

The module will be loaded automatically on the next page load.

---

## Project Stats

- Lines of code: ~1,250 (HTML/CSS/JS)  
- Built‑in skills: 12  
- Recognized commands: 50+  
- Avg. response time: <200 ms  
- License: MIT

---

## Changelog

- **2026‑08‑21** – Minor README cleanup, streamlined skill module exports.  
- **2026‑08‑06** – Added live weather command; fixed mobile UI overlap; reduced memory usage by 15 %.  

---

## License

MIT – see the `LICENSE` file.
