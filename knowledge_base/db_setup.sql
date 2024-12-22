-- Drop existing tables if they exist
DROP TABLE IF EXISTS keyword_mappings CASCADE;
DROP TABLE IF EXISTS facts CASCADE;

-- Create new domain-specific tables

-- Vessels table
CREATE TABLE vessels (
    id SERIAL PRIMARY KEY,
    vessel_name VARCHAR(255) NOT NULL,
    imo_number VARCHAR(50) UNIQUE,
    vessel_type VARCHAR(100),
    capacity_teu INTEGER,
    flag_country VARCHAR(100),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Clients table
CREATE TABLE clients (
    id SERIAL PRIMARY KEY,
    company_name VARCHAR(255) NOT NULL,
    client_type VARCHAR(50) CHECK (client_type IN ('Importer', 'Exporter', 'Both')),
    ntn_number VARCHAR(100) UNIQUE,
    contact_person VARCHAR(255),
    contact_email VARCHAR(255),
    contact_phone VARCHAR(50),
    address TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Containers table
CREATE TABLE containers (
    id SERIAL PRIMARY KEY,
    container_number VARCHAR(50) UNIQUE,
    container_type VARCHAR(50),
    size_feet INTEGER CHECK (size_feet IN (20, 40, 45)),
    weight_kg DECIMAL(10,2),
    status VARCHAR(50),
    current_location VARCHAR(255),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Shipments table
CREATE TABLE shipments (
    id SERIAL PRIMARY KEY,
    shipment_type VARCHAR(50) CHECK (shipment_type IN ('Import', 'Export')),
    vessel_id INTEGER REFERENCES vessels(id),
    client_id INTEGER REFERENCES clients(id),
    container_id INTEGER REFERENCES containers(id),
    booking_number VARCHAR(100) UNIQUE,
    origin_port VARCHAR(255),
    destination_port VARCHAR(255),
    departure_date DATE,
    arrival_date DATE,
    status VARCHAR(100),
    customs_declaration_number VARCHAR(100),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Port Operations table
CREATE TABLE port_operations (
    id SERIAL PRIMARY KEY,
    operation_type VARCHAR(100),
    shipment_id INTEGER REFERENCES shipments(id),
    start_time TIMESTAMP,
    end_time TIMESTAMP,
    berth_number VARCHAR(50),
    equipment_used TEXT[],
    personnel_assigned TEXT[],
    status VARCHAR(100),
    notes TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Create triggers for updating timestamps
CREATE OR REPLACE FUNCTION update_updated_at_column()
RETURNS TRIGGER AS $$
BEGIN
    NEW.updated_at = CURRENT_TIMESTAMP;
    RETURN NEW;
END;
$$ language 'plpgsql';

-- Create triggers for all tables
CREATE TRIGGER update_vessels_timestamp
    BEFORE UPDATE ON vessels
    FOR EACH ROW EXECUTE FUNCTION update_updated_at_column();

CREATE TRIGGER update_clients_timestamp
    BEFORE UPDATE ON clients
    FOR EACH ROW EXECUTE FUNCTION update_updated_at_column();

CREATE TRIGGER update_containers_timestamp
    BEFORE UPDATE ON containers
    FOR EACH ROW EXECUTE FUNCTION update_updated_at_column();

CREATE TRIGGER update_shipments_timestamp
    BEFORE UPDATE ON shipments
    FOR EACH ROW EXECUTE FUNCTION update_updated_at_column();

CREATE TRIGGER update_port_operations_timestamp
    BEFORE UPDATE ON port_operations
    FOR EACH ROW EXECUTE FUNCTION update_updated_at_column();

-- Create indexes for frequently accessed columns
CREATE INDEX idx_vessels_imo ON vessels(imo_number);
CREATE INDEX idx_clients_ntn ON clients(ntn_number);
CREATE INDEX idx_containers_number ON containers(container_number);
CREATE INDEX idx_shipments_booking ON shipments(booking_number);
CREATE INDEX idx_shipments_dates ON shipments(departure_date, arrival_date);
CREATE INDEX idx_port_operations_dates ON port_operations(start_time, end_time);