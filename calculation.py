
class Member:
    def __init__(self, name: str) -> None:
        self.name = name
        self.given: list[dict(Member, float)] = []
        

if __name__ == "__main__":
    member1 = Member("mim")
    member2 = Member("sezan")
    member1.given.append({member2:100.0})
    member2.given.append({member1:200.0})
    print(member1.given)
    print(member2.given)
