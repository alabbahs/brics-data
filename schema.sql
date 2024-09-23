CREATE TABLE countries (
    country_id SERIAL SMALLINT PRIMARY KEY,
    country_name VARCHAR(50) NOT NULL
);

CREATE TABLE metrics (
    metric_id SERIAL SMALLINT PRIMARY KEY,
    metric_name VARCHAR(200)
)

CREATE TABLE indicators (
    indicator_id SERIAL INT PRIMARY KEY,
    value FLOAT,
    country_id SMALLINT,
    metric_id SMALLINT,
    year DATE,
    FOREIGN KEY (country_id) REFERENCES countries (country_id),
    FOREIGN KEY (metric_id) REFERENCES metrics (metric_id)
)

INSERT INTO countries (country_name) VALUES 
    ('Brazil'),
    ('Russia'),
    ('India'),
    ('China'),
    ('South Africa'),
    ('United States of America'),
    ('Great Britain'),
    ('France'),
    ('Denmark')

INSERT INTO metrics (metric_name) VALUES
    ('NY.GDP.MKTP.CD'),
    (''),
    (),
    (),
    (),
    (),
    (),
    (),
    (),
    (),
    (),
    (),
    (),
    (),