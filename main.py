from dotenv import load_dotenv
from importlib.metadata import version

load_dotenv()

core_version = version("langchain-core")
lg_version = version("langgraph")

from langchain_openai import ChatOpenAI

print(f"langchain-core version: {core_version}")
print(f"langgraph version: {lg_version}")

def main():
    print("Hello from rag-production!")


if __name__ == "__main__":
    main()
