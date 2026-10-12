"""
Aplikasi Antarmuka Pengguna Streamlit untuk Autonomous Incident Triage.
Menyediakan visualisasi interaktif alur kognitif Thought-Action-Observation secara transparan.
"""
import streamlit as st
import json
from datetime import datetime
from agent.schema import IncidentTicket
from agent.engine import ReActIncidentAgent

# Konfigurasi Tampilan Halaman
st.set_page_config(
    page_title="Autonomous Incident Triage Agent",
    page_icon="🤖",
    layout="wide"
)

st.title("🤖 Autonomous Incident Triage & Resolution Agent")
st.caption("Penerapan Paradigma Agentic AI: Loop Kognitif Otonom untuk Pemulihan Insiden Enterprise")

# Inisialisasi Mesin Agen
if "agent_engine" not in st.session_state:
    st.session_state.agent_engine = ReActIncidentAgent()

# Pilihan Preset Tiket Insiden untuk Demonstrasi Industri
ticket_presets = {
    "Kasus 1: Out of Memory pada Auth Service (Dapat Sembuh Otonom)": IncidentTicket(
        ticket_id="INC-2026-9041",
        service_name="auth-service",
        severity="HIGH",
        error_message="High memory usage alert: memory_percent exceeds 94%, OutOfMemoryError in auth workers",
        reported_at=datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    ),
    "Kasus 2: Database Deadlock pada Payment Gateway (Butuh Eskalasi)": IncidentTicket(
        ticket_id="INC-2026-8812",
        service_name="payment-gateway",
        severity="CRITICAL",
        error_message="Severe payment latency: Deadlock detected in database transactions, connection pool exhausted",
        reported_at=datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    )
}

# Sidebar: Pengaturan, Metadata Tiket, dan Hak Cipta
with st.sidebar:
    st.header("📋 Konfigurasi Tiket Insiden")
    selected_preset_key = st.selectbox("Pilih Skenario Insiden:", list(ticket_presets.keys()))
    selected_ticket = ticket_presets[selected_preset_key]

    # Tombol diletakkan di atas agar langsung terlihat tanpa terpotong
    btn_start_agent = st.button("🚀 Jalankan Investigasi Agen", type="primary", use_container_width=True)

    st.divider()
    st.markdown(f"**ID Tiket:** `{selected_ticket.ticket_id}`")
    st.markdown(f"**Mikroservis:** `{selected_ticket.service_name}`")
    st.markdown(f"**Tingkat Keparahan:** `{selected_ticket.severity}`")
    st.markdown(f"**Waktu Masuk:** `{selected_ticket.reported_at}`")

    # Label diperjelas agar tidak disalahartikan sebagai eror aplikasi
    st.markdown("**Detail Gejala Insiden:**")
    st.info(selected_ticket.error_message)

    st.divider()
    st.markdown("© 2026 **Muryan Awaludin**  \nHak Cipta Dilindungi.")

# Area Kerja Utama
col_left, col_right = st.columns([1.1, 0.9])

with col_left:
    st.subheader("🔍 Jejak Kognitif Agen (Agent Reasoning Trace)")
    
    if btn_start_agent:
        with st.spinner("Agen sedang mengamati lingkungan, bernalar, dan mengeksekusi alat..."):
            resolution = st.session_state.agent_engine.run_investigation(selected_ticket)
            st.session_state.last_resolution = resolution
            st.session_state.last_ticket = selected_ticket

    if "last_resolution" in st.session_state:
        res = st.session_state.last_resolution
        
        for step in res.execution_steps:
            with st.expander(f"📍 **Iterasi {step.iteration}: Eksekusi `{step.action_name}`**", expanded=True):
                st.markdown(f"**🧠 Pemikiran Agen (Thought):**\n*{step.thought}*")
                st.markdown(f"**⚡ Aksi yang Dipanggil (Action):** `{step.action_name}`")
                st.code(json.dumps(step.action_params, indent=2), language="json")
                st.markdown("**🔬 Observasi dari Lingkungan (Observation):**")
                
                try:
                    formatted_obs = json.loads(step.observation)
                    st.json(formatted_obs)
                except Exception:
                    st.text(step.observation)

with col_right:
    st.subheader("📊 Hasil Resolusi & Dampak Operasional")
    
    if "last_resolution" in st.session_state:
        res = st.session_state.last_resolution
        
        if res.status == "RESOLVED":
            st.success("✅ **STATUS: INSIDEN TUNTAS SECARA OTONOM**")
        elif res.status == "ESCALATED_TO_HUMAN":
            st.warning("⚠️ **STATUS: DITERUSKAN KE TIM REKAYASA MANUSIA (ESCALATED)**")
        else:
            st.error("❌ **STATUS: INVESTIGASI GAGAL**")

        st.markdown("### Ringkasan Eksekutif")
        st.write(res.executive_summary)

        st.markdown("### Diagnosis Akar Masalah")
        st.info(res.root_cause)

        st.markdown("### Metrik Verifikasi Lingkungan Pasca-Aksi")
        st.code(res.verification_metrics, language="bash")

        st.markdown("### Rantai Aksi yang Dilakukan")
        st.write(", ".join([f"`{act}`" for act in res.actions_executed]))
    else:
        st.info("Silakan klik tombol **'Jalankan Investigasi Agen'** pada panel samping untuk memulai siklus kerja kognitif.")

# Kaki Halaman (Footer) Hak Cipta
st.divider()
st.caption("Rekayasa Agentic AI | © 2026 Muryan Awaludin. Seluruh hak cipta dilindungi undang-undang.")