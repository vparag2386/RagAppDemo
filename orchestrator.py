from typing import Dict

from langchain.llms import Ollama

from agents.architect import Architect
from agents.engineer import Engineer
from agents.reviewer import Reviewer
from agents.tester import Tester
from vectorstore import CodeVectorStore


class Orchestrator:
    """Coordinates the agent pipeline."""

    def __init__(self, store: CodeVectorStore, model: str = "mistral"):
        self.store = store
        self.llm = Ollama(model=model)
        self.architect = Architect(model=model)
        self.engineer = Engineer(model=model)
        self.reviewer = Reviewer(model=model)
        self.tester = Tester(model=model)

    def run(self, request: str) -> Dict[str, str]:
        docs = self.store.query(request)
        context = "\n".join(d.page_content for d in docs)

        arch_out = self.architect.run(request, context)
        eng_context = context + "\n" + arch_out
        eng_out = self.engineer.run(request, eng_context)
        rev_out = self.reviewer.run(eng_out, context)
        test_out = self.tester.run(eng_out, context)

        return {
            "architect": arch_out,
            "engineer": eng_out,
            "reviewer": rev_out,
            "tester": test_out,
        }
