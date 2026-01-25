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
        return "Output: " + result


class NumericProcessor(DataProcessor):
    def validate(self, data: Any) -> bool:
        try:
            sum(data)
            return True
        except Exception:
            try:
                _ = data + 1
                return True
            except Exception:
                return False

    def process(self, data: Any) -> str:
        if not self.validate(data):
            return "Invalid numeric data"

        try:
            total = sum(data)
            count = len(data)
        except Exception:
            total = data
            count = 1

        avg = total / count
        return (
            "Processed " + str(count) +
            " numeric values, sum=" + str(total) +
            ", avg=" + str(avg)
        )


class TextProcessor(DataProcessor):
    def validate(self, data: Any) -> bool:
        try:
            data.split()
            return True
        except Exception:
            return False

    def process(self, data: Any) -> str:
        if not self.validate(data):
            return "Invalid text data"

        char_count = len(data)
        word_count = len(data.split())

        return (
            "Processed text: " + str(char_count) +
            " characters, " + str(word_count) + " words"
        )


class LogProcessor(DataProcessor):
    def validate(self, data: Any) -> bool:
        try:
            parts = data.split(":", 1)
            if len(parts) == 2:
                return True
            return False
        except Exception:
            return False

    def process(self, data: Any) -> str:
        if not self.validate(data):
            return "Invalid log entry"

        parts = data.split(":", 1)
        level = parts[0].strip()
        message = parts[1].strip()

        return "[" + level + "] " + level + " level detected: " + message


def main() -> None:
    print("=== CODE NEXUS - DATA PROCESSOR FOUNDATION ===")

    processors: List[DataProcessor] = [
        NumericProcessor(),
        TextProcessor(),
        LogProcessor()
    ]

    samples: List[Any] = [
        [1, 2, 3, 4, 5],
        "Hello Nexus World",
        "ERROR: Connection timeout"
    ]

    names = ["Numeric", "Text", "Log"]

    i = 0
    while i < len(processors):
        print("\nInitializing " + names[i] + " Processor...")
        print("Processing data:", samples[i])

        result = processors[i].process(samples[i])
        print("Validation complete")
        print(processors[i].format_output(result))

        i += 1

    print("\n=== Polymorphic Processing Demo ===")
    print("Processing multiple data types through same interface...")

    i = 0
    while i < len(processors):
        result = processors[i].process(samples[i])
        print("Result " + str(i + 1) + ": " + result)
        i += 1

    print("\nFoundation systems online. Nexus ready for advanced streams.")


if __name__ == "__main__":
    main()
