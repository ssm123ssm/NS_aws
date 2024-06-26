# Imports
import time
import openai
from langchain.chains import RetrievalQA, ConversationalRetrievalChain
from langchain_community.document_loaders import DirectoryLoader, UnstructuredFileLoader
from langchain.memory import ConversationBufferMemory
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain import PromptTemplate, FAISS, ConversationChain, HuggingFaceHub
from langchain_community.llms import GPT4All
from langchain_community.chat_models import ChatOpenAI
from langchain.callbacks.streaming_stdout import StreamingStdOutCallbackHandler
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from langchain.schema import Document
from langchain.callbacks.manager import Callbacks
from langchain_openai import OpenAIEmbeddings
from langchain_community.chat_models import ChatOpenAI
from langchain_openai import OpenAI
from langchain_anthropic import ChatAnthropic


import os
import pickle
import logging

logging.basicConfig(level=logging.WARNING)


def get_docs(rt, txt, as_string=True):
    docs = ((rt.retriever.get_relevant_documents(txt)))

    keys_doc = ""
    for i in docs:
        keys_doc += str(i.page_content)

    if as_string:
        return keys_doc
    else:
        return docs


def set_tokens(OPENAI_TOKEN, HF_TOKEN, ANTHROPIC_API_KEY):
    os.environ['HUGGINGFACEHUB_API_TOKEN'] = HF_TOKEN
    os.environ['OPENAI_API_KEY'] = OPENAI_TOKEN
    os.environ['ANTHROPIC_API_KEY'] = ANTHROPIC_API_KEY


def load_vectorstore(store_name='vectorstore'):
    with open(store_name, 'rb') as f:
        logging.warning("Vectorstore loaded from disk")
        return pickle.load(f)


def load_txt(store_name='dump/txt.pkl'):
    with open(store_name, 'rb') as f:
        logging.warning("Txt splits loaded from disk")
        return pickle.load(f)


class VectorStore:
    def __init__(self, embedding_model, doc_path='data', chunk_size=1000, chunk_overlap=200, file=False, file_path=None,
                 from_large_embeddings=False, vectorstore=None):
        logging.warning("Loading input files...")
        if not from_large_embeddings:
            my_loader = DirectoryLoader(doc_path)
            if file:
                my_loader = UnstructuredFileLoader(file_path=file_path)
            docs = my_loader.load()
            text_split = RecursiveCharacterTextSplitter(
                chunk_size=chunk_size, chunk_overlap=chunk_overlap)
            logging.warning("Starting ingestion...")
            text = text_split.split_documents(docs)
            with open('dump/txt.pkl', 'wb') as f:
                pickle.dump(text, f)
                logging.warning("Text splits dumped...")

            # text = load_txt()
            self.store = FAISS.from_documents(text, embedding_model.model)
            self.retriever = self.store.as_retriever(
                search_type="similarity", search_kwargs={"k": 2})
        else:
            self.store = vectorstore
            self.retriever = self.store.as_retriever(
                search_type="similarity", search_kwargs={"k": 2})

        logging.warning(
            "Vector store created in memory. Use save method to write the store to disk.")

    def save(self, store_name='vectorstore'):
        path = store_name

        # Save the object to disk
        with open(path, 'wb') as f:
            pickle.dump(self, f)
            logging.warning("VectorStore on disk now...")


class Embedding:
    def __init__(self, model_name='sentence-transformers/all-MiniLM-L6-v2', model_type="hf"):
        md = HuggingFaceEmbeddings(
            model_name=model_name) if model_type == "hf" else OpenAIEmbeddings()
        self.model = md


class Retriever:
    def __init__(self, vectorstore, search_type='similarity', k=2):
        self.retriever = vectorstore.store.as_retriever(
            search_type=search_type, search_kwargs={"k": k})


