class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"products": {"A": 50, "B": 30, "C": 20}, "space": 100, "constraints": {"A": 2, "B": 3, "C": 5}},
            "2": {"products": {"X": 60, "Y": 40, "Z": 10}, "space": 120, "constraints": {"X": 4, "Y": 6, "Z": 8}}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""You are managing a warehouse and need to optimize the layout and inventory. The warehouse has a total space of {t['space']} units. The following products need to be stored with their respective quantities and space requirements per unit:
{t['products']}.

The space requirements per unit of each product are as follows:
{t['constraints']}.

Optimize the layout to fit as many units of each product as possible within the given space. Submit your response in the following format:

Product A: [units]
Product B: [units]
Product C: [units]

Ensure that the total space used does not exceed the available space, and that the quantities are non-negative integers."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        def parse_submission(submission):
            try:
                lines = submission.strip().split('\n')
                quantities = {line.split(': ')[0].strip(): int(line.split(': ')[1].strip()) for line in lines}
                return quantities
            except Exception as e:
                print(f"Parsing error: {e}")
                return None

        quantities = parse_submission(submission)
        if quantities is None:
            return 0.0

        try:
            total_space_used = sum(quantities[prod] * t['constraints'][prod] for prod in t['products'] if prod in quantities)
        except KeyError as e:
            print(f"Key error: {e}")
            return 0.0

        if total_space_used > t['space'] or any(q < 0 for q in quantities.values()):
            return 0.0

        return 1.0 if all(quantities.get(prod, 0) <= t['products'][prod] for prod in t['products']) else 0.0