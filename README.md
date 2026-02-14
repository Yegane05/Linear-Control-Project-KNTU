# Liquid Level Control System Project 🎛️💧
Final Project for Linear Control Systems Course - K.N. Toosi University of Technology - Winter 2026
**Instructor:** Dr. Hamid D. Taghirad  

---

## 👥 Authors
* **Rezvan Askari**
* **Yeganeh Tahmasebi**

---

## 🚀 Project Overview
This project involves the modeling, analysis, and controller design for a liquid level control system in a tank. The objective is to design a **PID Controller** to regulate the water level at $H=10m$ while handling physical constraints (valve saturation), measurement noise, and input disturbances.

### Key Features:
- **Modeling:** Non-linear system modeling and linearization.
- **Control:** Tuned PID controller with **Anti-Windup** and **Feedforward** mechanisms.
- **Analysis:** Frequency domain analysis (Bode & Nyquist) and time-domain performance verification.
- **Robustness:** Tested against Gaussian sensor noise and leakage disturbance.

---

## 📂 Repository Structure

The project files are organized into the following directories:

### `Report/`
* Contains the final technical report: **`Final_Report.pdf`**
* Includes detailed mathematical modeling, controller design steps, and simulation results.

### `Presentation/`
* Contains the presentation slides: **`Presentation.pdf`**
* Summary of the project flow, key findings, and diagrams.

### `Video/`
* Demonstration video of the project.

### `Code/` 💻 *(Simulation Files)*
* Contains the MATLAB scripts (`InitFcn.m`) and Simulink models (`Tank_Control_PID.slx`).

### `Report Source/`
* **LaTeX Source Codes:** Contains the `.tex` source files for both the **Technical Report** and the **Presentation Slides** (Beamer), along with necessary fonts and images.

---

## 📊 Results Snapshot
- **Steady State Error:** 0
- **Settling Time:** Optimized within physical limits.
- **Disturbance Rejection:** The system successfully rejects the step disturbance applied at $t=30s$.
