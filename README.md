🚀 Credit Card Fraud Detection - End-to-End MLOps Project










📌 Project Overview

This project demonstrates a production-grade MLOps pipeline for detecting fraudulent credit card transactions.

It covers the complete lifecycle of a Machine Learning system, including:

Data Ingestion from MongoDB
Data Validation & Transformation
Model Training & Evaluation
Model Versioning with AWS S3
Deployment using Docker & AWS EC2
CI/CD automation with GitHub Actions
🏗️ Architecture
MongoDB Atlas → Data Ingestion → Data Validation → Data Transformation
      ↓
 Model Training → Model Evaluation → Model Registry (AWS S3)
      ↓
   Model Deployment (Docker + EC2)
      ↓
   Prediction Pipeline (FastAPI App)
⚙️ Tech Stack
💻 Programming & Frameworks
Python 3.10
FastAPI
Scikit-learn
Pandas, NumPy
☁️ Cloud Services
AWS S3 (Model Registry)
AWS EC2 (Deployment)
AWS ECR (Docker Image Storage)
AWS IAM (Security)
🗄️ Database
MongoDB Atlas
🔄 MLOps & DevOps
Docker
GitHub Actions (CI/CD)
Self-hosted Runner (EC2)
✨ Features

✔️ End-to-End ML Pipeline
✔️ Modular Code Structure (Production Ready)
✔️ MongoDB Integration
✔️ Automated Model Training Pipeline
✔️ Model Versioning in S3
✔️ CI/CD Pipeline with GitHub Actions
✔️ Dockerized Application
✔️ Real-time Prediction using FastAPI
✔️ Deployment on AWS EC2

📂 Project Structure
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
🔧 Setup Instructions
1️⃣ Environment Setup
conda create -n vehicle python=3.10 -y
conda activate vehicle
pip install -r requirements.txt
2️⃣ MongoDB Setup
Create project in MongoDB Atlas
Create cluster (M0 Free Tier)
Add IP: 0.0.0.0/0
Get connection string
export MONGODB_URL="your_connection_string"
3️⃣ Data Pipeline
Data fetched from MongoDB
Converted into DataFrame
Passed through:
Data Validation
Data Transformation
Model Training
4️⃣ AWS Setup
Create IAM user with AdministratorAccess
Configure credentials:
export AWS_ACCESS_KEY_ID="your_key"
export AWS_SECRET_ACCESS_KEY="your_secret"
Create S3 bucket:
credit-card-fraud-detection-proj
5️⃣ Run Training Pipeline
python demo.py
🧠 ML Pipeline Components
Component	Description
Data Ingestion	Fetch data from MongoDB
Data Validation	Schema validation
Data Transformation	Feature engineering
Model Trainer	Train ML model
Model Evaluation	Compare with previous model
Model Pusher	Push to AWS S3
🌐 Prediction Pipeline
Built using FastAPI
Web interface using HTML/CSS
Supports:
Real-time predictions
Training trigger via /training route
🐳 Docker Setup
docker build -t fraud-detection .
docker run -p 5080:5080 fraud-detection
🔁 CI/CD Pipeline
GitHub Actions Workflow
Build Docker Image
Push to AWS ECR
Deploy to EC2 using Self-hosted Runner
☁️ AWS Deployment
Steps:
Create ECR repository
Launch EC2 instance (Ubuntu)
Install Docker
Configure Self-hosted Runner
Add GitHub Secrets:
AWS_ACCESS_KEY_ID
AWS_SECRET_ACCESS_KEY
AWS_DEFAULT_REGION
ECR_REPO
🚀 Live Application
http://<EC2-PUBLIC-IP>:5080
📊 Key Highlights

🔥 Production-level MLOps Pipeline
🔥 Real-world Deployment on AWS
🔥 Automated CI/CD
🔥 Scalable Architecture
🔥 Recruiter-ready Project

🙌 Future Improvements
Add monitoring (Prometheus/Grafana)
Add model drift detection
Improve UI/UX
Add authentication
👨‍💻 Author

Shubh Patel
B.Tech CSE | Aspiring Software Engineer | AI/ML Enthusiast
