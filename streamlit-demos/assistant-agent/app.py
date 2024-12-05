import streamlit as st
from langchain_groq import ChatGroq 
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_community.tools.tavily_search import TavilySearchResults


# Model and Agent tools
llm =  ChatGroq(api_key=st.secrets.get("GROQ_API_KEY"))
search = TavilySearchResults(max_results=2)
parser = StrOutputParser()

# Page Header
st.title("Assistant Agent")
st.markdown("Assistant Agent Powered by Groq.")
st.markdown("### Help researchers gather insights from academic papers, extract summaries, and identify key references.")


# Data collection/inputs
with st.form("paper_research", clear_on_submit=True):

  paper_url = st.text_input("Paper URL:")

  # For the llm insights result
  paper_insights = ""

  # Data process
  if st.form_submit_button("Generate Insights"):
    if paper_url:
      st.spinner("Processing...")

      # search internet
      paper_data = search.invoke(paper_url)
      print(paper_data)

      prompt = """
      You are a helpful AI assistant. Your job is to analyze the provided research paper data, to generate insights. Provide:

      1. A summary of the paper.
      2. Insights from the academic paper.
      3. Identify key references.

      Input variables:
      - {paper_data}
      """

      # Prompt Template
      prompt_template = ChatPromptTemplate([("system", prompt)])

      # Chain
      chain = prompt_template | llm | parser

      # Result/Insights
      paper_insights = chain.invoke({"paper_data": paper_data})

st.markdown(paper_insights)