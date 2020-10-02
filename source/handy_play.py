import cv2
from keras.models import load_model
import numpy as np
from random import choice
from datetime import datetime
from variables import *
from functions import *


#Load model
model = load_model("handy_cricket.h5")

#Intialize video frame
cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1900)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 1080)

#def display_winner(winner_flag):
#    if winner_flag==0:
#        cv2.putText(field, "Draw", (500, 550), font, 1.2, (0,128,255), 2, cv2.LINE_AA)
#
#    elif winner_flag==1:
#        cv2.putText(field, "Winner: User", (480, 550), font, 1.2, (0,128,255), 2, cv2.LINE_AA)
#
#    elif winner_flag==2:
#        cv2.putText(field, "Winner: Computer", (455, 550), font, 1.2, (0,128,255), 2, cv2.LINE_AA)

while True:
    
    field = cv2.imread("field.png")
    ret, frame = cap.read()
    if not ret:
        continue
    frame = cv2.flip(frame,1)
    
    # user's space
    cv2.rectangle(field,(800,100), (1200,500), (255,255,255), 2)
       
    # extracting user's image
    user_frame = frame[100:500, 800:1200]
    img = cv2.cvtColor(user_frame, cv2.COLOR_BGR2RGB)
    img = cv2.resize(img, (227,227))

    # predicting the move made
    pred = model.predict_classes(np.array([img]))
    user_move = mapper(pred[0])
    
    font = cv2.FONT_HERSHEY_COMPLEX

    #Computer_batting 
    if counter%2:
        cv2.putText(field, "Computer's Batting", (465, 650), font, 1.2, (255,255,0), 2, cv2.LINE_AA)

        if total_score!="OUT":
            if user_move != "None":
                k = cv2.waitKey(10)
                if k == ord('n'):
                    computer_move = choice(['1','2','3','4','5','6','7','8','9','10'])
                        
                    total_score = calculate_score(computer_move,user_move,total_run)
                    if total_score!="OUT":
                        computer_score=int(total_score)
            else:
                computer_move = "None"
       
        else:
            computer_out=1
            total_score="0"
            
        if computer_move != "None":
            computer_emoji = cv2.imread("icons/{}.png".format(computer_move))
            computer_emoji = cv2.resize(computer_emoji,(400,400))
            field[100:500, 100:500] = computer_emoji

        
        #increasing score
        if total_score!="OUT":
            total_run=int(total_score)
        
        # displaying the information
        cv2.putText(field,"User Move: " + user_move, (840, 50), font, 1.2, (0, 255, 255),2,cv2.LINE_AA)
        cv2.putText(field, "Computer Move: " + computer_move, (65, 50), font, 1.2, (0, 255, 255), 2, cv2.LINE_AA)
        cv2.putText(field, "Computer score: " + str(computer_score), (70, 600), font, 1.2, (0, 0, 255), 2, cv2.LINE_AA)
        cv2.putText(field, "User score: " + str(user_score), (840, 600), font, 1.2, (0, 0, 255), 2, cv2.LINE_AA)
        
        if computer_score>user_score:
            winner_flag=2
            startCounter = True
            startTime = datetime.now()
            print("WINNER computer")

            total_score="0"
            computer_out=1
                     
        
        #change of innings
        if computer_out:
            if user_score>computer_score:    
                winner_flag=1
                print("WINNER USER")
            if user_score==computer_score:    
                winner_flag=0           
                print("DRAW")

            startCounter = True
            startTime = datetime.now()
            counter=counter+1
            computer_out=0
        
        
    #User_batting   
    else:
        cv2.putText(field, "User's Batting", (490, 650), font, 1.2, (255, 255, 0), 2, cv2.LINE_AA)
  
        if total_score!="OUT":
            if user_move != "None":
                k = cv2.waitKey(10)
                if k == ord('n'):
                    computer_move = choice(['1','2','3','4','5','6','7','8','9','10'])
                    total_score = calculate_score(user_move,computer_move,total_run)
                    if total_score!="OUT":
                        user_score=int(total_score)
            else:
                computer_move = "None"
        else:
            user_out=1
            startTime = datetime.now()            
            total_score="0"
                  
        if computer_move != 'None':
            computer_emoji = cv2.imread("icons/{}.png".format(computer_move))
            computer_emoji = cv2.resize(computer_emoji,(400,400))
            field[100:500, 100:500] = computer_emoji
            
        #increasing score
        if total_score!="OUT":
            total_run=int(total_score)     

        # displaying the information
        cv2.putText(field,"User Move: " + user_move, (840, 50), font, 1.2, (0, 255, 255),2,cv2.LINE_AA)
        cv2.putText(field, "Computer Move: " + computer_move, (65, 50), font, 1.2, (0, 255, 255), 2, cv2.LINE_AA)
        cv2.putText(field, "Computer score: " + str(computer_score), (70, 600), font, 1.2, (0, 0, 255), 2, cv2.LINE_AA)
        cv2.putText(field, "User score: " + str(user_score), (840, 600), font, 1.2, (0, 0, 255), 2, cv2.LINE_AA)
        
        
        
        #change of innings
        if user_out:
            
            
            if nSecond < totalSec:
                
                display_out(field,cv2,font)
#                cv2.putText(field, "User: OUT!!", (500, 250), font, 1.2, (0,128,255), 2, cv2.LINE_AA)

                timeElapsed = (datetime.now() - startTime).total_seconds()
        
                if timeElapsed >= 1:
                    nSecond += 1
                    timeElapsed = 0
                    startTime = datetime.now()
            else:
                startTime = 0.0
                timeElapsed = 0.0
                nSecond = 1
                counter=counter+1
                user_out=0
           
    if startCounter:
#        nSecond=0
        if nSecond < totalSec:
            display_winner(winner_flag,field,cv2,font)
            timeElapsed = (datetime.now() - startTime).total_seconds()
            
            if timeElapsed >= 1:
                nSecond += 1
                timeElapsed = 0
                startTime = datetime.now()
        else:
            startCounter = False
            nSecond = 1
            startTime = 0.0
            timeElapsed = 0.0
            nSecond = 1
            winner_flag = -1
            user_score=0
            computer_score=0
            
    field[100:500, 800:1200]=user_frame
   
    cv2.putText(field, "Press key 'n' for next ball" , (370, 700), font, 1.2, (255, 255, 255), 2, cv2.LINE_AA)
    cv2.imshow("Handy cricket", field)
    
    #To end the game press 'q'
    k = cv2.waitKey(10)
    if k == ord('q'):
        break
    
cap.release()
cv2.destroyAllWindows()