import hashlib
import json
from typing import Optional, Callable
from functools import lru_cache
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langsmith import traceable
from dotenv import load_dotenv

load_dotenv()

