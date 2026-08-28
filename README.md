# JARVIS – Your Personal Browser‑Based AI Assistant  

![HTML5](https://img.shields.io/badge/HTML5-E34F26?style=flat-square&logo=html5&logoColor=white)  
![CSS3](https://img.shields.io/badge/CSS3-1572B6?style=flat-square&logo=css3&logoColor=white)  
![JavaScript](https://img.shields.io/badge/JavaScript-F7DF1E?style=flat-square&logo=javascript&logoColor=black)  
![License](https://img.shields.io/badge/license-MIT-blue?style=flat-square)  

A lightweight web app that brings a conversational assistant to the browser, inspired by J.A.R.V.I.S. from the Iron Man universe.

---  

## Overview  

JARVIS is a pure‑client side assistant built with HTML5, CSS3, and JavaScript. No server, no build tools, and no external dependencies—just drop the repository into a browser and start interacting.  

## Key Features  

- **Voice Recognition** – Uses the Web Speech API to understand natural‑language commands.  
- **Zero‑Setup Experience** – Open `index.html` and you’re ready; the app runs entirely in the browser.  
- **Modular Skill System** – Add new capabilities by placing a `.js` file in `/skills`. The assistant automatically loads and registers each skill.  
- **Retro‑Futuristic UI** – Neon HUD aesthetic with live audio waveform visualizations.  
- **Customizable** – Tweak wake word, color scheme, avatar, and response preferences via `config.js`.  

## Getting Started  

1. **Clone the repo**  
   ```bash
   git clone https://github.com/shubhyagami/jarvis.git
   cd jarvis
   ```  

2. **Open the app**  
   Double‑click `index.html` or serve the folder with any static server (e.g., `python -m http.server`).  

3. **Allow microphone access**  
   The browser will prompt for permission; grant it to enable voice input.  

4. **Start talking**  
   Say “Hey JARVIS” or any supported command such as “What’s the time?”  

## Supported Browsers  

- Chrome (recommended)  
- Microsoft Edge  
- Firefox  
- Safari  

> **Note:** Some advanced voice features may behave slightly differently on Safari or Firefox.  

## Architecture  

```
User speaks → Microphone → Speech Recognition API → Command Parser → 
   ├─ Skill Match? → Execute Skill → Voice / Visual Output
   └─ No Match → Fallback Response → Voice / Visual Output
```  

The pipeline is event‑driven and fully asynchronous, ensuring a responsive experience.  

## Customization  

- **Wake Word** – Edit `config.js` to set any trigger phrase you prefer.  
- **Voice Feedback** – Toggle spoken responses on or off via the settings gear icon.  
- **Add Skills** – Create a new file in `/skills` that exports a function matching the skill contract. The app loads all such modules automatically on startup.  

## Project Statistics  

| Metric | Value |
|--------|-------|
| Lines of Code (HTML/CSS/JS) | 1,250+ |
| Built‑in Skills | 12 |
| Recognized Commands | 50+ |
| Average Response Time | < 200 ms |
| Browser Support | Chrome, Edge, Firefox, Safari |
| License | MIT |

## Changelog  

### 2026‑08‑21  
- Cleaned up README formatting for readability.  
- Standardized skill module exports for easier extension.  

### 2026‑08‑06  
- Added live weather command (“What’s the weather?”).  
- Fixed mobile UI overlap in waveform animation.  
- Reduced memory usage by 15 % through optimized skill loading.  

---  

*JARVIS – Always at your service.*
