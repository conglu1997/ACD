import json
import csv
from io import StringIO

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "input_format": "json",
                "output_format": "csv",
                "data": "{\"students\": [{\"name\": \"Alice\", \"age\": 24, \"grade\": \"A\"}, {\"name\": \"Bob\", \"age\": 22, \"grade\": \"B\"}, {\"name\": \"Charlie\", \"age\": 23, \"grade\": \"C\"}]}"
            },
            "2": {
                "input_format": "csv",
                "output_format": "json",
                "data": "name,age,grade\nAlice,24,A\nBob,22,B\nCharlie,23,C"
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Convert the following data from {t['input_format'].upper()} format to {t['output_format'].upper()} format:

Data:
{t['data']}

Submit your converted data as a plain text string in the correct {t['output_format'].upper()} format."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        is_json_to_csv = t['input_format'] == 'json' and t['output_format'] == 'csv'
        is_csv_to_json = t['input_format'] == 'csv' and t['output_format'] == 'json'

        if is_json_to_csv:
            expected_output = 'name,age,grade\nAlice,24,A\nBob,22,B\nCharlie,23,C'
        elif is_csv_to_json:
            expected_output = '{"students": [{"name": "Alice", "age": 24, "grade": "A"}, {"name": "Bob", "age": 22, "grade": "B"}, {"name": "Charlie", "age": 23, "grade": "C"}]}'
        else:
            return 0.0

        criteria = [f'The converted data should match the expected {t["output_format"].upper()} format.']
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
