#!/bin/bash

# Start the FastAPI server in the background on port 8000
uvicorn server.app:app --host 0.0.0.0 --port 8000 &

# Store the PID of the FastAPI server
FASTAPI_PID=$!

# Start the Gradio app on the default port (which is typically 7860)
python ./client/app.py &

# Store the PID of the Gradio app
GRADIO_PID=$!

# Wait for both processes to finish
wait $FASTAPI_PID
wait $GRADIO_PID
