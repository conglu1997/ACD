import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        linguistic_features = [
            {
                "feature": "Tense",
                "description": "The grammatical expression of time in language"
            },
            {
                "feature": "Aspect",
                "description": "The nature of the action as perceived by the speaker"
            },
            {
                "feature": "Evidentiality",
                "description": "Grammatical marking of the source of information"
            },
            {
                "feature": "Honorifics",
                "description": "Linguistic forms that convey levels of social status"
            }
        ]
        return {
            "1": random.choice(linguistic_features),
            "2": random.choice(linguistic_features)
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Create a novel logical system based on the linguistic feature of {t['feature']}: {t['description']}. Then use this system to solve a complex reasoning problem. Your response should include:

1. Logical System Design (250-300 words):
   a) Describe the fundamental principles of your logical system based on {t['feature']}.
   b) Define at least 5 logical operators or rules inspired by this linguistic feature.
   c) Explain how these operators or rules can be combined to form complex logical statements.
   d) Provide examples of how your system represents simple and compound propositions.

2. Notation and Symbolism (100-150 words):
   a) Develop a unique notation system for your logic, including symbols for your operators and rules.
   b) Explain the rationale behind your choice of symbols and how they relate to {t['feature']}.
   c) Provide a key or legend for your notation system.

3. Truth Values and Evaluation (150-200 words):
   a) Describe how truth values are determined in your logical system.
   b) Explain how the linguistic feature of {t['feature']} influences the concept of truth in your system.
   c) Provide truth tables or equivalent structures for your logical operators.

4. Problem Formulation (100-150 words):
   a) Create a complex reasoning problem that can be solved using your logical system.
   b) Ensure the problem is related to real-world scenarios but requires abstract thinking.
   c) State the problem clearly, including any necessary background information.

5. Problem Solution (200-250 words):
   a) Solve the problem you formulated using your logical system.
   b) Show your work step-by-step, using your notation system.
   c) Explain your reasoning at each step, demonstrating how your logical system is applied.

6. Analysis and Reflection (150-200 words):
   a) Discuss the strengths and limitations of your logical system.
   b) Compare your system to traditional logic systems, highlighting unique features and potential advantages.
   c) Reflect on how this linguistic-based logic might offer new perspectives on reasoning and problem-solving.

Ensure your response demonstrates a deep understanding of both linguistics and logic. Be creative in your system design while maintaining internal consistency and practical applicability. Use appropriate terminology from both fields throughout your response.

Use clear headings for each section of your response. Your total response should be between 950-1250 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The logical system is clearly based on the given linguistic feature and demonstrates creativity and originality.",
            "The system includes at least 5 well-defined logical operators or rules inspired by the linguistic feature.",
            "The notation system is unique, well-explained, and consistent with the linguistic feature.",
            "The truth value determination process is logically sound and relates to the linguistic feature.",
            "The formulated problem is complex, related to real-world scenarios, and requires abstract thinking.",
            "The problem solution correctly applies the created logical system and shows clear step-by-step reasoning.",
            "The analysis demonstrates a deep understanding of both linguistics and logic, and offers insightful comparisons to traditional logic systems.",
            "The overall response is coherent, well-structured, and adheres to the word count guidelines for each section.",
            "The response includes all required sections with clear headings.",
            "The total word count of the response is between 950-1250 words."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
