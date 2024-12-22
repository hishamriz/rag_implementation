-- Insert sample vessels
INSERT INTO vessels (vessel_name, imo_number, vessel_type, capacity_teu, flag_country) VALUES
('MSC Karachi', 'IMO9234567', 'Container Ship', 8000, 'Panama'),
('Maersk Lahore', 'IMO9345678', 'Container Ship', 6000, 'Denmark'),
('COSCO Gwadar', 'IMO9456789', 'Bulk Carrier', 4000, 'China'),
('Emirates Pearl', 'IMO9567890', 'Container Ship', 7500, 'UAE'),
('PNS Trading', 'IMO9678901', 'General Cargo', 3000, 'Pakistan');

-- Insert sample clients
INSERT INTO clients (company_name, client_type, ntn_number, contact_person, contact_email, contact_phone, address) VALUES
('Ali Trading Co.', 'Both', 'NTN123456', 'Ali Ahmed', 'ali@alitrading.pk', '+92301-2345678', 'Plot 123, Block 2, Clifton, Karachi'),
('Lahore Exports Ltd.', 'Exporter', 'NTN234567', 'Sara Khan', 'sara@lahoreexports.pk', '+92321-3456789', '45-A, Gulberg III, Lahore'),
('Gwadar Imports', 'Importer', 'NTN345678', 'Bilal Shah', 'bilal@gwadarimports.pk', '+92333-4567890', 'Gwadar Port Complex, Gwadar'),
('Textile Masters', 'Exporter', 'NTN456789', 'Fatima Hassan', 'fatima@textilemasters.pk', '+92345-5678901', 'Industrial Area, Faisalabad'),
('Karachi Traders', 'Both', 'NTN567890', 'Zain Malik', 'zain@karachitraders.pk', '+92312-6789012', 'Port Qasim, Karachi');

-- Insert sample containers
INSERT INTO containers (container_number, container_type, size_feet, weight_kg, status, current_location) VALUES
('MSCU1234567', 'Dry', 40, 25000.00, 'In Transit', 'Karachi Port'),
('CMAU2345678', 'Reefer', 40, 22000.00, 'At Port', 'Berth 4'),
('CSQU3456789', 'Dry', 20, 18000.00, 'Loaded', 'Vessel'),
('UACU4567890', 'Tank', 20, 16000.00, 'Empty', 'Container Yard'),
('PKNU5678901', 'Dry', 40, 24000.00, 'Under Inspection', 'Customs Area');

-- Insert sample shipments
INSERT INTO shipments (shipment_type, vessel_id, client_id, container_id, booking_number, origin_port, destination_port, departure_date, arrival_date, status, customs_declaration_number) VALUES
('Export', 1, 2, 1, 'BK123456', 'Karachi', 'Dubai', '2024-01-15', '2024-01-20', 'Completed', 'CD123456'),
('Import', 2, 3, 2, 'BK234567', 'Shanghai', 'Karachi', '2024-01-18', '2024-02-05', 'In Transit', 'CD234567'),
('Export', 3, 4, 3, 'BK345678', 'Karachi', 'Rotterdam', '2024-02-01', '2024-02-20', 'Loading', 'CD345678'),
('Import', 4, 1, 4, 'BK456789', 'Singapore', 'Karachi', '2024-02-10', '2024-02-25', 'Customs Clearance', 'CD456789'),
('Export', 5, 5, 5, 'BK567890', 'Karachi', 'Jeddah', '2024-02-15', '2024-02-25', 'Documentation', 'CD567890');

-- Insert sample port operations
INSERT INTO port_operations (operation_type, shipment_id, start_time, end_time, berth_number, equipment_used, personnel_assigned, status, notes) VALUES
('Loading', 1, '2024-01-15 08:00:00', '2024-01-15 16:00:00', 'B4', ARRAY['Crane 1', 'Forklift 3'], ARRAY['Team A', 'Supervisor John'], 'Completed', 'Smooth operation, no delays'),
('Unloading', 2, '2024-02-05 09:00:00', '2024-02-05 18:00:00', 'B2', ARRAY['Crane 2', 'Forklift 1'], ARRAY['Team B', 'Supervisor Sarah'], 'In Progress', 'Weather delay of 2 hours'),
('Loading', 3, '2024-02-01 07:00:00', NULL, 'B5', ARRAY['Crane 3', 'Forklift 4'], ARRAY['Team C', 'Supervisor Ali'], 'Ongoing', 'Starting ahead of schedule'),
('Customs Inspection', 4, '2024-02-10 10:00:00', '2024-02-10 15:00:00', 'CY1', ARRAY['Scanner 1'], ARRAY['Customs Team A'], 'Completed', 'Regular inspection completed'),
('Documentation', 5, '2024-02-15 09:00:00', NULL, 'DO1', NULL, ARRAY['Admin Team'], 'Pending', 'Awaiting final clearance');