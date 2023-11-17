CREATE TABLE Users (
    id SERIAL PRIMARY KEY,
    username VARCHAR(50) NOT NULL,
    password VARCHAR(100) NOT NULL -- Hashed password

);

-- Define the 'attendance' table to track employee attendance
CREATE TABLE Attendance (
    id SERIAL PRIMARY KEY,
    user_id INT REFERENCES users(id),
    check_in TIMESTAMP NOT NULL,
    check_out TIMESTAMP,
    date DATE NOT NULL
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
    month DATE NOT NULL,
    amount DECIMAL(10, 2) NOT NULL
);

-- Define the 'documents' table to store employee documents
CREATE TABLE Documents (
    id SERIAL PRIMARY KEY,
    user_id INT REFERENCES users(id),
    document_name VARCHAR(100) NOT NULL,
    document_url TEXT NOT NULL
);
