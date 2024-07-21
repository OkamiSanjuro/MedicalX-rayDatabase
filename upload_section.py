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

    st.markdown('<div class="upload-title">Image upload and title</div>', unsafe_allow_html=True)

    patient_id = st.text_input("Patient ID (leave empty in case of new patient)", str(uuid.uuid4()))

    uploaded_file = st.file_uploader("Choose and image", type=["jpg", "jpeg", "png"])

    type = st.selectbox("Type", ["Fractured", "Normal", "Other"])
    type_comment = st.text_input("Specify (Other)") if type == "Other" else ""

    view = st.selectbox("View", ["AP", "Lateral", "Other"])
    view_comment = st.text_input("Specify (Other View)") if view == "Other" else ""

    main_region = st.selectbox("Main Region", ["Upper Extremity", "Lower Extremity", "Spine", "Skull", "Chest", "Abdomen"])

  if main_region == "Upper Extremity":
    sub_region = st.selectbox("Subregion", ["Clavicle", "Scapula", "Shoulder", "Humerus", "Forearm", "Elbow", "Radius", "Ulna", "Wrist", "Hand"])
    elif sub_region == "Humerus":
        specific_sub_region = st.selectbox("Specific Subregion", ["Proximal Humerus", "Humeral Shaft", "Distal Humerus"])
        elif specific_sub-region == "Proximal Humerus":
            type_of_fracture = st.selectbox("Type of Fracture", ["AO-A", "AO-B", "AO-C"])
        elif specific_sub-region == "Humeral Shaft":
            type_of_fracture = st.selectbox("Type of Fracture", ["Spiral", "Oblique", "Transverse", "Intact wedge", "Fragmentary wedge", "Segmentary"])
        elif specific_sub-region == "Distal Humerus":
            type_of_fracture = st.selectbox("Type of Fracture", ["Supracondylar", "Transcondylar", "Intercondylar", "Condylar", "Epicondylar", "Capitellar", "Trochlear"])

