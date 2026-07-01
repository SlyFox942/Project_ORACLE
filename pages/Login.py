import streamlit as st
import hashlib

from components.footer import show_footer

st.title("🔐 Login")
st.caption("Project ORACLE Access Control")


def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()


# Demo users for v5.1
USERS = {
    "vanessa": {
        "password_hash": hash_password("oracle123"),
        "role": "Admin"
    },
    "analyst": {
        "password_hash": hash_password("analyst123"),
        "role": "Analyst"
    },
    "guest": {
        "password_hash": hash_password("guest123"),
        "role": "Guest"
    }
}


if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

if "username" not in st.session_state:
    st.session_state.username = None

if "role" not in st.session_state:
    st.session_state.role = None


if st.session_state.logged_in:
    st.success(f"Logged in as {st.session_state.username}")
    st.info(f"Role: {st.session_state.role}")

    if st.button("Logout"):
        st.session_state.logged_in = False
        st.session_state.username = None
        st.session_state.role = None
        st.rerun()

else:
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")

    if st.button("Login"):
        user = USERS.get(username.lower())

        if user and user["password_hash"] == hash_password(password):
            st.session_state.logged_in = True
            st.session_state.username = username.lower()
            st.session_state.role = user["role"]
            st.success("Login successful.")
            st.rerun()
        else:
            st.error("Invalid username or password.")


st.divider()

st.subheader("Demo Accounts")

st.code("""
Admin:
username: vanessa
password: oracle123

Analyst:
username: analyst
password: analyst123

Guest:
username: guest
password: guest123
""")

show_footer()