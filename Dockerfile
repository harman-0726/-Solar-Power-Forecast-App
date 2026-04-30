FROM python:3.10-slim

WORKDIR /app

# copy all project files
COPY . .

# install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# expose ports
EXPOSE 8000
EXPOSE 8501

# run FastAPI + Streamlit
CMD ["sh", "-c", "uvicorn api:app --host 0.0.0.0 --port 8000 & streamlit run app.py --server.port 8501 --server.address 0.0.0.0"]