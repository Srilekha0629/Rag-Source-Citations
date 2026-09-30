import requests
from io import BytesIO
import time

from utils.config import API_URL

DEFAULT_TIMEOUT = 30
LONG_TIMEOUT = 120


def _request_with_retry(method: str, url: str, max_retries: int = 2, backoff: float = 1.5, **kwargs):
  kwargs.setdefault("timeout", DEFAULT_TIMEOUT)
  for attempt in range(max_retries + 1):
    try:
      response = requests.request(method, url, **kwargs)
      if response.status_code in (502, 503, 504) and attempt < max_retries:
        time.sleep(backoff * (attempt + 1))
        continue
      return response
    except (requests.exceptions.ConnectionError, requests.exceptions.Timeout) as e:
      if attempt < max_retries:
        time.sleep(backoff * (attempt + 1))
        continue
      raise Exception(f"Failed to connect to backend ({url}): {str(e)}")


def handle_response(response):
  if not response.ok:
    error_detail = response.text.strip() if response.text else f"HTTP {response.status_code} {response.reason}"
    try:
      json_err = response.json()
      if isinstance(json_err, dict) and json_err.get("message"):
        error_detail = json_err["message"]
    except Exception:
      pass
    raise Exception(f"API Error: HTTP {response.status_code} - {error_detail}")

  try:
    json_data = response.json()
  except Exception:
    preview = response.text[:100] if response.text else "Empty response"
    raise Exception(f"API Error: Invalid response format from server (received non-JSON: {preview})")

  if isinstance(json_data, dict):
    if json_data.get("status") == "success":
      return json_data.get("data")
    else:
      raise Exception(json_data.get("message", "Unknown error occurred."))

  return json_data

def get_supported_llm() -> list[str]:
  response = _request_with_retry("GET", f"{API_URL}/llm")
  return handle_response(response)

def get_supported_models(model_provider) -> list[str]:
  response = _request_with_retry("GET", f"{API_URL}/llm/{model_provider}")
  return handle_response(response)

def get_vectorstore_colllection_count(model_provider) -> int:
  response = _request_with_retry("GET", f"{API_URL}/vector_store/count/{model_provider}")
  return handle_response(response)

def get_vectorstore_similarity_search(model_provider, query) -> list[dict]:
  payload = {
    "model_provider": model_provider,
    "query": query
  }
  response = _request_with_retry("POST", f"{API_URL}/vector_store/search", json=payload)
  return handle_response(response)

def upload_and_process_pdfs(model_provider, uploaded_files) -> str:
  files = []
  for file in uploaded_files:
    if hasattr(file, "data"):
      files.append(("files", (file.name, BytesIO(file.data), file.type)))
    else:
      files.append(("files", (file.name, file.read(), file.type)))

  data = {
    "model_provider": model_provider
  }

  # Send the POST request with multiple files
  response = requests.post(f"{API_URL}/upload_and_process_pdfs", files=files, data=data, timeout=LONG_TIMEOUT)
  return handle_response(response)

def chat(model_provider, model_name, user_input) -> dict:
  payload = {
    "model_provider": model_provider,
    "model_name": model_name,
    "message": user_input
  }

  response = requests.post(f"{API_URL}/chat", json=payload, timeout=LONG_TIMEOUT)
  return handle_response(response)

