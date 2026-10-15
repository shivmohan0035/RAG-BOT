from dotenv import load_dotenv
load_dotenv()
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.document_loaders import PyPDFLoader
from langchain_community.vectorstores import InMemoryVectorStore
from langchain_google_genai import ChatGoogleGenerativeAI, GoogleGenerativeAIEmbeddings
from langchain_google_genai.chat_models import GoogleRateLimitError
import streamlit as st

from time import sleep

llm=ChatGoogleGenerativeAI(model="gemini-3.8-flash")

if 'vector_db' not in st.session_state:
    st.session_state.vector_db = None
    
    
    
def document_process(path):
    ##document loading
    loader = PyPDFLoader(path)
    docs=loader.load()

    ##splitting
    splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
    docs = splitter.split_documents(docs)  

    ##embedding and vector store creation
    for doc in docs:
        doc.page_content = f"title: none | text: {doc.page_content}"

    embeddings = GoogleGenerativeAIEmbeddings(model="gemini-embedding-2")
    vector_db = InMemoryVectorStore.from_documents(documents=docs, embedding=embeddings)
    ## chunk save in vector_db in session state
    st.session_state.vector_db = vector_db
    st.session_state.document_uploaded = True




st.subheader(" Document Q&A Chatbot - Ask questions about your PDF document")

if 'document_uploaded' not in st.session_state:
    st.session_state.document_uploaded = False
    
if not st.session_state.document_uploaded:
  file=st.file_uploader("Upload a PDF document", type=["pdf"], key="file_uploader")
  if file:
    with open("uploaded_document.pdf", "wb") as f:
        f.write(file.getvalue())
    with st.spinner("Processing the document..."):
       document_process("./uploaded_document.pdf")
    st.markdown("Document processed successfully! You can now ask questions about the document.")
    sleep(2)
    st.rerun()


if st.session_state.document_uploaded and st.session_state.vector_db:
    query = st.chat_input("Ask a question about the document:")
    if query:
       st.chat_message("user").markdown(query)
       search_query = f"task: question answering | query: {query}"
       documents = st.session_state.vector_db.similarity_search(search_query, k=5)
       context = ""
       
       for doc in documents:
           context += doc.page_content + "\n"
           
       prompt = f"""You are a helpful assistant for questions about an uploaded PDF. If the user is greeting you or making a brief conversational opener, respond naturally and invite them to ask about the PDF. For questions about the document, answer using only the context below. If the context does not contain the answer, say "I don't know."\n\nContext:\n{context}\n\nQuestion: {query}\nAnswer:"""
       
       try:
           result = llm.invoke(prompt)
       except GoogleRateLimitError:
           st.error(
               "Gemini's request quota is exhausted for this model. "
               "Wait for the retry period shown by Google, or check your "
               "project's quota and billing settings."
           )
           st.link_button(
               "Check Gemini API quotas",
               "https://ai.google.dev/gemini-api/docs/rate-limits",
           )
           st.stop()

       content = result.content
       if isinstance(content, str):
           answer = content
       else:
           answer = "\n".join(
               block["text"]
               for block in content
               if isinstance(block, dict)
               and block.get("type") == "text"
               and isinstance(block.get("text"), str)
           )

       if answer:
           st.chat_message("assistant").markdown(answer)
       else:
           st.error("The model returned no displayable text.")