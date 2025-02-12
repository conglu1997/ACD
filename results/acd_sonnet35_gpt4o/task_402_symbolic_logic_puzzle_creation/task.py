import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        tasks = [
            {
                'formal_system': 'Propositional calculus',
                'paradox': 'Liar paradox'
            },
            {
                'formal_system': 'First-order logic',
                'paradox': "Russell's paradox"
            },
            {
                'formal_system': 'Modal logic',
                'paradox': "Fitch's paradox of knowability"
            }
        ]
        return {str(i+1): task for i, task in enumerate(random.sample(tasks, 2))}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Your task is to create and solve a complex symbolic logic puzzle based on {t['formal_system']}, and then extend the system to incorporate the {t['paradox']}. Follow these steps:

1. Formal System Description (100-150 words):
   Explain the key components and rules of {t['formal_system']}. Include its syntax, semantics, and important axioms or inference rules. Provide an example of a well-formed formula, such as ((P ∧ Q) → R) for propositional calculus or ∀x(P(x) → Q(x)) for first-order logic.

2. Puzzle Creation (200-250 words):
   Design a challenging puzzle using {t['formal_system']}. Your puzzle should:
   a) Include at least 5 distinct propositions or predicates
   b) Utilize at least 3 different logical connectives or quantifiers
   c) Require multiple steps of logical deduction to solve
   Clearly state the puzzle premises and the question to be answered. Present your puzzle both in natural language and in formal notation. For example, a simple puzzle might start with: "If it's raining, the grass is wet. If the grass is wet, the dog gets muddy. It's raining. Is the dog muddy?"

3. Puzzle Solution (150-200 words):
   Provide a step-by-step solution to your puzzle, explaining each logical inference and how it follows from the rules of {t['formal_system']}. Use a combination of natural language explanations and formal logical notation. For instance: "Step 1: Given P → Q, P, we can conclude Q by modus ponens."

4. Paradox Integration (200-250 words):
   a) Explain the {t['paradox']} and its significance in logic and philosophy.
   b) Propose an extension or modification to {t['formal_system']} that incorporates this paradox. Specify new rules, axioms, or symbols you're introducing.
   c) Discuss the implications of this extension on the formal system's consistency and completeness.

5. Meta-Analysis (150-200 words):
   Reflect on the process of creating this puzzle and integrating the paradox. Discuss:
   a) Challenges in designing a logically sound yet solvable puzzle
   b) How the paradox integration affects the expressive power and limitations of the formal system
   c) Potential real-world applications or implications of your extended formal system

Ensure your response demonstrates a deep understanding of formal logic, creative problem-solving, and abstract reasoning. Use appropriate logical notation and explain technical terms. Balance formal rigor with clear, accessible explanations.

Format your response with clear headings for each section. Your total response should be between 800-1050 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The formal system description is accurate and includes a valid example (0.2 points)",
            "The created puzzle is logically sound, sufficiently complex, and uses the given formal system correctly (0.2 points)",
            "The puzzle solution is logically valid and clearly explained step-by-step (0.2 points)",
            "The paradox integration shows creativity and logical consistency with the formal system (0.2 points)",
            "The meta-analysis provides insightful reflection on the task and its implications (0.1 points)",
            "The response uses appropriate logical notation and explains technical terms (0.05 points)",
            "The response follows the specified format with clear headings for each section (0.025 points)",
            "The total word count is between 800-1050 words (0.025 points)"
        ]
        score = sum([float(c.split('(')[-1].split(' ')[0]) for c in criteria if eval_with_llm_judge(instructions, submission, [c])])
        return min(1.0, max(0.0, score))
