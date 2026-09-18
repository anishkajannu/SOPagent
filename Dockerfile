# Netramind SOP Assistant — container image
FROM python:3.12-slim

# System library a couple of the ML wheels expect at runtime.
RUN apt-get update && apt-get install -y --no-install-recommends libgomp1 \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

# Keep ONNX / BLAS thread pools to one — fewer memory arenas for the embedding
# model on a small instance (and no downside on a low-CPU tier).
ENV OMP_NUM_THREADS=1 \
    OPENBLAS_NUM_THREADS=1 \
    TOKENIZERS_PARALLELISM=false

# Install Python dependencies first (cached unless requirements.txt changes).
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the application (see .dockerignore for what's left out).
COPY . .

# Bake the lightweight ONNX embedding model into the image (no download at runtime).
RUN python -c "from langchain_community.embeddings import FastEmbedEmbeddings; \
FastEmbedEmbeddings(model_name='sentence-transformers/all-MiniLM-L6-v2').embed_query('warmup')"

# Build the SOP search index from ./sops at build time.
RUN python ingest.py

EXPOSE 8501

# Streamlit must listen on 0.0.0.0 to be reachable from outside the container.
CMD ["streamlit", "run", "app.py", \
     "--server.address=0.0.0.0", "--server.port=8501", "--server.headless=true"]
