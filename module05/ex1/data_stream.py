from abc import ABC, abstractmethod
from typing import Any, List, Dict, Union, Optional


# Abstract Base Stream

class DataStream(ABC):
    def __init__(self, stream_id: str) -> None:
        self.stream_id: str = stream_id
        self.processed_batches: int = 0

    @abstractmethod
    def process_batch(self, data_batch: List[Any]) -> str:
        pass

    def filter_data(
        self,
        data_batch,
        criteria = None
    ) -> List[Any]:
        # Default behavior: no filtering
        return data_batch

    def get_stats(self) -> Dict[str, Union[str, int, float]]:
        return {
            "stream_id": self.stream_id,
            "processed_batches": self.processed_batches
        }


# Sensor Stream

class SensorStream(DataStream):
    def process_batch(self, data_batch: List[Any]) -> str:
        try:
            temps = [
                item["temp"] for item in data_batch
                if isinstance(item, dict) and "temp" in item
            ]

            if not temps:
                raise ValueError("No temperature data")

            self.processed_batches += 1
            avg_temp: float = sum(temps) / len(temps)

            return (
                f"Sensor analysis: {len(temps)} readings processed, "
                f"avg temp: {avg_temp:.1f}°C"
            )

        except Exception as e:
            return f"Sensor processing error: {e}"

    def filter_data(
        self,
        data_batch: List[Any],
        criteria: Optional[str] = None
    ) -> List[Any]:
        if criteria == "high":
            return [
                item for item in data_batch
                if isinstance(item, dict)
                and item.get("temp", 0) > 30
            ]
        return data_batch


# =========================
# Transaction Stream
# =========================

class TransactionStream(DataStream):
    def process_batch(self, data_batch: List[Any]) -> str:
        try:
            net_flow: int = 0

            for item in data_batch:
                if isinstance(item, dict):
                    if "buy" in item:
                        net_flow -= item["buy"]
                    elif "sell" in item:
                        net_flow += item["sell"]

            self.processed_batches += 1

            sign: str = "+" if net_flow >= 0 else ""
            return (
                f"Transaction analysis: {len(data_batch)} operations, "
                f"net flow: {sign}{net_flow} units"
            )

        except Exception as e:
            return f"Transaction processing error: {e}"

    def filter_data(
        self,
        data_batch: List[Any],
        criteria: Optional[str] = None
    ) -> List[Any]:
        if criteria == "large":
            return [
                item for item in data_batch
                if isinstance(item, dict)
                and list(item.values())[0] > 100
            ]
        return data_batch


# =========================
# Event Stream
# =========================

class EventStream(DataStream):
    def process_batch(self, data_batch: List[Any]) -> str:
        try:
            errors: int = len([
                event for event in data_batch
                if isinstance(event, str) and event == "error"
            ])

            self.processed_batches += 1

            return (
                f"Event analysis: {len(data_batch)} events, "
                f"{errors} error detected"
            )

        except Exception as e:
            return f"Event processing error: {e}"

    def filter_data(
        self,
        data_batch: List[Any],
        criteria: Optional[str] = None
    ) -> List[Any]:
        if criteria == "critical":
            return [
                event for event in data_batch
                if event == "error"
            ]
        return data_batch


# =========================
# Stream Processor
# =========================

class StreamProcessor:
    def __init__(self) -> None:
        self.streams: List[DataStream] = []

    def add_stream(self, stream: DataStream) -> None:
        if not isinstance(stream, DataStream):
            raise TypeError("Invalid stream type")
        self.streams.append(stream)

    def process_all(self, batches: List[List[Any]]) -> None:
        for stream, batch in zip(self.streams, batches):
            result: str = stream.process_batch(batch)
            print("-", result)


# =========================
# Demo / Main
# =========================

if __name__ == "__main__":
    print("=== CODE NEXUS - POLYMORPHIC STREAM SYSTEM ===\n")

    sensor_stream = SensorStream("SENSOR_001")
    transaction_stream = TransactionStream("TRANS_001")
    event_stream = EventStream("EVENT_001")

    print("Initializing Sensor Stream...")
    print("Stream ID:", sensor_stream.stream_id, ", Type: Environmental Data")
    print(sensor_stream.process_batch([
        {"temp": 22.5, "humidity": 65, "pressure": 1013}
    ]))
    print()

    print("Initializing Transaction Stream...")
    print("Stream ID:", transaction_stream.stream_id, ", Type: Financial Data")
    print(transaction_stream.process_batch([
        {"buy": 100}, {"sell": 150}, {"buy": 75}
    ]))
    print()

    print("Initializing Event Stream...")
    print("Stream ID:", event_stream.stream_id, ", Type: System Events")
    print(event_stream.process_batch([
        "login", "error", "logout"
    ]))
    print()

    print("=== Polymorphic Stream Processing ===")
    processor = StreamProcessor()
    processor.add_stream(sensor_stream)
    processor.add_stream(transaction_stream)
    processor.add_stream(event_stream)

    print("Processing mixed stream types through unified interface...")
    processor.process_all([
        [{"temp": 35.0}, {"temp": 20.0}],
        [{"sell": 200}, {"buy": 50}, {"sell": 25}, {"buy": 150}],
        ["login", "error", "error"]
    ])

    print("\nAll streams processed successfully. Nexus throughput optimal.")
