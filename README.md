# ☀️ Solar Power Forecasting App

An end-to-end Machine Learning web application that predicts **solar energy generation** using real-time weather data.
Built with **FastAPI (backend)**, **Streamlit (frontend)**, and deployed using **Docker**.

---

## 🚀 Features

* 🔍 City-based solar power prediction
* 🌦️ Real-time weather data integration
* 📊 7-day solar generation forecast
* ⏱️ Hourly energy breakdown visualization
* 📈 Interactive charts using Plotly
* 🔐 API key-based request validation
* 🐳 Fully Dockerized (API + UI)

---

## 🧠 Tech Stack

* **Machine Learning**: Scikit-learn, NumPy, Pandas
* **Backend**: FastAPI
* **Frontend**: Streamlit
* **Visualization**: Plotly
* **API Source**: Open-Meteo
* **Deployment**: Docker

---

## 📂 Project Structure

```
Solar_power/
│
├── api.py              # FastAPI backend
├── app.py              # Streamlit frontend
├── main.py             # ML pipeline & prediction logic
├── requirements.txt
├── Dockerfile
│
├── Model/
│   └── model_results.png
│
└── README.md
```

---

## ⚙️ How It Works

1. User enters a **city name**
2. App fetches **weather data** from API
3. Data is processed and converted into features
4. ML model predicts **solar energy (kWh)**
5. Results are shown via charts and metrics

---

## 🐳 Run with Docker

```bash
docker build -t solar-app .
docker run -p 8000:8000 -p 8501:8501 solar-app
```

* FastAPI → http://localhost:8000
* Streamlit → http://localhost:8501

---

## 💻 Run Locally

```bash
pip install -r requirements.txt

# Run API
uvicorn api:app --reload

# Run Streamlit
streamlit run app.py
```

---

## 📊 Sample Output

* Daily solar generation (kWh)
* Hourly energy prediction
* Weather metrics (temperature, humidity, wind, cloud)

---

## ⚠️ Note

* Datasets are **not included** due to size limitations
* Model file (`.pkl`) should be placed inside the `Model/` folder

---

## 📌 Future Improvements

* Deploy on cloud (AWS / Render)
* Add user authentication
* Improve model accuracy
* Add historical data comparison

---

## 👨‍💻 Author

Harmandeep Singh

---

## ⭐ If you like this project

Give it a ⭐ on GitHub!
