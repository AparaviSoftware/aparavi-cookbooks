# Aparavi Cookbooks

Welcome to the Aparavi Cookbooks repository! Here, you'll find a selection of example projects that demonstrate how to integrate Aparavi into your personal GenAI projects. Whether you're just starting or looking to enhance your professional AI development, these cookbooks will guide you in utilizing Aparavi software to streamline data ingestion and power your projects with relevant, proprietary data. [Go to Getting Started](#getting-started-with-aparavi-ai-software)

**Goal**

The goal of this repository is to help you kickstart your journey by using Aparavi as the backbone for managing and ingesting data into your AI-driven applications.

**Why Aparavi?**

Aparavi is a data-native solution that seamlessly connects to a wide variety of data sources. Built as a comprehensive data management platform, Aparavi enables enterprises to:
- Discover value in vast amounts of unstructured data
- Run powerful analytics on that data
- Enforce organizational policies
- Identify and mitigate compliance risks

![Aparavi Architecture](/images/AparaviArchitecture.png)

**Aparavi AI**

For AI developers, Aparavi also acts as an essential pipeline for your data, enabling RAG (Retrieval-Augmented Generation) in your AI agents. With the example projects provided in this repository, you'll learn how to:
1. **Ingest data** seamlessly from all kind of sources into your AI pipelines 
2. **Query against your unstructured data** to enhance your AI models
3. **Automate policy enforcement** while developing AI-driven solutions
4. **Enable permissions** for all users in your organisation
5. **Identify PII** through all your data

![Aparavi AI Capabilities](/images/AparaviAiCapabilities.png)


Each project includes step-by-step instructions, code snippets, and best practices to help you make the most out of Aparavi for your GenAI initiatives.

### Aparavi AI Pipelines for Developers

Aparavi provides two key AI pipelines for developers:

1. **RAG as a Service**: This service offers developers a semantic search endpoint, allowing them to query data and retrieve relevant text chunks efficiently from sources that have been previously processed by Aparavi and loaded into our in-house vector database.

![Aparavi Architecture](/images/AparaviSemanticRetriever.png)

To learn how the semantic search endpoint works, check out this [notebook](https://github.com/AparaviSoftware/langchain-retriever), which demonstrates how to implement it using Aparavi's Langchain retriever.

2. **Vector Database Loader**: This pipeline enables the loading of embedding vectors into a vector database of your choice, optimizing data retrieval and AI model performance. It also allows developers to seamlessly continue with projects they might have already started, integrating existing data into Aparavi’s platform.

![Aparavi Architecture](/images/AparaviVectorDbLoader.png)

For an example project using the Vector Database Loader with AssistantGPT and Milvus as the vector database, check out this [repository](https://github.com/AparaviSoftware/aparavi-cookbooks/tree/main/AssistantGpt).


### Getting started with Aparavi AI Software

To set up Aparavi using Docker Compose, [follow the instructions here](https://github.com/AparaviSoftware/aparavi-platform-compose/blob/main/README.md).

In this reopistory we have the follwing cookbooks already for you to make you git the ground running

1. aparavi assistnat gpt 
this what it doses balblalbl

2. ....

3. ....  



