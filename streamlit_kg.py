import pandas as pd
import streamlit as st
from advertools import knowledge_graph

st.title("Query Google's Kowledge Graph")

container = st.container()

container.write("This tool makes it easier and simplier to query Google's Knowledge Graph using Google's Knowledge Graph API.")
container.write("Before using the tool, retrieve an API key through the Google Cloud platform. Find a quicklink in the \"?\" next to the API Key input box.")

container.write("Created by "<a href="https://www.linkedin.com/in/tyler-rouwhorst/">Tyler Rouwhorst</a>)

key = container.text_input("Input API Key Below:", help="https://developers.google.com/knowledge-graph/how-tos/authorizing")
query = container.text_input("Input Query Below")

options = st.multiselect(
    'Select Elements for Export',
    ['Name','Result Score','Result ID','Detailed Description','Description','Image URL','Result URL','Schema.org Type','Detailed Description Source URL'])

csv = None

if st.button("Start Query"):
    try:
        kg_df = knowledge_graph(key=key, query=query)
        if kg_df.empty: 
            None
        else:
            kg_df.rename(columns ={'query':'Query','resultScore':'Result Score','result.name':'Name','result.url':'Result URL','result.detailedDescription.url':'Detailed Description Source URL','result.detailedDescription.articleBody':'Detailed Description','result.@type':'Schema.org Type','result.image.url':'Image URL','result.description':'Description','result.@id':'Result ID'}, inplace=True)
            user_df = kg_df[options]
            csv = user_df.to_csv().encode('utf-8')
    except:
        st.write("Sorry, there are no results for this query")

if csv != None: 
    st.download_button(
        label="Download data as CSV",
        data=csv,
        file_name='kg_export.csv')