if main_region == "Lower Extremity":
        sub_region = st.selectbox("Subregion", ["Hip", "Tigh", "Knee", "Tibia", "Fibula", "Ankle", "Foot"])
   
  elif sub_region == "Pelvis":
        type_of_fracture = st.selectbox("Type of Fracture", ["Acetabular", "Iliac Wing", "Sacral", "Pubic Ramus", "Symphysis Pubis"])
  elif sub_region == "Hip":
        type_of_fracture = st.selectbox("Type of Fracture", ["Femoral Neck", "Intertrochanteric", "Subtrochanteric"])
   
  elif sub_region == "Femur":
        specific_sub_region = st.selectbox("Specific Subregion", ["Proximal Femur", "Femoral Shaft", "Distal Femur"])  
        if specific_sub_region == "Proximal Femur":
            type_of_fracture = st.selectbox("Type of Fracture", ["AO-A", "AO-B", "AO-C"])
        elif specific_sub_region == "Femoral Shaft":
            type_of_fracture = st.selectbox("Type of Fracture", ["Spiral", "Oblique", "Transverse", "Intact wedge", "Fragmentary wedge", "Segmentary"])
        elif specific_sub_region == "Distal Femur":
            type_of_fracture = st.selectbox("Type of Fracture", ["Supracondylar", "Transcondylar", "Intercondylar", "Condylar", "Epicondylar"])
  
  elif sub_region == "Knee":
        type_of_fracture = st.selectbox("Type of Fracture", ["Patellar", "Tibial Plateau", "Segond", "Avulsion"])
  
  elif sub_region == "Tibia":
        specific_sub_region = st.selectbox("Specific Subregion", ["Proximal Tibia", "Tibial Shaft", "Distal Tibia"])
        if specific_sub_region == "Proximal Tibia":
            type_of_fracture = st.selectbox("Type of Fracture", ["AO-A", "AO-B", "AO-C"])
        elif specific_sub_region == "Tibial Shaft":
            type_of_fracture = st.selectbox("Type of Fracture", ["Spiral", "Oblique", "Transverse", "Intact wedge", "Fragmentary wedge", "Segmentary"])
        elif specific_sub_region == "Distal Tibia":
            type_of_fracture = st.selectbox("Type of Fracture", ["Pilon", "Malleolar", "Anterior Margin", "Posterior Margin"])
  
  elif sub_region == "Fibula":
        type_of_fracture = st.selectbox("Type of Fracture", ["Proximal Fibula", "Fibular Shaft", "Distal Fibula", "Syndesmolysis"])
   
  elif sub_region == "Ankle":
        type_of_fracture = st.selectbox("Type of Fracture", ["Medial Malleolus", "Lateral Malleolus", "Posterior Malleolus", "Bimalleolar", "Trimalleolar"])
   
  elif sub_region == "Foot":
        specific_sub_region = st.selectbox("Specific Subregion", ["Tarsal", "Metatarsal", "Phalangeal"]) 
        if specific_sub_region == "Tarsal":
            type_of_fracture = st.selectbox("Type of Fracture", ["Calcaneal", "Talus", "Navicular", "Cuboid", "Cuneiform"]
        elif specific_sub_region == "Metatarsal":
            type_of_fracture = st.selectbox("Type of Fracture", ["First Metatarsal", "Second Metatarsal", "Third Metatarsal", "Fourth Metatarsal", "Fifth Metatarsal"])
        elif specific_sub_region == "Phalangeal":
            type_of_fracture = st.selectbox("Type of Fracture", ["Proximal Phalanx", "Middle Phalanx", "Distal Phalanx"])
      
elif main_region == "Spine":
        sub_region = st.selectbox("Subregion", ["C-spine", "T-spine", "L-spine", "S-spine"])
    if sub_region == "C-spine":
        specific_sub_region = st.selectbox("Specific Subregion", ["C1", "C2", "C3-C7"])
        if specific_sub_region == "C1":
            type_of_fracture = st.selectbox("Type of Fracture", ["Jefferson Fracture", "Posterior Arch Fracture"])  
        elif specific_sub_region == "C2":
            type_of_fracture = st.selectbox("Type of Fracture", ["Odontoid Fracture", "Hangman's Fracture"])
        elif specific_sub_region == "C3-C7":
            type_of_fracture = st.selectbox("Type of Fracture", ["Compression Fracture", "Burst Fracture", "Teardrop Fracture", "Facet Dislocation", "Clay Shoveler's Fracture"])

    elif sub_region == "T-spine":
        specific_sub_region = st.selectbox("Specific Subregion", ["T1-T4", "T5-T8", "T9-T12"])
        if specific_sub_region == "T1-T4":
            type_of_fracture = st.selectbox("Type of Fracture", ["Compression Fracture", "Burst Fracture", "Flexion-Distraction Fracture"])
        elif specific_sub_region == "T5-T8":
            type_of_fracture = st.selectbox("Type of Fracture", ["Compression Fracture", "Burst Fracture", "Flexion-Distraction Fracture"])
        elif specific_sub_region == "T9-T12":
            type_of_fracture = st.selectbox("Type of Fracture", ["Compression Fracture", "Burst Fracture", "Flexion-Distraction Fracture", "Chance Fracture"])
    
    elif sub_region == "L-spine":
        specific_sub_region = st.selectbox("Specific Subregion", ["L1-L2", "L3-L4", "L5"])
        if specific_sub_region == "L1-L2":
            type_of_fracture = st.selectbox("Type of Fracture", ["Compression Fracture", "Burst Fracture", "Flexion-Distraction Fracture"])
        elif specific_sub_region == "L3-L4":
            type_of_fracture = st.selectbox("Type of Fracture", ["Compression Fracture", "Burst Fracture", "Flexion-Distraction Fracture"])
        elif specific_sub_region == "L5":
            type_of_fracture = st.selectbox("Type of Fracture", ["Compression Fracture", "Burst Fracture", "Flexion-Distraction Fracture"])
   
    elif sub_region == "S-spine":
        specific_sub_region = st.selectbox("Specific Subregion", ["S1-S5"])
        if specific_sub_region == "S1-S5":
            type_of_fracture = st.selectbox("Type of Fracture", ["Sacral Fracture", "Coccygeal Fracture"])
        
    if main_region == "Skull":
    sub_region = st.selectbox("Subregion", ["Face", "Calvaria", "Mandible", "Base of skull"])
    if sub_region == "Face":
        specific_sub_region = st.selectbox("Specific Subregion", ["Orbital", "Nasal", "Zygomatic", "Maxillary", "Le Fort Fracture"])
        if specific_sub_region == "Orbital":
            type_of_fracture = st.selectbox("Type of Fracture", ["Orbital Floor Fracture", "Orbital Roof Fracture"])
        elif specific_sub_region == "Nasal":
            type_of_fracture = st.selectbox("Type of Fracture", ["Nasal Bone Fracture", "Septal Fracture"])
        elif specific_sub_region == "Zygomatic":
            type_of_fracture = st.selectbox("Type of Fracture", ["Zygomatic Arch Fracture", "Zygomaticomaxillary Complex Fracture"])
        elif specific_sub_region == "Maxillary":
            type_of_fracture = st.selectbox("Type of Fracture", ["Alveolar Ridge Fracture", "Palatal Fracture"])
        elif specific_sub_region == "Le Fort Fracture":
            type_of_fracture = st.selectbox("Type of Fracture", ["Le Fort I", "Le Fort II", "Le Fort III"])

    elif sub_region == "Calvaria":
        specific_sub_region = st.selectbox("Specific Subregion", ["Frontal Bone", "Parietal Bone", "Temporal Bone", "Occipital Bone"])
        if specific_sub_region == "Frontal Bone":
            type_of_fracture = st.selectbox("Type of Fracture", ["Linear Fracture", "Depressed Fracture", "Comminuted Fracture"])
        elif specific_sub_region == "Parietal Bone":
            type_of_fracture = st.selectbox("Type of Fracture", ["Linear Fracture", "Depressed Fracture", "Comminuted Fracture"])
        elif specific_sub_region == "Temporal Bone":
            type_of_fracture = st.selectbox("Type of Fracture", ["Longitudinal Fracture", "Transverse Fracture", "Mixed Fracture"])
        elif specific_sub_region == "Occipital Bone":
            type_of_fracture = st.selectbox("Type of Fracture", ["Linear Fracture", "Depressed Fracture", "Comminuted Fracture"]
                                            
    elif sub_region == "Mandible":
        specific_sub_region = st.selectbox("Specific Subregion", ["Symphysis", "Body", "Angle", "Ramus", "Condylar Process", "Coronoid Process"])
        if specific_sub_region == "Symphysis":
            type_of_fracture = st.selectbox("Type of Fracture", ["Linear Fracture", "Comminuted Fracture"])
        elif specific_sub_region == "Body":
            type_of_fracture = st.selectbox("Type of Fracture", ["Linear Fracture", "Comminuted Fracture"])
        elif specific_sub_region == "Angle":
            type_of_fracture = st.selectbox("Type of Fracture", ["Linear Fracture", "Comminuted Fracture"])
        elif specific_sub_region == "Ramus":
            type_of_fracture = st.selectbox("Type of Fracture", ["Linear Fracture", "Comminuted Fracture"])
        elif specific_sub_region == "Condylar Process":
            type_of_fracture = st.selectbox("Type of Fracture", ["Linear Fracture", "Comminuted Fracture"])
        elif specific_sub_region == "Coronoid Process":
            type_of_fracture = st.selectbox("Type of Fracture", ["Linear Fracture", "Comminuted Fracture"])
    
    elif sub_region == "Base of skull":
        specific_sub_region = st.selectbox("Specific Subregion", ["Anterior Cranial Fossa", "Middle Cranial Fossa", "Posterior Cranial Fossa"])
        if specific_sub_region == "Anterior Cranial Fossa":
            type_of_fracture = st.selectbox("Type of Fracture", ["Linear Fracture", "Comminuted Fracture"])
        elif specific_sub_region == "Middle Cranial Fossa":
            type_of_fracture = st.selectbox("Type of Fracture", ["Linear Fracture", "Comminuted Fracture"])
        elif specific_sub_region == "Posterior Cranial Fossa":
            type_of_fracture = st.selectbox("Type of Fracture", ["Linear Fracture", "Comminuted Fracture"])
    else:
        sub_region = ""

    age = st.slider("Age", min_value=0, max_value=120, step=1, format="%d", value=0)
    comment = st.text_area("Comments", key="comment", value="")

    if st.button("Upload"):
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
                st.success("Image Successfully Uploaded!")
            except Exception as e:
                st.error(f"Error-Image not saved: {e}")
        else:
            st.warning("Please fill out all required fields!")

upload_section()
