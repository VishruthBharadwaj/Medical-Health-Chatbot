import openai
import gradio as gr


openai.api_key = 'API KEY'

def chatbot_response(user_input, history):
    if history is None:
        history = []

    conversation = [{"role": "system", "content": "You are ChatGPT, a large language model trained by OpenAI. You are talking to a person about health issues and providing suggestions based on their responses. Please be empathetic and considerate."}]
    conversation.extend([{"role": "user", "content": u} if i % 2 == 0 else {"role": "assistant", "content": a} for i, (u, a) in enumerate(history)])
    conversation.append({"role": "user", "content": user_input})

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=conversation
    )

    assistant_message = response['choices'][0]['message']['content']
    history.append((user_input, assistant_message))

    return history, history

iface = gr.Interface(
    fn=chatbot_response,
    inputs=[gr.Textbox(lines=1, label="You"), gr.State()],
    outputs=[gr.Chatbot(), gr.State()],
    title="Health Advisor Chatbot",
    description="Ask me any health-related questions and I'll do my best to help you.",
)

iface.launch()
