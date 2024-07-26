import streamlit as st
import os
import uuid
import io
import zipfile
import firebase_admin
from firebase_admin import credentials, firestore, storage
from PIL import Image

from firebase_helpers import save_image, create_zip, get_counts
import uuid

from upload_section import upload_section
from search_section import search_section
from tracker_section import tracker_section

def main():
    st.title("Orvosi Röntgen Adatbázis")
    upload_section()
    search_section()
    tracker_section()

if __name__ == "__main__":
    main()

