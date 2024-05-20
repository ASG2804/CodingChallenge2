class Db_prop:
    @staticmethod
    def getconstring():
        con_string = {
            "Driver": "{SQL Server}",
            "server_name": "OMEN",
            "database_name": "Loan_Management_System",
            "Trusted_Connection": "Yes",
        }
        return con_string
