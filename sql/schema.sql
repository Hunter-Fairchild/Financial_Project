--Schema for SGA records database. 

DROP TABLE IF EXISTS balance_updates CASCADE;
DROP TABLE IF EXISTS accounts CASCADE;
DROP TABLE IF EXISTS organizations CASCADE;
DROP TABLE IF EXISTS agency_reports CASCADE;
DROP TABLE IF EXISTS sga_allocations CASCADE;
DROP TABLE IF EXISTS allocation_items CASCADE;

CREATE TABLE IF NOT EXISTS organizations (
    id SERIAL PRIMARY KEY,
    name TEXT NOT NULL, 
    funding_category VARCHAR(255),
    creation_date DATE,
    advisor VARCHAR(255),
    member_count INTEGER,
    description TEXT
);

CREATE TABLE IF NOT EXISTS accounts (
    id SERIAL PRIMARY KEY,
    organization_id INTEGER REFERENCES organizations(id), 
    account_number VARCHAR(11) NOT NULL UNIQUE,
    name VARCHAR(255) NOT NULL,
    creation_date DATE,
    description TEXT
);

CREATE TABLE IF NOT EXISTS agency_reports (
    id SERIAL PRIMARY KEY,
    file_name TEXT NOT NULL UNIQUE,
    date DATE,
    uploaded_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS balance_updates (
    id SERIAL PRIMARY KEY,
    account_id INTEGER REFERENCES accounts(id),
    report_id INTEGER REFERENCES agency_reports(id),
    date DATE NOT NULL,
    opening_balance NUMERIC(12, 2),
    cactivity NUMERIC(12, 2),
    ending_balance NUMERIC(12, 2),
    CONSTRAINT update UNIQUE (account_id, report_id)
);

CREATE TABLE IF NOT EXISTS sga_allocations (
    id SERIAL PRIMARY KEY,
    organization_id INTEGER REFERENCES organizations(id),
    date DATE, 
    treasurer_email VARCHAR(255),   
    rollover NUMERIC(12, 2), 
    fundraising NUMERIC(12, 2),
    expenses NUMERIC(12, 2),
    request NUMERIC(12, 2)
);

CREATE TABLE IF NOT EXISTS allocation_items (
    id SERIAL PRIMARY KEY, 
    allocation_id INTEGER REFERENCES sga_allocations(id),
    type VARCHAR(255),
    name TEXT, 
    amount NUMERIC(12, 2),
    description TEXT
);


