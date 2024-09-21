import os
from dotenv import load_dotenv

# .env 파일에서 환경 변수를 로드합니다.
load_dotenv()

# 환경 변수 출력
print(f"[API KEY]\n{os.environ['OPEN_API_KEY']}")
print(f"[LANGCHAIN_TRACING_V2]\n{os.environ['LANGCHAIN_TRACING_V2']}")
print(f"[LANGCHAIN_ENDPOINT]\n{os.environ['LANGCHAIN_ENDPOINT']}")
print(f"[LANGCHAIN_API_KEY]\n{os.environ['LANGCHAIN_API_KEY']}")
print(f"[LANGCHAIN_PROJECT]\n{os.environ['LANGCHAIN_PROJECT']}")
