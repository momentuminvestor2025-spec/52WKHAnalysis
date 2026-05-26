SCHEMA_SQL = """
CREATE TABLE IF NOT EXISTS stocks_master (
    id SERIAL PRIMARY KEY,
    symbol VARCHAR(32) UNIQUE NOT NULL,
    company_name VARCHAR(255) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS daily_52week_high (
    id SERIAL PRIMARY KEY,
    stock_id INTEGER NOT NULL REFERENCES stocks_master(id),
    trade_date DATE NOT NULL,
    current_price NUMERIC(14,2),
    historical_count INTEGER DEFAULT 1,
    first_seen_date DATE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    UNIQUE(stock_id, trade_date)
);

CREATE TABLE IF NOT EXISTS daily_most_active (
    id SERIAL PRIMARY KEY,
    stock_id INTEGER NOT NULL REFERENCES stocks_master(id),
    trade_date DATE NOT NULL,
    volume BIGINT,
    turnover NUMERIC(18,2),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    UNIQUE(stock_id, trade_date)
);

CREATE TABLE IF NOT EXISTS occurrence_history (
    id SERIAL PRIMARY KEY,
    stock_id INTEGER NOT NULL REFERENCES stocks_master(id),
    source_name VARCHAR(64) NOT NULL,
    trade_date DATE NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    UNIQUE(stock_id, source_name, trade_date)
);

CREATE TABLE IF NOT EXISTS overlap_analytics (
    id SERIAL PRIMARY KEY,
    stock_id INTEGER NOT NULL REFERENCES stocks_master(id),
    trade_date DATE NOT NULL,
    overlap_status BOOLEAN NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    UNIQUE(stock_id, trade_date)
);
"""
