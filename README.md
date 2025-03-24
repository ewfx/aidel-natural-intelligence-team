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

# 🎯 Introduction
Our hackathon project focuses on developing a Python-based API for entity risk analysis in bank transactions.

---

## 🎥 Demo

🔗 [Local Video Demo](https://github.com/ewfx/aidel-natural-intelligence-team/raw/refs/heads/develop/artifacts/demo/Demo%20Recording(Trimmed)%202025-03-23%20111113.mp4)  
📹 [Google Cloud Video Demo](https://github.com/ewfx/aidel-natural-intelligence-team/raw/refs/heads/develop/artifacts/demo/Google%20Cloud%20API%20Demo%20Trimmed.mp4)  
🖼️ [Screenshots](https://github.com/ewfx/aidel-natural-intelligence-team/raw/refs/heads/develop/artifacts/demo/Testing.docx)

---

## 💡 Inspiration
Generative AI is a new buzz in the market. If properly leveraged, it can help increase accuracy in risk and compliance analysis.

---

## ⚙️ What It Does
This API extracts and evaluates entities such as **companies and individuals**, assessing them against multiple risk factors, including:
- 🛑 **Sanctions & AML compliance**
- 🔍 **VPN usage detection**
- 🚨 **Fraudulent entity detection**
- 📰 **Adverse news screening**
- 🏢 **Corporate reports & due diligence**

The system provides a **risk and compliance rating**, helping organizations detect and prevent illicit financial activities while ensuring regulatory compliance. It processes transaction data as input and generates a **structured risk assessment report in JSON format**, enabling seamless integration with compliance workflows.

---

## 🛠️ How We Built It
Our project leverages a modern tech stack to ensure **scalability, performance, and AI-driven risk analysis**:

- **🖥️ Backend API:** Developed using **Python** with **FastAPI**, deployed on **Uvicorn** for high-performance asynchronous processing.
- **🧠 AI/LLM Integration:** Utilizes **OpenRouter** to access **DeepSeek** and **Llama 3.1 NVIDIA 70B** models for advanced entity recognition and risk assessment.
- **📊 Data Processing:** Extracts structured and unstructured data from bank transactions, analyzing it for compliance risks.
- **☁️ Deployment:** Hosted on a cloud environment, ensuring seamless API accessibility and real-time processing.
- **📄 Output Format:** Generates **JSON-based risk reports** for easy integration with regulatory and compliance systems.

---

## 🚧 Challenges We Faced
One major challenge was finding a **reliable, free Generative AI API** for entity risk analysis. Initially, we explored OpenAI and Meta AI APIs, but none offered suitable free-tier access.

After extensive testing, we found **OpenRouter**, which provided access to high-quality free models, including **DeepSeek and NVIDIA Llama 3.1 70B**. Many other free models fell short in delivering accurate risk assessments, but these models met our expectations, enabling effective **entity recognition and risk evaluation** within our API.

---

## 🏃 How to Test Cloud API
The API has been deployed in the cloud. You can access it using the **Swagger API documentation**:

🔗 [Swagger Documentation](https://nitriskanalysis-75609355859.us-east4.run.app/docs)

### Steps to Test:
1. Open the Swagger documentation.
2. Click on the **/entity/assessment** API.
3. Click on Try it Out button
4. Click on **Choose File** and upload a JSON file with structured or unstructured bank transaction details.
5. Click **Execute** and wait for the response (**Processing time: A few seconds to minutes**).
6. Verify the risk assessment results.

---

## 🏃 How to Run Locally
### 1️⃣ Clone the Repository
```sh
git clone https://github.com/ewfx/aidel-natural-intelligence-team.git
```

### 2️⃣ Install Dependencies
```sh
cd aidel-natural-intelligence-team/backend/src
pip install --no-cache-dir -r requirements.txt
```

### 3️⃣ Run the API Locally
```sh
uvicorn main:app --reload
```

📌 **Access the API Swagger Document at:** [http://localhost:8000/docs](http://localhost:8000/docs)

---

## 🏗️ Tech Stack
- 🔹 **Frontend:** NA
- 🔹 **Backend:** FastAPI
- 🔹 **Database:** NA
- 🔹 **AI Models:** OpenRouter API for model access / DeepSeek / NVIDIA Llama 3.1 70B
- 🔹 **Cloud Hosting:** Google Cloud Run
- 🔹 **Dev Tools:** Visual Studio Code, Python
  
---

## 👥 Team
- **Rajesh Hegde** (rajeshhegde8)
- **Sowmya Ambala**
- **Mansur**
- **Chiranjeevi**
- **Sanjeev**
