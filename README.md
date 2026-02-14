# Pursuit Curve Visualizer 🎯

A high-performance Python visualization tool built with **Pygame** to simulate and animate mathematical pursuit curves. This project allows users to explore how "chasers" react to the movement of "targets" in real-time, creating complex geometric patterns and organic-looking motion.



## 🚀 Features

* **Real-time Simulation:** Watch pursuit patterns emerge dynamically at 60 FPS.
* **Multiple Modes:** Support for "Mice Problems" (polygon pursuit) and "Lead-Follow" dynamics.
* **Customizable Parameters:** Easily adjust velocity, acceleration, and the number of entities.
* **Vector Math:** Built using `pygame.math.Vector2` for clean, accurate physics.

## 🧠 What are Pursuit Curves?

A **curve of pursuit** is a curve constructed by analogy to having an object or "pursuer" at a point $P$ chasing an object or "target" at a point $T$. The pursuer's velocity vector always points directly toward the target.

### The Physics
The motion is governed by the differential equation:
$$\frac{dy}{dx} = \frac{y - y_t}{x - x_t}$$

Where $(x, y)$ is the position of the pursuer and $(x_t, y_t)$ is the position of the target.

---

## 🛠️ Installation

1. **Clone the repository:**
   ```bash
   git clone [https://github.com/TayyibMohammad/Pursuit-Curves-Visualized.git](https://github.com/YOUR_USERNAME/pursuit-curve-visualizer.git)
   cd pursuit-curve-visualizer
