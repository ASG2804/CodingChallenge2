create database Loan_Management_System
use Loan_Management_System

create table Customer(
Customer_ID int identity(1,1) Primary key,
Name varchar(20),
Email Varchar(20),
Phone_Number varchar(20),
Address varchar(50),
Credit_Score int)

create table Loan(
Loan_ID int identity(1,1) Primary key,
Customer_ID int,
Principal_Amount int,
Interest_Rate int,
Loan_Term int,
Loan_Type varchar(20),
Loan_Status varchar(20) default 'Pending',
FOREIGN KEY (Customer_ID) REFERENCES Customer(Customer_ID)
)

ALTER TABLE Loan NOCHECK CONSTRAINT FK__Loan__Customer_I__3E52440B;