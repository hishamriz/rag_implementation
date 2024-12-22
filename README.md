# rag_implementation
Database Layer


Uses PostgreSQL to store data about:

Vessels (ships, capacity, flags)
Containers (tracking numbers, types, status)
Shipments (imports/exports)
Port Operations (loading, unloading, schedules)
Clients (importers/exporters)


Retriever Module (retriever.py)


Acts as a data access layer
Connects to database using db_connector.py
Provides methods to:

Get active shipments
Search containers
Check vessel schedules
Track port operations

Generator Module (generator.py)


Uses OpenAI's API to generate natural language responses
Takes user queries and relevant context
Processes data to ensure it's properly formatted
Returns human-readable answers


Web Interface (app.py)


Built with Streamlit
Provides:

Dashboard view of port operations
Natural language query interface
Shipment tracking
Vessel scheduling

For example, if someone asks "What vessels are arriving today?":

Retriever pulls vessel schedule from database
Generator takes this data and the question
OpenAI formats a natural language response
User sees a clear answer through Streamlit

