# AssitantGPT🤖 - A Customer Support Chatbot powered by Aparavi Software

![diagram](https://github.com/AparaviSoftware/aparavi-cookbooks/blob/main/AssistantGpt/images/CoverImage.jpg)

Assistify is an AI-powered chatbot designed to assist customers by providing relevant responses using a vector database and pre-trained models. This repository includes a full implementation of the chatbot, leveraging OpenAI's GPT-3.5-turbo, Langchain, and a Milvus vector database for fast information retrieval.
Features

    Vector Database (Milvus) Integration: Efficiently retrieves contextual data.
    Sentence Transformers: For encoding user queries into vectors.
    GPT-3.5-turbo: Provides intelligent and context-aware responses.
    Streamlit: User-friendly web interface for interacting with the chatbot.

Prerequisites

    Python 3.8+
    OpenAI API key
    Milvus server for vector storage

Installation

    Clone the repository:

    bash

git clone https://github.com/your-repo/assistify.git
cd assistify

Install the required packages: Install the dependencies specified in the requirements.txt:

bash

pip install -r requirements.txt

Configure environment variables: Set your OpenAI API key and Milvus connection details:

bash

export OPENAI_API_KEY='your-openai-key'
export MILVUS_URI='your-milvus-uri'
export MILVUS_USERNAME='your-username'
export MILVUS_PASSWORD='your-password'
export MILVUS_DB_NAME='your-db-name'

Start the Streamlit application:

bash

    streamlit run assistify.py

Usage

After starting the Streamlit app, you can interact with the chatbot by typing queries into the input field. The chatbot augments user queries by retrieving relevant data from the Milvus vector database and generating responses using GPT-3.5-turbo.
Key Components

    MilvusClient: Handles the connection to the Milvus vector database for storing and retrieving context data.
    Langchain: Manages the augmentation of prompts with retrieved data.
    SentenceTransformer: Transforms user queries into embedding vectors for searching the database.
    OpenAI GPT-3.5-turbo: Generates intelligent responses based on the user query and retrieved context.
    Streamlit: Provides an intuitive web interface for users to interact with the chatbot.

File Structure

bash

├── assistify.py        # Main script containing the chatbot logic
├── requirements.txt    # List of dependencies
├── README.md           # Project documentation

Future Enhancements

    Add support for more vector databases.
    Improve context retrieval and augmenting mechanism.
    Enhance the chatbot interface with more interaction options.

Contributing

We welcome contributions! Please feel free to submit issues, feature requests, or pull requests.