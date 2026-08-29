# JARVIS – Browser‑Based AI Assistant  

![HTML5](https://img.shields.io/badge/HTML5-E34F26?style=flat-square&logo=html5&logoColor=white)  
![CSS3](https://img.shields.io/badge/CSS3-1572B6?style=flat-square&logo=css3&logoColor=white)  
![JavaScript](https://img.shields.io/badge/JavaScript-F7DF1E?style=flat-square&logo=javascript&logoColor=black)  
![License](https://img.shields.io/badge/license-MIT-blue?style=flat-square)  

A lightweight, client‑only web app that brings a conversational assistant to the browser, inspired by J.A.R.V.I.S. from the Iron Man universe. No server, no build tools, and no external dependencies—just drop the repository into a browser and start interacting.

---  

## Overview  

JARVIS is a pure‑client assistant built with HTML5, CSS3, and JavaScript. It runs entirely in the browser, so you can open `index.html` directly or serve the folder with any static server. The assistant uses the Web Speech API for voice recognition and a modular skill system that loads automatically from the `/skills` directory.

---  

## Key Features  

- **Voice Control** – Speech Recognition API interprets natural‑language commands.  
- **Zero‑Setup** – Open `index.html` or serve static files; no installation required.  
- **Modular Skills** – Add new capabilities by placing a `.js` file in `/skills`. The app registers each skill on startup.  
- **Retro‑Futuristic UI** – Neon HUD aesthetic with live waveform visualizations.  
- **Customizable** – Adjust wake word, color scheme, avatar, and response preferences via `config.js`.  
- **Cross‑Browser** – Works in Chrome, Edge, Firefox, and Safari (some features may vary).

---  

## Getting Started  

1. **Clone the repository**  
   ```bash
   git clone https://github.com/shubhyagami/jarvis.git
   cd jarvis
   ```  

2. **Run the app**  
   - Double‑click `index.html` or serve the folder with a static server (e.g., `python -m http.server`).  
   - Grant microphone permission when prompted.  

3. **Activate the assistant**  
   Say “Hey JARVIS” or any supported command such as “What’s the time?”  

---  

## Architecture  

```
User speaks → Microphone → Speech Recognition API → Command Parser → 
   ├─ Skill Match? → Execute Skill → Voice / Visual Output
   └─ No Match → Fallback Response → Voice / Visual Output
```  

The pipeline is fully asynchronous, delivering a responsive experience without blocking the UI.

---  

## Customization  

- **Wake Word** – Edit `config.js` to set a trigger phrase of your choice.  
- **Voice Feedback** – Toggle spoken responses via the settings gear icon.  
- **Add Skills** – Create a new file in `/skills` that exports a function matching the skill contract. The app loads all such modules automatically.  

---  

## Project Statistics  

| Metric | Value |
|--------|-------|
| Total code (HTML/CSS/JS) | 1,250+ |
| Built‑in skills | 12 |
| Recognized commands | 50+ |
| Average response time | < 200 ms |
| Browser support | Chrome, Edge, Firefox, Safari |
| License | MIT |

---  

## Changelog (selected)  

- **2026‑08‑21** – Cleaned up README formatting; standardized skill module exports.  
- **2026‑08‑06** – Added weather command; fixed mobile UI overlap; reduced memory usage by 15 %.  

---  

*JARVIS – Always at your service.*
