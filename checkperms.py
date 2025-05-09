from google.oauth2 import service_account
from googleapiclient.discovery import build

# Load credentials
creds = service_account.Credentials.from_service_account_file(
    "/Users/johnhousley/Downloads/repos/BigQuery/kuiu-klaviyodata-to-lawyer-1651249f5a7f.json",
    scopes=["https://www.googleapis.com/auth/cloud-platform"]
)

# Build Cloud Resource Manager API client
crm = build("cloudresourcemanager", "v1", credentials=creds)

# Replace with your actual project ID
project_id = "kuiu-klaviyodata-to-lawyer"

# Try to call getIamPolicy (may fail if you lack permission)
try:
    policy = crm.projects().getIamPolicy(
        resource=project_id,
        body={}
    ).execute()
    print("✅ Can read IAM policy")
except Exception as e:
    print("❌ Cannot read IAM policy:", e)
