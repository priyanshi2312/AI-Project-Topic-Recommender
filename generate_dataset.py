import pandas as pd
import random

domains = {
    "Machine Learning": [
        "House Price Prediction",
        "Student Performance Prediction",
        "Customer Churn Prediction",
        "Sales Forecasting",
        "Loan Approval Prediction",
        "Insurance Premium Prediction",
        "Employee Attrition Prediction",
        "Stock Price Prediction",
        "Movie Recommendation System",
        "Music Recommendation System"
    ],

    "Natural Language Processing": [
        "Fake News Detection",
        "Resume Screening System",
        "Medical Chatbot",
        "College Query Chatbot",
        "Spam Email Detection",
        "Sentiment Analysis",
        "Language Translator",
        "Grammar Checker",
        "Text Summarizer",
        "AI Email Generator"
    ],

    "Computer Vision": [
        "Face Recognition System",
        "Face Mask Detection",
        "Vehicle Detection",
        "Fire Detection",
        "Traffic Sign Recognition",
        "Number Plate Detection",
        "Hand Gesture Recognition",
        "Image Caption Generator",
        "Human Pose Detection",
        "Plant Disease Detection"
    ],

    "Healthcare": [
        "Heart Disease Prediction",
        "Diabetes Prediction",
        "Brain Tumor Detection",
        "Medical Report Analyzer",
        "Hospital Management AI",
        "Skin Disease Detection",
        "Medicine Recommendation",
        "AI Health Assistant",
        "Disease Prediction System",
        "Medical Image Classification"
    ],

    "Finance": [
        "Credit Card Fraud Detection",
        "Expense Tracker",
        "Loan Eligibility Checker",
        "Stock Market Dashboard",
        "Personal Finance Assistant",
        "Fraud Transaction Detection",
        "Budget Prediction",
        "Investment Advisor",
        "Bank Customer Segmentation",
        "Risk Analysis System"
    ],

    "Education": [
        "AI Study Planner",
        "Smart Attendance System",
        "AI Quiz Generator",
        "Exam Performance Analyzer",
        "Course Recommendation System",
        "Student Feedback Analysis",
        "Placement Prediction",
        "Online Exam Proctoring",
        "AI Tutor",
        "Learning Progress Tracker"
    ],

    "Agriculture": [
        "Crop Recommendation",
        "Soil Quality Prediction",
        "Smart Irrigation System",
        "Plant Disease Detection",
        "Weather Forecasting",
        "Crop Yield Prediction",
        "Fertilizer Recommendation",
        "Smart Farming Assistant",
        "Livestock Health Prediction",
        "Farm Monitoring System"
    ],

    "Cybersecurity": [
        "Phishing Website Detection",
        "Password Strength Analyzer",
        "Malware Detection",
        "Network Intrusion Detection",
        "Cyber Threat Detection",
        "Email Spam Filter",
        "Secure Login System",
        "Face Authentication",
        "File Encryption Tool",
        "AI Security Assistant"
    ],

    "Generative AI": [
        "AI Resume Builder",
        "AI Story Generator",
        "AI Interview Coach",
        "AI Code Assistant",
        "AI Research Assistant",
        "AI Meeting Summarizer",
        "AI Career Advisor",
        "AI Content Generator",
        "AI Notes Generator",
        "AI Image Caption Generator"
    ],

    "IoT": [
        "Smart Home Automation",
        "Smart Parking System",
        "Smart Street Lights",
        "Air Quality Monitoring",
        "Water Quality Monitoring",
        "Smart Dustbin",
        "Smart Energy Meter",
        "Weather Monitoring System",
        "Smart Traffic Management",
        "IoT Health Monitoring"
    ]
}

skills = [
    "Python",
    "Pandas",
    "NumPy",
    "Scikit-learn",
    "TensorFlow",
    "PyTorch",
    "OpenCV",
    "NLTK",
    "spaCy",
    "Flask",
    "SQL"
]

levels = ["Beginner", "Intermediate", "Advanced"]

durations = [
    "2 Weeks",
    "3 Weeks",
    "4 Weeks",
    "5 Weeks",
    "6 Weeks",
    "8 Weeks"
]

projects = []

project_id = 1

for domain, titles in domains.items():

    for title in titles:

        projects.append({

            "project_id": f"P{project_id:03}",

            "title": title,

            "domain": domain,

            "skills": ", ".join(random.sample(skills, 4)),

            "interests": domain,

            "difficulty": random.choice(levels),

            "duration": random.choice(durations),

            "description":
            f"{title} using Artificial Intelligence and Machine Learning techniques."

        })

        project_id += 1

df = pd.DataFrame(projects)

df.to_csv(
    "dataset/project_topics.csv",
    index=False
)

print("="*60)
print("✅ Dataset Generated Successfully!")
print(f"Total Projects : {len(df)}")
print("Saved as : dataset/project_topics.csv")
print("="*60)