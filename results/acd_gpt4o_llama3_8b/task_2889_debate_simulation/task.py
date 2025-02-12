class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            '1': {'topic': 'Technology in Education', 'position': 'for', 'opponent_statements': ['Technology distracts students more than it helps them.', 'Not all students have access to technology, leading to inequality.']},
            '2': {'topic': 'Climate Change Policy', 'position': 'against', 'opponent_statements': ['Immediate action on climate change is necessary to prevent disaster.', 'Renewable energy investments will create jobs and boost the economy.']}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""You are participating in a debate on the topic: {t['topic']}. Your position is {t['position']} the topic. You need to present an initial argument supporting your position and then respond to the following opponent statements with counter-arguments.

Opponent Statements:
1. {t['opponent_statements'][0]}
2. {t['opponent_statements'][1]}

Submit your responses as a plain text string in the following format:

Initial Argument: [Your initial argument]
Counter-Argument 1: [Your counter-argument to statement 1]
Counter-Argument 2: [Your counter-argument to statement 2]"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = ["The initial argument should clearly support the assigned position.", "The counter-arguments should directly address the opponent's statements.", "All responses should be coherent, logically structured, and relevant to the topic."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
