"""
SentinelAI - Local Application Launcher
Starts the Uvicorn ASGI server with automatic model verification and browser launcher.
"""

import os
import sys
import webbrowser
import threading
import time

# Ensure project root is in sys.path
root_dir = os.path.dirname(os.path.abspath(__file__))
if root_dir not in sys.path:
    sys.path.insert(0, root_dir)

import uvicorn
from backend.config import settings
from backend.database import init_db

def open_browser():
    time.sleep(1.5)
    url = f"http://localhost:{settings.PORT}"
    print(f"[*] Opening browser at {url}...")
    try:
        webbrowser.open(url)
    except Exception as e:
        print(f"[!] Could not launch browser automatically: {e}")

def main():
    print("=" * 65)
    print(f"  {settings.APP_NAME} v{settings.APP_VERSION}")
    print("  AI-Powered Real-Time Cyber Threat Detection & Response Platform")
    print("=" * 65)

    # 1. Initialize DB
    print("[1/3] Initializing database schema and seed users...")
    init_db()

    # 2. Check ML model
    model_path = settings.MODEL_PATH
    if not os.path.exists(model_path):
        print("[!] ML model not found. Training Scikit-learn Isolation Forest...")
        from backend.ml.train_model import train_and_save_model
        train_and_save_model()
    else:
        print(f"[2/3] Isolation Forest ML model verified at: {model_path}")

    # 3. Launch browser thread
    threading.Thread(target=open_browser, daemon=True).start()

    # 4. Start ASGI server
    print(f"[3/3] Starting SentinelAI server on http://{settings.HOST}:{settings.PORT} ...")
    print("=" * 65)
    print("  Default Admin Credentials:")
    print("    Username: admin")
    print("    Password: SentinelAdmin2026!")
    print("=" * 65)
    print("Press CTRL+C to stop the server.")
    print("=" * 65)

    uvicorn.run(
        "backend.main:app",
        host=settings.HOST,
        port=settings.PORT,
        reload=False
    )

if __name__ == "__main__":
    main()
