# ---------- Base ----------
FROM python:3.11-slim

# Prevent Python buffering
ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1

WORKDIR /mlctl

# System deps (optional but safe)
RUN apt-get update && apt-get install -y --no-install-recommends \
    ca-certificates \
    curl \
 && rm -rf /var/lib/apt/lists/*

# Install uv
RUN pip install --no-cache-dir uv

# Copy project
COPY pyproject.toml uv.lock* ./
COPY mlctl ./mlctl

# Install CLI
RUN uv pip install --system -e .

# Default command
ENTRYPOINT ["mlctl"]
CMD ["--help"]