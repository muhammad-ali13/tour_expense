import pandas as pd
class Member:
    def __init__(self, name) -> None:
        self.name = name
        self.lent_members = {}
        self.receive_members = {}
        self.members = []
        self.total_calc = {}
    def calculate(self):

        for member in list(self.total_calc.keys()):
            lend_amount = self.lent_members.get(member, 0)
            receive_amount = self.receive_members.get(member, 0)
            self.total_calc[member] 
    def update_member(self, member, amount, typ):
        if member not in self.total_calc:
            self.total_calc[member] = {}
        if typ == "lent":
            if member in self.lent_members:
                self.lent_members[member] += amount
            else:
                self.lent_members[member] = amount

        elif typ == "receive":
            if member in self.receive_members:
                self.receive_members[member] += amount
            else:
                self.receive_members[member] = amount
        

def calculate_members():
    pass

if __name__ == "__main__":
    member = Member()
    member.lent_members = {"mim":100, "ali":200}
    member.receive_members = {"mim":200}
