from langchain.llms import Ollama
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain


class Reviewer:
    """Agent that reviews generated code."""

    def __init__(self, model: str = "mistral"):
        llm = Ollama(model=model)
        prompt = PromptTemplate(
            input_variables=["code", "context"],
            template=(
                "You are a code reviewer. Review the following code:\n"
                "{code}\n"
                "Using this context:\n{context}\n"
                "Provide improvement suggestions."
            ),
        )
        self.chain = LLMChain(llm=llm, prompt=prompt)

    def run(self, code: str, context: str) -> str:
        return self.chain.run(code=code, context=context)
