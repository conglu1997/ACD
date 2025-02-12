class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "events": [
                    "Event 1: The Industrial Revolution (1760 - 1840)",
                    "Event 2: The Great Depression (1929 - 1939)",
                    "Event 3: The Fall of the Berlin Wall (1989)",
                    "Event 4: The Dot-com Bubble Burst (2000)",
                    "Event 5: The Global Financial Crisis (2007 - 2008)"
                ],
                "question": "Based on the patterns observed in the given historical events, predict a possible major global event that could occur in the next decade. Provide a detailed explanation of your reasoning."
            },
            "2": {
                "events": [
                    "Event 1: The Renaissance (14th - 17th Century)",
                    "Event 2: The Age of Exploration (15th - 17th Century)",
                    "Event 3: The Industrial Revolution (1760 - 1840)",
                    "Event 4: The Space Race (1957 - 1975)",
                    "Event 5: The Digital Revolution (1970s - present)"
                ],
                "question": "Analyze the patterns in the given historical events and predict a significant technological advancement that could occur within the next 20 years. Provide a detailed explanation of your reasoning."
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        events_text = '\n'.join(t['events'])
        return f"""Your task is to analyze the following historical events and use the observed patterns to make a prediction about a future event.

Historical Events:
{events_text}

Question:
{t['question']}

Provide your prediction and explanation in the following format:
Prediction: [Your prediction]
Explanation: [Your detailed explanation]"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        return 1.0 if eval_with_llm_judge(instructions, submission) else 0.0
