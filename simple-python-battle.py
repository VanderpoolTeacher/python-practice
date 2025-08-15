player_name = input("Enter your name:")
print(f"Welcome {player_name}! Let's get ready to rumble!")

player_health = 100
boss_health = 150

# Fight loop

while player_health > 0 and boss_health > 0:
    print(f"Player health: {player_health} | Boss health: {boss_health}")

    action = input("Type 'attack' to hit the boss.").lower()

    if action == "attack":
        boss_health -= 200
        print("You hit the boss!")
    else:
        print("You hesitate...")

    if boss_health > 0:
        player_health -= 15
        print("The boss hits back!")

if player_health <= 0:
    print(f"You lose, good day, you get nothing!")
elif boss_health <= 0:
    print(f"You win. You are awesome!")