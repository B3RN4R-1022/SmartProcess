
from flask import Flask, render_template, request, jsonify, send_from_directory
import openai
import os

app = Flask(__name__)

# Configure a sua chave de API da OpenAIF
openai.api_key = ""

# Carrega os prompts de arquivos
PROMPT_DIR = os.path.join(os.getcwd(), 'prompts')
prompt_files = os.listdir(PROMPT_DIR)
prompts = {}
for file in prompt_files:
    if file.endswith('.txt'):
        with open(os.path.join(PROMPT_DIR, file), 'r') as f:
            content = f.read()
            prompts[file] = content

@app.route('/componentes/fonts/<font_file>')
def servir_arquivo_fonte(font_file):
    return send_from_directory('componentes/fonts', font_file)

@app.route('/image/<nome_da_imagem>')
def servir_imagem(nome_da_imagem):
    return send_from_directory('image', nome_da_imagem)


@app.route('/pagina-tab')
def pagina_tab():
    return render_template('pagina_tab.html')




@app.route('/pagina-doc')
def pagina_doc():
    return render_template('pagina_doc.html')




@app.route('/pagina-prompt')
def pagina_prompt():
    return render_template('pagina_prompt.html')




@app.route('/pagina-ge')
def pagina_ge():
    return render_template('pagina_ge.html')




@app.route('/pagina-home')
def pagina_home():
    return render_template('pagina_home.html')


@app.route('/')
def index():
    return render_template('index.html', prompts=prompts)


@app.route('/submit', methods=['POST'])
def submit():
    prompt = request.form['prompt']
    user_input = request.form['user_input']
    print("Prompt recebido:", prompt)
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=f"{prompt} {user_input}",
        temperature=0.7,
        max_tokens=1500,
        n=1,
        stop=None
    )
    assistant_response = response.choices[0].text.strip()
    return jsonify({'response': assistant_response})


if __name__ == '__main__':
    app.run(debug=True)
