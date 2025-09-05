# HexaLingua 🗣️🌐  
*A Multilingual Campus AI Assistant for Smart India Hackathon (SIH)*  

HexaLingua is an intelligent campus assistant designed to handle student queries, provide instant responses, and support multilingual communication. It starts as a simple FAQ chatbot and will gradually evolve into a powerful AI assistant with NLP capabilities.  

---

## ✨ Features
- Answer campus-related FAQs instantly  
- Simple Flask backend with `/ask` API  
- Knowledge base stored in JSON for easy updates  
- Easy to extend with NLP, embeddings, and multilingual support  
- Can be integrated with a frontend chatbox  

---

## 📂 Project Structure
HexaLingua/
│── app.py # Flask backend
│── faqs.json # Knowledge base
│── requirements.txt # Dependencies
│── test_api.py # Script to test chatbot API

📌 Project Roadmap
✅ Phase 1 – Backend Setup (Done)

Flask backend (app.py) with /ask API

Basic knowledge base (faqs.json)

Test script (test_api.py)

Requirements file (requirements.txt)

🚧 Phase 2 – Smart NLP Integration (Next)

Add sentence-transformers for embeddings

Implement semantic search for better answers

Support multilingual queries (English + Hindi first)

🔮 Phase 3 – User Experience

Build a simple chatbox frontend (HTML/JS)

Connect frontend to Flask API

Make responses more interactive

🌐 Phase 4 – Deployment

Containerize with Docker

Deploy on Render / Railway / Azure (for judges demo)

🤝 Team Roles

AI/ML Engineer → Core NLP pipeline & embeddings

Backend Developer → Flask APIs, integration with ML models

Frontend Developer → Chatbox UI for students

Data Curator → Maintain campus FAQs knowledge base

Deployment Engineer → Hosting, scalability, and monitoring

📜 License

This project is licensed under the MIT License – free to use, modify, and distribute.

🚀 Vision

HexaLingua will become a smart multilingual digital assistant for campuses across India, making information accessible to every student in their preferred language.
🚀 Demo

After installing dependencies and starting the backend, you can run a quick demo to test HexaLingua.

1. Start the backend
python app.py


This will start Flask on:

http://127.0.0.1:5000

2. Run the demo script
python demo.py


This script will automatically send sample questions to the backend and show the answers.

✅ Sample Output
🚀 HexaLingua Demo Started

Q: When does the library open?
A: The library is open from 9 AM to 6 PM on weekdays and 10 AM to 2 PM on Saturdays.
--------------------------------------------------
Q: Is breakfast available in the cafeteria?
A: The cafeteria serves breakfast from 7:30 AM to 9:30 AM on all working days.
--------------------------------------------------
Q: Where is the admission office?
A: The admission office is located in Block A, ground floor, near the main entrance.
--------------------------------------------------
Q: How can I get a bonafide certificate?
A: To get a bonafide certificate, you need to apply online through the student portal and collect it from the registrar office after approval.
--------------------------------------------------
Q: How do I apply for hostel accommodation?
A: You can apply for a hostel room by filling out the online form on the hostel management system and submitting required documents.
--------------------------------------------------

🎯 What this proves

The backend (app.py) is running.

The semantic search (core_pipeline.py) is working with sentence-transformers.

Questions don’t need to be exact — similar wording still gives the right answer.
