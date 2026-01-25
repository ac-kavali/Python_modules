from abc import ABC, abstractmethod
from typing import Any, List, Dict, Union, Optional

#The Core Class of abstracting Methods
class DataProcessor(ABC):
    @abstractmethod
    def process(self, data: Any) -> str:
        pass

    @abstractmethod
    def validate(self, data: Any) -> bool:
        pass

    def format_output(self, result: str) -> str:
        return f"Output: {result}"

# process numeric data
class NumericProcessor(DataProcessor):
    def process(self, data: Any) -> str:
        if not self.validate(data):
            raise ValueError("Invalid numeric data")

        if isinstance(data, list):
            total = sum(data)
            count = len(data)
        else:
            total = data
            count = 1

        avg = total / count
        return (
            f"Processed {count} numeric values, "
            f"sum={total}, avg={avg}"
        )

    def validate(self, data: Any) -> bool:
        if isinstance(data, list):
            return all(isinstance(x, (int, float)) for x in data)
        return isinstance(data, (int, float))


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
        return isinstance(data, str)


class LogProcessor(DataProcessor):
    def process(self, data: Any) -> str:
        if not self.validate(data):
            raise ValueError("Invalid log entry")

        level, message = data.split(":", 1)
        level = level.strip()
        message = message.strip()

        return f"[{level}] {level} level detected: {message}"

    def validate(self, data: Any) -> bool:
        if not isinstance(data, str):
            return False
        return ":" in data


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
