# retriever/db_connector.py

import psycopg2
from psycopg2.extras import RealDictCursor
from config import DB_CONFIG

class DBConnector:
    def __init__(self):
        self.conn_params = {
            'dbname': 'rag_knowledge_base',
            'user': DB_CONFIG['user'],
            'password': DB_CONFIG['password'],
            'host': DB_CONFIG['host'],
            'port': DB_CONFIG['port']
        }

    def get_connection(self):
        return psycopg2.connect(**self.conn_params)

    def execute_query(self, query, params=None):
        """Execute a query and return results as dictionary"""
        with self.get_connection() as conn:
            with conn.cursor(cursor_factory=RealDictCursor) as cur:
                cur.execute(query, params)
                return cur.fetchall()

    def get_shipment_details(self, booking_number=None, container_number=None):
        """Get shipment details by booking number or container number"""
        query = """
            SELECT s.*, v.vessel_name, c.container_number, cl.company_name
            FROM shipments s
            JOIN vessels v ON s.vessel_id = v.id
            JOIN containers c ON s.container_id = c.id
            JOIN clients cl ON s.client_id = cl.id
            WHERE 1=1
        """
        params = []
        
        if booking_number:
            query += " AND s.booking_number = %s"
            params.append(booking_number)
        if container_number:
            query += " AND c.container_number = %s"
            params.append(container_number)
            
        return self.execute_query(query, params)

    def get_vessel_schedule(self, date_from=None, date_to=None):
        """Get vessel schedule for a date range"""
        query = """
            SELECT v.vessel_name, s.departure_date, s.arrival_date, 
                   s.origin_port, s.destination_port, s.status
            FROM vessels v
            JOIN shipments s ON v.id = s.vessel_id
            WHERE 1=1
        """
        params = []
        
        if date_from:
            query += " AND s.departure_date >= %s"
            params.append(date_from)
        if date_to:
            query += " AND s.arrival_date <= %s"
            params.append(date_to)
            
        query += " ORDER BY s.departure_date"
        return self.execute_query(query, params)

    def get_port_operations(self, operation_date=None, status=None):
        """Get port operations with optional date and status filters"""
        query = """
            SELECT po.*, s.booking_number, v.vessel_name
            FROM port_operations po
            JOIN shipments s ON po.shipment_id = s.id
            JOIN vessels v ON s.vessel_id = v.id
            WHERE 1=1
        """
        params = []
        
        if operation_date:
            query += " AND DATE(po.start_time) = %s"
            params.append(operation_date)
        if status:
            query += " AND po.status = %s"
            params.append(status)
            
        return self.execute_query(query, params)