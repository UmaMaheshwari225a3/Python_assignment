class Recharge:
    plans = {
        "basic": {"price": 199, "validity": 28},
        "standard": {"price": 399, "validity": 56},
        "premium": {"price": 599, "validity": 84}
    }

    def __init__(self, balance=0, validity=0):
        self.balance = balance
        self.validity = validity

    def do_recharge(self, plan_name):
        if plan_name in Recharge.plans:
            plan = Recharge.plans[plan_name]
            self.balance -= plan["price"]
            self.validity += plan["validity"]
            return "Recharge successful"
        return "Invalid plan"

    def check_validity(self):
        return self.validity

    def show_balance(self):
        return self.balance

    @classmethod
    def update_recharge_plans(cls, plan_name, price, validity):
        cls.plans[plan_name] = {"price": price, "validity": validity}
r1 = Recharge(1000, 30)
print(r1.do_recharge("standard"))
print("Balance:", r1.show_balance())
print("Validity:", r1.check_validity())
Recharge.update_recharge_plans("super_premium", 999, 365)
print(r1.do_recharge("super_premium"))
print("Balance:", r1.show_balance())