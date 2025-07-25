from __future__ import annotations

import os
from typing import List

from langchain.docstore.document import Document
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.embeddings import OllamaEmbeddings
from langchain.vectorstores import FAISS


class CodeVectorStore:
    """Utility for indexing and querying the codebase."""

    def __init__(self, path: str, model: str = "mistral"):
        self.path = path
        self.embedding = OllamaEmbeddings(model=model)
        self.store: FAISS | None = None

    def _load_documents(self) -> List[Document]:
        docs: List[Document] = []
        for root, _, files in os.walk(self.path):
            for file in files:
                if file.endswith((".py", ".java", ".md", ".txt")):
                    fpath = os.path.join(root, file)
                    try:
                        with open(fpath, "r", encoding="utf-8") as f:
                            text = f.read()
                    except Exception:
                        continue
                    docs.append(Document(page_content=text, metadata={"source": fpath}))
        splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=100)
        return splitter.split_documents(docs)

    def index(self) -> None:
        """Load documents from the path and build the vector store."""
        docs = self._load_documents()
        self.store = FAISS.from_documents(docs, self.embedding)

    def query(self, text: str, k: int = 4) -> List[Document]:
        if not self.store:
            raise ValueError("Vector store not indexed")
        return self.store.similarity_search(text, k=k)
