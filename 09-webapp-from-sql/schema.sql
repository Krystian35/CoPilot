-- schema.sql
-- Simple product catalog: categories + products

DROP TABLE IF EXISTS products;
DROP TABLE IF EXISTS categories;

CREATE TABLE categories (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    description TEXT
);

CREATE TABLE products (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    category_id INTEGER NOT NULL,
    title TEXT NOT NULL,
    author TEXT,
    price REAL,
    stock INTEGER DEFAULT 0,
    FOREIGN KEY (category_id) REFERENCES categories(id)
);

-- Sample data
INSERT INTO categories (name, description)
VALUES
    ("Science Fiction", "Sci-fi & future worlds"),
    ("Programming", "Development, software engineering"),
    ("Business", "Leadership & productivity");

INSERT INTO products (category_id, title, author, price, stock)
VALUES
    (1, "Dune", "Frank Herbert", 39.99, 12),
    (1, "Neuromancer", "William Gibson", 29.99, 8),
    (2, "Clean Code", "Robert C. Martin", 59.99, 5),
    (2, "Fluent Python", "Luciano Ramalho", 69.99, 3),
    (3, "Deep Work", "Cal Newport", 49.99, 11),
    (3, "The Lean Startup", "Eric Ries", 34.99, 7),
    (3, "Atomic Habits", "James Clear", 24.99, 15),
    (2, "The Pragmatic Programmer", "Andrew Hunt", 44.99, 4),
    (1, "Foundation", "Isaac Asimov", 27.99, 9),
    (2, "Introduction to Algorithms", "Cormen, Leiserson, Rivest, Stein", 89.99, 2),
    (3, "Good to Great", "Jim Collins", 39.99, 6),
    (1, "Snow Crash", "Neal Stephenson", 32.99, 10);
    

