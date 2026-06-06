def verify_2fa(username):
    if st.session_state.get("logged_in", False):
        return True
    
    if is_blocked(username):
        block_until = st.session_state[f"blocked_until_{username}"]
        minutes_left = int((block_until - datetime.now()).total_seconds() / 60) + 1
        st.error(f"❌ Cont blocat temporar. Încearcă din nou peste {minutes_left} minute.")
        if st.button("◀️ Înapoi la autentificare"):
            st.session_state.awaiting_2fa = False
            st.session_state.pending_2fa_user = None
            st.rerun()
        return False
    
    # Afișare 2FA
    st.markdown("---")
    st.markdown("<h3 style='text-align: center;'>🔐 Verificare cod securitate</h3>", unsafe_allow_html=True)
    st.markdown(f"<p style='text-align: center;'>Utilizator: <b>{username}</b></p>", unsafe_allow_html=True)
    
    # Încercări rămase
    attempts_used = st.session_state.get(f"{LOGIN_ATTEMPTS_KEY}_{username}", 0)
    remaining = MAX_ATTEMPTS - attempts_used
    if remaining > 0:
        st.warning(f"⚠️ Mai ai {remaining} încercări rămase.")
    
    # Câmp PIN
    pin_input = st.text_input("Cod PIN (6 cifre)", type="password", max_chars=6, placeholder="Introdu PIN", key="pin_input_field")
    
    col1, col2, col3 = st.columns([1, 1, 1])
    with col1:
        if st.button("✅ Verifică", use_container_width=True):
            if not pin_input:
                st.error("Introdu codul PIN")
                st.rerun()
            elif len(pin_input) != 6 or not pin_input.isdigit():
                st.error("PIN invalid. Trebuie să fie exact 6 cifre.")
                st.rerun()
            elif verify_pin(username, pin_input):
                st.session_state[f"{LOGIN_ATTEMPTS_KEY}_{username}"] = 0
                st.success("✅ Cod corect!")
                return True
            else:
                was_blocked = register_failed_attempt(username)
                remaining_after = MAX_ATTEMPTS - st.session_state.get(f"{LOGIN_ATTEMPTS_KEY}_{username}", 0)
                if was_blocked:
                    st.error(f"❌ Prea multe încercări eșuate! Cont blocat {BLOCK_DURATION_MINUTES} minute.")
                else:
                    st.error(f"❌ Cod incorect! Mai ai {remaining_after} încercări.")
                st.rerun()
    
    with col3:
        if st.button("◀️ Înapoi", use_container_width=True):
            st.session_state.awaiting_2fa = False
            st.session_state.pending_2fa_user = None
            st.rerun()
    
    return False
