import streamlit as st

# ============================================================
# VAULT SECURIZAT - Pagina Modul in Lucru
# ============================================================

st.markdown("""
<style>
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
        <span style="font-size:32px;">&#128274;</span> Vault Securizat
        <span class="badge-in-lucru">IN LUCRU</span>
    </div>
    <div class="hero-subtitle">
        Arhiva completa, securizata — gata de audit Big4
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
# CARDURI CAPABILITATI
# ============================================================
capabilities = [
    {
        "icon": "&#128451;",
        "title": "Clienti + Documente",
        "bullets": [
            "Stocheaza toate documentele procesate (facturi, comenzi, avize)",
            "Structura pe clienti si proiecte, acces instant",
            "Versiuni si istoric complet pentru fiecare document",
            "Cautare full-text in continutul documentelor"
        ]
    },
    {
        "icon": "&#128190;",
        "title": "Backup Dual Automat",
        "bullets": [
            "Backup automat dual: cloud + HDD fizic",
            "Alerta la apropiere de limita stocare",
            "Verificare automata a integritatii backup-urilor",
            "Restaurare rapida la orice moment"
        ]
    },
    {
        "icon": "&#128220;",
        "title": "Retentie Legala",
        "bullets": [
            "Pastreaza istoric clienti si documente 5 ani (conform legii)",
            "Situatii financiare anuale: retentie 10 ani",
            "Dosare de personal: retentie 50 ani",
            "Format digital acceptat legal (PDF/A)"
        ]
    },
    {
        "icon": "&#128737;",
        "title": "Securitate Deplina",
        "bullets": [
            "Zero ransomware — izolare completa",
            "Criptare AES-256 end-to-end",
            "Acces bazat pe roluri si audit trail",
            "Conformitate GDPR si ISO 27001"
        ]
    },
    {
        "icon": "&#128269;",
        "title": "Audit Big4 Ready",
        "bullets": [
            "Export structurat pentru audit extern",
            "PDF-uri originale + hash de verificare",
            "Loguri imutabile cu timestamp",
            "Rapoarte de conformitate generate automat"
        ]
    }
]

# Render carduri in grid 3 coloane
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
    <p><strong>&#128737; Securitate deplina</strong> — zero ransomware, acces controlat, backup-uri verificate automat.</p>
    <p style="margin-top: 8px;"><strong>&#128202; Big 4 ready</strong> — export structurat pentru audit, PDF-uri originale + hash de verificare.</p>
</div>
""", unsafe_allow_html=True)

# ============================================================
# CTA BUTTON
# ============================================================
st.markdown("<br>", unsafe_allow_html=True)
col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    if st.button("&#128276; Anunta-ma cand e gata", use_container_width=True, type="primary"):
        st.success("Vei fi notificat cand modulul Vault Securizat devine disponibil!")
