MiniRank – Search Engine with TF-IDF Ranking & Secure Query Handling

MiniRank is a lightweight Python + Flask search engine that applies TF-IDF vectorization and cosine similarity to rank documents based on query relevance.
It demonstrates core concepts used in modern search engines such as query preprocessing, term weighting, feature vectorization, and document scoring.

Along with ranking logic, MiniRank includes secure input handling, ensuring that search queries are sanitized to prevent common web vulnerabilities (XSS, injection patterns, malformed payloads).

🚀 Key Features

TF-IDF Based Search Ranking
Uses Scikit-learn’s TfidfVectorizer to convert documents into weighted feature vectors
Computes similarity using cosine similarity
Returns results sorted in descending order of relevance

⚡ Real-Time Query Processing

Processes search queries dynamically
Ranking results displayed instantly in a responsive web UI

🔐 Secure Input Handling

Validates and sanitizes user search queries
Prevents basic web-based attacks (XSS, script injection)
Ensures safe request processing

🗄️ SQLite Document Storage

Lightweight, file-based database
Stores user-provided or pre-loaded documents
Simple schema for easy extension

🌐 Flask-Based Web Interface

Minimalistic, clean UI for fast searching
Suitable for deployment or integration into other apps


📁 Tech Stack

Python 3
Flask
SQLite
Scikit-learn
HTML / CSS

📚 Future Enhancements

Add BM25 ranking
Add document upload support (PDF, text)
Implement search caching
Add user authentication
Integrate Elasticsearch as backend
Add rate-limiting & WAF-style security filters

