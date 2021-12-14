from entities.budget import Budget

from repositories.budget_repository import budget_repository

class BudgetService:
    """Provides functionality for safely communication with the database repository"""

    def __init__(self, budget_repository):
        self._budget_repository = budget_repository
        self.store = None

    def get_total_fiscal_year_sales(self, store_id):
        """Retrieves the actual sales for the entire previous fiscal year"""

        self._yearly_sales =  self._budget_repository.get_sales_from_total_fiscal_year(store_id)

        return self._yearly_sales

    def get_last_year_sales_by_month(self, store_id):
        """Gets monthly sales from database"""
        sales = self._budget_repository.get_sales_by_month(3, store_id)
        return sales


    def edit_yearly_target_budget(self, new_budget, store_id):
        """Edit fiscal year targets based on user input"""
        earlier_value = self._budget_repository.check_if_values_budget(store_id)
        if earlier_value == False:
            self._budget_repository.insert_yearly_target_budget(new_budget, store_id)

        else:
            self._budget_repository.edit_yearly_target_budget(
            new_budget, store_id
        )

    def get_new_budget_for_current_fiscal(self, store_id):
        """Gets the new target for upcoming fiscal year"""

        self._new_budget = self._budget_repository.get_new_budget(store_id)
        return self._new_budget


budget_service = BudgetService(budget_repository)



