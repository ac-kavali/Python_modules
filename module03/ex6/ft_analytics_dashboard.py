print("=== Game Analytics Dashboard ===")

# Sample Data
players = [
    ("alice", 2300, 5, "north"),
    ("bob", 1800, 3, "east"),
    ("charlie", 2150, 7, "central"),
    ("diana", 2050, 4, "north"),
]

achievements = [
    ("alice", "first_kill"),
    ("alice", "level_10"),
    ("bob", "first_kill"),
    ("charlie", "boss_slayer"),
    ("charlie", "level_10"),
    ("diana", "first_kill"),
]

# List Comprehensions
print("=== List Comprehension Examples ===")

high_scorers = [name for name, score, _, _ in players if score > 2000]
print("High scorers (>2000):", high_scorers)

scores_doubled = [score * 2 for _, score, _, _ in players]
print("Scores doubled:", scores_doubled)

active_players = [name for name, score, _, _ in players if score >= 1800]
print("Active players:", active_players)

# Dict Comprehensions
print("\n=== Dict Comprehension Examples ===")

player_scores = {name: score for name, score, _, _ in players}
print("Player scores:", player_scores)

score_categories = {
    "high": len([1 for _, s, _, _ in players if s > 2100]),
    "medium": len([1 for _, s, _, _ in players if 1800 <= s <= 2100]),
    "low": len([1 for _, s, _, _ in players if s < 1800]),
}
print("Score categories:", score_categories)

achievement_counts = {name: ach for name, _, ach, _ in players}
print("Achievement counts:", achievement_counts)

# Set Comprehensions
print("\n=== Set Comprehension Examples ===")

unique_players = {name for name, _, _, _ in players}
print("Unique players:", unique_players)

unique_achievements = {ach for _, ach in achievements}
print("Unique achievements:", unique_achievements)

active_regions = {region for _, _, _, region in players}
print("Active regions:", active_regions)

# Combined Analysis
print("\n=== Combined Analysis ===")

total_players = len(unique_players)
print("Total players:", total_players)

total_unique_achievements = len(unique_achievements)
print("Total unique achievements:", total_unique_achievements)

average_score = sum(score for _, score, _, _ in players) / len(players)
print("Average score:", average_score)

top_score = max(score for _, score, _, _ in players)
top_player = [name for name, score, _, _ in players if score == top_score][0]
top_achievements = [
    ach for name, score, ach, _ in players if score == top_score
][0]

print(
    "Top performer:",
    top_player,
    "(",
    top_score,
    "points,",
    top_achievements,
    "achievements)",
)
