# 🌌 Page Visit Tracker — A Celestial Web App

This is a dynamic, visually engaging web application that tracks the number of visits to the page in real time. It features:

- An **hourly-updating bar chart** to visualize traffic trends
- A **celestial, moving background** that adds flair
- **Glowing text and UI elements** for an immersive aesthetic
- Fully **Dockerized setup** for consistent development and deployment

---

## 🚀 Why I Built This

This project was part of my learning journey at **CoderCo** — a space that encourages hands-on development and creative exploration.

I wanted to build something that wasn't just functional, but fun and visually different. So I combined:
- Real-time data tracking
- A custom, glowing UI with animated effects
- And Docker, to learn how to deploy and manage containerized apps

The goal was to challenge myself to build a full-stack app from scratch, containerize it, and make it look... out of this world ✨

---

## 🛠️ Tech Stack

- **Frontend:** HTML, CSS, JavaScript
- **Backend:** Node.js / Express
- **Database:** (e.g., SQLite / JSON / custom file logging)
- **Charting:** Chart.js (or your chosen library)
- **Containerization:** Docker

---

## 🧠 What I Struggled With

### ⚙️ Docker
- Setting up the right configuration for my containers took more effort than expected.
- Learning to write and debug Dockerfiles and Compose files was a valuable (but sometimes painful) experience.
- Managing volumes and persistent data within containers pushed me to think more like a DevOps engineer.

### 🔄 Syncing Data
- Making sure visit counts were accurately logged and updated every hour was harder than it sounded.
- I explored different storage approaches to ensure the data persisted even after restarts.

### 📊 Real-time Bar Chart
- Figuring out how to structure the data per hour and update the chart automatically required a mix of backend logic and frontend tricks.

### 🎨 UI + Animation
- Getting the background animation to look smooth across devices wasn’t trivial.
- Making the glowing text readable but still cool-looking took a lot of CSS tweaking.

---

## 🧩 What I Learned

- How to **containerize a full-stack web app** from development to deployment
- Why Docker is so powerful for creating predictable environments
- Practical frontend/backend communication and working with persistent data
- That aesthetics and interactivity go a long way when presenting data

---

## 🐳 Why Docker Made a Difference

- No more "it works on my machine" — everything runs the same no matter where it's deployed
- I could rebuild, test, and deploy the entire app in seconds
- Helped me understand the real-world importance of containerization and reproducible dev environments

---

## 📦 How to Run

```bash
# Clone the repo
git clone https://github.com/your-username/page-visit-tracker.git
cd page-visit-tracker

# Build and run with Docker
docker-compose up --build
