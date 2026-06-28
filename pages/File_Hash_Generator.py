import streamlit as st
import hashlib

from components.footer import show_footer

st.title("🔐 File Hash Generator")
st.caption("ORACLE Cyber Lab")

st.write(
    """
Upload a file to calculate its cryptographic hash values.
This is useful for file integrity checks, malware analysis basics,
and digital forensics workflows.
"""
)

uploaded_file = st.file_uploader("Upload a file", type=None)

def calculate_hash(file_bytes, algorithm):
    hash_object = hashlib.new(algorithm)
    hash_object.update(file_bytes)
    return hash_object.hexdigest()

if uploaded_file:
    file_bytes = uploaded_file.read()

    st.subheader("📁 File Information")
    st.write(f"**File Name:** {uploaded_file.name}")
    st.write(f"**File Size:** {len(file_bytes)} bytes")

    st.subheader("🔎 Hash Values")

    md5_hash = calculate_hash(file_bytes, "md5")
    sha1_hash = calculate_hash(file_bytes, "sha1")
    sha256_hash = calculate_hash(file_bytes, "sha256")

    st.code(f"MD5:    {md5_hash}")
    st.code(f"SHA-1:  {sha1_hash}")
    st.code(f"SHA-256:{sha256_hash}")

    st.success("Hashes generated successfully.")

st.subheader("✅ Verify File Hash")

known_hash = st.text_input(
        "Paste a known hash to compare",
        placeholder="Paste MD5, SHA-1, or SHA-256 hash here"
    )

if known_hash:
        known_hash = known_hash.strip().lower()

        if known_hash in [md5_hash, sha1_hash, sha256_hash]:
            st.success("Hash match! File integrity verified.")
        else:
            st.error("Hash does not match this file.")

show_footer()