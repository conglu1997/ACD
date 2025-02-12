class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "events": [
                    "She was born.",
                    "She moved into her first apartment.",
                    "She started her first job.",
                    "She graduated from college."
                ]
            },
            "2": {
                "events": [
                    "The product was launched.",
                    "The company was founded.",
                    "The company went public.",
                    "The first prototype was created."
                ]
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Reorder the following list of events into the correct chronological sequence:

{t['events']}

Submit your ordered list as a plain text string, with each event on a new line, in the order you believe they occurred."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        correct_sequences = [
            ["She was born.", "She graduated from college.", "She started her first job.", "She moved into her first apartment."],
            ["The company was founded.", "The first prototype was created.", "The product was launched.", "The company went public."]
        ]
        task_index = 1 if t['events'][0] == 'The product was launched.' else 0
        criteria = ["The events should be in the correct chronological order."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) and submission.split('\n') == correct_sequences[task_index] else 0.0
