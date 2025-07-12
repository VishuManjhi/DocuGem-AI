# 📄DocuGem-AI

An AI-powered web application that extracts meaningful insights (like title, abstract, authors, and publication date) from uploaded research PDFs using **Google Gemini**, **LangChain**, and **ChromaDB**. Users can also ask natural language questions and get context-aware answers.

![App Screenshot](Screenshot.png)

---

## 🚀 Features

- 🔍 Extracts key metadata: title, abstract, authors, etc.
- 💬 Ask questions about the document using semantic search
- 🤖 Powered by Gemini's LLMs and `models/embedding-001`
- 🧠 Uses LangChain and ChromaDB for RAG (retrieval-augmented generation)
- 🌐 Simple UI built with Streamlit

---

## 🧱 Tech Stack

- **Frontend:** Streamlit  
- **LLM & Embeddings:** Google Gemini (via LangChain)  
- **Vector Store:** ChromaDB  
- **PDF Parsing:** PyPDF2  
- **Backend Language:** Python  
- **Deployment:** Ngrok / Localhost / Streamlit Cloud  

---

## 🛠️ Setup Instructions

```bash
# Clone the repository
git clone https://github.com/yourusername/DocuGem-AI.git
cd DocuGem-AI

# Create a virtual environment
python -m venv venv
source venv/Scripts/activate   # On Windows

# Install dependencies
pip install -r requirements.txt

# Create .env file
touch .env
# Add your Gemini API key inside it:
# GEMINI_API_KEY=your_key_here

# Run the app
streamlit run app/app.py
  