class Llm:
    def __init__(self, model_type='gpt4all', model_path='bin/nous-hermes-13b.ggmlv3.q4_0.bin'):
        repo_id = "tiiuae/falcon-7b-instruct"
        if model_type == 'gpt4all':
            callbacks = [StreamingStdOutCallbackHandler()]
            self.model = GPT4All(
                model=model_path, backend="gptj", callbacks=callbacks, verbose=True)
        elif model_type == 'hf':
            self.model = HuggingFaceHub(repo_id=repo_id,
                                        model_kwargs={"temperature": 0.2, "max_new_tokens": 2000})
        elif model_type == 'gpt-4' or model_type == 'gpt-3.5-turbo-1106' or model_type == 'gpt-3.5-turbo-32k' or model_type == 'gpt-4-1106-preview':
            print("OpenAI Model GPT 4o")
            self.model = ChatOpenAI(model_name="gpt-4o", temperature=0)

        elif (model_type == '' or model_type == 'gpt-3.5-turbo-instruct'):
            self.model = OpenAI(model_name=model_type, temperature=0)

        elif (model_type == 'claude-3'):
            print("Anthropic Model, high MAX TOKEN")
            self.model = ChatAnthropic(
                model='claude-3-opus-20240229', temperature=0, max_tokens=4096)


class Persona:
    def __init__(self, personality_type='truthful'):

        prompt_template_mcq = """Use the following pieces of context to answer the question at the end. If the answer 
        is not in the context, guess the most probable answer. If the context does not provide the answer, say The context
        does not prove the exact answer, but the most probable answer is...

        {context}
        
        Question: {question}
        You must give an answer.
        """

        prompt_template_idiot = """Say I don't know
        {context}
        {question}
        You should not give the answer. Instead pretend that you don't know the answer.
        """

        prompt_template_truthful = """Use the following pieces of context to answer the question at the end.

        {context}
        
        Question: {question}
        Give a detailed answer. If the context does not provide the answer, say the answer cannot be found from the 
        given context. Always start with OK....
        """

        prompt_template_explainer = """Use the following pieces of context to answer the question at the end. If the provided context is not sufficient to answer the question, mention "Based on the Safety Level configuration, additional human intervention is recommended", followed up by the exact reason for you to say so.

        {context}
        
        Question: {question}
        Give a detailed answer with the help of the provided piece of information.
        """

        prompt_template_ca = """
        <role>

        You are an expert AI financial analyst. Complete the assignement ONLY based on the context provided. If the context does not contain the required information, keep it blank. When the question that was asked can be answered with confidence just by extracting data from the given context, give only the relevant output. Only if the question needs additional calculations where the given context is not providing sufficient information, mention "Based on the Safety Level configuration, additional human intervention is recommended", followed up by the exact reason for you to say so.".

        NEVER provide preambles like "Here is the analysis you asked...". ONLY provide the required tables/paragraphs in HTML.
        </role>

        <context>

        {context}

        </context>
        
        <assignment>

        {question} 

        </assignment>

        """

        prompt_template_rapper = """Use the following pieces of context to answer the question at the end.

        {context}
        
        Question: {question}
        Give a detailed answer with the help of the provided piece of information. You are a rapper and answer in a rap.
        """
        if personality_type == 'mcq':
            prompt_template = prompt_template_mcq
        elif personality_type == 'idiot':
            prompt_template = prompt_template_idiot
        elif personality_type == 'explainer':
            print("Explainer persona")
            prompt_template = prompt_template_explainer
        elif personality_type == 'rapper':
            prompt_template = prompt_template_rapper
        elif personality_type == 'ca':
            print("CA persona-2")
            prompt_template = prompt_template_ca
        else:
            prompt_template = prompt_template_truthful

        prompt = PromptTemplate(
            template=prompt_template, input_variables=["context", "question"]
        )

        pr = {"prompt": prompt}
        self.persona = pr


class Chain:
    def __init__(self, retriever, llm, persona, template, chain_type="stuff", source_nodes=True):
        self.qa = RetrievalQA.from_chain_type(llm=llm.model, chain_type=chain_type, retriever=retriever.retriever,
                                              # return_source_documents=source_nodes,
                                              chain_type_kwargs=persona.persona, verbose=False)
        self.con_qa = RetrievalQA.from_chain_type(llm=llm.model, chain_type=chain_type, retriever=retriever.retriever,
                                                  chain_type_kwargs=persona.persona, verbose=False,
                                                  memory=ConversationBufferMemory(), )

        self.direct_qa = LLMChain.from_string(llm=llm.model, template=template)


class DirectQuery:
    def __init__(self, llm, template):
        self.direct_qa = LLMChain.from_string(llm=llm.model, template=template)
# %%
