# 🎹 Music Scale & Chord Finder

A Python-based music theory engine designed to identify scales and chords from user-provided notes. 

## 🚀 Overview
This tool allows musicians and developers to input a set of notes and instantly discover:
1. **Scale Matching:** Which musical scales (Major, Minor, Dorian, etc.) contain these notes.
2. **Chord Identification:** (Feature 3) Recognizing specific triads and seventh chords.
3. **Robust Input:** Handles various formats (spaces, commas, case-sensitivity).

## 🛠️ Features & Logic
- **Pattern Matching:** Utilizes Set Theory (`issubset`) to compare user input against predefined scale intervals.
- **Data Normalization:** Employs `.strip()`, `.capitalize()`, and `.split()` to ensure clean data processing.
- **Modulo Arithmetic:** Uses `(root + interval) % 12` to handle the circular nature of musical notes (the "Musical Clock").

## 📁 Status
- [x] Feature 1: Root-based Scale Finder


## 💻 Usage
```bash
python scale_finder.py
