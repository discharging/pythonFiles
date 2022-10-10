batsman(sachin).
batsman(virat).
bowler(sachin).

all_rounder(X):- batsman(X), bowler(X).
cricketer(X):- batsman(X).
