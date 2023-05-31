-- Create the 'user' table
CREATE TABLE IF NOT EXISTS user (
  id INT PRIMARY KEY,
  email VARCHAR(255),
  firstname VARCHAR(255),
  lastname VARCHAR(255),
  language VARCHAR(50),
  timezone VARCHAR(50),
  is_stakeholder BOOLEAN,
  last_visit_time DATETIME,
  role VARCHAR(50),
  account_id INT,
  updated DATETIME,
  created DATETIME
);

-- Insert example data into the 'user' table
INSERT INTO user (id, email, firstname, lastname, language, timezone, is_stakeholder, last_visit_time, role, account_id, updated, created)
VALUES
  (1, 'john@example.com', 'John', 'Doe', 'English', 'UTC', 1, '2023-05-23 10:00:00', 'Admin', 1, '2023-05-23 10:00:00', '2023-05-23 10:00:00'),
  (2, 'jane@example.com', 'Jane', 'Smith', 'Spanish', 'EST', 0, '2023-05-22 15:30:00', 'User', 2, '2023-05-22 15:30:00', '2023-05-22 15:30:00');

-- Create the 'account' table
CREATE TABLE IF NOT EXISTS account (
  id INT PRIMARY KEY,
  is_demo BOOLEAN,
  plan VARCHAR(50),
  license_count INT,
  user_count INT,
  purchase_time DATETIME,
  customer_io_opted_in BOOLEAN,
  last_visit_time DATETIME,
  updated DATETIME,
  created DATETIME
);

-- Insert example data into the 'account' table
INSERT INTO account (id, is_demo, plan, license_count, user_count, purchase_time, customer_io_opted_in, updated, created)
VALUES
  (1, 0, 'Premium', 10, 5, '2023-05-21 09:45:00', 1, '2023-05-23 10:30:00','2023-05-23 10:30:00'),
  (2, 1, 'Basic', 5, 2, '2023-05-20 14:00:00', 0, '2023-05-22 16:45:00', '2023-05-22 16:45:00');