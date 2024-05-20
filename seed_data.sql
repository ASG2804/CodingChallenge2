-- Inserting values into Customer table
INSERT INTO Customer (Name, Email, Phone_Number, Address, Credit_Score) VALUES
('Aarav', 'aarav@mail.com', '111222333', 'Bangalore', 800),
('Ishaan', 'ishaan@mail.com', '111222444', 'Mumbai', 810),
('Aadhya', 'aadhya@mail.com', '111222555', 'Delhi', 600),
('Avni', 'avni@mail.com', '111222666', 'Kolkata', 400);

-- Inserting values into Loan table
INSERT INTO Loan (Customer, Principal_Amount, Interest_Rate, Loan_Term, Loan_Type, Loan_Status) VALUES
(1, 50000, 2, 12, 'HomeLoan', 'Approved'),
(2, 75000, 5, 24, 'HomeLoan', 'Pending');
