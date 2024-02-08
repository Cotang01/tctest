FROM python:3.11-alpine
WORKDIR /app
COPY requirements.txt ./
ADD src tests ./
RUN pip install --no-cache-dir -r requirements.txt
CMD ["python", "pytest"]
