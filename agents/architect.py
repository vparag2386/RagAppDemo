from langchain.llms import Ollama
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain


class Architect:
    """Agent that designs high-level architecture."""

    def __init__(self, model: str = "mistral"):
        llm = Ollama(model=model)
        prompt = PromptTemplate(
            input_variables=["request", "context"],
            template=(
                "You are a software architect. Using the following context:\n"
                "{context}\n"
                "Design an architecture for the feature request: {request}"
            ),
        )
        self.chain = LLMChain(llm=llm, prompt=prompt)

    def run(self, request: str, context: str) -> str:
        """Generate an architecture plan."""
        return self.chain.run(request=request, context=context)
