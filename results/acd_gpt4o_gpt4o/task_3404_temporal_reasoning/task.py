class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "events": [
                    "John's birthday is on June 5th.",
                    "Mary's birthday is 10 days after John's.",
                    "They plan a joint party 5 days after Mary's birthday."
                ]
            },
            "2": {
                "events": [
                    "The project started on February 1st and lasted for 45 days.",
                    "A follow-up project begins 30 days after the first project ends.",
                    "The follow-up project lasts for 60 days."
                ]
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Based on the following events, answer the question related to the timeline of events:

Events:
- {t['events'][0]}
- {t['events'][1]}
- {t['events'][2]}

Here's an example to help you understand how to derive the date:

Example Events:
- Event A happens on March 1st.
- Event B happens 3 days after Event A.
- Event C happens 7 days after Event B.

To find the date of Event C, calculate as follows:
1. Start with March 1st.
2. Add 3 days to find the date of Event B: March 4th.
3. Add 7 days to find the date of Event C: March 11th.

Ensure to calculate each event step-by-step, without skipping any steps.

Question: What is the date of the joint party? Provide your response in the following format:

Date: [Your answer here]"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response should include the correct date of the joint party.",
            "The response should correctly follow the logical sequence of events provided."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
