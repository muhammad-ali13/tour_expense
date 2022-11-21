
class Member:
    def __init__(self, name: str) -> None:
        self.name = name
        self.given: dict(Member, float) = {}
        

if __name__ == "__main__":
    member1 = Member("mim")
    member2 = Member("sezan")
    member3 = Member("ali")
    member1.given[member2] = 100.0 # member1 to member2
    member2.given[member1] = 200.0 # member2 to member1
    member2.given[member3] = 300.0 # member2 to member3
    member3.given[member1] = 100.0
    member1.given[member3] = 200.0
    members = [member1, member2, member3]
    for member in members:
        name = member.name
        for k_member in list(member.given.keys()):
            if member in k_member.given:
                due = member.given[k_member] - k_member.given[member]
            else:
                due = member.given[k_member]
            if due > 0:
                print(f'{name} will get {due} from {k_member.name}')
            elif due < 0:
                print(f'{name} will return {abs(due)} to {k_member.name}')
            else:
                pass
