CREATE TABLE tasks (
    time DATETIME NOT NULL,
    note TEXT NOT NULL,
    status INTEGER DEFAULT 0 NOT NULL
);