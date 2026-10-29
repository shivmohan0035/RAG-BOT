# 📄 Document Q&A Chatbot

An AI-powered PDF Question Answering Chatbot built using **Streamlit, LangChain, and Google Gemini**. This application allows users to upload PDF documents and ask questions about their content using natural language.

The chatbot uses Retrieval-Augmented Generation (RAG) to retrieve relevant information from the uploaded PDF and generate accurate, context-aware answers.

## 🚀 Features

- **PDF Upload:** Upload PDF documents directly through the Streamlit interface.
- **Document Processing:** Extract text from PDFs using PyPDFLoader.
- **Text Chunking:** Split documents into smaller chunks using RecursiveCharacterTextSplitter.
- **Vector Embeddings:** Generate embeddings using Google's Gemini embedding model.
- **Semantic Search:** Retrieve relevant document chunks using similarity search.
- **AI-Powered Answers:** Generate answers using Google Gemini 2.5 Flash.
- **Interactive Chat:** Ask multiple questions about the uploaded document.
- **Chat History:** View previous questions and answers during the session.
- **Context-Aware Responses:** Answers are generated using the retrieved document content.
- **Error Handling:** Handles API rate limits and document processing errors.

## 🛠️ Tech Stack

| Technology | Purpose |
|---|---|
| Python | Programming language |
| Streamlit | Interactive web application |
| LangChain | LLM integration and RAG workflow |
| Google Gemini 2.5 Flash | Answer generation |
| Gemini Embeddings | Text embedding generation |
| PyPDF | PDF text extraction |
| InMemoryVectorStore | Vector storage and similarity search |
| python-dotenv | Environment variable management |

## 🧠 How It Works

The chatbot follows a Retrieval-Augmented Generation (RAG) pipeline.

1. **Upload PDF:** The user uploads a PDF document.
2. **Text Extraction:** PyPDFLoader extracts text from the PDF.
3. **Text Chunking:** The extracted text is divided into chunks of 1000 characters with an overlap of 200 characters.
4. **Embedding Generation:** Google Gemini generates vector embeddings for each chunk.
5. **Vector Storage:** The embeddings are stored in an in-memory vector database.
6. **Question Input:** The user asks a question through the chat interface.
7. **Semantic Retrieval:** The application retrieves the top 5 relevant document chunks.
8. **Context Preparation:** The retrieved chunks are passed to Gemini along with the user's question.
9. **Answer Generation:** Gemini generates a response based on the retrieved context.
10. **Response Display:** The answer is displayed in the Streamlit chat interface.

## 📂 Project Structure

```text
Document-QA-Chatbot/
│
├── app.py                 # Main Streamlit application
├── requirements.txt        # Python dependencies
├── .env                  # Google Gemini API key
├── .gitignore             # Files excluded from Git
└── README.md              # Project documentation
```

## ⚙️ Installation and Setup

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/Document-QA-Chatbot.git
```

Navigate to the project directory:

```bash
cd Document-QA-Chatbot
```

### 2. Create a Virtual Environment

```bash
python -m venv venv
```

Activate the virtual environment.

**Windows:**

```bash
venv\Scripts\activate
```

**macOS/Linux:**

```bash
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure the Google Gemini API Key

Create a `.env` file in the root directory of the project.

Add your Google Gemini API key:

```env
GOOGLE_API_KEY=your_google_gemini_api_key
```

Get your API key from:

https://aistudio.google.com/app/apikey

**Important:** Never share your API key or upload your `.env` file to GitHub.

### 5. Run the Application

```bash
streamlit run app.py
```

The application will open in your browser, usually at:

```text
http://localhost:8501
```

## 📦 Dependencies

The application uses the following Python packages:

```text
streamlit
python-dotenv
langchain
langchain-community
langchain-text-splitters
langchain-google-genai
pypdf
```

## 💻 Usage

1. Start the application.
2. Upload a PDF document.
3. Wait for the document to be processed.
4. Enter your question in the chat input.
5. The chatbot retrieves relevant information from the PDF.
6. Read the generated answer.
7. Continue asking questions about the uploaded document.

## 🔍 Example

**Sample Question:**

```text
What are the main objectives discussed in the document?
```

**Chatbot Response:**

```text
The main objectives discussed in the document are...
```

The response is generated based on the content retrieved from the uploaded PDF.

## 🔐 Environment Variables

| Variable | Description |
|---|---|
| `GOOGLE_API_KEY` | API key required to access Google Gemini |

## ⚠️ Limitations

- Currently supports PDF documents only.
- Scanned PDFs without a text layer may not be processed correctly.
- The vector database is stored in memory and is not persistent.
- The application processes one uploaded document at a time.
- Gemini API usage is subject to rate limits and quotas.
- Answer quality depends on the extracted text and retrieved context.

## 🔮 Future Improvements

- Support multiple PDF uploads.
- Add OCR support for scanned PDFs.
- Add persistent vector storage using FAISS or ChromaDB.
- Display source pages and document citations.
- Add document download functionality.
- Improve chat history persistence.
- Support additional document formats such as DOCX and TXT.
- Deploy the application to Streamlit Community Cloud.

## 👨‍💻 Author

**Shivmohan Chaurasia**

B.Tech CSE-AIML | Backend Developer | AI/ML Developer


## 📜 License

This project is intended for educational and learning purposes.
