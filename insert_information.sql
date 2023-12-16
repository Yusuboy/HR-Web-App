-- Inserting more sample users to reach a total of 15
INSERT INTO Users (username, password) VALUES
('Aiden_Rivers', 'hashed_password_aiden'),
('Bella_Winter', 'hashed_password_bella'),
('Cameron_Stone', 'hashed_password_cameron'),
('Dylan_Skyler', 'hashed_password_dylan'),
('Eva_Blaze', 'hashed_password_eva'),
('Felix_Thunder', 'hashed_password_felix'),
('Grace_Harmony', 'hashed_password_grace'),
('Hunter_Nightshade', 'hashed_password_hunter'),
('Ivy_Moonlight', 'hashed_password_ivy'),
('Jasper_Willow', 'hashed_password_jasper'),
('Kara_Silver', 'hashed_password_kara'),
('Liam_Starlight', 'hashed_password_liam'),
('Mia_Shadow', 'hashed_password_mia'),
('Noah_Rain', 'hashed_password_noah'),
('Olivia_Storm', 'hashed_password_olivia');



INSERT INTO Attendance (user_id, working_time, hour_class, check_in, check_out, checkout_reason)
VALUES
(1, 'Day job', 'Working hours', '2023-01-01 09:00:00'::TIMESTAMP, '2023-01-01 17:00:00'::TIMESTAMP, 'Checkout'),
(2, 'Evening shift', 'Working hours', '2023-01-01 16:00:00'::TIMESTAMP, '2023-01-01 17:30:00'::TIMESTAMP, 'For a coffee break'),
(2, 'Evening shift', 'Working hours', '2023-01-01 17:45:00'::TIMESTAMP, '2023-01-01 22:30:00'::TIMESTAMP, 'Checkout'),
(3, 'Day job', 'Working hours', '2023-01-01 09:15:00'::TIMESTAMP, '2023-01-01 12:15:00'::TIMESTAMP, 'For a Break'),
(3, 'Day job', 'Working hours', '2023-01-01 13:00:00'::TIMESTAMP, '2023-01-01 16:15:00'::TIMESTAMP, 'Checkout'),
(4, 'Evening shift', 'Travel', '2023-01-01 16:00:00'::TIMESTAMP, '2023-01-01 23:00:00'::TIMESTAMP, 'Checkout'),
(5, 'Day job', 'Working hours', '2023-01-01 09:30:00'::TIMESTAMP, '2023-01-01 12:30:00'::TIMESTAMP, 'For a coffee break'),
(5, 'Day job', 'Working hours', '2023-01-01 12:45:00'::TIMESTAMP, '2023-01-01 16:45:00'::TIMESTAMP, 'Checkout'),
(6, 'Day job', 'Working hours', '2023-01-01 08:00:00'::TIMESTAMP, '2023-01-01 12:00:00'::TIMESTAMP, 'Other'),
(7, 'Day job', 'Travel', '2023-01-01 09:30:00'::TIMESTAMP, '2023-01-01 13:30:00'::TIMESTAMP, 'Other'),
(7, 'Day job', 'Meeting', '2023-01-01 13:40:00'::TIMESTAMP, '2023-01-01 16:30:00'::TIMESTAMP, 'Checkout'),
(8, 'Evening job', 'Working hours', '2023-01-01 16:45:00'::TIMESTAMP, '2023-01-01 18:00:00'::TIMESTAMP, 'For a break'),
(8, 'Evening job', 'Working hours', '2023-01-01 18:15:00'::TIMESTAMP, '2023-01-01 23:00:00'::TIMESTAMP, 'Checkout'),
(9, 'Day job', 'Meeting', '2023-01-01 09:30:00'::TIMESTAMP, '2023-01-01 13:30:00'::TIMESTAMP, 'Checkout'),
(10, 'Evening shift', 'Travel', '2023-01-01 08:45:00'::TIMESTAMP, '2023-01-01 15:45:00'::TIMESTAMP, 'For a coffee break'),
(11, 'Day job', 'Working hours', '2023-01-01 09:00:00'::TIMESTAMP, '2023-01-01 17:00:00'::TIMESTAMP, 'Checkout'),
(12, 'Holidays', 'Working hours', '2023-12-24 13:00:00'::TIMESTAMP, '2023-12-24 15:00:00'::TIMESTAMP, 'For a break'),
(12, 'Holidays', 'Working hours', '2023-12-24 15:15:00'::TIMESTAMP, '2023-12-24 18:00:00'::TIMESTAMP, 'Checkout'),
(13, 'Holidays', 'Working hours', '2023-12-06 08:30:00'::TIMESTAMP, '2023-12-06 10:30:00'::TIMESTAMP, 'For a break'),
(13, 'Holidays', 'Working hours', '2023-12-06 10:45:00'::TIMESTAMP, '2023-12-06 15:30:00'::TIMESTAMP, 'Checkout'),
(14, 'Day job', 'Working hours', '2023-01-01 09:15:00'::TIMESTAMP, '2023-01-01 16:15:00'::TIMESTAMP, 'Checkout'),
(15, 'Evening shift', 'Meeting', '2023-01-01 16:00:00'::TIMESTAMP, '2023-01-01 22:00:00'::TIMESTAMP, 'Checkout');


INSERT INTO Leave_requests (user_id, start_date, end_date, reason, status) VALUES
(1, '2023-01-05', '2023-01-07', 'Annual Vacation', 'Pending'),
(2, '2023-01-10', '2023-01-12', 'Family Event - Wedding', 'Pending'),
(3, '2023-01-15', '2023-01-17', 'Personal Medical Appointment', 'Pending'),
(4, '2023-01-20', '2023-01-22', 'Attending a Workshop', 'Pending'),
(5, '2023-01-25', '2023-01-27', 'Long Weekend Getaway', 'Pending'),
(6, '2023-01-30', '2023-02-01', 'Family Reunion', 'Pending'),
(7, '2023-02-05', '2023-02-07', 'Sick Leave - Flu', 'Pending'),
(8, '2023-02-10', '2023-02-12', 'Personal Family Matter', 'Pending'),
(9, '2023-02-15', '2023-02-17', 'Annual Vacation', 'Pending'),
(10, '2023-02-20', '2023-02-22', 'Family Birthday Celebration', 'Pending'),
(11, '2023-02-25', '2023-02-27', 'Sick Leave - Cold', 'Pending'),
(12, '2023-03-05', '2023-03-07', 'Attending a Conference', 'Pending'),
(13, '2023-03-10', '2023-03-12', 'Annual Vacation', 'Pending'),
(14, '2023-03-15', '2023-03-17', 'Family Gathering', 'Pending'),
(15, '2023-03-20', '2023-03-22', 'Sick Leave - Doctors Appointment', 'Pending');

INSERT INTO Salaries (user_id, start_date, end_date, hourly_rate, total_earnings)
SELECT
    user_id,
    MIN(check_in::DATE) AS start_date,
    MAX(check_out::DATE) AS end_date,
    12 AS hourly_rate,
    (EXTRACT(EPOCH FROM SUM(check_out - check_in)) / 3600) * 12 AS total_earnings
FROM
    Attendance
GROUP BY
    user_id;