CREATE TABLE IF NOT EXISTS orders (
    id SERIAL PRIMARY KEY,
    order_id VARCHAR(50) UNIQUE NOT NULL,
    customer_name VARCHAR(255) NOT NULL,
    country VARCHAR(100),
    product VARCHAR(255),
    quantity INTEGER,
    price NUMERIC(10,2),
    order_date DATE,
    source_type VARCHAR(50),
    ingestion_timestamp TIMESTAMP DEFAULT NOW()
);

CREATE TABLE IF NOT EXISTS ingestion_errors (
    id SERIAL PRIMARY KEY,
    raw_data TEXT,
    error_message TEXT,
    source_file VARCHAR(255),
    created_at TIMESTAMP DEFAULT NOW()
);