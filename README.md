# 🎹 Music Scale & Chord Finder

A Python-based music theory engine designed to identify scales and chords from user-provided notes. This project serves as the foundational "Phase 1" project for **Roadmap 2: AI, ML, DL, and NLP**.

## 🚀 Overview
This tool allows musicians and developers to input a set of notes and instantly discover:
1. **Scale Matching:** Which musical scales (Major, Minor, Dorian, etc.) contain these notes.
2. **Chord Identification:** (Feature 3) Recognizing specific triads and seventh chords.
3. **Robust Input:** Handles various formats (spaces, commas, case-sensitivity).

## 🛠️ Features & Logic
- **Pattern Matching:** Utilizes Set Theory (`issubset`) to compare user input against predefined scale intervals.
- **Data Normalization:** Employs `.strip()`, `.capitalize()`, and `.split()` to ensure clean data processing.
- **Modulo Arithmetic:** Uses `(root + interval) % 12` to handle the circular nature of musical notes (the "Musical Clock").

## 📁 Roadmap Status
- [x] Feature 1: Root-based Scale Finder
- [x] Version Control: GitHub Repository Integration
- [ ] Feature 2: Probability/Fuzzy Matching (Upcoming)
- [ ] Feature 3: Full Chord Library Integration (Upcoming)

## 💻 Usage
```bash
python scale_finder.py
