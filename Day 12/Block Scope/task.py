game_level = 3
enemies = ["Skeleton","Zombie","ALien" ]
def create_enemy():
    new_enemy = 0

    if game_level < 5:
        new_enemy = enemies[0]

    print(new_enemy)