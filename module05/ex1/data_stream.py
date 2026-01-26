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

        exce
