numOfStudent=int(input("Number of students:\n"))
numOfTeam=int(input("Number of teams:\n"))

rem=int(numOfStudent%numOfTeam);
quo=int(numOfStudent/numOfTeam);

print(f"The number of students in each team, left out is ({quo},{rem})")