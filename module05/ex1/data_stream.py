from abc import ABC, abstractmethod
from typing import Any, List, Dict, Union, Optional


# =====================
# Abstract Base Class
# =====================

class DataStream(ABC):
    def __init__(self, stream_id: str) -> None:
        self.stream_id = stream_id
        self.batches = 0

    @abstractmethod
    def process_batch(self, data_batch: List[Any]) -> str:
        pass

    def filter_data(
        self,
        data_batch: List[Any],
        criteria: Optional[str] = None
    ) -> List[Any]:
        return data_batch

    def get_stats(self) -> Dict[str, Union[str, int]]:
        return {
            "stream_id": self.stream_id,
            "batches": self.batches
        }


# =====================
# Sensor Stream
# =====================

class SensorStream(DataStream):
    def process_batch(self, data_batch: List[Any]) -> str:
        try:
            total_temp = 0.0
            count = 0

            for item in data_batch:
                if isinstance(item, dict):
                    if "temp" in item:
                        total_temp = total_temp + item["temp"]
                        count = count + 1

            if count == 0:
                raise ValueError("No sensor data")

            self.batches = self.batches + 1
            avg_temp = total_temp / count

            return (
                "Sensor analysis: "
                + str(count)
                + " readings processed, avg temp: "
                + str(round(avg_temp, 1))
                + "°C"
            )

        except Exception as e:
            return "Sensor error: " + str(e)


# =====================
# Transaction Stream
# =====================

class TransactionStream(DataStream):
    def process_batch(self, data_batch: List[Any]) -> str:
        try:
            net = 0

            for item in data_batch:
                if isinstance(item, dict):
                    if "buy" in item:
                        net = net - item["buy"]
                    elif "sell" in item:
                        net = net + item["sell"]

            self.batches = self.batches + 1

            return (
                "Transaction analysis: "
                + str(len(data_batch))
                + " operations, net flow: "
                + str(net)
            )

        except Exception as e:
            return "Transaction error: " + str(e)


# =====================
# Event Stream
# =====================

class EventStream(DataStream):
    def process_batch(self, data_batch: List[Any]) -> str:
        try:
            errors = 0

            for event in data_batch:
                if event == "error":
                    errors = errors + 1

            self.batches = self.batches + 1

            return (
                "Event analysis: "
                + str(len(data_batch))
                + " events, "
                + str(errors)
                + " error detected"
            )

        except Exception as e:
            return "Event error: " + str(e)


# =====================
# Stream Processor
# =====================

class StreamProcessor:
    def __init__(self) -> None:
        self.streams = []

    def add_stream(self, stream: DataStream) -> None:
        self.streams.append(stream)

    def process_all(self, batches: List[List[Any]]) -> None:
        for i in range(len(self.streams)):
            result = self.streams[i].process_batch(batches[i])
            print(result)


# =====================
# Main
# =====================

if __name__ == "__main__":
    print("=== SIMPLE POLYMORPHIC STREAM SYSTEM ===\n")

    sensor = SensorStream("SENSOR_001")
    transaction = TransactionStream("TRANS_001")
    event = EventStream("EVENT_001")

    processor = StreamProcessor()
    processor.add_stream(sensor)
    processor.add_stream(transaction)
    processor.add_stream(event)

    processor.process_all([
        [{"temp": 22.5}, {"temp": 25.0}],
        [{"buy": 100}, {"sell": 150}],
        ["login", "error", "logout"]
    ])
