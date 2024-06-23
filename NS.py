import importlib
import reporter
import reporter_comps
from flask_cors import CORS  # Import the CORS module
from flask import Flask, request, jsonify, send_file
from custom import *
from dotenv import load_dotenv
import os
import shutil
from weasyprint import HTML

load_dotenv()
openai_embeddings = Embedding(model_type='openai')
persona = Persona(personality_type='ca')
llm = Llm(model_type='gpt-4-1106-preview')
llm_2 = Llm(model_type='gpt-4')


importlib.reload(reporter)
importlib.reload(reporter_comps)


def cleanup():
    print("Cleaning up resources...")
    down_folder = "down"

    if os.path.exists(down_folder):
        for filename in os.listdir(down_folder):
            file_path = os.path.join(down_folder, filename)
            try:
                if os.path.isfile(file_path):
                    os.remove(file_path)
                elif os.path.isdir(file_path):
                    shutil.rmtree(file_path)
            except Exception as e:
                print(f"Failed to remove {file_path}. Reason: {e}")
    else:
        print(f"The '{down_folder}' folder does not exist.")


def open_html_file(file_name):
    import subprocess
    import os

    current_dir = os.getcwd()
    html_file = os.path.join(current_dir, file_name)
    print(f"Opening file: {html_file}")

    if os.path.isfile(html_file):
        subprocess.call(['open', html_file])
    else:
        print(f"Error: File '{html_file}' not found.")


cleanup()

app = Flask(__name__)
CORS(app)

UPLOAD_FOLDER = 'down'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

app.config['vs'] = None
app.config['user_vars_1'] = None
app.config['user_vars_2'] = None


@app.route('/upload', methods=['POST'])
def upload_file():

    chunk = 3000
    chunk_overlap = 800
    k = 8
    print("uploading")

    if 'files' not in request.files:
        return jsonify({'error': 'No file part'})

    files = request.files.getlist('files')

    for file in files:
        if file.filename == '':
            return jsonify({'error': 'No selected file'})

        filename = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
        file.save(filename)

    vs = VectorStore(embedding_model=openai_embeddings,
                     chunk_size=chunk, chunk_overlap=chunk_overlap, doc_path='down')
    print("vector store created")

    main_chain = Chain(retriever=Retriever(vectorstore=vs, k=k), llm=llm_2,
                       persona=persona, template=reporter_comps.component().tester_template_balance_sheet_1_1)

    query_chain = Chain(retriever=Retriever(vectorstore=vs, k=3), llm=llm_2,
                        persona=persona, template=reporter_comps.component().tester_template_balance_sheet_1_2)
    
    query_chain_2 = Chain(retriever=Retriever(vectorstore=vs, k=3), llm=llm_2,
                        persona=Persona(personality_type='explainer'), template=reporter_comps.component().tester_template_balance_sheet_1_2)

    app.config['user_vars_1'] = query_chain
    app.config['user_vars_2'] = query_chain_2

    print("Stage 1")
    result_obj_tester_summary = main_chain.con_qa(
        inputs={"query": reporter_comps.component().summary})

    print("Stage 2")
    result_obj_tester_balance_1 = main_chain.con_qa(
        inputs={"query": reporter_comps.component().tester_template_balance_sheet_1_1})

    result_obj_tester_balance_2 = main_chain.con_qa(
        inputs={"query": reporter_comps.component().tester_template_balance_sheet_2})

    print("Stage 3")
    result_obj_tester_ratios = main_chain.con_qa(
        inputs={"query": reporter_comps.component().ratios_1_1})

    print("Stage 4")
    result_obj_tester_risks = main_chain.con_qa(
        inputs={"query": reporter_comps.component().risks})

    reporter_store = [None, None, None, None,
                      None, None, None, None, None, None, None, None]
    k = k

    reporter_store[0] = ((result_obj_tester_summary['result']))
    reporter_store[1] = ((result_obj_tester_balance_1['result']))
    reporter_store[2] = ((result_obj_tester_balance_2['result']))
    reporter_store[3] = ((result_obj_tester_ratios['result']))
    reporter_store[4] = ((result_obj_tester_risks['result']))

    reporter.creator(reporter_store)
    #open_html_file(input_html_file)

   # html_file_to_pdf(input_html_file, output_pdf_file)

    def html_to_pdf(input_file, output_file):
        try:
            HTML(input_file).write_pdf(output_file)
            print(f'PDF created successfully at: {output_file}')
        except Exception as e:
            print(f'Error creating PDF: {e}')

    input_html_file = 'reports/report_new.html'
    output_pdf_file = 'reports/s.pdf'

    html_to_pdf(input_html_file, output_pdf_file)

    return jsonify({'message': 'Files uploaded successfully'})


@app.route('/chat', methods=['POST'])
def chat():

    # Get the message from the request data
    data = request.get_json()
    message = data.get('message', '')
    print(message)

    result_obj = app.config['user_vars_2'].con_qa(inputs={"query": message})
    reply = result_obj['result']

    return jsonify({'reply': reply})

@app.route('/pdf', methods=['GET'])
def serve_pdf():
    try:
        pdf_path = 'reports/s.pdf'
        return send_file(pdf_path, as_attachment=True)
    except Exception as e:
        return jsonify({'error': str(e)}), 500
    
@app.route('/html', methods=['GET'])
def serve_html():
    try:
        pdf_path = 'reports/report_new.html'
        return send_file(pdf_path, as_attachment=True)
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=150)
