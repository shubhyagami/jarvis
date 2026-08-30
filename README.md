# JARVIS – Your Personal Browser‑Based AI Assistant  

![HTML5](https://img.shields.io/badge/HTML5-E34F26?style=flat-square&logo=html5&logoColor=white)  
![CSS3](https://img.shields.io/badge/CSS3-1572B6?style=flat-square&logo=css3&logoColor=white)  
![JavaScript](https://img.shields.io/badge/JavaScript-F7DF1E?style=flat-square&logo=javascript&logoColor=black)  
![License](https://img.shields.io/badge/license-MIT-blue?style=flat-square)  

A lightweight, pure‑client web app that brings a conversational assistant to the browser. Inspired by J.A.R.V.I.S. from the Iron Man universe, JARVIS runs entirely on the client—no server, no build tools, and no external dependencies. Open `index.html` and start interacting.

---  

## Overview  

JARVIS is a single‑page application built with HTML5, CSS3, and vanilla JavaScript. All processing happens locally, making it ideal for offline use or rapid prototyping. The app listens for voice commands, parses them, and executes modular “skills” you can extend yourself.

## Key Features  

- **Voice recognition** – Uses the Web Speech API for natural‑language input.  
- **Zero‑setup experience** – Open `index.html` directly or serve the folder with any static server.  
- **Modular skill system** – Place a `.js` file in `/skills` to add new capabilities; the app automatically loads and registers each skill.  
- **Retro‑futuristic UI** – Neon HUD aesthetic with live audio‑waveform visualizations.  
- **Customizable** – Adjust wake word, color scheme, avatar, and response preferences via `config.js`.  

## Getting Started  

1. **Clone the repository**  
   ```bash
   git clone https://github.com/shubhyagami/jarvis.git
   cd jarvis
   ```  

2. **Run the app**  
   - Double‑click `index.html` in your file explorer, **or**  
   - Start a simple static server (e.g., `python -m http.server`) in the project directory.  

3. **Grant microphone permission**  
   The browser will request access to the microphone; allow it to enable voice commands.  

4. **Start speaking**  
   Say “Hey JARVIS” or any supported command such as “What’s the time?”  

## Supported Browsers  

- Chrome (recommended)  
- Microsoft Edge  
- Firefox  
- Safari  

Advanced voice features may behave slightly differently on Safari or Firefox.

## Architecture  

```
User speaks → Microphone → Speech Recognition API → Command Parser → 
   ├─ Skill matched? → Execute skill → Voice / visual output
   └─ No match → Fallback response → Voice / visual output
```  

The pipeline is fully asynchronous and event‑driven, delivering a responsive experience.

## Customization  

- **Wake word** – Edit `config.js` to set any trigger phrase you prefer.  
- **Voice feedback** – Toggle spoken responses on or off using the settings icon.  
- **Add skills** – Create a new file in `/skills` that exports a function matching the skill contract. The app loads all such modules automatically on startup.  

## Project Statistics  

| Metric | Value |
|--------|-------|
| Code (HTML/CSS/JS) | 1,250+ lines |
| Built‑in skills | 12 |
| Recognized commands | 50+ |
| Average response time | < 200 ms |
| Browser support | Chrome, Edge, Firefox, Safari |
| License | MIT |

## Changelog  

- **2026‑08‑21** – Cleaned up README formatting and standardized skill module exports for easier extension.  
- **2026‑08‑06** – Added live weather command; fixed mobile UI overlap in waveform animation; reduced memory usage by 15 % through optimized skill loading.  

---  

*JARVIS – Always at your service.*
