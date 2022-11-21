import pandas as pd
class Member:
    def __init__(self, name: str) -> None:
        self.name = name
        self.given: dict(Member, float) = {}
        

if __name__ == "__main__":
    csv_file = "/src/tour_cost.csv"
    member_col_idx_start = 4
    member_col_idx_end = 12
    paid_name_column_name = 'who'
    df = pd.read_csv(csv_file)
    columns = df.columns

    members = {member_name:Member(member_name) for member_name in columns[member_col_idx_start:member_col_idx_end + 1]}
    for member_name in columns[member_col_idx_start:member_col_idx_end + 1]:
        for received_member in members.values():
                    members[member_name].given[received_member] = 0

    for index, row in df.iterrows():
        indiv_amount = row['how much'] / row['total number']
        for received_member in members.values():
            flag = 1 if row['ALL'] else row[received_member.name]
            members[row['who']].given[received_member] += indiv_amount * flag
    for name in list(members.keys()):
        member = members[name]
        for k_member in list(member.given.keys()):

            due = member.given[k_member] - k_member.given[member]
            
            if abs(due) > 0:
                print(f'{name} will get {due} from {k_member.name}')
