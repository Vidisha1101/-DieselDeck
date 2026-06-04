<div align="center">

```
██████╗ ██╗███████╗███████╗███████╗██╗     ██████╗ ███████╗ ██████╗██╗  ██╗
██╔══██╗██║██╔════╝██╔════╝██╔════╝██║     ██╔══██╗██╔════╝██╔════╝██║ ██╔╝
██║  ██║██║█████╗  ███████╗█████╗  ██║     ██║  ██║█████╗  ██║     █████╔╝ 
██║  ██║██║██╔══╝  ╚════██║██╔══╝  ██║     ██║  ██║██╔══╝  ██║     ██╔═██╗ 
██████╔╝██║███████╗███████║███████╗███████╗██████╔╝███████╗╚██████╗██║  ██╗
╚═════╝ ╚═╝╚══════╝╚══════╝╚══════╝╚══════╝╚═════╝ ╚══════╝ ╚═════╝╚═╝  ╚═╝
```

### 🚛 Fleet Intelligence Dashboard for Indian Truck Owners
### *Every rupee tracked. Every route optimised. Every driver accountable.*

---

[![Live App](https://img.shields.io/badge/🚛%20Live%20App-Open%20DieselDeck-F5A623?style=for-the-badge&logoColor=black)](https://gerryhpmd8gnoobk3lfzds.streamlit.app/)
[![Python](https://img.shields.io/badge/Python-3.10+-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://python.org)
[![Streamlit](https://img.shields.io/badge/Streamlit-1.x-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)](https://streamlit.io)
[![Pandas](https://img.shields.io/badge/Pandas-2.x-150458?style=for-the-badge&logo=pandas&logoColor=white)](https://pandas.pydata.org)
[![Plotly](https://img.shields.io/badge/Plotly-Interactive-3F4F75?style=for-the-badge&logo=plotly&logoColor=white)](https://plotly.com)
[![Excel](https://img.shields.io/badge/Excel-Trip%20Sheet%20Input-217346?style=for-the-badge&logo=microsoftexcel&logoColor=white)](https://microsoft.com/excel)

</div>

---

## 📌 Overview

**DieselDeck** is a fleet management web app built for Indian truck fleet owners — not accountants, not software engineers, not the boardroom.

Upload your **Excel trip sheet** and instantly get a full intelligence dashboard: live truck status, per-KM cost breakdown, fuel theft detection, driver rankings, and a one-click WhatsApp summary for Monday morning — all without touching a formula.

> Built with Python + Streamlit. Runs in any browser. No installation for end users.

---

## ✨ Features

### 🛣️ Live Truck Status Board
- See every truck's current status at a glance
- Per-KM cost breakdown per vehicle
- Route progress tracker — know where each truck is in its journey

### ⛽ Fuel Anomaly Detection
- Automatically detects unusual fuel consumption patterns
- Flags suspected theft with a **₹ loss estimate**
- No manual cross-checking required — spots it before the month ends

### 🏆 Driver Leaderboard
- Every driver scored on **efficiency + cost control**
- Reward your best performers with data to back it up
- Coach underperformers with specifics, not guesswork

### 📋 Auto-Generated Daily Action List
- Priority list auto-generated each day
- **One-click WhatsApp summary** formatted for Monday reports
- Fleet owners actually read it — because it's built for them

### 📊 Trip Profit / Loss Preview
- Add or edit trips and see **live P&L impact before saving**
- Confirm margins before committing — no surprises at month-end

### 📁 Excel Trip Sheet Upload
- Upload your existing `.xlsx` trip sheet directly
- DieselDeck parses it instantly — **no reformatting needed**
- Supports standard Indian fleet trip sheet formats

---

## 🖥️ Tech Stack

| Technology | Version | Role |
|---|---|---|
| 🐍 Python | 3.10+ | Core backend & data processing |
| 🎈 Streamlit | 1.x | Web UI framework |
| 🐼 Pandas | 2.x | Trip sheet parsing & data wrangling |
| 🔢 NumPy | 1.x | Numerical calculations |
| 📈 Plotly | 5.x | Interactive charts & visualisations |
| 📊 OpenPyXL / Excel | — | `.xlsx` trip sheet ingestion |
| 💬 WhatsApp | Web | One-click report sharing |

---

## 🚀 Quick Start

### Prerequisites
- Python 3.10 or higher
- pip
- An `.xlsx` trip sheet (standard format)

### Installation

```bash
# 1. Clone the repository
git clone https://github.com/your-username/DieselDeck.git
cd DieselDeck

# 2. Create and activate a virtual environment (recommended)
python -m venv venv
source venv/bin/activate        # macOS / Linux
venv\Scripts\activate           # Windows

# 3. Install dependencies
pip install -r requirements.txt

# 4. Run the app
streamlit run app.py
```

Open your browser at **`http://localhost:8501`** — then upload your Excel trip sheet to get started.

---

## 📊 Excel Trip Sheet Format

DieselDeck reads your existing `.xlsx` trip sheet. Expected columns:

| Column | Description | Example |
|---|---|---|
| `Truck No` | Vehicle registration number | `MH 12 AB 1234` |
| `Driver Name` | Driver full name | `Ramesh Kumar` |
| `Route` | Source → Destination | `Mumbai → Pune` |
| `Distance (km)` | Trip distance | `150` |
| `Fuel (L)` | Fuel consumed in litres | `45` |
| `Freight (₹)` | Revenue earned | `12000` |
| `Expenses (₹)` | Total trip expenses | `8500` |
| `Date` | Trip date | `2024-06-01` |

> ⚠️ Column names should match exactly (case-insensitive). Extra columns are ignored.

---

## 📁 Project Structure

```
DieselDeck/
├── modules/
│   ├── truck_status.py       # Live board + per-KM cost engine
│   ├── fuel_anomaly.py       # Theft & anomaly detection logic
│   ├── driver_board.py       # Leaderboard scoring algorithm
│   ├── action_list.py        # Daily priorities + WhatsApp formatter
│   └── trip_editor.py        # Add/edit trips with P&L preview
├── utils/
│   ├── excel_parser.py       # .xlsx ingestion & validation
│   └── formatters.py         # ₹ formatting, date helpers
├── app.py                    # Main Streamlit entry point
├── requirements.txt          # Python dependencies
└── README.md
```

---

## 📦 requirements.txt

```
streamlit>=1.30.0
pandas>=2.0.0
numpy>=1.24.0
plotly>=5.18.0
openpyxl>=3.1.0
xlrd>=2.0.1
```

---

## 🌍 Live Demo

Try the deployed app — no installation needed:

**👉 [https://gerryhpmd8gnoobk3lfzds.streamlit.app/](https://gerryhpmd8gnoobk3lfzds.streamlit.app/)**

Upload any `.xlsx` trip sheet and the full dashboard loads instantly.

---

## 🤝 Contributing

Pull requests are welcome. For major changes, open an issue first.

```bash
git checkout -b feature/your-feature
git commit -m "Add: your feature description"
git push origin feature/your-feature
# → Open a Pull Request
```

---

## 📄 License

This project is licensed under the **Apache 2.0 License** — free to use, modify, and distribute.

---

## 👨‍💻 Author

Built for Indian fleet owners who manage trucks on WhatsApp and Excel.

> *"Fleet management built for the road, not the boardroom."*

---

<div align="center">

🚛 &nbsp; **DieselDeck** &nbsp; • &nbsp; Fleet Intelligence Dashboard &nbsp; • &nbsp; Made in 🇮🇳

</div>
