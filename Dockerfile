# Netramind SOP Assistant — container image
FROM python:3.12-slim

# System library a couple of the ML wheels expect at runtime.
RUN apt-get update && apt-get install -y --no-install-recommends libgomp1 \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

# Install Python dependencies first (cached unless requirements.txt changes).
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the application (see .dockerignore for what's left out).
COPY . .

# Bake the local embedding model into the image so there's no download at runtime.
RUN python -c "from sentence_transformers import SentenceTransformer; \
SentenceTransformer('sentence-transformers/all-MiniLM-L6-v2')"

# Build the SOP search index from ./sops at build time.
RUN python ingest.py

EXPOSE 8501

# Streamlit must listen on 0.0.0.0 to be reachable from outside the container.
CMD ["streamlit", "run", "app.py", \
     "--server.address=0.0.0.0", "--server.port=8501", "--server.headless=true"]
