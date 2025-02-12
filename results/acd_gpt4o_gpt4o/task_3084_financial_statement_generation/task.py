class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            '1': {
                'data': [
                    {'account': 'Revenue', 'amount': 500000},
                    {'account': 'Cost of Goods Sold', 'amount': 300000},
                    {'account': 'Operating Expenses', 'amount': 100000},
                    {'account': 'Interest Expense', 'amount': 20000},
                    {'account': 'Tax Expense', 'amount': 30000}
                ]
            },
            '2': {
                'data': [
                    {'account': 'Revenue', 'amount': 750000},
                    {'account': 'Cost of Goods Sold', 'amount': 450000},
                    {'account': 'Operating Expenses', 'amount': 150000},
                    {'account': 'Interest Expense', 'amount': 25000},
                    {'account': 'Tax Expense', 'amount': 50000}
                ]
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return 'Using the provided data, generate an Income Statement formatted as follows:\n\nRevenue: $[Revenue]\nCost of Goods Sold: $[Cost of Goods Sold]\nGross Profit: $[Gross Profit]\nOperating Expenses: $[Operating Expenses]\nOperating Income: $[Operating Income]\nInterest Expense: $[Interest Expense]\nPre-Tax Income: $[Pre-Tax Income]\nTax Expense: $[Tax Expense]\nNet Income: $[Net Income]\n\nCalculation steps:\n1. Gross Profit = Revenue - Cost of Goods Sold\n2. Operating Income = Gross Profit - Operating Expenses\n3. Pre-Tax Income = Operating Income - Interest Expense\n4. Net Income = Pre-Tax Income - Tax Expense\n\nEnsure the financial statement is accurately calculated and formatted in plain text. Do not include any additional text or calculations.'

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        data = t['data']
        revenue = next(item['amount'] for item in data if item['account'] == 'Revenue')
        cogs = next(item['amount'] for item in data if item['account'] == 'Cost of Goods Sold')
        operating_expenses = next(item['amount'] for item in data if item['account'] == 'Operating Expenses')
        interest_expense = next(item['amount'] for item in data if item['account'] == 'Interest Expense')
        tax_expense = next(item['amount'] for item in data if item['account'] == 'Tax Expense')

        gross_profit = revenue - cogs
        operating_income = gross_profit - operating_expenses
        pre_tax_income = operating_income - interest_expense
        net_income = pre_tax_income - tax_expense

        expected_output = f"Revenue: ${revenue}\nCost of Goods Sold: ${cogs}\nGross Profit: ${gross_profit}\nOperating Expenses: ${operating_expenses}\nOperating Income: ${operating_income}\nInterest Expense: ${interest_expense}\nPre-Tax Income: ${pre_tax_income}\nTax Expense: ${tax_expense}\nNet Income: ${net_income}"

        criteria = [f'The financial statement should match the following format and values:\n{expected_output}']

        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
