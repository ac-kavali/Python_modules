from abc import ABC, abstractmethod
from typing import Any, List


class DataProcessor(ABC):
    @abstractmethod
    def process(self, data: Any) -> str:
        pass

    @abstractmethod
    def validate(self, data: Any) -> bool:
        pass

    def format_output(self, result: str) -> str:
        return f"Output: {result}"


class NumericProcessor(DataProcessor):
    def process(self, data: Any) -> str:
        if not self.validate(data):
            raise ValueError("Invalid numeric data")

        try:
            total = sum(data)
            count = len(data)
        except TypeError:
            total = data
            count = 1

        avg = total / count
        return (
            f"Processed {count} numeric values, "
            f"sum={total}, avg={avg}"
        )

    def validate(self, data: Any) -> bool:
        try:
            _ = data + 0
            return True
        except TypeError:
            try:
                sum(data)
                return True
            except TypeError:
                return False


class TextProcessor(DataProcessor):
    def process(self, data: Any) -> str:
        if not self.validate(data):
            raise ValueError("Invalid text data")

        char_count = len(data)
        word_count = len(data.split())
        return (
            f"Processed text: {char_count} characters, "
            f"{word_count} words"
        )

    def validate(self, data: Any) -> bool:
        try:
            data.split()
            return True
        except AttributeError:
            return False


class LogProcessor(DataProcessor):
    def process(self, data: Any) -> str:
        if not self.validate(data):
            raise ValueError("Invalid log entry")

        level, message = data.split(":", 1)
        level = level.strip()
        message = message.strip()

        return f"[{level}] {level} level detected: {message}"

    def validate(self, data: Any) -> bool:
        try:
            data.split(":", 1)
            return True
        except AttributeError:
            return False


def main() -> None:
    print("=== CODE NEXUS - DATA PROCESSOR FOUNDATION ===")

    processors: List[DataProcessor] = [
        NumericProcessor(),
        TextProcessor(),
        LogProcessor(),
    ]

    samples: List[Any] = [
        [1, 2, 3, 4, 5],
        "Hello Nexus World",
        "ERROR: Connection timeout",
    ]

    names = ["Numeric", "Text", "Log"]

    for name, processor, data in zip(names, processors, samples):
        print(f"\nInitializing {name} Processor...")
        print(f"Processing data: {data}")

        try:
            result = processor.process(data)
            print("Validation: Data verified")
            print(processor.format_output(result))
        except Exception as exc:
            print(f"Error: {exc}")

    print("\n=== Polymorphic Processing Demo ===")
    print("Processing multiple data types through same interface...")

    for i, processor in enumerate(processors, start=1):
        result = processor.process(samples[i - 1])
        print(f"Result {i}: {result}")

    print("\nFoundation systems online. Nexus ready for advanced streams.")


if __name__ == "__main__":
    main()
