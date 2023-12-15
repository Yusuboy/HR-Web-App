CREATE TABLE Users (
    id SERIAL PRIMARY KEY,
    username VARCHAR(50) NOT NULL,
    password VARCHAR(1000) NOT NULL -- Hashed password

);

-- Define the 'attendance' table to track employee attendance
CREATE TABLE Attendance (
    id SERIAL PRIMARY KEY,
    user_id INT REFERENCES users(id),
    working_time TEXT,
    hour_class TEXT,
    check_in TIMESTAMP NOT NULL,
    check_out TIMESTAMP,
    checkout_reason TEXT
);

-- Define the 'leave_requests' table to manage employee leave requests
CREATE TABLE Leave_requests (
    id SERIAL PRIMARY KEY,
    user_id INT REFERENCES users(id),
    start_date DATE NOT NULL,
    end_date DATE NOT NULL,
    reason TEXT,
    status VARCHAR(20) NOT NULL -- Pending, Approved, Rejected
);

-- Define the 'salaries' table to manage employee salaries
CREATE TABLE Salaries (
    id SERIAL PRIMARY KEY,
    user_id INT REFERENCES users(id),
    start_date DATE NOT NULL,
    end_date DATE,
    hourly_rate DECIMAL(10, 2) NOT NULL,
    total_earnings DECIMAL(10, 2),
    CONSTRAINT user_id_end_date_unique UNIQUE (user_id, end_date)
);



CREATE TABLE Admin (
    id SERIAL PRIMARY KEY,
    username VARCHAR(50) NOT NULL,
    password VARCHAR(1000) NOT NULL
);


-- -- Define the 'documents' table to store employee documents
-- CREATE TABLE Documents (
--     id SERIAL PRIMARY KEY,
--     user_id INT REFERENCES users(id),
--     document_name VARCHAR(100) NOT NULL,
--     document_url TEXT NOT NULL
-- );

INSERT INTO Admin (username, password) VALUES ('Admin', 'hashed_password_of_123456');
ALTER TABLE Users ADD COLUMN is_admin BOOLEAN DEFAULT FALSE;
UPDATE Users SET is_admin = TRUE WHERE username = 'Admin';
