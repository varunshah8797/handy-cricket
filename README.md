# Handy Cricket :cricket_game:

## Introduction
Howzattt!! Remember the school days when everyone would gather around in recess time and team up to throw hands at each other (no karate-kid here). From cheering on the half-century and century to arguing on getting out to nail-bitting clutches. The game gave us a lot of good memories.
This repo indeed does contain the virtual version of the great Game. The game was made using powers of Open-CV and Keras library. The game would be played between you and the computer. So get scoring and winning big!

## Rules of the Game :clipboard:
The rules are simple as followed:
- There are 10 available hand signs which you can choose to play your move (Check out demo images to learn hand signs :point_up_2:)
- Each hand sign is assigned to a unique score ranging from 1-10
- The game starts with user at the batting side.
- Batting score increases if user and computer select different signs
- However, if user and computer selects the same sign it results in getting out and end of innings for the batsmen
- To win, its simple you just have to score higher than computer (Not that simple :grimacing:)
- Equal scores would result in a Draw

## How to Play the Game :video_game:
- Download the repo in your local
- Run the handy_play.py with webcam enabled laptop/PC
- Show your hand sign in the user space
- Press 'n' to register your move
- Score big and beat the Computer

## Technical Stuff :man_technologist:
### Generating the Dataset
- Create a imageData folder just like we created here
- Update the handy_generate.py with your label of the data you are generating
- Also, update the number of images you want to capture of the selected label
- Run the code
- Press 'a' to start capturing, number of images captured would be displayed
- Repeat the above steps for each label you want to train the data with

### Augmenting the Dataset
- To make the model generalized and be able to work in any environment, we augment the images using basic image preprocessing
- Set rotation, zoom, flip etc according to your liking in handy_augment.py
- Create a preview folder inside the label 
- Run the code in a particular label folder
- Cut/Paste the images from preview folder into main label folder

### Training the Model
- We choose to use Squeezenet from keras library to train our image classification model
- Read more about Squeezenet at https://towardsdatascience.com/review-squeezenet-image-classification-e7414825581a
- Update the handy_train.py with your number of epochs based on size of your dataset
- Run the code
- Save the model for future use

### User Interface 
- handy_play.py is where all the magic happens
- We used open_CV to capture user hand movements using webcam, to create a display screen to show user, computer score and most importantly the winner
- Check out the comments to get more idea here

# If you played the game and it brought the memories back, do leave us a :star2: on this repository so that it reaches more people

## Possible Enhancements
- Apply weighted choice on computer selection so that it limits user to score higher number, making the game more challenging
- Use reinforcement learning to predict the computer move
- Convert the code to a full-fledged application
