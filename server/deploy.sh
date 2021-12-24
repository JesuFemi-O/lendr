gcloud config set run/platform managed
gcloud config set run/region us-central1
gcloud builds submit --tag gcr.io/<PROJECT_ID>/<SERVICE_ID>
gcloud run deploy --image gcr.io/<PROJECT_ID>/<SERVICE_ID>