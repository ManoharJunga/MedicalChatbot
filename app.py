#AIzaSyBqMYh2hkbe-0OS3wTAHZ3vsqqrjUU4eig

import streamlit as st
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.prompts import PromptTemplate
from langchain.chains.llm import LLMChain

# Initialize the language model
llm = ChatGoogleGenerativeAI(model="gemini-pro", google_api_key="AIzaSyBqMYh2hkbe-0OS3wTAHZ3vsqqrjUU4eig")

def main():
    st.title(" ⚕️ Medical Chatbot")

    # Input field for user query
    user_query = st.text_input("Enter your query:", "")

    # Button to request suggestions
    if st.button("Get Response"):
        # Define the template for the language model
        template = "Given the following information:\n\"{user_query}\"\ngive about this disease ?"
        prompt = PromptTemplate.from_template(template)
        
        # Initialize the language model chain
        llm_chain = LLMChain(llm=llm, prompt=prompt)
        
        # Invoke the language model and get response
        response = llm_chain.invoke(user_query)
        
        # Display the response
        st.write("Chatbot Response:")
        st.write(response["text"])

# Run the Streamlit app
if __name__ == "__main__":
    main()
