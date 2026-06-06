"""
Modul 2FA simplu cu PIN fix + blocare dupa 3 incercari
FARA fisier JSON - PIN-uri direct in cod
"""

import streamlit as st
import hashlib
from datetime import datetime, timedelta

# ========== CONFIGURARE ==========
LOGIN_ATTEMPTS_KEY = "pin_failed_attempts"
BLOCK_DURATION_MINUTES = 15
MAX_ATTEMPTS = 3

# ========== PIN-URI DIRECT IN COD ==========
# Modifica aici PIN-urile pentru fiecare utilizator
PIN_URI = {
    "angajat": hashlib.sha256("111111".encode()).hexdigest(),
    "manager": hashlib.sha256("123456".encode()).hexdigest(),
    "admin": hashlib.sha256("333333".encode()).hexdigest()
}

def is_blocked(username):
    if f"blocked_until_{username}" not in st.session_state:
        return False
    block_until = st.session_state[f"blocked_until_{username}"]
    if datetime.now() < block_until:
        return True
    del st.session_state[f"blocked_until_{username}"]
    st.session_state[f"{LOGIN_ATTEMPTS_KEY}_{username}"] = 0
    return False

def register_failed_attempt(username):
    attempts_key = f"{LOGIN_ATTEMPTS_KEY}_{username}"
    attempts = st.session_state.get(attempts_key, 0) + 1
    st.session_state[attempts_key] = attempts
    if attempts >= MAX_ATTEMPTS:
        block_until = datetime.now() + timedelta(minutes=BLOCK_DURATION_MINUTES)
        st.session_state[f"blocked_until_{username}"] = block_until
        st.session_state[attempts_key] = 0
        return True
    return False

def unblock_user(username):
    if f"blocked_until_{username}" in st.session_state:
        del st.session_state[f"blocked_until_{username}"]
    st.session_state[f"{LOGIN_ATTEMPTS_KEY}_{username}"] = 0

def verify_pin(username, pin_input):
    if username not in PIN_URI:
        return False
    pin_hash = hashlib.sha256(pin_input.encode()).hexdigest()
    return pin_hash == PIN_URI[username]

def change_pin(username, new_pin):
    """Schimba PIN-ul in memorie (pierdut la restart)"""
    if username not in PIN_URI:
        return False
    PIN_URI[username] = hashlib.sha256(new_pin.encode()).hexdigest()
    return True
# ====================================================
def verify_2fa(username):
    if st.session_state.get("logged_in", False):
        return True
    
    # Verifică blocarea
    block_key = f"blocked_until_{username}"
    if block_key in st.session_state:
        block_until = st.session_state[block_key]
        if datetime.now() < block_until:
            minutes_left = int((block_until - datetime.now()).total_seconds() / 60) + 1
            st.error(f"❌ Cont blocat temporar. Încearcă din nou peste {minutes_left} minute.")
            c1, c2, c3 = st.columns([1, 2, 1])
            with c2:
                if st.button("◀️ Înapoi la autentificare", key="back_blocked", use_container_width=True):
                    st.session_state.awaiting_2fa = False
                    st.session_state.pending_2fa_user = None
                    st.rerun()
            return False
        else:
            # Blocarea a expirat - curățare
            del st.session_state[block_key]
            st.session_state[f"{LOGIN_ATTEMPTS_KEY}_{username}"] = 0
    
    # Container centrat pentru 2FA
    col1, col2, col3 = st.columns([3, 3, 3])
    with col2:
        st.markdown("---")
        st.markdown("<h3 style='text-align: center;'>🔐 Verificare cod securitate</h3>", unsafe_allow_html=True)
        st.markdown(f"<p style='text-align: center;'>Utilizator: <b>{username}</b></p>", unsafe_allow_html=True)
        
        with st.form(key=f"2fa_form_{username}"):
            pin_input = st.text_input("Cod PIN (6 cifre)", type="password", max_chars=6, placeholder="Introdu PIN și apasă Enter", label_visibility="collapsed")
            
            col_btn1, col_btn2 = st.columns(2)
            
            with col_btn1:
                submitted = st.form_submit_button("✅ Verifică", use_container_width=True)
            
            with col_btn2:
                if st.form_submit_button("◀️ Înapoi", use_container_width=True):
                    st.session_state.awaiting_2fa = False
                    st.session_state.pending_2fa_user = None
                    st.rerun()
            
            if submitted:
                if not pin_input:
                    st.error("❌ Introdu codul PIN")
                elif len(pin_input) != 6 or not pin_input.isdigit():
                    st.error("❌ PIN invalid. Trebuie să fie exact 6 cifre.")
                elif verify_pin(username, pin_input):
                    st.session_state[f"{LOGIN_ATTEMPTS_KEY}_{username}"] = 0
                    st.success("✅ Cod corect!")
                    return True
                else:
                    was_blocked = register_failed_attempt(username)
                    new_attempts = st.session_state.get(f"{LOGIN_ATTEMPTS_KEY}_{username}", 0)
                    if was_blocked:
                        st.error(f"❌ Prea multe încercări eșuate! Cont blocat {BLOCK_DURATION_MINUTES} minute.")
                    else:
                        st.error(f"❌ Cod incorect! Mai ai {MAX_ATTEMPTS - new_attempts} încercări.")
        
        # Mesaj încercări eșuate
        attempts_used = st.session_state.get(f"{LOGIN_ATTEMPTS_KEY}_{username}", 0)
        if attempts_used > 0:
            st.markdown(f"""
            <div style="background-color: #fff3cd; border-left: 4px solid #ffc107; padding: 10px; border-radius: 5px; text-align: center;">
                ⚠️ <b>Atenție!</b> Ai deja <b>{attempts_used}</b> încercări eșuate.<br>
                Mai ai <b>{MAX_ATTEMPTS - attempts_used}</b> încercări înainte de blocare.
            </div>
            """, unsafe_allow_html=True)
    
    return False
