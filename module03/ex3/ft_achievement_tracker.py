print("=== Achievement Tracker System ===\n")

alice = {"first_kill",
         "level_10",
         "treasure_hunter",
         "speed_demon",
         "first_kill"}

bob = {"first_kill",
       "level_10",
       "boss_slayer",
       "collector"}

charlie = {"level_10",
           "treasure_hunter",
           "boss_slayer",
           "speed_demon",
           "perfectionist"}

print("Player alice achievements:", alice)
print("Player bob achievements:", bob)
print("Player charlie achievements:", charlie)

print("\n=== Achievement Analytics ===")

# All unique achievements
all_achievements = alice.union(bob).union(charlie)
print("All unique achievements:", all_achievements)
print("Total unique achievements:", len(all_achievements))

# Common to all players
common_all = alice.intersection(bob).intersection(charlie)
print("\nCommon to all players:", common_all)

# Achievements shared by at least two players
shared_any = (
    alice.intersection(bob)
    .union(alice.intersection(charlie))
    .union(bob.intersection(charlie))
)

# Rare achievements (owned by only one player)
rare = all_achievements.difference(shared_any)
print("Rare achievements (1 player):", rare)

# Player comparisons
print("\nAlice vs Bob common:", alice.intersection(bob))
print("Alice vs bob unique:", alice.difference(bob))
print("charlie vs alice unique:", bob.difference(alice))
