import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        tasks = [
            {
                "cognitive_principle": "Conceptual Metaphor Theory",
                "problem_domain": "Data Visualization"
            },
            {
                "cognitive_principle": "Mental Spaces Theory",
                "problem_domain": "Natural Language Processing"
            }
        ]
        return {str(i+1): task for i, task in enumerate(tasks)}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a programming language based on the cognitive linguistics principle of {t['cognitive_principle']} and use it to solve a problem in the domain of {t['problem_domain']}. Your response should include:

1. Language Design (250-300 words):
   a) Explain the key features of your programming language and how they relate to {t['cognitive_principle']}.
   b) Describe the syntax and semantics of your language, providing examples of basic operations.
   c) Explain how your language facilitates cognitive processes related to {t['cognitive_principle']}.

2. Problem Solution (200-250 words):
   a) Describe a specific problem in {t['problem_domain']} that your language is well-suited to solve.
   b) Provide a code snippet (or pseudocode) in your language that solves this problem.
   c) Explain how your solution leverages the cognitive linguistics principles embedded in your language.

3. Analysis (200-250 words):
   a) Discuss the strengths and limitations of your language in solving problems in {t['problem_domain']}.
   b) Compare your language to traditional programming paradigms, highlighting key differences and potential advantages.
   c) Analyze how your language might influence a programmer's cognitive processes and problem-solving approaches.

4. Cognitive Impact (150-200 words):
   a) Speculate on how programming in your language might affect a user's cognitive patterns or mental models.
   b) Discuss potential applications of your language in cognitive science research or education.

5. Ethical Considerations (100-150 words):
   a) Discuss any potential ethical implications or concerns related to a programming language based on cognitive linguistics principles.
   b) Propose guidelines for responsible development and use of such languages.

Ensure your response demonstrates a deep understanding of both cognitive linguistics and programming concepts. Be creative in your approach while maintaining scientific and technological plausibility. Use appropriate terminology from linguistics, cognitive science, and computer science.

Format your response with clear headings for each section."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response includes a well-designed programming language based on {t['cognitive_principle']}",
            f"The language is applied to solve a problem in {t['problem_domain']}",
            "The analysis demonstrates understanding of both cognitive linguistics and programming concepts",
            "The response includes creative and plausible ideas while maintaining scientific integrity",
            "Ethical considerations are thoughtfully addressed"
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
