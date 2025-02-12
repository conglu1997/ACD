class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "text_data": "John, Mary, and Alice went to a market. John bought 3 apples, 2 bananas, and 4 oranges. Mary bought 1 apple, 5 bananas, and 2 oranges. Alice bought 2 apples, 1 banana, and 3 oranges.",
                "instructions": "Generate a table showing how many apples, bananas, and oranges each person bought. The table should have columns for 'Name', 'Apples', 'Bananas', and 'Oranges'. Format the table as plain text with columns separated by tabs."
            },
            "2": {
                "table_data": "Name,Apples,Bananas,Oranges\nJohn,3,2,4\nMary,1,5,2\nAlice,2,1,3",
                "questions": [
                    "Who bought the most bananas?",
                    "How many apples did Alice buy?",
                    "What is the total number of oranges bought by all three people?"
                ]
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        if 'text_data' in t:
            return f"""Generate a table based on the given textual data.

Text: {t['text_data']}

Instructions: {t['instructions']}"""
        elif 'table_data' in t:
            table_data_formatted = t['table_data'].replace(',', '\t')
            return f"""Interpret the given table and answer the questions. Format your answers as a numbered list.

Table:
{table_data_formatted}

Questions:
1. {t['questions'][0]}
2. {t['questions'][1]}
3. {t['questions'][2]}"""
        else:
            return ""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        if 'text_data' in t:
            validation_criteria = [
                "The table should have columns for 'Name', 'Apples', 'Bananas', and 'Oranges'.",
                "The table should correctly reflect the quantities of each fruit bought by each person.",
                "The table should be well-formatted and easy to read."
            ]
        elif 'table_data' in t:
            validation_criteria = [
                "The answers should correctly interpret the information from the table.",
                "The answers should be concise and directly address the questions posed.",
                "The answers should be formatted as a numbered list."
            ]
        return 1.0 if eval_with_llm_judge(instructions, submission, validation_criteria) else 0.0
