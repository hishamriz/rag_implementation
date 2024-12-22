# tests/test_retriever.py

from retriever.retriever import PortDataRetriever

def test_retriever():
    retriever = PortDataRetriever()
    
    print("Testing retriever functionality...")
    
    # Test active shipments
    print("\n1. Active Shipments:")
    active_shipments = retriever.get_active_shipments()
    for shipment in active_shipments:
        print(f"- {shipment['booking_number']}: {shipment['vessel_name']} - {shipment['status']}")
    
    # Test container search
    print("\n2. Container Search (MSCU1234567):")
    container = retriever.search_container("MSCU1234567")
    if container:
        print(f"- Found container on vessel: {container[0]['vessel_name']}")
    
    # Test today's operations
    print("\n3. Today's Port Operations:")
    operations = retriever.get_today_operations()
    for op in operations:
        print(f"- {op['operation_type']} at berth {op['berth_number']}")
    
    # Test berthing schedule
    print("\n4. Current Berthing Schedule:")
    schedule = retriever.get_berthing_schedule()
    for berth in schedule:
        print(f"- Berth {berth['berth_number']}: {berth['vessel_name']}")

if __name__ == "__main__":
    test_retriever()