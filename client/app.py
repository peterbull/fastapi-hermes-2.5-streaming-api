import gradio as gr
import requests


def ask_model(question):
    response = requests.get(
        f'http://localhost:8000/llamastatic', params={'question': question})

    # Handle request errors
    if response.status_code != 200:
        return f"Error: Received status code {response.status_code}"

    return response.json()


iface = gr.Interface(
    fn=ask_model,
    inputs=gr.Textbox(lines=2, placeholder="Ask your question here..."),
    outputs="json",
    title="Hermes 2.5 Model Q&A",
    description="Ask any question and the Hermes 2.5 model will respond."
)

iface.launch()

