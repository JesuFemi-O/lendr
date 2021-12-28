gcloud config set run/platform managed
gcloud config set run/region us-central1
gcloud builds submit --tag gcr.io/fireloans-bff91/fireloans
gcloud run deploy --image gcr.io/fireloans-bff91/fireloans