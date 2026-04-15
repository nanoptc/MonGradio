import gradio as gr

def salutation(nom):
    return f"Félicitations {nom}, votre premier environnement GitHub et Gradio fonctionne !"

demo = gr.Interface(fn=salutation, inputs="text", outputs="text")

if __name__ == "__main__":
    demo.launch(share=True)