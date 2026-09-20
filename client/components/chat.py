import pandas as pd
import streamlit as st

from datetime import datetime

from utils.helpers import process_user_input


def render_sources_expander(sources: list):
  if not sources:
    return
  with st.expander("📚 Sources & References", expanded=False):
    for idx, src in enumerate(sources, start=1):
      file_name = src.get("file_name", "Unknown document") if isinstance(src, dict) else getattr(src, "file_name", "Unknown document")
      page = src.get("page") if isinstance(src, dict) else getattr(src, "page", None)
      snippet = src.get("snippet", "") if isinstance(src, dict) else getattr(src, "snippet", "")

      page_info = f" (Page {page})" if page is not None else ""
      st.markdown(f"**Source {idx}:** `{file_name}`{page_info}")
      if snippet:
        st.caption(f'"{snippet}"')

def render_user_input(model_provider, model):
  disable_input = (
    st.session_state.get("unsubmitted_files", False)
    or not st.session_state.get(f"uploaded_files_{st.session_state.uploader_key}", [])
    or not st.session_state.get("chat_ready")
  )

  question = st.chat_input(
    "💬 Ask a Question from the PDF Files",
    disabled=disable_input
  )

  if not question:
    return

  with st.chat_message("user"):
    st.markdown(question)
  with st.chat_message("ai"):
    with st.spinner("Thinking..."):
      try:
        output = process_user_input(model_provider, model, question)
        if isinstance(output, dict):
          answer = output.get("answer", "")
          sources = output.get("sources", [])
        else:
          answer = str(output)
          sources = []

        st.markdown(answer)
        render_sources_expander(sources)

        pdf_names = [f.name for f in st.session_state.get("pdf_files", [])]
        st.session_state.chat_history.append(
          (question, answer, model_provider, model, pdf_names, datetime.now(), sources)
        )
      except Exception as e:
        st.error(f"Error: {str(e)}")

def render_uploaded_files_expander():
  uploaded_files = st.session_state.get(f"uploaded_files_{st.session_state.uploader_key}", [])
  if uploaded_files and not st.session_state.get("unsubmitted_files"):
    with st.expander("📎 Uploaded Files:"):
      for f in uploaded_files:
        st.markdown(f"- {f.name}")

def render_chat_history():
  for entry in st.session_state.get("chat_history", []):
    q = entry[0]
    a = entry[1]
    sources = entry[6] if len(entry) > 6 else []
    with st.chat_message("user"):
      st.markdown(q)
    with st.chat_message("ai"):
      st.markdown(a)
      render_sources_expander(sources)

def render_download_chat_history():
  records = []
  for entry in st.session_state.get("chat_history", []):
    q = entry[0] if len(entry) > 0 else ""
    a = entry[1] if len(entry) > 1 else ""
    provider = entry[2] if len(entry) > 2 else ""
    model = entry[3] if len(entry) > 3 else ""
    pdfs = entry[4] if len(entry) > 4 else []
    timestamp = entry[5] if len(entry) > 5 else ""
    sources = entry[6] if len(entry) > 6 else []

    sources_formatted = []
    if isinstance(sources, list):
      for s in sources:
        if isinstance(s, dict):
          fn = s.get("file_name", "")
          pg = s.get("page")
          sources_formatted.append(f"{fn} (Page {pg})" if pg is not None else fn)
        elif hasattr(s, "file_name"):
          fn = getattr(s, "file_name", "")
          pg = getattr(s, "page", None)
          sources_formatted.append(f"{fn} (Page {pg})" if pg is not None else fn)

    sources_str = "; ".join(sources_formatted) if sources_formatted else "N/A"
    pdf_files_str = ", ".join(pdfs) if isinstance(pdfs, list) else str(pdfs)

    records.append({
      "Question": q,
      "Answer": a,
      "Model Provider": provider,
      "Model Name": model,
      "PDF File": pdf_files_str,
      "Timestamp": timestamp,
      "Sources": sources_str
    })

  df = pd.DataFrame(records)

  with st.expander("📎 Download Chat History:"):
    st.sidebar.download_button(
      "📥 Download Chat History",
      data=df.to_csv(index=False),
      file_name="chat_history.csv",
      mime="text/csv"
    )
