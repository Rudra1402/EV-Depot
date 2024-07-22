import os
import firebase_admin
from firebase_admin import credentials

# Load environment variables from ..env file (if using python-dotenv)
from dotenv import load_dotenv
load_dotenv()

def initialize_firebase():
    if not firebase_admin._apps:  # Check if Firebase is already initialized
        cred = credentials.Certificate({
            "type": "service_account",
            "project_id": os.getenv('GOOGLE_CLOUD_PROJECT_ID'),
            "private_key_id": os.getenv('GOOGLE_CLOUD_PRIVATE_KEY_ID'),
            "private_key": os.getenv('GOOGLE_CLOUD_PRIVATE_KEY').replace('\\n', '\n'),
            "client_email": os.getenv('GOOGLE_CLOUD_CLIENT_EMAIL'),
            "client_id": os.getenv('GOOGLE_CLOUD_CLIENT_ID'),
            "auth_uri": os.getenv('GOOGLE_CLOUD_AUTH_URI'),
            "token_uri": os.getenv('GOOGLE_CLOUD_TOKEN_URI'),
            "auth_provider_x509_cert_url": os.getenv('GOOGLE_CLOUD_AUTH_PROVIDER_X509_CERT_URL'),
            "client_x509_cert_url": os.getenv('GOOGLE_CLOUD_CLIENT_X509_CERT_URL'),
            "universe_domain": "googleapis.com"
        })
        firebase_admin.initialize_app(cred, {
            'storageBucket': 'evdepot-5c9d4.appspot.com'
        })
