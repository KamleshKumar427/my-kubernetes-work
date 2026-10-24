import os

import uvicorn
from fastapi import FastAPI

app = FastAPI()
port = int(os.environ.get("PORT", 8000))

if __name__ == "__main__":
    print(f"Server started in port {port}", flush=True)
    uvicorn.run(app, host="0.0.0.0", port=port)
