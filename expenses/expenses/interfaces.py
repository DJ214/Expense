from abc import ABC, abstractmethod

class ExpenseSplittingStrategy(ABC):
    @abstractmethod
    def calculate_shares(self, total_amount, participants):
        pass

class EqualExpenseSplitting(ExpenseSplittingStrategy):
    def calculate_shares(self, total_amount, participants):
        # Implement logic for equal expense splitting
        pass

class ExactExpenseSplitting(ExpenseSplittingStrategy):
    def calculate_shares(self, total_amount, participants, shares):
        # Implement logic for exact expense splitting
        pass

class PercentExpenseSplitting(ExpenseSplittingStrategy):
    def calculate_shares(self, total_amount, participants, percentages):
        # Implement logic for percent expense splitting
        pass
