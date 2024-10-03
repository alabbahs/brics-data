-- Create countries table
CREATE TABLE countries (
    country_id SMALLSERIAL PRIMARY KEY,  -- SMALLSERIAL is the correct type for small integer serial
    country_name VARCHAR(50) NOT NULL
);

-- Create metrics table
CREATE TABLE metrics (
    metric_id SMALLSERIAL PRIMARY KEY,  -- SMALLSERIAL is the correct type here as well
    metric_name VARCHAR(200)
);

-- Create indicators table
CREATE TABLE indicators (
    indicator_id SERIAL PRIMARY KEY,  -- SERIAL by default creates integer columns, no need to specify INT
    value FLOAT,
    country_id SMALLINT,
    metric_id SMALLINT,
    year DATE,
    FOREIGN KEY (country_id) REFERENCES countries (country_id),
    FOREIGN KEY (metric_id) REFERENCES metrics (metric_id)
);

-- Insert countries data
INSERT INTO countries (country_name) VALUES
    ('Brazil'),
    ('Russia'),
    ('India'),
    ('China'),
    ('South Africa'),
    ('United States of America'),
    ('Great Britain'),
    ('France'),
    ('Denmark');

-- Insert metrics data
INSERT INTO metrics (metric_name) VALUES
    ('NY.GDP.MKTP.CD [GDP (current USD)]'),
    ('NY.GDP.PCAP.CD [GDP per capita]'),
    ('SL.UEM.TOTL.ZS [Unemployment rate]'),
    ('FP.CPI.TOTL.ZG [Inflation (consumer prices)]'),
    ('NY.GNP.PCAP.CD [GNI per capita (Atlas method)]'),
    ('DT.DOD.DECT.CD [External debt]'),
    ('GC.DOD.TOTL.GD.ZS [Government debt to GDP]'),
    ('NE.RSB.GNFS.CD [Trade balance]'),
    ('SP.DYN.LE00.IN [Life expectancy (proxy for HDI)]'),
    ('BX.KLT.DINV.CD.WD [Foreign direct investment (net inflows)]');
