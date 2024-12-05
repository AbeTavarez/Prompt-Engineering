import streamlit as st
from langchain_groq import ChatGroq 
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_community.tools.tavily_search import TavilySearchResults


# Model and Agent tools
llm =  ChatGroq(api_key=st.secrets.get("GROQ_API_KEY"))
search = TavilySearchResults(max_results=2)
parser = StrOutputParser()
# tools = [search] # add tools to the list

# Page Header
st.title("Assistant Agent")
st.markdown("Assistant Agent Powered by Groq.")


# Data collection/inputs
with st.form("company_info", clear_on_submit=True):

  product_name = st.text_input("Product Name:")
  company_url = st.text_input("Company URL:")
  competitors = st.text_input("Competitors list (ex. Apple, Tesla):")

  # For the llm insights result
  company_insights = ""

  # Data process
  if st.form_submit_button("Generate Insights"):
    if product_name and company_url:
      st.spinner("Processing...")

      # search internet
      company_data = search.invoke(company_url)
      print(company_data)

      prompt = """
      You are a helpful AI assisting a sales representative. Your job is to analyze the provided company data, the product being sold, and the competitors to generate actionable insights. Provide:

      1. A summary of the company's strategy.
      2. Potential competitors from the list or company overview.
      3. Key leadership or decision-maker insights.

      Input variables:
      - {company_data}
      - {product_name}
      - {competitors}
      """

      # Prompt Template
      prompt_template = ChatPromptTemplate([("system", prompt)])

      # Chain
      chain = prompt_template | llm | parser

      # Result/Insights
      company_insights = chain.invoke({"company_data": company_data, "product_name": product_name, "competitors": competitors})

st.markdown(company_insights)