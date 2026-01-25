from abc import ABC, abstractmethod
from typing import Any


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
        except:
            try:
                data + 1
                return True
            except:
                return False

    def process(self, data: Any) -> str:
        if not self.validate(data):
            return "Invalid numeric data"

        try:
            total = sum(data)
            count = len(data)
        except:         # this to handle the error of a single num, Error:this is not iterable.
            total = data
            count = 1

        avg = total / count
        return (
            "Processed " + str(count) +             # type casting because they ask to return int.
            " numeric values, sum=" + str(total) +
            ", avg=" + str(avg)
        )


class TextProcessor(DataProcessor):
    def validate(self, data: Any) -> bool:
        try:
            data.split()
            return True
        except:
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
        except:
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

    processors = [
        NumericProcessor(),
        TextProcessor(),
        LogProcessor()
    ]

    samples = [
        [1, 2, 3, 4, 5],
        "Hello Nexus World",
        "ERROR: Connection timeout"
    ]

    names = ["Numeric", "Text", "Log"]

    for i in range(3):
        print("\nInitializing " + names[i] + " Processor...")
        print("Processing data:", samples[i])

        result = processors[i].process(samples[i])
        print("Validation complete")
        print(processors[i].format_output(result))

    print("\n=== Polymorphic Processing Demo ===")
    print("Processing multiple data types through same interface...")

    for i in range(3):
        result = processors[i].process(samples[i])
        print("Result " + str(i + 1) + ": " + result)

    print("\nFoundation systems online. Nexus ready for advanced streams.")


if __name__ == "__main__":
    main()
