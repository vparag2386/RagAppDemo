from langchain.llms import Ollama
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain


class Tester:
    """Agent that generates test cases."""

    def __init__(self, model: str = "mistral"):
        llm = Ollama(model=model)
        prompt = PromptTemplate(
            input_variables=["code", "context"],
            template=(
                "You are a QA engineer. Write test cases for the following code:\n"
                "{code}\n"
                "Use this context:\n{context}\n"
                "Return the test plan or test code."
            ),
        )
        self.chain = LLMChain(llm=llm, prompt=prompt)

    def run(self, code: str, context: str) -> str:
        return self.chain.run(code=code, context=context)
