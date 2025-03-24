# 🚀 Bank Transaction Risk and Compliance Analysis API

## 📌 Table of Contents
- [Introduction](#introduction)
- [Demo](#demo)
- [Inspiration](#inspiration)
- [What It Does](#what-it-does)
- [How We Built It](#how-we-built-it)
- [Challenges We Faced](#challenges-we-faced)
- [How to Run](#how-to-run)
- [Tech Stack](#tech-stack)
- [Team](#team)

---

## 🎯 Introduction
Our hackathon project focuses on developing a Python-based API for entity risk analysis in bank transactions. 

## 🎥 Demo
🔗 [Live Demo](#) (if applicable)  
📹 [Video Demo](#) (if applicable)  
🖼️ Screenshots:

![Screenshot 1](link-to-image)

## 💡 Inspiration
Generative AI is a new buzz in market. If properly leveraged it can help to increase accuracy in risk and compliance analysis.

## ⚙️ What It Does

This API will extract and evaluate entities such as companies and individuals, assessing them against multiple risk factors, including sanctions, anti-money laundering (AML), VPN usage, fraudulent entities, adverse news, and corporate reports. 

By providing a risk and compliance rating, the system will help organizations detect and prevent illicit financial activities, ensuring regulatory compliance. The API will process transaction data as input and generate a structured risk assessment report in JSON format, enabling seamless integration with compliance workflows.

## 🛠️ How We Built It
Our project leverages a modern tech stack to ensure **scalability, performance, and AI-driven risk analysis**:  

- **Backend API**: Developed using **Python** with **FastAPI**, deployed on **Uvicorn** for high-performance asynchronous processing.  
- **AI/LLM Integration**: Utilizes **OpenRouter** to access **DeepSeek** and **Llama 3.1 NVIDIA 70B** models for advanced entity recognition and risk assessment.  
- **Data Processing**: Extracts structured and unstructured data from bank transactions, analyzing it for compliance risks.  
- **Deployment**: Hosted on a cloud environment, ensuring seamless API accessibility and real-time processing.  
- **Output Format**: Generates **JSON-based risk reports** for easy integration with regulatory and compliance systems.

## 🚧 Challenges We Faced

One of the major challenges we faced was finding a reliable, free Generative AI API for entity risk analysis. We initially explored OpenAI and Meta AI APIs, but none offered free-tier access suitable for our needs. After extensive testing, we found OpenRouter, which provided access to a few high-quality free models, including DeepSeek and NVIDIA Llama 3.1 70B. While we evaluated other free models, most fell short in delivering accurate risk assessments. OpenRouter’s models, however, met our expectations, enabling effective entity recognition and risk evaluation within our API.


## 🏃 How to Access Cloud API

This API has been deployed in cloud. You can access using below Swagger API.
https://nitriskanalysis-75609355859.us-east4.run.app/docs

It will open Swagger Documentation of the API
Click on /entity/assessment API
Click on choose file
Browse and select structured or unstructured json which contains bank transaction details
Click on Execute
Wait till response comes from API (It could take few seconds to few minutes for the risk analysis.)
Verify the data

## 🏃 How to Run
1. Clone the repository  
   ```sh
   git clone https://github.com/ewfx/aidel-natural-intelligence-team.git
   ```
2. Install dependencies  
   ```sh
   cd aidel-natural-intelligence-team\backend\src
   pip install --no-cache-dir -r requirements.txt
   ```
3. Run the project  
   ```sh
   uvicorn main:app --reload
   ```
Access API Swagger Document at http://localhost:8000/docs

## 🏗️ Tech Stack
- 🔹 Frontend: NA
- 🔹 Backend: FastAPI
- 🔹 Database: NA
- 🔹 Other: OpenRouter API / DeepSeek or NVIDIA LLama 3.1 70B

## 👥 Team
- Rajesh Hegde (rajeshhegde8)
- Sowmya Ambala
- Mansur
- Chiranjeevi
- Sanjeev