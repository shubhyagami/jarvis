# JARVIS

![HTML5](https://img.shields.io/badge/HTML5-E34F26?style=flat-square&logo=html5&logoColor=white)
![CSS3](https://img.shields.io/badge/CSS3-1572B6?style=flat-square&logo=css3&logoColor=white)
![JavaScript](https://img.shields.io/badge/JavaScript-F7DF1E?style=flat-square&logo=javascript&logoColor=black)
![License](https://img.shields.io/badge/license-MIT-blue?style=flat-square)
![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen?style=flat-square)

A browser-based AI assistant inspired by J.A.R.V.I.S. Built entirely with vanilla HTML, CSS, and JavaScript, it processes voice commands locally without relying on a backend server.

## ✨ Features

- **Voice Recognition:** Listens and responds to natural language commands.
- **Zero Setup:** No build tools or dependencies required. Just open `index.html`.
- **Client-Side Processing:** All logic executes locally in the browser with minimal latency.
- **Privacy First:** Microphone audio and commands never leave your machine.
- **Modular Skill System:** Add new capabilities by dropping a `.js` file into the `/skills` directory.
- **Retro-Futuristic UI:** Neon HUD aesthetic with real-time audio waveform visualizations.
- **Customizable:** Modify the color scheme, wake word, and avatar via standard config files.

## 🚀 Getting Started

1. **Clone the repository:**
   ```bash
   git clone https://github.com/shubhyagami/jarvis.git
   ```
2. **Launch the app:** Open the project folder and double-click `index.html` to open it in your preferred browser.
3. **Grant microphone access:** Your browser will prompt for microphone permissions. Allow it to enable voice interaction.
4. **Speak a command:** Try saying *"Hello JARVIS."* or *"What's the time?"*

## 🛠️ Architecture

The application uses an event-driven pipeline: **Listen → Parse → Match → Execute → Respond**.

```mermaid
flowchart LR
    A[You speak] --> B[Microphone]
    B --> C[Speech Recognition API]
    C --> D[Command Parser]
    D --> E{Match Skill?}
    E -- Yes --> F[Execute Skill]
    E -- No --> G[Fallback Response]
    F --> H[Voice / Visual Output]
    G --> H
```

## 💡 Configuration

You can customize JARVIS by modifying `config.js` in the root directory:

- **Wake Word:** Defaults to *"Jarvis"*, but can be changed to any trigger word you prefer.
- **Voice Feedback:** Spoken responses can be toggled on or off via the settings panel (the gear icon in the top-right corner of the UI).
- **Custom Skills:** Create a new `.js` file in the `/skills` folder following the existing module structure. The app will automatically load it on startup.

## 📊 Project Stats

| Metric | Value |
|--------|-------|
| **Lines of Code** (HTML/CSS/JS) | 1,250+ |
| **Built-in Skills** | 12 |
| **Recognized Voice Commands** | 50+ |
| **Average Response Time** | < 200ms |
| **Browser Support** | Chrome, Edge, Firefox, Safari |

## 📅 Changelog

### 2026-08-21
- **Docs:** Cleaned up README formatting and improved clarity.
- **Refactor:** Standardized module exports in the `/skills` directory for easier custom additions.

### 2026-08-06
- **New voice command:** *"What's the weather?"* – JARVIS now fetches live weather data (requires internet).
- **Fixed:** Mobile UI glitch where the waveform animation would overlap the command history.
- **Performance:** Reduced memory footprint by 15% through optimized skill loading.

---

*JARVIS – Always at your service.*
