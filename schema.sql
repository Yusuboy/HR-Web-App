CREATE TABLE IF NOT EXISTS Users (
    id SERIAL PRIMARY KEY,
    username VARCHAR(50) NOT NULL,
    password VARCHAR(1000) NOT NULL -- Hashed password

);

-- Define the 'attendance' table to track employee attendance
CREATE TABLE IF NOT EXISTS Attendance (
    id SERIAL PRIMARY KEY,
    user_id INT REFERENCES users(id),
    working_time TEXT,
    hour_class TEXT,
    check_in TIMESTAMP NOT NULL,
    check_out TIMESTAMP,
    checkout_reason TEXT
);

-- Define the 'leave_requests' table to manage employee leave requests
CREATE TABLE IF NOT EXISTS Leave_requests (
    id SERIAL PRIMARY KEY,
    user_id INT REFERENCES users(id),
    start_date DATE NOT NULL,
    end_date DATE NOT NULL,
    reason TEXT,
    status VARCHAR(20) NOT NULL -- Pending, Approved, Rejected
);

-- Define the 'salaries' table to manage employee salaries
CREATE TABLE IF NOT EXISTS Salaries (
    id SERIAL PRIMARY KEY,
    user_id INT REFERENCES users(id),
    start_date DATE NOT NULL,
    end_date DATE,
    hourly_rate DECIMAL(10, 2) NOT NULL,
    total_earnings DECIMAL(10, 2),
    CONSTRAINT user_id_end_date_unique UNIQUE (user_id, end_date)
);



CREATE TABLE IF NOT EXISTS Admin (
    id SERIAL PRIMARY KEY,
    username VARCHAR(50) NOT NULL,
    password VARCHAR(1000) NOT NULL
);


INSERT INTO Admin (username, password) VALUES ('Admin', '123456');
ALTER TABLE Users ADD COLUMN is_admin BOOLEAN DEFAULT FALSE;

