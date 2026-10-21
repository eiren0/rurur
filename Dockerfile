FROM python:3.11-slim
WORKDIR /app
RUN pip install scikit-learn
COPY app.py .
CMD ["python", "app.py"]
EOF
