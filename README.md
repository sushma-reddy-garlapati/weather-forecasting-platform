# 🌦️ Weather Forecasting Platform

A real-time AI-powered dashboard for weather prediction across multiple cities. Built with Python, Streamlit, and GitHub Actions, this project includes modular components for data ingestion, model inference, and visualization — all wrapped in a clean, interactive UI.

---

## 🌟 Project Highlights

- 📈 **Forecasting Engine**: Predicts temperature and humidity using historical weather data
- 🧠 **Modular ML Pipeline**: Includes ingestion, preprocessing, model training, and inference
- 🎨 **Streamlit Dashboard**: Interactive UI with city-level filtering and dynamic charts
- ⚙️ **CI/CD Automation**: GitHub Actions automate model training and dashboard deployment
- 🧪 **Clean Architecture**: Structured repo with folders for `api`, `dashboard`, `models`, `ingestion`, and `infra`

---

## 💼 Skills Demonstrated

- Python, pandas, scikit-learn
- Streamlit for frontend UI
- GitHub Actions for CI/CD
- Modular repo design and automation
- Real-time data visualization and caching

---

## 🧰 Tech Stack

### ⚙️ Backend & Modeling
- **Python** – Core language for data processing and modeling  
- **pandas** – Data ingestion and transformation  
- **scikit-learn** – ML models for temperature and humidity prediction  
- **joblib** – Model serialization and loading  
- **cities.py** – Custom city metadata and location mapping

### 🎨 Frontend
- **Streamlit** – Interactive dashboard with dropdown filters and charts  
- **Matplotlib / Plotly** – Visualizations for forecast trends

### 🔁 Automation & DevOps
- **GitHub Actions** – CI/CD pipeline for model training and dashboard deployment  
- **requirements.txt** – Dependency management  
- **.github/workflows/** – Contains automated workflow definitions

### 📁 Repo Structure
- `api/` – API logic and endpoints  
- `dashboard/` – Streamlit UI components  
- `data/` – Raw and processed weather datasets  
- `models/` – Trained model files  
- `ingestion/` – Scripts for data loading and cleaning  
- `infra/` – CI/CD and deployment configs  
- `notebooks/` – Exploratory analysis and model prototyping

---

## 🚀 Setup Instructions

```bash
# Clone the repository
git clone https://github.com/sushma-reddy-garlapati/weather-forecasting-platform.git
cd weather-forecasting-platform

# Install dependencies
pip install -r requirements.txt

# Run the dashboard
streamlit run dashboard/app.py
