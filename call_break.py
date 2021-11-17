import pandas as pd
 
class CallBreak:
    def __init__(self) -> None:
        self.users = []
        self.df = None
        self.lekheko_hat = None
        self.khako_hat = None
        self.round = 1
       
   
    def get_users(self):
        users = input("Enter users(in order): ")
        self.users = users.split(" ")
        game_data = {
            "index": [0, 1, 2, 3],
            "user": self.users,
        }
        self.df = pd.DataFrame(game_data)
       
    def get_lekheko_haat(self, round):
        self.round = round
        lekheko_hat = []
        print("\nEnter your expected hands for this round.")
        ordered_players = [self.users[self.round % 4], self.users[(self.round + 1) % 4], self.users[(self.round + 2) % 4], self.users[(self.round + 3) % 4]]
        while True:
            try:
                lekheko_hat = [int(input(f"{player}: ")) for player in ordered_players]
            except ValueError:
                continue
            proceed = input("Do you wish to proceed(y/n): ")
            if proceed == "y":
                total = sum(lekheko_hat)
                if total < 9:
                    print("Please raise the bid..\n")
                    continue
                else:
                    self.lekheko_hat = lekheko_hat
                    return self.lekheko_hat
               
    def get_khako_haat(self, total_nine):
        if total_nine:
            self.khako_hat = [haat + 1 for haat in self.lekheko_hat]
            return self.khako_hat
       
        print("Enter your final hands for this round")
        ordered_players = [self.users[self.round % 4], self.users[(self.round + 1) % 4], self.users[(self.round + 2) % 4], self.users[(self.round + 3) % 4]]
        while True:
            try:
                khako_hat = [int(input(f"{player}: ")) for player in ordered_players]
            except ValueError:
                continue
            if sum(khako_hat) == 13:
                next_round = input("Do you wish to continue(y/n): ")
                if next_round == "y":
                    self.khako_hat = khako_hat
                    return khako_hat
               
           
    def evaluate_total_this_round(self):
        total_score = [0, 0, 0, 0]
        for each in range(0, 4):
            if int(self.lekheko_hat[each]) == int(self.khako_hat[each]):
                # total_score.append(str(float(self.lekheko_hat[each])))
                total_score[(self.round + each) % 4] = str(float(self.lekheko_hat[each]))
            elif int(self.lekheko_hat[each]) > int(self.khako_hat[each]):
                # total_score.append(str(float(self.lekheko_hat[each]) * -1))
                total_score[(self.round + each) % 4] = str(float(self.lekheko_hat[each]) * -1)
            else:
                score = float(int(self.lekheko_hat[each]) + (int(self.khako_hat[each]) - int(self.lekheko_hat[each])) * 0.1)
                # total_score.append(str(float(score)))
                total_score[(self.round + each) % 4] = str(float(score))
               
            if int(self.lekheko_hat[each])>= 8 and int(self.khako_hat[each]) >= 8:
                return [total_score, True]
                # print("Game Over")
        return [total_score, False]
       
    def add_data(self, total_score_in_this_round):
        self.df[f"round{self.round}"] = pd.Series(total_score_in_this_round)
        self.df.to_csv("game_data.csv", index=False)
        print(f"\n{self.df}\n")
       
    def game_over_by_8_haat(self):
        current_round = f"round{self.round}"
        winner_row = self.df[self.df[current_round] >= 8]
        print(f"\n\n{winner_row.user[0]} is the winner")
   
    def calculate_initial_total(self):
        initial_total = []
        # data = pd.read_csv("game_data.csv")
        for index, row in self.df.iterrows():
            one = row.round1.split(".")
            two = row.round2.split(".")
            three = row.round3.split(".")
            four = row.round4.split(".")
            total_int_part = int(one[0]) + int(two[0]) + int(three[0]) + int(four[0])
            total_float_part = int(one[1]) + int(two[1]) + int(three[1]) + int(four[1])
            total = str(total_int_part) + "." + str(total_float_part)
            initial_total.append(total)
        self.df["initial_total"] = pd.Series(initial_total)
        print(self.df)
       
    def calculate_final_total(self):
        final_total = []
        for index, row in self.df.iterrows():
            initial_total = row["initial_total"].split(".")
            final_round = row.round5.split(".")
            total_int_part = int(initial_total[0]) + int(final_round[0])
            total_float_part = int(initial_total[1]) + int(final_round[1])
            total = str(total_int_part) + "." + str(total_float_part)
            final_total.append(total)
        self.df["total"] = pd.Series(final_total)
        print(f"\n{self.df}")
       
    def game_over(self):
        total_scores = self.df.total.to_list()
        total_scores_num = [float(score) for score in total_scores]
        total_scores_num.sort()
        total_scores_num.reverse()
        winner = self.df[self.df["total"] == str(total_scores_num[0])]
        second_place = self.df[self.df["total"] == str(total_scores_num[1])]
        third_place = self.df[self.df["total"] == str(total_scores_num[2])]
        fourth_place = self.df[self.df["total"] == str(total_scores_num[3])]
        print(f"\n\n{winner['user']} is the winner")
        print(f"{second_place['user']} pays 10")
        print(f"{third_place['user']} pays 15")
        print(f"{fourth_place['user']} pays 20")
   
       
       
   
