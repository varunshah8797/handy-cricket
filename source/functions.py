
#Display winner name
def display_winner(winner_flag,field,cv2,font):
    if winner_flag==0:
        cv2.putText(field, "Draw", (500, 550), font, 1.2, (0,128,255), 2, cv2.LINE_AA)

    elif winner_flag==1:
        cv2.putText(field, "Winner: User", (495, 550), font, 1.2, (0,128,255), 2, cv2.LINE_AA)

    elif winner_flag==2:
        cv2.putText(field, "Winner: Computer", (455, 550), font, 1.2, (0,128,255), 2, cv2.LINE_AA)

        
def display_out(field,cv2,font):
    cv2.putText(field, "User: OUT!!", (550, 400), font, 1.2, (0,0,255), 2, cv2.LINE_AA)

#Calculate and Update score
def calculate_score(move1, move2,total_run):

    if move1 == move2:
        return "OUT"
    else:       
        return str(total_run+int(move1))



CLASS_REV_MAP = {
    0: "1",
    1: "2",
    2: "3",
    3: "4",
    4: "5",
    5: "6",
    6: "7",
    7: "8",
    8: "9",
    9: "10",
    10: "None"
}
    
def mapper(index):
    return CLASS_REV_MAP[index]
