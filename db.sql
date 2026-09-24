
DROP TABLE IF EXISTS spendings;
DROP TABLE IF EXISTS users;
CREATE TABLE  users(
    id INTEGER,
    name VARCHAR,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    PRIMARY KEY (id));
CREATE TABLE spendings (
    id INTEGER,
    month VARCHAR(10),
    user_id INTEGER NOT NULL,
    description VARCHAR,
    amount INTEGER,
    time TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    PRIMARY KEY (id)
    FOREIGN KEY (user_id) REFERENCES users(id)
);