
CREATE TABLE IF NOT EXISTS users (
    id SERIAL PRIMARY KEY,
    username VARCHAR(50) UNIQUE NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    password VARCHAR(255) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);


CREATE TABLE IF NOT EXISTS items (
    id SERIAL PRIMARY KEY,
    title VARCHAR(100) NOT NULL,
    description TEXT,
    owner_id INTEGER REFERENCES users(id) ON DELETE CASCADE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);


INSERT INTO users (username, email, password) VALUES
    ('admin', 'admin@example.com', 'hashedpassword123'),
    ('john', 'john@example.com', 'hashedpassword456');

INSERT INTO items (title, description, owner_id) VALUES
    ('Item 1', 'Description for item 1', 1),
    ('Item 2', 'Description for item 2', 2);