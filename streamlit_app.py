import streamlit as st #import pkg
from langchain.prompts import PromptTemplate
from langchain.llms import CTransformers

##function to get response from LLAma 2

def getLLamaresponse(input_text,no_words,x_style):
    ##llama2model calling
    llm = CTransformers(model="model/llama-2-7b-chat.ggmlv3.q8_0.bin",
                        model_type='llama',
                        config={'max_new_tokens':256,
                                'temperature':0.01})
    
##prompt temple
    template="""
        Write a blog for {x_style} job profile for a topic {input_text}
        within {no_words} words.
            """
    
    prompt=PromptTemplate(input_variables=["x_style","input_text",'no_words'],
                         template=template)
    
##generate response
    response=llm(prompt.format(x_style=x_style,input_text=input_text,no_words=no_words))
    print(response)
    return response

##craeate layout
st.set_page_config(page_title="Generate Blogs",
                   page_icon ='👽',
                   layout = 'centered',
                   initial_sidebar_state='auto')

st.header("Generate Blogs 👽 ")

input_text = st.text_input("Enter the blog topic")

##creating to more columns for addiitonal fileds

col1,col2=st.columns([5,5])

with col1:
    no_words=st.text_input('No of words')
with col2:
    x_style=st.selectbox('Writing the blog for',('Researcher','Data scientist','Common people'))


submit=st.button('Generate')

                        
if submit:
    st.write(getLLamaresponse(input_text,no_words,x_style))



