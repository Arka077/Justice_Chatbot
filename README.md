# ⚖️ Justice Chatbot - AI-Powered Legal Services Portal

A comprehensive legal assistance platform that combines AI-powered chatbot capabilities, lawyer discovery, video consultations, and case tracking to provide accessible legal services to users across India.

## 🎯 Features

### 1. 🤖 Legal Chatbot (RAG-Powered)
- **AI-Powered Legal Assistant**: Ask legal questions and receive accurate, context-aware responses
- **RAG (Retrieval-Augmented Generation)**: Uses Pinecone vector database and Mistral AI for intelligent responses
- **Real-time Web Search**: Fetches latest legal information from the web using SerpAPI
- **Semantic Search**: Powered by SentenceTransformers for accurate information retrieval

### 2. 📍 Find Lawyers
- **Geolocation-Based Discovery**: Find lawyers near your location
- **Auto-Detection**: Automatically detect your location using IP-based geolocation
- **Manual Search**: Search for lawyers in any specific location
- **Comprehensive Details**: View lawyer profiles with ratings, reviews, contact info, and opening hours
- **Powered by Google Maps**: Uses Apify's Google Maps scraper for accurate, up-to-date information

### 3. 📹 Video Consultations
- **Live Video Calls**: Connect with lawyers via secure video consultations
- **Powered by Jitsi Meet**: Free, secure, and reliable video conferencing
- **Direct Integration**: Seamlessly start video calls from lawyer profiles
- **No Additional Software Required**: Works directly in your browser

### 4. 🧾 Case Tracking
- **e-Courts Integration**: Track your legal case status in real-time
- **Case Details**: View case number, status, court information, and latest updates
- **Next Hearing Information**: Stay informed about upcoming court dates

## 🏗️ Architecture

```
Justice_Chatbot/
├── app.py                      # Main Streamlit application entry point
├── pages/                      # Multi-page Streamlit app pages
│   ├── Legal_Chatbot.py       # AI chatbot interface
│   ├── Find_Lawyers.py        # Lawyer discovery and geolocation
│   └── Track_Case.py          # Case tracking interface
├── modules/
│   └── video_chat.py          # Jitsi video chat integration
├── utils/
│   ├── ecourt_api.py          # e-Courts API integration
│   ├── lawyers.py             # Lawyer search and geolocation utilities
│   └── pdf_utils.py           # PDF text extraction utilities
├── rag_indexer.py             # RAG indexing with Pinecone and SerpAPI
├── rag_qa.py                  # RAG query and answer generation
├── mistral_api.py             # Mistral AI API integration
├── google_content.py          # Google search integration
├── requirements.txt           # Python dependencies
└── .env                       # Environment variables (API keys)
```

## 🚀 Installation

### Prerequisites

- **Python 3.8 or higher**
- **pip** package manager
- **Git** (for cloning the repository)
- **API Keys** (see Environment Setup below)

### Step-by-Step Setup

1. **Clone the Repository**
   ```bash
   git clone https://github.com/Arka077/Justice_Chatbot.git
   cd Justice_Chatbot
   ```

2. **Create Virtual Environment (Recommended)**
   ```bash
   python -m venv venv
   
   # On Windows
   venv\Scripts\activate
   
   # On macOS/Linux
   source venv/bin/activate
   ```

3. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set Up Environment Variables**
   
   Create a `.env` file in the root directory with the following API keys:
   ```env
   MISTRAL_API_KEY=your-mistral-api-key-here
   PINECONE_API_KEY=your-pinecone-api-key-here
   SERPAPI_KEY=your-serpapi-key-here
   APIFY_TOKEN=your-apify-token-here
   ```

   **How to Obtain API Keys:**
   
   - **Mistral API**: Sign up at [Mistral AI](https://mistral.ai/) for AI language model access
   - **Pinecone**: Create account at [Pinecone](https://www.pinecone.io/) for vector database services
   - **SerpAPI**: Register at [SerpAPI](https://serpapi.com/) for Google search integration
   - **Apify**: Get token from [Apify](https://apify.com/) for Google Maps scraping

5. **Run the Application**
   ```bash
   streamlit run app.py
   ```

6. **Access the Application**
   
   Open your browser and navigate to `http://localhost:8501`

## 📊 Tech Stack

### Frontend
- **Streamlit** - Modern Python web framework for data apps
- **Streamlit Components** - Custom iframe components for Jitsi integration

### AI & Machine Learning
- **Mistral AI** - Large language model for generating legal responses
- **SentenceTransformers** - Semantic text embeddings (all-MiniLM-L6-v2)
- **Pinecone** - Vector database for semantic search
- **FAISS** - Facebook AI Similarity Search for efficient vector operations

### APIs & Integrations
- **SerpAPI** - Google search API for fetching legal web content
- **Apify** - Google Maps scraper for lawyer discovery
- **e-Courts API** - Case tracking integration
- **Jitsi Meet** - Video conferencing platform

### Data Processing
- **PyMuPDF (fitz)** - PDF text extraction
- **pdf2image** - PDF to image conversion
- **pytesseract** - OCR for scanned documents
- **pandas** - Data manipulation and analysis

### Utilities
- **python-dotenv** - Environment variable management
- **requests** - HTTP client for API calls
- **geocoder** - Geolocation services

## 🔧 Usage

### Legal Chatbot

1. Navigate to the **Legal Chatbot** page from the home screen
2. Type your legal question in the chat input box
3. The system will:
   - Fetch relevant legal information from the web
   - Index it in the Pinecone vector database
   - Use RAG to generate an accurate, context-aware response
4. View the answer along with your original question

**Example Questions:**
- "What are the legal rights of a tenant in India?"
- "How do I file a consumer complaint?"
- "What is the process for trademark registration?"

### Find Lawyers

1. Navigate to **Find Lawyers** page
2. Choose your location method:
   - **Auto-Detect**: Click "Auto-Detect Location" to use IP-based geolocation
   - **Manual Entry**: Enter your city/location manually
3. Click "Find Lawyers Near Me"
4. Browse through the list of nearby lawyers with details:
   - Name, rating, and reviews
   - Address and contact information
   - Opening hours
   - Category/specialization
5. Click "Start Video Chat" to initiate a video consultation

### Video Consultation

1. From the lawyer list, click **Start Video Chat**
2. You'll be redirected to a Jitsi Meet room
3. Share the room link with the lawyer
4. Start your video consultation
5. Click "Back to Search" to return to the lawyer finder

### Case Tracking

1. Navigate to **Track a Case** page
2. Enter your case number (e.g., SC/1234/2022)
3. Click "Track Case"
4. View case details including:
   - Case number and status
   - Court information
   - Parties involved
   - Latest updates and next hearing date

## 🧪 RAG Pipeline

The **Retrieval-Augmented Generation (RAG)** pipeline is the core of the Legal Chatbot's intelligence:

### How It Works

```
User Query → Web Search → Embedding → Vector Search → Context Retrieval → AI Response
```

### Detailed Flow

1. **Query Input**: User asks a legal question

2. **Web Search (SerpAPI)**
   - Searches Google for relevant legal information
   - Fetches top 10 results with titles and snippets
   - Extracts metadata (source links, rankings)

3. **Text Embedding (SentenceTransformers)**
   - Converts text into 384-dimensional vectors
   - Uses `all-MiniLM-L6-v2` model for semantic understanding

4. **Vector Indexing (Pinecone)**
   - Stores embeddings in Pinecone vector database
   - Creates searchable index with cosine similarity

5. **Context Retrieval**
   - Converts user query to embedding
   - Searches Pinecone for top 5 most relevant chunks
   - Retrieves contextual information

6. **Answer Generation (Mistral AI)**
   - Constructs prompt with retrieved context
   - Sends to Mistral AI language model
   - Generates natural, accurate legal response

7. **Response Delivery**
   - Displays answer to user
   - Maintains conversation context

### Key Components

**rag_indexer.py**
```python
# Fetches legal content from web and indexes in Pinecone
def index_query_from_google(query: str):
    # Fetch web results
    entries = fetch_legal_web_results(query)
    # Create embeddings
    embeddings = EMBED_MODEL.encode(texts)
    # Store in Pinecone
    index.upsert(vectors)
```

**rag_qa.py**
```python
# Retrieves context and generates answer
def answer_query_with_context(query: str):
    # Search Pinecone for relevant context
    context_chunks = search_index_for_context(query)
    # Generate answer using Mistral AI
    return call_mistral(prompt_with_context)
```

## 📝 Key Files

| File | Description |
|------|-------------|
| `app.py` | Main Streamlit application entry point, home page navigation |
| `rag_indexer.py` | Handles RAG indexing: fetches web content, creates embeddings, stores in Pinecone |
| `rag_qa.py` | RAG query processing: retrieves context from Pinecone, generates AI responses |
| `mistral_api.py` | Mistral AI API integration for language model inference |
| `google_content.py` | Google search integration using SerpAPI |
| `pages/Legal_Chatbot.py` | Legal chatbot UI and conversation interface |
| `pages/Find_Lawyers.py` | Lawyer discovery interface with geolocation |
| `pages/Track_Case.py` | Case tracking interface with e-Courts integration |
| `modules/video_chat.py` | Jitsi Meet video chat integration module |
| `utils/ecourt_api.py` | e-Courts API wrapper for case status retrieval |
| `utils/lawyers.py` | Lawyer search utilities using Apify Google Maps scraper |
| `utils/pdf_utils.py` | PDF text extraction with PyMuPDF and OCR fallback |
| `requirements.txt` | Python package dependencies |
| `.env` | Environment variables for API keys (not committed to repo) |

## 🤝 Contributing

We welcome contributions to improve the Justice Chatbot! Here's how you can help:

### Getting Started

1. **Fork the Repository**
   ```bash
   # Click the "Fork" button on GitHub
   ```

2. **Clone Your Fork**
   ```bash
   git clone https://github.com/YOUR_USERNAME/Justice_Chatbot.git
   cd Justice_Chatbot
   ```

3. **Create a Feature Branch**
   ```bash
   git checkout -b feature/your-feature-name
   ```

4. **Make Your Changes**
   - Follow the existing code style
   - Add comments for complex logic
   - Test your changes thoroughly

5. **Commit Your Changes**
   ```bash
   git add .
   git commit -m "Add: Brief description of your changes"
   ```

6. **Push to Your Fork**
   ```bash
   git push origin feature/your-feature-name
   ```

7. **Create a Pull Request**
   - Go to the original repository on GitHub
   - Click "New Pull Request"
   - Select your feature branch
   - Provide a clear description of your changes

### Contribution Guidelines

- **Code Quality**: Write clean, readable, and well-documented code
- **Testing**: Test your changes before submitting
- **Documentation**: Update README if you add new features
- **Commit Messages**: Use clear, descriptive commit messages
- **Issues**: Check existing issues before creating new ones

### Areas for Contribution

- 🐛 Bug fixes and error handling improvements
- ✨ New features (e.g., additional legal services, better UI/UX)
- 📚 Documentation improvements
- 🧪 Adding tests and improving code coverage
- 🌐 Localization and multi-language support
- ⚡ Performance optimizations
- 🔒 Security enhancements

## 📄 License

This project is licensed under the **MIT License**.

```
MIT License

Copyright (c) 2025 Justice Chatbot Contributors

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```

## 🙏 Acknowledgments

- **Mistral AI** for providing the language model API
- **Pinecone** for vector database infrastructure
- **Streamlit** for the amazing web framework
- **Jitsi Meet** for open-source video conferencing
- **SerpAPI** for Google search integration
- **Apify** for Google Maps scraping capabilities
- All contributors who help improve this project

## 📞 Support

If you encounter any issues or have questions:

1. Check the [Issues](https://github.com/Arka077/Justice_Chatbot/issues) page
2. Create a new issue with a detailed description
3. Contact the maintainers

## 🚀 Future Roadmap

- [ ] Integration with more legal databases and APIs
- [ ] Multi-language support (Hindi, Tamil, Telugu, etc.)
- [ ] Document analysis and summarization
- [ ] Advanced case law search
- [ ] Mobile application
- [ ] Appointment scheduling system
- [ ] Payment integration for consultations
- [ ] Enhanced security and privacy features
- [ ] AI-powered legal document drafting

---

**Made with ❤️ for accessible legal services in India**

**⭐ Star this repository if you find it helpful!**
