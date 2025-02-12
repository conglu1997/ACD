import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        scenarios = [
            {
                "language_feature": "Non-linear time representation",
                "problem_domain": "Predictive modeling in quantum systems",
                "specific_problem": "Predicting the outcome of a quantum entanglement experiment"
            },
            {
                "language_feature": "Fluid concept boundaries",
                "problem_domain": "Ethical decision-making in complex scenarios",
                "specific_problem": "Resolving conflicting ethical principles in an autonomous vehicle accident scenario"
            }
        ]
        return {str(i+1): scenario for i, scenario in enumerate(random.sample(scenarios, 2))}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a hypothetical AI system that uses a constructed language as its internal representation, incorporating the following language feature: {t['language_feature']}. Then, apply this system to solve the specific problem of {t['specific_problem']} in the domain of {t['problem_domain']}.

Your response must follow this structure and word limits:

1. Language Design (250-300 words):
   a) Describe 3-5 key features of your constructed language, focusing on how it incorporates {t['language_feature']}.
   b) Explain how this language structure enhances AI cognition for the given problem domain.
   c) Provide 2-3 examples of how key concepts related to {t['problem_domain']} are represented in this language.

2. AI System Architecture (200-250 words):
   a) Outline the core components of your AI system's architecture.
   b) Explain how the system processes information using the constructed language.
   c) Describe the mechanism for translating between natural language and the internal language.

3. Problem-Solving Application (300-350 words):
   a) Break down the problem of {t['specific_problem']} into 3-5 key steps or components.
   b) For each step, explain how your AI system would approach it using the constructed language.
   c) Highlight at least 2 specific instances where the language feature provides an advantage in solving the problem.
   d) Compare your AI's approach to how a human expert might tackle the same problem, noting key differences.

4. Comparative Analysis (200-250 words):
   a) Identify 2-3 traditional AI methods that could be used for this problem.
   b) Compare your system's approach to these methods, highlighting pros and cons.
   c) Discuss potential limitations of your approach and propose one way to address each limitation.

5. Ethical and Societal Implications (150-200 words):
   a) Discuss 2-3 ethical considerations specific to using your AI system for {t['specific_problem']}.
   b) Analyze potential societal impacts (both positive and negative) of deploying such a system.

6. Future Research Directions (100-150 words):
   a) Propose one specific experiment to test the effectiveness of your system.
   b) Suggest one way this approach could be extended to a different problem domain.

Ensure your response demonstrates a deep understanding of linguistics, cognitive science, and artificial intelligence. Be creative while maintaining scientific plausibility. Use clear headings and subheadings as specified above.

Your total response should be between 1200-1500 words. Provide a word count at the end of each section."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response includes all six required sections with appropriate content and adheres to the specified word limits",
            "The language design is creative, coherent, and clearly incorporates the specified feature with relevant examples",
            "The AI system architecture is well-explained and demonstrates how it leverages the constructed language",
            "The problem-solving application provides a detailed, step-by-step approach to the specific problem, highlighting the language's advantages",
            "The comparative analysis offers insightful reasoning about the advantages and limitations of the approach compared to traditional methods",
            "The ethical and societal implications are thoughtfully considered and directly related to the specific problem",
            "The proposed future research directions are relevant and well-defined"
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
