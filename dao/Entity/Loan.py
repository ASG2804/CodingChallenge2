class Loan:
    def __init__(self, loan_id, customer_id, principal_amount, interest_rate, loan_term, loan_type, loan_status) -> None:
        self.loan_id = loan_id
        self.customer_id = customer_id
        self.principal_amount = principal_amount
        self.interest_rate = interest_rate
        self.loan_term = loan_term
        self.loan_type = loan_type
        self.loan_status = loan_status

    class HomeLoan:
        def __init__(self, property_address, property_value) -> None:
            self.property_address = property_address
            self.property_value = property_value

    class CarLoan:
        def __init__(self, car_model, car_value):
            self.car_model = car_model
            self.car_value = car_value
