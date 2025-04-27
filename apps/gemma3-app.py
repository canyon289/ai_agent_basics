import gradio as gr
import ollama

model = 'gemma3:4b-it-qat'

def chat_with_model(prompt):
    response = ollama.chat(model=model, messages=[{'role': 'user', 'content': prompt}])
    return response['message']['content']

iface = gr.Interface(
    fn=chat_with_model,
    inputs=gr.Textbox(lines=2, placeholder="Type your message here..."),
    outputs="text",
    title="Chat with Gemma",
    description="Enter a message and get a response from Gemma3!",
)

print("Launching Gradio app...")  # 👈 Add this line

iface.launch()