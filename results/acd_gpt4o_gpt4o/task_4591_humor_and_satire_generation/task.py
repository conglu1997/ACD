class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            '1': {'humor_topic': 'technology', 'satire_text': 'In a world where smartphones are smarter than their owners, one man dares to turn off his notifications. But can he survive the social media backlash? As days go by, he starts noticing something strange. His friends begin to think he is ignoring them, and soon, he is left out of all social gatherings. The irony is that in an attempt to gain control over his life, he ends up losing touch with everyone.'},
            '2': {'humor_topic': 'politics', 'satire_text': 'The government has announced a new initiative to solve the traffic problem: flying cars. Critics argue that the plan lacks feasibility, but officials insist that it will create new jobs for flying car traffic police. The plan also includes building sky highways, which has sparked a debate about airspace regulations. In the end, the initiative is seen as a classic example of over-promising and under-delivering.'}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Your task involves two parts: creation and analysis.

Part 1: Creation
Using the given topic, generate a humorous piece. Ensure your content is witty, engaging, and contextually appropriate. Provide your humorous content in plain text format.

Humor Topic: {t['humor_topic']}

Part 2: Analysis
Analyze the provided satirical piece. Identify the underlying message, its effectiveness, and any cultural nuances. Provide your analysis in plain text format.

Provided Satire: {t['satire_text']}

Response format:
1. Humorous Piece: [Your humorous piece here]
2. Satire Analysis: [Your analysis here]"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            'The generated humor should be witty, engaging, and contextually appropriate.',
            'The analysis should correctly identify the underlying message, effectiveness, and cultural nuances of the provided satire.'
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
