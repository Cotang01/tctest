FROM python:3.11-alpine
WORKDIR /app
ADD src tests ./
CMD ["python", "pytest"]
