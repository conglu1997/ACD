import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        philosophical_arguments = [
            "Socrates is a man. All men are mortal. Therefore, Socrates is mortal.",
            "If God is omnipotent, then He can create a stone so heavy that He cannot lift it. If He cannot lift the stone, then He is not omnipotent. Therefore, God cannot be omnipotent.",
            "I think, therefore I am.",
            "The ship of Theseus paradox: If all parts of a ship are replaced over time, is it still the same ship?"
        ]
        logical_operators = [
            "Conjunction (AND)",
            "Disjunction (OR)",
            "Conditional (IF-THEN)",
            "Biconditional (IF AND ONLY IF)"
        ]
        return {
            "1": {
                "argument": random.choice(philosophical_arguments),
                "operator": random.choice(logical_operators)
            },
            "2": {
                "argument": random.choice(philosophical_arguments),
                "operator": random.choice(logical_operators)
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"Your task involves translating a philosophical argument into formal logic and then using that logic to construct a novel argument. Follow these steps:\n\n" \
               f"1. Formal Logic Translation (200-250 words):\n" \
               f"   a) Translate the following philosophical argument into formal logic: '{t['argument']}'\n" \
               f"   b) Use standard logical symbols (∧ for AND, ∨ for OR, → for IF-THEN, ↔ for IF AND ONLY IF, ¬ for NOT, ∀ for ALL, ∃ for SOME).\n" \
               f"   c) Explain your translation, including the symbols and logical structures you've used.\n" \
               f"   d) Discuss any ambiguities or challenges in the translation process.\n\n" \
               f"2. Logical Analysis (150-200 words):\n" \
               f"   a) Analyze the logical structure of your translation.\n" \
               f"   b) Identify any logical fallacies or valid reasoning in the original argument.\n" \
               f"   c) Explain how the {t['operator']} operator is or could be used in this logical structure.\n\n" \
               f"3. Novel Argument Construction (300-350 words):\n" \
               f"   a) Using the logical structure from your translation and incorporating the {t['operator']} operator, construct a novel philosophical argument.\n" \
               f"   b) Present your argument in both natural language and formal logic.\n" \
               f"   c) Explain the philosophical implications of your new argument.\n" \
               f"   d) Discuss potential counterarguments to your novel argument and how you might address them.\n\n" \
               f"4. Philosophical Reflection (150-200 words):\n" \
               f"   a) Discuss how formal logic can illuminate or obscure philosophical ideas.\n" \
               f"   b) Reflect on the limitations and strengths of using formal logic in philosophical reasoning.\n\n" \
               f"Ensure your response demonstrates a deep understanding of both formal logic and philosophical concepts. Be creative in your novel argument while maintaining logical validity. Use appropriate terminology and provide clear explanations for complex concepts. Format your response with clear headings for each section."

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The formal logic translation accurately represents the given philosophical argument and uses standard logical symbols.",
            "The logical analysis correctly identifies the structure and any fallacies in the argument, and explains the use of the specified logical operator.",
            f"The novel argument effectively incorporates the {t['operator']} operator, is logically valid, and includes a discussion of potential counterarguments.",
            "The philosophical reflection demonstrates a deep understanding of the relationship between formal logic and philosophy, including both strengths and limitations.",
            "The response is well-structured with clear headings and adheres to the specified word counts for each section."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
