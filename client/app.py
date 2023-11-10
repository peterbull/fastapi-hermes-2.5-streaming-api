import gradio as gr
import requests


def ask_model(question):
    response = requests.get(
        f'http://fastapi_app:8000/llamastatic', params={'question': question})

    # Handle request errors
    if response.status_code != 200:
        return f"Error: Received status code {response.status_code}"
    
    res_dict = response.json()

    return res_dict["choices"][0]["text"]


iface = gr.Interface(
    fn=ask_model,
    inputs=gr.Textbox(lines=2, placeholder="Ask your question here..."),
    outputs="text",
    title="Hermes 2.5 Model Q&A",
    description="Ask any question and the Hermes 2.5 model will respond."
)

iface.launch(server_name='0.0.0.0')

