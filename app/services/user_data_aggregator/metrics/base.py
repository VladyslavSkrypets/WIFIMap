from abc import ABC, abstractmethod

import pandas as pd


class MetricInterface(ABC):
    def __init__(self, aggregated_model) -> None:
        self.aggregated_model = aggregated_model
    
    @abstractmethod
    def calculate(self, calculated_dataframe: pd.DataFrame) -> None:
        pass
