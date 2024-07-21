# Fracture-Database-for-X-rays
A database created in order to collect and store the necessary amount of X-rays for further development of a fracture evaluating and classifying AI program. 
Welcome to the Medical X-ray Image Database application. This application allows for the uploading, searching, and tracking of medical X-ray images. Its purpose is to facilitate the collection, analysis, and management of X-ray images, thereby supporting healthcare professionals and researchers in their diagnostic and research work.

Alternatively, you can view the hosted version of the application here: Medical X-ray Image Database.

Features

Upload Page

Image Upload and Tagging: Allows users to upload X-ray images with various tags, including patient ID, type, view, main region, subregion, age, and comments.
Confirmation Step: Users can review the provided information and confirm submission before the final upload.
Search Page

Image Search: Provides a comprehensive search function that allows searching for images based on tags, type, view, main region, subregion, age, and associated conditions.
Paginated Results: Displays search results in a paginated format, 10 images per page, and allows easy navigation between pages.
Download Option: Users can download all images that match the search criteria in a ZIP file.
Status Page

Status Tracking: Tracks the progress of image collection and displays it in an organized manner.
Progress Bars: Shows the completion percentage for each main and subregion with numeric values and progress bars for better visualization.
Overall Progress: Displays the overall progress of collection goals for each phase.
Getting Started

Prerequisites

Python 3.7 or higher
Streamlit
Firebase account

**Installation:
1)Clone the repository:
git clone https://github.com/Weston0793/SCHF.git
cd SCHF

2)Install required passage:
pip install -r requirements.txt

3)Set up Firebase:
Create a Firebase project.
Set up Firestore and Firebase Storage.
Obtain the serviceAccount.json file and add its contents to Streamlit secrets.

4)Add your Firebase configuration to the secrets.toml file:
[firebase]
type = "service_account"
project_id = "your_project_id"
private_key_id = "your_private_key_id"
private_key = "your_private_key"
client_email = "your_client_email"
client_id = "your_client_id"
auth_uri = "https://accounts.google.com/o/oauth2/auth"
token_uri = "https://oauth2.googleapis.com/token"
auth_provider_x509_cert_url = "https://www.googleapis.com/oauth2/v1/certs"
client_x509_cert_url = "your_client_x509_cert_url"

5)Start the application:
streamlit run app.py

Authors

Aba Lőrincz1,2,3,*

Hermann Nudelman1,3

András Kedves2

Gergő Józsa1,3

Affiliated Institutions

Department of Thermophysiology, Institute of Translational Medicine, Faculty of General Medicine, University of Pécs, Szigeti út 12, H7624 Pécs, Hungary; aba.lorincz@gmail.com (AL)

Department of Automation, Faculty of Engineering and Information Technology, University of Pécs, Boszorkány út 2, H7624 Pécs, Hungary

Department of Surgery, Traumatology, Urology, and ENT, Pediatric Clinic, Clinical Center, University of Pécs, József Attila utca 7, H7623 Pécs, Hungary
