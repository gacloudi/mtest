import streamlit as st
import pymongo
url=st.secrets(["url"])

# Initialize connection.
# Uses st.cache_resource to only run once.
#@st.cache_resource
def init_connection():
    return pymongo.MongoClient(url)

client = init_connection()


# Pull data from the collection.
# Uses st.cache_data to only rerun when the query changes or after 10 min.
#@st.cache_data(ttl=600)
def get_data():
    db = client.Test
    items = db.C1.find()
    items = list(items)  # make hashable for st.cache_data
    
    st.write("===")
    ##st.write(items)
    return items
items = get_data()
st.write("Hi")
# Print results.
for item in items:
    st.write({item['title']})
