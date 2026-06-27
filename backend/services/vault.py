import streamlit as st

# ============================================================
# VAULT SECURIZAT - Pagina Modul in Lucru
# ============================================================
# Fisier: pages/vault_module.py sau direct in app.py

# --- CSS Custom pentru carduri si badge ---
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap');

body {
    font-family: 'Inter', sans-serif;
}

/* Badge IN LUCRU */
.badge-in-lucru {
    display: inline-block;
    background-color: #fff7ed;
    color: #c2410c;
    font-size: 12px;
    font-weight: 600;
    padding: 4px 12px;
    border-radius: 999px;
    border: 1px solid #fed7aa;
    letter-spacing: 0.5px;
    text-transform: uppercase;
}

/* Card principal (hero) */
.card-module {
    background: #ffffff;
    border: 1px solid #e2e8f0;
    border-radius: 16px;
    padding: 32px;
    margin-bottom: 24px;
    box-shadow: 0 1px 3px rgba(0,0,0,0.04);
}

/* Card capabilitate */
.card-capability {
    background: #ffffff;
    border: 1px solid #e2e8f0;
    border-radius: 12px;
    padding: 24px;
    height: 100%;
    transition: border-color 0.2s, box-shadow 0.2s;
}

.card-capability:hover {
    border-color: #cbd5e1;
    box-shadow: 0 4px 12px rgba(0,0,0,0.05);
}

/* Icon in card */
.card-icon {
    font-size: 28px;
    margin-bottom: 12px;
    display: block;
}

/* Titlu card */
.card-title {
    font-size: 15px;
    font-weight: 600;
    color: #1e293b;
    margin-bottom: 16px;
    line-height: 1.3;
}

/* Lista bullet */
.card-bullets {
    list-style: none;
    padding: 0;
    margin: 0;
}

.card-bullets li {
    font-size: 13px;
    color: #475569;
    line-height: 1.6;
    margin-bottom: 8px;
    padding-left: 16px;
    position: relative;
}

.card-bullets li::before {
    content: "•";
    position: absolute;
    left: 0;
    color: #94a3b8;
    font-weight: 700;
}

/* Progress bar custom */
.progress-container {
    margin-top: 16px;
}

.progress-label {
    font-size: 12px;
    color: #64748b;
    margin-bottom: 6px;
}

.progress-bar-bg {
    background: #e2e8f0;
    border-radius: 999px;
    height: 8px;
    overflow: hidden;
}

.progress-bar-fill {
    background: #3b82f6;
    width: 40%;
    height: 100%;
    border-radius: 999px;
    transition: width 0.3s;
}

/* Buton CTA */
.cta-button {
    background: #1e293b;
    color: #ffffff;
    border: none;
    border-radius: 8px;
    padding: 12px 24px;
    font-size: 14px;
    font-weight: 500;
    cursor: pointer;
    transition: background 0.2s;
}

.cta-button:hover {
    background: #334155;
}

/* Hero section */
.hero-title {
    font-size: 28px;
    font-weight: 700;
    color: #1e293b;
    margin-bottom: 8px;
    display: flex;
    align-items: center;
    gap: 12px;
}

.hero-subtitle {
    font-size: 15px;
    color: #64748b;
    margin-bottom: 20px;
    line-height: 1.5;
}

/* Highlight box */
.highlight-box {
    background: #f8fafc;
    border-left: 3px solid #3b82f6;
    border-radius: 0 8px 8px 0;
    padding: 16px 20px;
    margin-top: 24px;
}

.highlight-box p {
    font-size: 14px;
    color: #334155;
    margin: 0;
    line-height: 1.6;
}

.highlight-box strong {
    color: #1e293b;
}
</style>
""", unsafe_allow_html=True)

# ============================================================
# HERO SECTION
# ============================================================
st.markdown("""
<div class="card-module">
    <div class="hero-title">
        🔒 Vault Securizat
        <span class="badge-in-lucru">ÎN LUCRU</span>
    </div>
    <div class="hero-subtitle">
        Arhivă completă, securizată — gata de audit Big4
    </div>
    <div class="progress-container">
        <div class="progress-label">Progres implementare: 40%</div>
    </div>
    <div class="progress-bar-bg">
        <div class="progress-bar-fill"></div>
    </div>
</div>
""", unsafe_allow_html=True)

# ============================================================
# CARDURI CAPABILITĂȚI
# ============================================================
capabilities = [
    {
        "icon": "📁",
        "title": "Clienți + Documente",
        "bullets": [
            "Stochează toate documentele procesate (facturi, comenzi, avize)",
            "Structură pe clienți și proiecte, acces instant",
            "Versiuni și istoric complet pentru fiecare document",
            "Căutare full-text în conținutul documentelor"
        ]
    },
    {
        "icon": "💾",
        "title": "Backup Dual Automat",
        "bullets": [
            "Backup automat dual: cloud + HDD fizic",
            "Alertă la apropiere de limită stocare",
            "Verificare automată a integrității backup-urilor",
            "Restaurare rapidă la orice moment"
        ]
    },
    {
        "icon": "📜",
        "title": "Retenție Legală",
        "bullets": [
            "Păstrează istoric clienți și documente 5 ani (conform legii)",
            "Situații financiare anuale: retenție 10 ani",
            "Dosare de personal: retenție 50 ani",
            "Format digital acceptat legal (PDF/A)"
        ]
    },
    {
        "icon": "🛡️",
        "title": "Securitate Deplină",
        "bullets": [
            "Zero ransomware — izolare completă",
            "Criptare AES-256 end-to-end",
            "Acces bazat pe roluri și audit trail",
            "Conformitate GDPR și ISO 27001"
        ]
    },
    {
        "icon": "🔍",
        "title": "Audit Big4 Ready",
        "bullets": [
            "Export structurat pentru audit extern",
            "PDF-uri originale + hash de verificare",
            "Loguri imutabile cu timestamp",
            "Rapoarte de conformitate generate automat"
        ]
    }
]

# Render carduri in grid 3 coloane (ultimul rand va avea 2 carduri)
for row_start in range(0, len(capabilities), 3):
    cols = st.columns(3)
    for i in range(3):
        idx = row_start + i
        if idx < len(capabilities):
            cap = capabilities[idx]
            with cols[i]:
                bullets_html = "\n".join([f'<li>{b}</li>' for b in cap["bullets"]])
                st.markdown(f"""
                <div class="card-capability">
                    <span class="card-icon">{cap["icon"]}</span>
                    <div class="card-title">{cap["title"]}</div>
                    <ul class="card-bullets">
                        {bullets_html}
                    </ul>
                </div>
                """, unsafe_allow_html=True)

# ============================================================
# HIGHLIGHT BOX (oferta de servicii)
# ============================================================
st.markdown("""
<div class="highlight-box">
    <p><strong>🛡️ Securitate deplină</strong> — zero ransomware, acces controlat, backup-uri verificate automat.</p>
    <p style="margin-top: 8px;"><strong>📊 Big 4 ready</strong> — export structurat pentru audit, PDF-uri originale + hash de verificare.</p>
</div>
""", unsafe_allow_html=True)

# ============================================================
# CTA BUTTON
# ============================================================
st.markdown("<br>", unsafe_allow_html=True)
col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    if st.button("🔔 Anunță-mă când e gata", use_container_width=True, type="primary"):
        st.success("✅ Vei fi notificat când modulul Vault Securizat devine disponibil!")
