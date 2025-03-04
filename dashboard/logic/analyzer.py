from typing import TypedDict, Optional
from typing_extensions import Unpack
import datetime

class FilterParams(TypedDict):
    region: Optional[str]
    question_group: Optional[str]
    period: Optional[tuple[datetime.datetime, datetime.datetime]]

class Analyzer:
    """Data processing class. Loads data and gives metrics"""

    data: list

    def _filter_data(self, **filters: Unpack[FilterParams]) -> list:
        region = filters.get('region')
        question_group = filters.get('question_group')
        period = filters.get('period')

        if region is not None and question_group is not None:
            return [1, 4, 8, 8]
        if region is not None:
            return [8, 800, 555, 35, 35]
        if question_group is not None:
            return [42, 42, 42]
        return self.data
    

    def load(self, f: str):
        self.data = [0, 1, 2, 3, 4, 5]

    def context_recall(self, **filters: Unpack[FilterParams]):
        data = self._filter_data(**filters)

        return 0.3 + len(data) * 0.1
    
    def context_precision(self, **filters: Unpack[FilterParams]):
        data = self._filter_data(**filters)

        return 0.43 - len(data) * 0.02
    
    def answer_correctness_literal(self, **filters: Unpack[FilterParams]):
        data = self._filter_data(**filters)

        return 0.23 + 0.01 * data[0]
    
    def answer_correctness_neural(self, **filters: Unpack[FilterParams]):
        data = self._filter_data(**filters)

        return 0.1 + data[1]%2 * 0.1
    
    def regions_frequency(self, **filters: Unpack[FilterParams]):
        data = self._filter_data(**filters)

        return {
            'Нижний Новгород': 1070 + len(data) * 2,
                     'Москва': 6025 - len(data * 2),  
        }
    
    def question_groups_frequency(self, **filters: Unpack[FilterParams]):
        data = self._filter_data(**filters)
        
        return {
                       'Закон': 2027,
            'Внеучебная жизнь': 1800,
        }

    def average_time_and_delta(self, **filters: Unpack[FilterParams]):
        data = self._filter_data(**filters)

        return 1.5, -0.1
    
    def like_fraction(self, **filters: Unpack[FilterParams]):
        data = self._filter_data(**filters)

        return 0.8
    
    def asked_second_time_fraction(self, **filters: Unpack[FilterParams]):
        data = self._filter_data(**filters)
        
        return 0.2

    
    def available_regions(self):
        return ["Москва", "Нижний Новгород"]
    
    def available_question_groups(self):
        return ["Закон", "Внеучебная жизнь"]
    