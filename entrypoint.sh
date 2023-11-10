#!/bin/bash
# Start the FastAPI server in the background on port 8000
uvicorn server.server:app --host 0.0.0.0 --port 8000 &

# Start the Gradio app on the default port (which is typically 7860)
python ./client/app.py
