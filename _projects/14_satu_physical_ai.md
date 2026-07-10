---
layout: page
title: "SATU: Agentic Physical AI for Human Friends"
description: "An intelligent, autonomous mobile robot designed to serve as a receptionist and human assistant. Built as a research agentic system, it integrates custom tools and Model Context Protocol (MCP) to provide the LLM with a physical, human-like embodiment capable of natural Thai conversation, real-time human detection, and safe autonomous navigation."
img: assets/img/satu2.png
tiktok_url: "https://vt.tiktok.com/ZSHVtfB3H/"
importance: 1
category: capstone
team: "Kirawut Chalermkitpaisan, Krittin Sakharin, Natcha Rungruang, Natwasa Manomaiwiboon"
advisor: "Asst. Prof. Dr. Sarucha Yangyong"
brain: "Typhoon2-70B & Typhoon2-8B"
database: "Milvus Vector DB"
navigation: "ROS 2 Jazzy, Nav2 Stack, RPLiDAR"
speech: "SileroVAD, Typhoon 2 Audio"
vision: "Jetson Nano, SCRFD, ArcFace"
performance: "~2.55s (p50)"
safety: "100% Success Rate"
year: 2025
---

## SATU: Physical AI for Human Friends

**Full Project Title**: LLM-Based Wheel Human Interaction Robot for Receptionist and Human Assistant (RAI 5 Capstone Project, RAI-6518)  
**Advisor**: Asst. Prof. Dr. Sarucha Yangyong  
**Team Members**:

- **Kirawut Chalermkitpaisan** (65011333): ROS, Navigation, Frontend UI, Testing & Optimization
- **Krittin Sakharin** (65011356): End-to-end multi-modal AI processing pipeline, Model evaluation
- **Natcha Rungruang** (65011386): Embedded data collection, RAG, Dockerization
- **Natwasa Manomaiwiboon** (65011402): Electrical systems, Design and calculation, Hardware assembly

---

### 1. Project Overview & Requirements

SATU is an intelligent, autonomous mobile robot designed to serve as a receptionist and human assistant within the university environment.

- **Language**: Thai Conversation
- **Area of Operation**: 9th & 12th Floor Hallways
- **Strict Safety Requirements**: Must safely stop within 30cm of an obstacle.
- **Latency**: First verbal reaction must be within 10 seconds.
- **Interaction**: Fully supports immediate barge-in/interruption capabilities.

> **🎥 Watch SATU in Action:** [Click here to watch the TikTok Demo Video](https://vt.tiktok.com/ZSHVtfB3H/)

---

### 2. System Architecture

Our system is structured across distributed edge nodes and a central AI server to guarantee low latency and responsiveness.

#### AI Processing Pipeline (End-to-End)

1. **Vision Node (Jetson Nano)**: Runs lightweight OpenCV for tracking, `SCRFD` (640x640) for face detection, and `ArcFace` (512-dim) for face recognition. It filters engagements using `ByteTracker` for head pose gating (Yaw < 25°, Pitch < 15°).
2. **Audio & Display Node (Raspberry Pi 5 #1)**: Captures audio at 16kHz mono. Pre-processes using `SileroVAD` (0.73 confidence threshold) as a probability gate. Runs a frontend UI showing robot emotions based on state (Idle, Scanning, Talking, Happy, Thinking).
3. **AI Server (GPU)**:
   - **Grammar Correction**: `Typhoon2-8B` corrects misheard words before logic processing.
   - **Generation**: `Typhoon2-70B` (via vLLM) generates responses strictly driven by the RAG retrieved context.
   - **Text-to-Speech (TTS)**: `Typhoon 2 Audio 8B` synthesizes Thai responses.
4. **Memory Retrieval (RAG)**: Integrates `Milvus` Vector DB (`bge-m3` 1024-dim embeddings) for retrieving University curriculum, timetables, and student profiles from a MySQL database based on facial recognition ID.
5. **Navigation Node (Raspberry Pi 5 #2)**: Executes ROS 2 Jazzy Nav2 stack with AMCL and LiDAR scan matching for drift-free autonomous movement.

---

### 3. Hardware & Power Consumption

The robot employs a dual 24V 12Ah battery setup powering an isolated step-down system (Buck Converters to 5V and 19V).

| Component                        | Operating Voltage | Current | Est. Power |  Load Type   |
| :------------------------------- | :---------------: | :-----: | :--------: | :----------: |
| **Raspberry Pi 5 (x2)**          |        5V         |  5.0A   |    25W     |  Continuous  |
| **Jetson Nano**                  |        19V        |  3.4A   |   64.6W    |  Continuous  |
| **Intel RealSense Depth Camera** |        5V         |  0.8A   |     4W     |  Continuous  |
| **RPLiDAR A1**                   |        5V         |  0.1A   |    0.5W    |  Continuous  |
| **7-inch HDMI Touch Display**    |        5V         |  3.0A   |    15W     |  Continuous  |
| **Motors (x4)**                  |        24V        |  1.7A   |    160W    | Intermittent |

_Estimated Operation Time: ~2 Hours (Ideal Continuous Load), 56 minutes (Worst-Case)._

---

### 4. Performance & Evaluation Metrics

We benchmarked the system across several dimensions including latency, safety, and conversation accuracy:

#### System Latency Breakdown

Using `vLLM` on an `4 x A100` cluster, the system achieved phenomenal speeds:

- **RAG Retrieval**: 50 - 200 ms
- **LLM Generation**: ~2,497 ms (p50)
- **TTS Synthesis**: ~633 ms
- **Total Time to First Reaction**: **~2.55 seconds (p50)** _(Exceeding the <10s requirement)._

#### AI Evaluation Accuracy

- **Intent Accuracy**: 0.955
- **Task Success Rate**: 95%
- **Language Compliance**: 100%

#### Robotics Safety Accuracy

**Test Scenario**: Human jumps across the robot's forward path during navigation.

- **Results**: 25/25 trials successfully detected dynamic intrusion. The robot either completely stopped or replanned an alternative route, ensuring **0 physical contact** across all trials (100% success rate).
