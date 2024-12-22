from retriever.retriever import PortDataRetriever
from generator.generator import ResponseGenerator
import sys

def test_rag_components():
    print("Testing RAG components...\n")
    
    try:
        # Test Retriever
        print("1. Testing Retriever...")
        retriever = PortDataRetriever()
        shipments = retriever.get_active_shipments()
        print(f"✓ Retrieved {len(shipments)} active shipments")
        
        # Test specific container
        container = retriever.search_container("MSCU1234567")
        if container:
            print("✓ Successfully retrieved container information")
        
        # Test Generator
        print("\n2. Testing Generator...")
        generator = ResponseGenerator()
        test_query = "What vessels are in port?"
        response = generator.generate_response(test_query, shipments)
        print("✓ Successfully generated response")
        print("\nSample Response:")
        print(response)
        
        print("\n✅ All components working correctly!")
        
    except Exception as e:
        print(f"\n❌ Error occurred: {str(e)}")
        print(f"Error type: {type(e).__name__}")
        print(f"Location: {sys.exc_info()[2].tb_frame.f_code.co_filename}, Line {sys.exc_info()[2].tb_lineno}")

if __name__ == "__main__":
    test_rag_components()