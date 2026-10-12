# 🤖 Autonomous Incident Triage & Resolution Agent

> **Bab 1: Paradigma Agentic AI — Dari Model Generatif Pasif ke Entitas Otonom**  
> *Implementasi praktis loop kognitif otonom (Perceive-Reason-Act) untuk investigasi, remediasi mandiri, dan eskalasi insiden server SRE enterprise.*

[![Open in Streamlit](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://agentic-incident-triage.streamlit.app)
[![GitHub Repository](https://img.shields.io/badge/GitHub-agentic__incident__triage-blue?logo=github)](https://github.com/muryanawaludin/agentic_incident_triage.git)
[![Python 3.10+](https://img.shields.io/badge/Python-3.10%2B-blue?logo=python)](https://www.python.org/)

---

## 🚀 Live Demo Aplikasi

Uji coba langsung bagaimana agen SRE otonom mendeteksi anomali, membersihkan cache, me-restart pod, dan mengeskalasi insiden kritis ke tim manusia tanpa perlu instalasi lokal:

👉 [**KLIK DI SINI UNTUK DEMO APLIKASI**](https://agentic-incident-triage.streamlit.app)

*(Repositori GitHub: [muryanawaludin/agentic_incident_triage](https://github.com/muryanawaludin/agentic_incident_triage.git))*

---

## ⚡ Pergeseran Paradigma: AI Pasif vs Agentic AI

| Dimensi | AI Generatif Pasif (Single-Turn) | Agentic AI (Closed Cognitive Loop) |
| :--- | :--- | :--- |
| **Pola Interaksi** | Statis (*Prompt* $\to$ *Response*) | Dinamis (*Perceive* $\to$ *Reason* $\to$ *Act* $\to$ *Observe*) |
| **Intervensi Sistem** | Tidak bisa mengubah status server | Mengeksekusi alat riil (telemetri, API, restart pod) |
| **Penanganan Masalah**| Terbatas pada saran berbasis teks | Mengambil tindakan korektif mandiri sampai tuntas |
| **Mitigasi Risiko** | Rawan halusinasi tanpa verifikasi | Terikat *guardrails* & eskalasi manusia (*Human-in-the-Loop*) |

---

## 🎯 2 Skenario Uji Industri

1. **Auto-Remediation (Auth Service - OOM Error):**  
   Agen mendeteksi penggunaan RAM >90%, memeriksa runbook SRE, membersihkan stale cache Redis, melakukan *rolling restart*, dan memverifikasi kesehatan metrik hingga status `RESOLVED`.
2. **Responsible Human Escalation (Payment Gateway - DB Deadlock):**  
   Agen menemukan kebuntuan transaksi (*deadlock*) pada core banking yang berisiko finansial, membatasi kewenangan otonomnya, dan mengalihkan tiket ke tim insinyur manusia dengan status `ESCALATED_TO_HUMAN`.

---

## 🛠️ Panduan Menjalankan Cepat (3 Langkah)

```bash
# 1. Kloning repositori
git clone https://github.com/muryanawaludin/agentic_incident_triage.git
cd agentic_incident_triage

# 2. Pasang dependensi pustaka
pip install -r requirements.txt

# 3. Jalankan aplikasi Streamlit
streamlit run app.py
```

Aplikasi akan otomatis terbuka pada peramban di alamat `http://localhost:8501`.

---

## 📁 Struktur Direktori

```text
agentic_incident_triage/
├── agent/
│   ├── schema.py         # Skema data Pydantic (tiket, langkah kognitif, resolusi)
│   ├── tools.py          # Registri alat SRE (telemetri, log, redis, restart pod)
│   └── engine.py         # Mesin penalaran ReAct loop
├── config.py             # Konfigurasi sistem dan parameter agen
├── requirements.txt      # Dependensi proyek
├── app.py                # Dasbor visualisasi interaktif Streamlit
└── README.md             # Dokumentasi repositori
```

---

## 👨‍💻 Penulis & Peneliti

**Muryan Awaludin, S.Kom., M.Kom.**  
Dosen, Peneliti Kecerdasan Buatan & Konsultan Teknologi Informasi  
GitHub: [@muryanawaludin](https://github.com/muryanawaludin)

---

## ⚖️ Hak Cipta

© 2026 **Muryan Awaludin**. Seluruh hak cipta dilindungi undang-undang.  
*Materi ini merupakan bagian dari buku **Rekayasa Agentic AI: Dari Blueprint Kognitif hingga Orkestrasi Sistem Multi-Agen Enterprise**.*