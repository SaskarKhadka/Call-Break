from game import CallBreak
       
users = []
is_game_over = False
game = CallBreak()
 
game.get_users()
 
for round in range(1, 6):
    print(f"Round {round}")
    if round == 5:
        game.calculate_initial_total()
       
    # get lekheko haat
    lekheko_hat = game.get_lekheko_haat(round)
    total_nine = False
    if sum(lekheko_hat) == 9 and round != 5:
        # add .1 and continue to next round
        print("\nThe total bid this round is 9. So 1 otti is added to each player")
        total_nine = True
       
    #get khako haat
    khako_hat = game.get_khako_haat(total_nine)
 
    # calculate total for this round
    total_score_in_this_round : list = game.evaluate_total_this_round()
 
    game.add_data(total_score_in_this_round[0])
    if total_score_in_this_round[1]:
            game.game_over_by_8_haat()
            break
       
game.calculate_final_total()
game.game_over()
   
       
# scores = input("Enter scores for this round")
