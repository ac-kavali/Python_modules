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



