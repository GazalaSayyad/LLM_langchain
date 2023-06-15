from langchain import OpenAI, PromptTemplate, LLMChain
from langchain.text_splitter import CharacterTextSplitter
from langchain.chains.mapreduce import MapReduceChain
from langchain.prompts import PromptTemplate
from langchain.docstore.document import Document
from langchain.chains.summarize import load_summarize_chain

model_name = "text-davinci-003"

llm = OpenAI(temperature=0,model_name=model_name,openai_api_key='............')


text_splitter = CharacterTextSplitter()
with open("pdf_dataset/shakespare.txt") as f:
    state_of_the_union = f.read()
texts = text_splitter.split_text(state_of_the_union)


docs = [Document(page_content=t) for t in texts[:3]]
chain = load_summarize_chain(llm, chain_type="map_reduce")
res =chain.run(docs)
print(res)