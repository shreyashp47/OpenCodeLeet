FROM python:3.11-slim

WORKDIR /app

# Install JDK + Kotlin compiler (optional; remove if you only need Python)
RUN apt-get update && apt-get install -y --no-install-recommends \
    curl \
    unzip \
    default-jdk \
    && rm -rf /var/lib/apt/lists/*

ENV KOTLIN_VERSION=2.1.0
RUN curl -sL https://github.com/JetBrains/kotlin/releases/download/v${KOTLIN_VERSION}/kotlin-compiler-${KOTLIN_VERSION}.zip \
    -o /tmp/kotlin.zip \
    && unzip /tmp/kotlin.zip -d /opt \
    && rm /tmp/kotlin.zip \
    && ln -s /opt/kotlinc/bin/kotlinc /usr/local/bin/kotlinc \
    && ln -s /opt/kotlinc/bin/kotlin /usr/local/bin/kotlin

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 5000

CMD ["python", "python/app.py"]
