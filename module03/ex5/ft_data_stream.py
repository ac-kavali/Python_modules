import time


def game_event_generator(total_events):
    """Yield game events one by one."""
    players = ["alice", "bob", "charlie", "dave", "eve"]
    actions = ["killed monster", "found treasure", "leveled up"]
    for i in range(1, total_events + 1):
        player = players[i % len(players)]
        level = i % 20 + 1
        action = actions[i % len(actions)]
        yield f"Event {i}: Player {player} (level {level}) {action}"


def fibonacci_generator(n):
    """Yield first n Fibonacci numbers."""
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b


def prime_generator(n):
    """Yield first n prime numbers."""
    count = 0
    num = 2
    while count < n:
        is_prime = True
        for i in range(2, num):
            if num % i == 0:
                is_prime = False
                break
        if is_prime:
            yield num
            count += 1
        num += 1


# === Main program ===

def main():
    print("=== Game Data Stream Processor ===")
    total_events = 1000
    print(f"Processing {total_events} game events...")

    # Stats
    high_level_players = 0
    treasure_events = 0
    level_up_events = 0

    start_time = time.time()

    # Process events
    for event_number, event in zip(range(1, total_events + 1),
                                   game_event_generator(total_events)):
        print(event)

        # Simple analytics
        if "level" in event:
            level_str = event.split("level ")[1].split(")")[0]
            level = int(level_str)
            if level >= 10:
                high_level_players += 1
        if "treasure" in event:
            treasure_events += 1
        if "leveled up" in event:
            level_up_events += 1

    elapsed_time = time.time() - start_time

    print("\n=== Stream Analytics ===")
    print(f"Total events processed: {total_events}")
    print(f"High-level players (10+): {high_level_players}")
    print(f"Treasure events: {treasure_events}")
    print(f"Level-up events: {level_up_events}")
    print("Memory usage: Constant (streaming)")
    print(f"Processing time: {elapsed_time:.3f} seconds")

    print("\n=== Generator Demonstration ===")

    # Fibonacci sequence
    fib_gen = fibonacci_generator(10)
    print("Fibonacci sequence (first 10):", end=" ")
    first_item = True
    for num in fib_gen:
        if not first_item:
            print(",", end=" ")
        print(num, end="")
        first_item = False
    print()

    # Prime numbers
    print("Prime numbers (first 5):", end=" ")
    first_item = True
    for num in prime_generator(5):
        if not first_item:
            print(",", end=" ")
        print(num, end="")
        first_item = False
    print()


if __name__ == "__main__":
    main()
