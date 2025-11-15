from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from sklearn.feature_extraction.text import TfidfVectorizer
import validators
import os

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
db = SQLAlchemy(app)

# Database model to store documents
class Document(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200))
    content = db.Column(db.Text)

# Initialize DB
with app.app_context():
    db.create_all()
    # Prepopulate DB with sample documents if empty
    if Document.query.count() == 0:
        docs = [
            Document(title="Python Basics", content="Python is a high-level programming language."),
            Document(title="Flask Web Development", content="Flask is a lightweight web framework for Python."),
            Document(title="Machine Learning", content="Machine learning allows computers to learn from data."),
            Document(title="Cybersecurity Fundamentals", content="Cybersecurity protects systems against threats."),
            Document(title="Search Algorithms", content="Search algorithms are used to find specific data efficiently.")
        ]
        db.session.bulk_save_objects(docs)
        db.session.commit()

@app.route('/', methods=['GET', 'POST'])
def index():
    results = []
    query = ''
    if request.method == 'POST':
        query = request.form.get('query', '').strip()
        if not query:
            return render_template('index.html', results=[], query='', message="Please enter a search query.")
        if not validators.string(query):
            return render_template('index.html', results=[], query='', message="Invalid query input.")

        # Retrieve all documents
        docs = Document.query.all()
        corpus = [doc.content for doc in docs]

        # Compute TF-IDF
        vectorizer = TfidfVectorizer()
        tfidf_matrix = vectorizer.fit_transform(corpus)
        query_vec = vectorizer.transform([query])

        # Compute similarity (cosine similarity)
        from sklearn.metrics.pairwise import cosine_similarity
        similarities = cosine_similarity(query_vec, tfidf_matrix).flatten()

        # Sort results
        ranked_docs = sorted(zip(docs, similarities), key=lambda x: x[1], reverse=True)
        results = [(doc.title, doc.content, sim) for doc, sim in ranked_docs if sim > 0]

    return render_template('index.html', results=results, query=query, message='')

if __name__ == '__main__':
    app.run(debug=True)
