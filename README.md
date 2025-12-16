# DevOps CI/CD Pipeline Running on Kubernetes

## 📌 Project Overview
This project demonstrates a real-world DevOps CI/CD pipeline for a Python application using modern DevOps tools.
Developed an end-to-end CI/CD pipeline using GitHub Actions, Docker, and Kubernetes to automate testing, containerization, and deployment of a Python application.

## 🛠 Tech Stack
- Python
- Pytest
- Git & GitHub
- GitHub Actions (CI)
- Docker
- Kubernetes (Kind)

## 🚀 Features
- Automated CI pipeline with GitHub Actions
- Unit testing with Pytest
- Dockerized Python application
- Kubernetes deployment using Deployment & Service
- Application exposed using port-forwarding

## Complete Idea 
- The developer writes a simple Python application on a local machine
- The code is pushed to a GitHub repository using Git
- GitHub Actions automatically starts a CI pipeline on every push
- The pipeline installs dependencies and runs unit tests using Pytest
- If tests pass, a Docker image of the application is built
- The Docker image contains the app and all required dependencies
- The image is loaded into a local Kubernetes cluster (Kind)
- Kubernetes Deployment creates and manages the application Pod
- A Kubernetes Service exposes the application internally
- The app is accessed locally using kubectl port-forward in a browser

