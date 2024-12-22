# app.py
import streamlit as st
from retriever.retriever import PortDataRetriever
from generator.generator import ResponseGenerator

# Set page config
st.set_page_config(
    page_title="Port Management System",
    page_icon="🚢"
)

# Title
st.title("🚢 Port Management System")

# Simple test query interface
st.subheader("Ask about port operations")
user_query = st.text_input("Enter your question:")

if user_query:
    try:
        # Initialize components
        retriever = PortDataRetriever()
        generator = ResponseGenerator()
        
        # Get some basic data
        shipments = retriever.get_active_shipments()
        
        # Process and generate response
        processed_data = generator.preprocess_context(shipments)
        response = generator.generate_response(user_query, processed_data)
        
        # Show response
        st.write("Response:", response)
        
        # Show raw data (for debugging)
        with st.expander("Show raw data"):
            st.write(processed_data)
            
    except Exception as e:
        st.error(f"Error: {str(e)}")