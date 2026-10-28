FROM python:3.11-slim
WORKDIR /app
COPY app_server.py .
RUN pip install scikit-learn
EXPOSE 8000
CMD ["python", "app_server.py"]
