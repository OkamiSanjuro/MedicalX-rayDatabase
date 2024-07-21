import streamlit as st
from firebase_helpers import save_image
import uuid

def upload_section():
    st.markdown(
        """
        <style>
        .upload-title {
            font-size: 24px;
            font-weight: bold;
            color: black;
            margin-bottom: 20px;
            text-align: center;
        }
        .upload-button {
            font-size: 20px;
            background-color: #4CAF50;
            color: white;
            padding: 10px 20px;
            border: none;
            cursor: pointer;
            text-align: center;
            margin-top: 20px;
        }
        .upload-button:hover {
            background-color: #45a049;
        }
        </style>
        """,
        unsafe_allow_html=True,
    )

    st.markdown('<div class="upload-title">Kép feltöltése és címkézése</div>', unsafe_allow_html=True)

    patient_id = st.text_input("Beteg azonosító (hagyja üresen új beteg esetén)", str(uuid.uuid4()))

    uploaded_file = st.file_uploader("Válassz egy képet", type=["jpg", "jpeg", "png"])

    type = st.selectbox("Típus", ["Törött", "Normál", "Egyéb"])
    type_comment = st.text_input("Specifikálás (Egyéb)") if type == "Egyéb" else ""

    view = st.selectbox("Nézet", ["AP", "Lateral", "Egyéb"])
    view_comment = st.text_input("Specifikálás (Egyéb Nézet)") if view == "Egyéb" else ""

    main_region = st.selectbox("Fő régió", ["Felső végtag", "Alsó végtag", "Gerinc", "Koponya"])

    if main_region == "Felső végtag":
        sub_region = st.selectbox("Alrégió", ["Clavicula", "Scapula", "Váll", "Humerus", "Könyök", "Radius", "Ulna", "Csukló", "Kéz"])
    elif main_region == "Alsó végtag":
        sub_region = st.selectbox("Alrégió", ["Csípő", "Comb", "Térd", "Tibia", "Fibula", "Boka", "Láb"])
    elif main_region == "Gerinc":
        sub_region = st.selectbox("Alrégió", ["Nyaki", "Háti", "Ágyéki", "Kereszt- és farokcsonti"])
    elif main_region == "Koponya":
        sub_region = st.selectbox("Alrégió", ["Arckoponya", "Agykoponya", "Állkapocs"])
    else:
        sub_region = ""

    age = st.slider("Életkor", min_value=0, max_value=120, step=1, format="%d", value=0)
    comment = st.text_area("Megjegyzés", key="comment", value="")

    if st.button("Feltöltés"):
        if uploaded_file and type and view and main_region and sub_region:
            upload_data = {
                "patient_id": patient_id,
                "type": type,
                "view": view,
                "main_region": main_region,
                "sub_region": sub_region,
                "age": age,
                "comment": comment + " " + type_comment + " " + view_comment,
                "file": uploaded_file
            }
            try:
                save_image(**upload_data)
                st.success("Kép sikeresen feltöltve!")
            except Exception as e:
                st.error(f"Hiba a kép mentésekor: {e}")
        else:
            st.warning("Kérlek, töltsd ki az összes mezőt!")

upload_section()
