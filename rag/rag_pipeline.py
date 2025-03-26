from langchain_community.utilities import SearchApiAPIWrapper
from langchain_community.document_loaders import WebBaseLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_chroma import Chroma

import asyncio


web_search = SearchApiAPIWrapper()

embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-mpnet-base-v2")


async def load_docs_from_urls(urls) -> list:
    docs = []
    for url in urls:
        try:
            loader = WebBaseLoader(web_paths=[url])
            async for doc in loader.alazy_load():
                docs.append(doc)
        except Exception as e:
            print(f"Failed to load {url}: {e}")
    return docs


def get_context_from_subtopic(subtopic: str) -> str:
    search_results = web_search.results(subtopic)
    urls = [
        result["link"]
        for result in search_results.get("organic_results", [])
        if "link" in result
    ][:3]

    if not urls:
        return ""

    docs = asyncio.run(load_docs_from_urls(urls))
    if not docs:
        return ""

    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=100,
        chunk_overlap=50,
        length_function=len,
        is_separator_regex=False,
    )
    split_docs = text_splitter.split_documents(docs)
    if not split_docs:
        return ""

    vector_store = Chroma(
        collection_name="research_collection",
        embedding_function=embeddings,
        persist_directory="./chroma_langchain_db",
    )
    
    vector_store.reset_collection()
    vector_store.add_documents(split_docs)

    # Retrieve relevant chunks
    retriever = vector_store.as_retriever(search_kwargs={"k": 3})
    relevant_docs = retriever.invoke(subtopic)

    return "\n\n".join([doc.page_content for doc in relevant_docs])
