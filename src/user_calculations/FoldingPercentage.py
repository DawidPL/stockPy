from typing import List


class FoldingPercentage:

    @staticmethod
    def folding_percentage(start_value: float, return_rate: float, time_period: int) -> List[float]:
        folding_percentage_list: List[float] = []
        n: int = 0
        while n != time_period:
            if not n:
                x: float = round(start_value + (start_value * (return_rate/100)), 2)
                folding_percentage_list.append(x)
                n += 1
            y: float = round(folding_percentage_list[n-1] + (folding_percentage_list[n-1] * (return_rate/100)), 2)
            folding_percentage_list.append(y)
            n += 1
        return folding_percentage_list


folding_percentage = FoldingPercentage()
