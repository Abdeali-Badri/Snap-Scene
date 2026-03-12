🎬 Snap-Scene — AI-Powered Text-to-Video Generation
An end-to-end generative AI system that converts text prompts or story inputs into videos — powered by locally hosted Stable Diffusion with two distinct generation approaches explored and compared.

![Python](https://img.shields.io/badge/Python-3.11+-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Stable Diffusion](https://img.shields.io/badge/Stable%20Diffusion-Local%20Hosted-FF6B35?style=for-the-badge)
![OpenCV](https://img.shields.io/badge/OpenCV-Image%20Processing-5C3EE8?style=for-the-badge&logo=opencv&logoColor=white)
![Jupyter](https://img.shields.io/badge/Jupyter-Notebook-F37626?style=for-the-badge&logo=jupyter&logoColor=white)
![Google Colab](https://img.shields.io/badge/Google%20Colab-GPU%20Pipeline-F9AB00?style=for-the-badge&logo=googlecolab&logoColor=white)
![pytest](https://img.shields.io/badge/pytest-Tested-0A9EDC?style=for-the-badge&logo=pytest&logoColor=white)
![uv](https://img.shields.io/badge/Package%20Manager-uv-DE5FE9?style=for-the-badge)
![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)

# Overview :-
Snap-Scene is a text-to-video generative AI project that explores how to produce short AI-generated videos from text prompts. The project went through two distinct approaches before arriving at the final solution:
1) Approach 1 — Dataset-based generation (V1): Generated video frames from a custom image dataset and stitched them into a video. While functional, the output resembled a slideshow rather than a smooth video due to lack of temporal consistency between frames.
2) Approach 2 — Locally hosted Stable Diffusion (Final): To solve the slideshow problem, Stable Diffusion was locally hosted and used to generate temporally coherent frames with consistent style and motion. This produced significantly smoother and more realistic video output. The Stable Diffusion pipeline is available in the ```colab (optional)``` folder.
This project demonstrates real problem-solving progression — identifying the limitations of an initial approach and engineering a better solution from scratch.

## Key Features

- 🎥 **Text-to-video generation** from natural language prompts
- 🧠 **Locally hosted Stable Diffusion** — no API dependency, full control over generation
- 🗄️ **Custom dataset built from scratch** — manually curated and prepared own image dataset for the V1 generation pipeline
- 🔄 **Two approaches documented** — dataset-based V1 and SD-powered final version
- 🧪 **Unit tested** with `pytest` — production-quality code standards
- 📓 **Colab notebook** for Stable Diffusion pipeline (optional, GPU-accelerated)
- 🗂️ **Modular architecture** — backend, shared utilities, and notebooks separated cleanly
- ⚙️ **Environment config** via `.env` for easy setup

# Tech Stack :-
| Component          | Technology                      |
|--------------------|---------------------------------|
| Video Generation   | Stable Diffusion (Local)        |
| Backend            | Python                          |
| Notebook Pipeline  | Jupyter Notebook / Google Colab |
| Image Processing   | OpenCV / PIL                    |
| Package Manager    | uv                              |
| Testing            | pytest                          |
| Language           | Python 3.11+                    |

# Two Approaches — The Journey :-
V1 — Dataset-Based Video (Slideshow Approach)
```
Text Prompt
    │
    ▼
Custom image dataset → frames selected per prompt keyword
    │
    ▼
Frames stitched into video using OpenCV
    │
    ▼
⚠️ Result: Functional but looked like a slideshow
         (no temporal consistency between frames)
```
V2 — Locally Hosted Stable Diffusion (Final)
```
Text Prompt
    │
    ▼
Locally hosted Stable Diffusion generates frames
    │
    ▼
Consistent style + motion across frames
    │
    ▼
Frames compiled into smooth video
    │
    ▼
✅ Result: Smooth, coherent AI-generated video
```

# Project Structure :-
```
Snap-Scene/
│
├── backend/                # Core Python backend — generation pipeline
├── shared/                 # Shared utilities and helper modules
├── colab (optional)/       # Stable Diffusion video generation notebook (Colab/GPU)
│
├── main.py                 # Entry point — orchestrates the full pipeline
├── pytest.ini              # Pytest configuration
├── requirements.txt        # Python dependencies
├── pyproject.toml          # Project metadata
├── .env                    # Environment variables (API keys, config)
└── .gitignore
```

# Getting Started Prerequisites :-

1) Python 3.11+
2) GPU recommended for Stable Diffusion (or use the Colab notebook)
3) uv (recommended) or pip

# Installation :-
```bash
# Clone the repository
git clone https://github.com/Abdeali-Badri/Snap-Scene.git
cd Snap-Scene
```
# Using uv (recommended) :-
```bash
uv sync
```
# Using pip :-

```bash
pip install -r requirements.txt
```
# Configuration :-
Edit the .env file with your settings:
```bash
# Add your config values here
```
# Run the Pipeline :-
```bash
python main.py
```
# Run with Stable Diffusion (Colab) :-
Open ```colab (optional)``` in Google Colab for GPU-accelerated Stable Diffusion video generation.

# Run Tests :-
```bash
pytest
```

# Future Improvements :-

 1) Audio/narration layer synced to video
 2) Longer video generation with scene transitions
 3) Web UI for prompt input and video preview

## Author

**Abdeali Badri**
[![GitHub](https://img.shields.io/badge/GitHub-Abdeali--Badri-181717?style=for-the-badge&logo=github)](https://github.com/Abdeali-Badri)
