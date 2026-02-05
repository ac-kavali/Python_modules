import time
from functools import wraps


# spell_timer
def spell_timer(func: callable) -> callable:
    @wraps(func) # make the function a wrapper
    def wrapper(*args, **kwargs):
        print(f"Casting {func.__name__}...")
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"Spell completed in {end - start:.3f} seconds")
        return result

    return wrapper


# power_validator
def power_validator(min_power: int) -> callable:
    def decorator(func: callable) -> callable:
        @wraps(func)
        def wrapper(*args, **kwargs):
            power = args[2]  # ✅ correct index
            if power < min_power:
                return "Insufficient power for this spell"
            return func(*args, **kwargs)

        return wrapper

    return decorator


# retry_spell
def retry_spell(max_attempts: int) -> callable:
    def decorator(func: callable) -> callable:
        @wraps(func)
        def wrapper(*args, **kwargs):
            attempts = 0
            while attempts < max_attempts:
                try:
                    return func(*args, **kwargs)
                except Exception:
                    attempts += 1
                    print(
                        f"Spell failed, retrying... "
                        f"(attempt {attempts}/{max_attempts})"
                    )
            return f"Spell casting failed after {max_attempts} attempts"

        return wrapper

    return decorator


# MageGuild class
class MageGuild:
    @staticmethod
    def validate_mage_name(name: str) -> bool:
        return (
            len(name) >= 3
            and all(char.isalpha() or char.isspace() for char in name)
        )

    @power_validator(min_power=10)
    def cast_spell(self, spell_name: str, power: int) -> str:
        return f"Successfully cast {spell_name} with {power} power"


# TESTING
if __name__ == "__main__":
    print("Testing spell timer...")

    @spell_timer
    def fireball():
        time.sleep(0.1)
        return "Fireball cast!"

    result = fireball()
    print("Result:", result)

    print("\nTesting MageGuild...")
    print(MageGuild.validate_mage_name("Gandalf"))
    print(MageGuild.validate_mage_name("12"))

    guild = MageGuild()
    print(guild.cast_spell("Lightning", 15))
    print(guild.cast_spell("Spark", 5))
