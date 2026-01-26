# nexus_pipeline.py

from abc import ABC, abstractmethod
from typing import Any, List, Dict, Union, Optional, Protocol


# Stage Protocol
class StageProtocol(Protocol):
    def process(self, data: Any) -> Any:
        ...


# Base class for pipelines
class ProcessingPipeline(ABC):
    def __init__(self, pipeline_id: str) -> None:
        self.pipeline_id: str = pipeline_id
        self.stages: List[StageProtocol] = []
        self.stats: Dict[str, int] = {"stages_executed": 0}

    def add_stage(self, stage: StageProtocol) -> None:
        self.stages.append(stage)

    def run_stages(self, data: Any) -> Any:
        """Execute all stages in order, tracking stats."""
        current: Any = data
        for stage in self.stages:
            current = stage.process(current)
            self.stats["stages_executed"] += 1
        return current

    @abstractmethod
    def process(self, data: Any) -> Union[str, Any]:
        pass


# Stage classes
class InputStage:
    def process(self, data: Any) -> Any:
        if data is None:
            raise ValueError("InputStage: data is None")
        print("Stage 1: Input validation and parsing")
        return data


class TransformStage:
    def process(self, data: Any) -> Any:
        print("Stage 2: Data transformation and enrichment")
        if isinstance(data, dict):
            data["metadata"] = "validated"
        return data


class OutputStage:
    def process(self, data: Any) -> Any:
        print("Stage 3: Output formatting and delivery")
        return data


# Pipeline adapters
class JSONAdapter(ProcessingPipeline):
    def process(self, data: Any) -> Union[str, Any]:
        print(f"Processing JSON data through pipeline {self.pipeline_id}...")
        try:
            result: Any = self.run_stages(data)
            return f"Processed JSON data: {result}"
        except Exception as e:
            return f"JSONAdapter Error: {e}"


class CSVAdapter(ProcessingPipeline):
    def process(self, data: Any) -> Union[str, Any]:
        print(f"Processing CSV data through pipeline {self.pipeline_id}...")
        try:
            result: Any = self.run_stages(data)
            return f"Processed CSV data: {result}"
        except Exception as e:
            return f"CSVAdapter Error: {e}"


class StreamAdapter(ProcessingPipeline):
    def process(self, data: Any) -> Union[str, Any]:
        print(f"Processing Stream data through pipeline {self.pipeline_id}...")
        try:
            result: Any = self.run_stages(data)
            return f"Processed Stream data: {result}"
        except Exception as e:
            return f"StreamAdapter Error: {e}"


# Nexus manager
class NexusManager:
    def __init__(self) -> None:
        self.pipelines: List[ProcessingPipeline] = []

    def register_pipeline(self, pipeline: ProcessingPipeline) -> None:
        self.pipelines.append(pipeline)

    def execute_all(self, data: Any) -> None:
        for pipeline in self.pipelines:
            output: Union[str, Any] = pipeline.process(data)
            print(output)


# Main execution
if __name__ == "__main__":
    print("=== CODE NEXUS - ENTERPRISE PIPELINE SYSTEM ===\n")

    manager = NexusManager()

    # Create pipelines
    json_pipeline = JSONAdapter("JSON_01")
    csv_pipeline = CSVAdapter("CSV_01")
    stream_pipeline = StreamAdapter("STREAM_01")

    # Add stages and register pipelines
    for pipeline in [json_pipeline, csv_pipeline, stream_pipeline]:
        pipeline.add_stage(InputStage())
        pipeline.add_stage(TransformStage())
        pipeline.add_stage(OutputStage())
        manager.register_pipeline(pipeline)

    print("\n=== Multi-Format Data Processing ===\n")

    manager.execute_all({"sensor": "temp", "value": 23.5})
    # manager.execute_all("user,action,timestamp")
    # manager.execute_all(["stream", "data", "values"])

    print("\n=== Pipeline Chaining Demo ===")
    chained_output: Union[str, Any] = json_pipeline.process({"raw": "data"})
    final_output: Union[str, Any] = csv_pipeline.process(chained_output)
    print("Chain result:", final_output)

    print("\n=== Error Recovery Test ===")
    print(stream_pipeline.process(None))

    print("\nNexus Integration complete. All systems operational.")
