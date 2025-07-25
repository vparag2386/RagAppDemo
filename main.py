from orchestrator import Orchestrator
from vectorstore import CodeVectorStore


def main() -> None:
    # Index the current codebase
    store = CodeVectorStore(path=".")
    store.index()

    feature_request = input("Enter feature request: ")

    orchestrator = Orchestrator(store)
    outputs = orchestrator.run(feature_request)

    for agent, result in outputs.items():
        print(f"\n=== {agent.capitalize()} Output ===\n{result}\n")


if __name__ == "__main__":
    main()
