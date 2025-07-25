from langchain.llms import Ollama
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain


class Engineer:
    """Agent that writes code implementations."""

    def __init__(self, model: str = "mistral"):
        llm = Ollama(model=model)
        prompt = PromptTemplate(
            input_variables=["request", "context"],
            template=(
                "You are a senior software engineer. Using the context:\n"
                "{context}\n"
                "Implement the feature request: {request}. Provide code snippets only."
            ),
        )
        self.chain = LLMChain(llm=llm, prompt=prompt)

    def run(self, request: str, context: str) -> str:
        return self.chain.run(request=request, context=context)
