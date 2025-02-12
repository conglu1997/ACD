import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        poetic_forms = [
            {
                "name": "Sonnet",
                "structure": "14 lines with a specific rhyme scheme",
                "logical_element": "Syllogism"
            },
            {
                "name": "Haiku",
                "structure": "3 lines with 5-7-5 syllable pattern",
                "logical_element": "Modus Ponens"
            }
        ]
        return {
            "1": random.choice(poetic_forms),
            "2": random.choice(poetic_forms)
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a formal logic system based on the structures and rules of the {t['name']} poetic form, then use it to prove a theorem. Your task has the following parts:

1. Poetic Logic System Design (300-350 words):
   a) Describe how you will adapt the structure of a {t['name']} ({t['structure']}) to create a formal logic system.
   b) Define the basic elements of your system (e.g., variables, operators, rules of inference) in terms of poetic elements.
   c) Explain how your system incorporates the logical element of {t['logical_element']}.
   d) Provide at least three axioms or rules of your poetic logic system, explaining their poetic and logical significance.

2. Notation and Syntax (200-250 words):
   a) Develop a notation system for your poetic logic that reflects both logical and poetic elements.
   b) Explain the syntax rules of your system, including how to construct well-formed formulas.
   c) Provide examples of valid and invalid expressions in your system.

3. Theorem and Proof (250-300 words):
   a) State a non-trivial theorem in your poetic logic system.
   b) Provide a step-by-step proof of this theorem using your system's rules and notation.
   c) Explain how each step in the proof corresponds to both logical and poetic elements.

4. Interpretation and Analysis (200-250 words):
   a) Interpret the meaning of your theorem and proof in terms of traditional logic.
   b) Analyze the strengths and limitations of your poetic logic system compared to classical logic systems.
   c) Discuss any insights or novel perspectives gained from this poetic approach to logic.

5. Applications and Extensions (150-200 words):
   a) Propose a potential real-world application of your poetic logic system.
   b) Suggest how this system might be extended or adapted to other poetic forms or logical structures.
   c) Discuss the implications of this approach for understanding the relationship between language, logic, and creative expression.

Ensure your response demonstrates a deep understanding of both formal logic and poetic structures. Be creative in your system design while maintaining logical consistency and poetic integrity. Use appropriate terminology from both fields and provide clear explanations for complex concepts.

Format your response with clear headings for each section. Your total response should be between 1100-1350 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response includes a well-designed formal logic system based on the {t['name']} poetic form.",
            "The system incorporates both logical and poetic elements in a creative and coherent manner.",
            f"The logical element of {t['logical_element']} is effectively integrated into the system.",
            "The notation and syntax are clearly defined and reflect both logical and poetic aspects.",
            "A non-trivial theorem is stated and proven using the developed poetic logic system.",
            "The interpretation and analysis demonstrate a deep understanding of both logic and poetry.",
            "The proposed applications and extensions are innovative and thought-provoking."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
