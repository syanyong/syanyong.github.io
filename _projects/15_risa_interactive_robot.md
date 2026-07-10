---
layout: page
title: "RISA: A Human-Engaging Agentic Robotic Interactive Assistant"
description: "An interactive robotic assistant tailored for guided lab tours, built from scratch using a prototype robot from the RoboCup Japan Open 2024, Logistics League. RISA is a research agentic framework that leverages custom tools and Model Context Protocol (MCP) to give the LLM a physical presence. It combines Retrieval-Augmented Generation (RAG) with facial recognition for personalized, highly accurate human engagement."
img: assets/img/risa.png
importance: 2
category: capstone
team: "Mrs. Chatchaya Miyamoto, Mr. Phoomiphat Kittisuphat, Mr. Siripong Boonsiri, Mr. Sivakorn Samorkam"
advisor: "Dr. Sarucha Yanyong"
brain: "Llama 3.2 & Mistral"
database: "ChromaDB + MongoDB"
navigation: "ROS1 Noetic, LiDAR, IMU"
speech: "OpenAI Whisper, Botnoi Voice API"
vision: "YOLOv5s, DeepFace"
performance: "Hybrid RAG + LLM"
safety: "80% Avoidance Success"
year: 2024
---

## RISA: A Human-Engaging Robotic Interactive Assistant

**Full Project Title**: A Human-Engaging Robotic Interactive Assistant (RISA)  
**Advisor**: Dr. Sarucha Yanyong  
**Team Members**:

- **Chatchaya Miyamoto** (64011373): LLM and RAG
- **Phoomiphat Kittisuphat** (64011550): Control and Navigation
- **Siripong Boonsiri** (64011620): ASR and TTS
- **Sivakorn Samorkam** (64011625): Design and assembly

---

### 1. Project Overview & Requirements

RISA is an interactive robotic assistant designed for lab tours, addressing scalability and adaptability challenges in human-centric spaces. It features multimodal operation, AI-driven speech and gesture recognition, LiDAR-based navigation, and a RAG system for accurate responses.

- **Objective**: Create an always-available robot that can provide information to visitors, eliminating human-related inconsistencies.
- **Key Features**: Continuous patrolling, chatbot for general/specific questions, face recognition, real-time visual feedback, and lab navigation with a sound guide.

---

### 2. System Architecture

The system is structured around three core functional components: Speech Processing, Knowledge Retrieval and Response Generation, and Navigation & Interaction.

#### AI Processing Pipeline (End-to-End)

1. **Speech Processing**: Captures user input through a Fifine Condenser Microphone. Automatic Speech Recognition (ASR) uses OpenAI's `Whisper` to convert speech to text.
2. **Knowledge Retrieval (RAG)**: Integrates `Chroma DB` (Vector Database) for embedded knowledge chunks and `MongoDB` for structured curriculum data.
3. **Response Generation**: Uses a hybrid approach combining `Mistral` (for speed and summarization efficiency via Grouped-Query Attention) and `Llama 3.2` (for fact-checking and multi-document retrieval).
4. **Text-to-Speech (TTS)**: Synthesizes speech using the `Botnoi Voice API` for natural-sounding Thai/multilingual responses, played through Creative Pebble Speakers.
5. **Vision & Face Recognition**: Utilizes a webcam with `YOLOv5s` for >80% accuracy in human detection and `DeepFace` (VGG-Face) for facial recognition to provide personalized interaction.

---

### 3. Hardware & Navigation

The robot operates on a dual-processing setup, utilizing both a Raspberry Pi 4B and an Edge Computing laptop.

- **Primary Node**: `Raspberry Pi 4B` handles core ROS node management, motor control coordination, and sensor data integration.
- **Navigation Sensors**: `RPLiDAR A1` provides 360-degree environmental laser scanning and real-time obstacle detection. An `IMU` tracks robot orientation and motion state.
- **ROS Navigation Stack**: Implements `AMCL` for localization, `Costmap 2D` (global and local) for obstacle avoidance, and Dijkstra's/A\* algorithms for path planning.
- **Physical Design**: The robot features a 4-floor cylindrical structure (44cm diameter) 3D-printed using PLA material, housing the batteries, LiDAR, processing boards, and an LCD screen on a top-level extension rod.

---

### 4. Performance & Evaluation Metrics

The system underwent rigorous testing across multiple domains:

#### Navigation Performance

- **Average path planning time**: 1.0 second
- **Path optimization success rate**: 70%
- **Average position error**: 8 cm
- **Obstacle avoidance success rate**: 80%

#### AI Evaluation

- **Face Recognition**: 70-75% accuracy with the recommended minimum dataset size.
- **Human Detection (YOLOv5s)**: >90% accuracy for clear, front-facing subjects in natural indoor light.
- **LLM with RAG**: Successfully retrieved and generated accurate responses for most factual questions based on program-specific knowledge, such as course credits and department heads.
