# retriever/retriever.py

from .db_connector import DBConnector
from datetime import datetime, timedelta

class PortDataRetriever:
    def __init__(self):
        self.db = DBConnector()

    def get_active_shipments(self):
        """Retrieve all active shipments"""
        query = """
            SELECT s.*, v.vessel_name, c.container_number, cl.company_name
            FROM shipments s
            JOIN vessels v ON s.vessel_id = v.id
            JOIN containers c ON s.container_id = c.id
            JOIN clients cl ON s.client_id = cl.id
            WHERE s.status NOT IN ('Completed', 'Cancelled')
            ORDER BY s.departure_date
        """
        return self.db.execute_query(query)

    def search_container(self, container_number):
        """Search for a container and its current status"""
        return self.db.get_shipment_details(container_number=container_number)

    def get_today_operations(self):
        """Get all port operations scheduled for today"""
        return self.db.get_port_operations(operation_date=datetime.now().date())

    def get_upcoming_vessels(self, days=7):
        """Get vessels expected to arrive in the next X days"""
        end_date = datetime.now().date() + timedelta(days=days)
        return self.db.get_vessel_schedule(
            date_from=datetime.now().date(),
            date_to=end_date
        )

    def get_client_shipments(self, client_id):
        """Get all shipments for a specific client"""
        query = """
            SELECT s.*, v.vessel_name, c.container_number
            FROM shipments s
            JOIN vessels v ON s.vessel_id = v.id
            JOIN containers c ON s.container_id = c.id
            WHERE s.client_id = %s
            ORDER BY s.created_at DESC
        """
        return self.db.execute_query(query, [client_id])

    def get_berthing_schedule(self):
        """Get current berthing schedule"""
        query = """
            SELECT DISTINCT ON (po.berth_number)
                po.berth_number,
                v.vessel_name,
                po.start_time,
                po.end_time,
                po.status
            FROM port_operations po
            JOIN shipments s ON po.shipment_id = s.id
            JOIN vessels v ON s.vessel_id = v.id
            WHERE po.berth_number IS NOT NULL
                AND (po.end_time IS NULL OR po.end_time >= NOW())
            ORDER BY po.berth_number, po.start_time DESC
        """
        return self.db.execute_query(query)