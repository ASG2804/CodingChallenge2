from dao.Entity import Loan
from dao import ILoanRepositoryImpl


def display_menu():
    print("1. Apply for a Loan")
    print("2. Compute Interest")
    print("3. Calculate EMI")
    print("4. Repay Loan")
    print("5. View All Loans")
    print("6. Find Loan by ID")
    print("7. Check Loan Status")
    print("8. Exit Application")


def main():
    loan_service = ILoanRepositoryImpl()
    while True:
        display_menu()
        user_choice = int(input("Enter your choice: "))

        if user_choice == 1:
            loanID = input("Enter Loan ID: ")
            customerID = input("Enter Customer ID: ")
            principalAmount = float(input("Enter Principal Amount: "))
            interestRate = float(input("Enter Interest Rate: "))
            loanTerm = int(input("Enter Loan Term (in months): "))
            loanType = input("Enter Loan Type (CarLoan/HomeLoan): ")
            loanStatus = "Pending"

            new_loan = Loan(
                loanID,
                customerID,
                principalAmount,
                interestRate,
                loanTerm,
                loanType,
                loanStatus,
            )
            loan_service.applyLoan(new_loan)
        elif user_choice == 2:
            loan_id = int(input("Enter the Loan ID: "))
            loan_service.calculateInterest(loanID)
        elif user_choice == 3:
            loan_id = int(input("Enter the Loan ID: "))
            loan_service.calculateEMI(loanID)
        elif user_choice == 4:
            loan_id = int(input("Enter the Loan ID: "))
            loan_service.loanRepayment(loanID)
        elif user_choice == 5:
            loan_service.getAllLoan()
        elif user_choice == 6:
            loan_id = int(input("Enter the Loan ID: "))
            loan_service.getLoanById(loanID)
        elif user_choice == 7:
            loan_id = int(input("Enter the Loan ID: "))
            loan_service.loanStatus(loanID)
        elif user_choice == 8:
            loan_service.close()
            break
        else:
            print("Please enter a valid choice between 1 and 8.")


if __name__ == "__main__":
    main()
