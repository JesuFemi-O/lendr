import os

timeout = 60
bind = f":{os.environ.get('PORT', '8080')}"
worker_class = "uvicorn.workers.UvicornWorker"