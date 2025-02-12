class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"dataset": "name,age,city\nAlice,30,New York\nBob,25,Los Angeles\nCharlie,35,Chicago\nDavid,40,Houston\nEve,28,San Francisco", "rules": ["Change all names to uppercase.", "Increment age by 5.", "Replace 'New York' with 'NYC'.", "Replace 'Houston' with 'HOU'.", "Replace 'San Francisco' with 'SF'."]},
            "2": {"dataset": "product,price,quantity\nLaptop,1000,5\nPhone,500,10\nTablet,750,8\nMonitor,300,15\nKeyboard,100,20", "rules": ["Decrease all prices by 10%.", "Double the quantity.", "Replace 'Tablet' with 'iPad'.", "Replace 'Monitor' with 'Display'.", "Replace 'Keyboard' with 'Keypad'."]}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        instructions = f"""Your task is to transform the given dataset based on the specified rules. Ensure that each rule is applied sequentially and correctly. The final output should reflect all the transformations accurately. Here is the dataset and the rules to apply:

Dataset:
{t['dataset']}

Rules:
1. {t['rules'][0]}
2. {t['rules'][1]}
3. {t['rules'][2]}
4. {t['rules'][3]}
5. {t['rules'][4]}

Provide your transformed dataset in the same format as the input dataset. Each transformation should be applied in the given order. Ensure that the final dataset is correctly formatted as a CSV string.

Example:
Initial Dataset:
name,age,city\nAlice,30,New York

Rules:
1. Change all names to uppercase.
2. Increment age by 5.
3. Replace 'New York' with 'NYC'.

Step-by-Step Transformation:
1. Change all names to uppercase:
NAME,age,city\nALICE,30,New York

2. Increment age by 5:
NAME,age,city\nALICE,35,New York

3. Replace 'New York' with 'NYC':
NAME,age,city\nALICE,35,NYC

Continue applying the rules in this manner."""
        return instructions

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The transformed dataset should match the expected output after applying all rules sequentially.",
            "The final dataset should be correctly formatted as a CSV string.",
            "All transformations should be applied in the correct order."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
