# 🚀 Credit Card Fraud Detection - End-to-End MLOps Project

---

## 📌 Project Overview

This project demonstrates a **production-grade MLOps pipeline** for detecting fraudulent credit card transactions.

It covers the complete lifecycle of a Machine Learning system:

- Data Ingestion from MongoDB  
- Data Validation & Transformation  
- Model Training & Evaluation  
- Model Versioning with AWS S3  
- Deployment using Docker & AWS EC2  
- CI/CD using GitHub Actions  

---

## 🏗️ Architecture

```
MongoDB Atlas → Data Ingestion → Data Validation → Data Transformation
      ↓
 Model Training → Model Evaluation → Model Registry (AWS S3)
      ↓
   Model Deployment (Docker + EC2)
      ↓
   Prediction Pipeline (FastAPI App)
```

---

## ⚙️ Tech Stack

### 💻 Programming & Frameworks
- Python 3.10  
- FastAPI  
- Scikit-learn  
- Pandas, NumPy  

### ☁️ Cloud Services
- AWS S3  
- AWS EC2  
- AWS ECR  
- AWS IAM  

### 🗄️ Database
- MongoDB Atlas  

### 🔄 MLOps & DevOps
- Docker  
- GitHub Actions  
- Self-hosted Runner  

---

## ✨ Features

- ✅ End-to-End ML Pipeline  
- ✅ Modular Code Structure  
- ✅ MongoDB Integration  
- ✅ Automated Training Pipeline  
- ✅ Model Versioning (S3)  
- ✅ CI/CD Pipeline  
- ✅ Dockerized Application  
- ✅ FastAPI Deployment  

---

## 📂 Project Structure

```
├── src/
│   ├── components/
│   ├── configuration/
│   ├── data_access/
│   ├── entity/
│   ├── aws_storage/
│
├── notebook/
├── static/
├── templates/
├── app.py
├── requirements.txt
├── Dockerfile
├── .github/workflows/
```

---

## 🔧 Setup Instructions

### 1️⃣ Environment Setup

```
conda create -n vehicle python=3.10 -y
conda activate CreditCardFraudDetection
pip install -r requirements.txt
```

---

### 2️⃣ MongoDB Setup

- Create project in MongoDB Atlas  
- Create cluster (M0 Free Tier)  
- Add IP: `0.0.0.0/0`  
- Get connection string  

```
export MONGODB_URL="your_connection_string"
```

---

### 3️⃣ Run Project

```
python demo.py
```

---

## 🐳 Docker

```
docker build -t fraud-detection .
docker run -p 5080:5080 fraud-detection
```

---

## 🚀 Live App

```
http://<EC2-PUBLIC-IP>:5080
```

---

## 👨‍💻 Author

**Shubh Patel**  
B.Tech CSE | AI/ML Enthusiast  

---

⭐ Star this repo if you found it useful!
