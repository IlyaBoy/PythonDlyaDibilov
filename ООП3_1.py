class employee:
    def calculate_payroll():
        pass

class hourlyemployee (employee):

    def __init__(self,hours):
        self.hours=hours

    def calculate_payroll(self):
        self.payroll=20.8 * 8 * self.hours

    def print_info(self):
        print('Оплата: ', self.payroll)

class termemployee (employee):

    def __init__(self,fixedmoney):
        self.fixedmoney=fixedmoney

    def calculate_payroll(self):
        self.payroll=self.fixedmoney

    def print_info(self):
        print('Оплата: ', self.payroll)

Work1=hourlyemployee(10)
Work1.calculate_payroll()
Work1.print_info()

Work2=termemployee(10)
Work2.calculate_payroll()
Work2.print_info()
