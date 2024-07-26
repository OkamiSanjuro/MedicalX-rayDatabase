import streamlit as st
from firebase_helpers import get_counts, get_progress_summary
import uuid

def tracker_section():
    st.markdown(
        """
        <style>
        .tracker-box {
            border: 2px solid black;
            padding: 20px;
            margin-bottom: 20px;
        }
        .tracker-title {
            font-size: 24px;
            font-weight: bold;
        }
        .sub-region-title {
            margin-left: 20px;
            font-weight: bold;
        }
        </style>
        """,
        unsafe_allow_html=True,
    )

    st.markdown('<div class="tracker-box">', unsafe_allow_html=True)
    st.markdown('<div class="tracker-title">Státusz követése</div>', unsafe_allow_html=True)

    counts, data = get_counts()
    summary = get_progress_summary(counts)

    for main_region, sub_regions in counts.items():
        st.subheader(main_region)
        main_progress = summary[main_region]["progress"] / summary[main_region]["total"] * 100
        st.progress(main_progress / 100)  # st.progress expects a value between 0 and 1
        
        for sub_region, view_types in sub_regions.items():
            st.markdown(f'<div class="sub-region-title">{sub_region}</div>', unsafe_allow_html=True)
            
            for view_type, percentage in view_types.items():
                if percentage > 0:
                    st.text(f"{view_type}: {percentage:.2f}%")
            
            total_progress = sum(view_types.values()) / (len(view_types) * 100) * 100
            st.progress(total_progress / 100)  # st.progress expects a value between 0 and 1

    st.markdown('</div>', unsafe_allow_html=True)
tracker_section()
