import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        elements = [
            {
                "name": "Chronium",
                "atomic_number": 150,
                "properties": ["time-dilating", "gravity-resistant", "bioluminescent"]
            },
            {
                "name": "Quantium",
                "atomic_number": 200,
                "properties": ["quantum-entangled", "phase-shifting", "energy-amplifying"]
            }
        ]
        return {
            "1": random.choice(elements),
            "2": random.choice(elements)
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""You are a xenogeologist studying the fictional element {t['name']} (atomic number {t['atomic_number']}) on an alien planet. Your task is to create and solve a puzzle involving the geological and chemical properties of this element. Your response should include:

1. Element Description (100-150 words):
   a) Describe the physical and chemical properties of {t['name']}, incorporating its unique characteristics: {', '.join(t['properties'])}.
   b) Explain how these properties might affect the geology and environment of the planet where it's found.

2. Puzzle Creation (150-200 words):
   a) Design a geological puzzle or phenomenon involving {t['name']} that explorers on this alien planet might encounter.
   b) The puzzle should incorporate at least two of the element's unique properties.
   c) Describe the observable effects or challenges this puzzle presents to the explorers.

3. Scientific Analysis (200-250 words):
   a) Propose a hypothesis that explains the puzzle or phenomenon, based on known scientific principles and the properties of {t['name']}.
   b) Describe an experiment or investigation that the explorers could conduct to test this hypothesis.
   c) Include at least one chemical equation or physical formula in your analysis.

4. Puzzle Solution (150-200 words):
   a) Provide a scientifically plausible solution to the puzzle, explaining how it relates to the properties of {t['name']}.
   b) Discuss any potential applications or implications of this solution for future exploration or technology.

5. Ethical Consideration (100-150 words):
   a) Briefly discuss one potential ethical issue that might arise from the discovery or use of {t['name']}.
   b) Propose a guideline or protocol to address this ethical concern.

Ensure your response demonstrates a deep understanding of chemistry, geology, and physics principles, while creatively applying these to a speculative scenario. Use scientific terminology appropriately and provide explanations where necessary."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response includes a detailed and scientifically plausible description of {t['name']} and its properties.",
            "The geological puzzle is creative, incorporates the element's unique properties, and presents a clear challenge.",
            "The scientific analysis includes a well-reasoned hypothesis, a relevant experiment, and at least one chemical equation or physical formula.",
            "The puzzle solution is scientifically plausible and clearly relates to the properties of the element.",
            "The ethical consideration is thoughtful and relevant, with a reasonable proposed guideline or protocol.",
            "The overall response demonstrates a strong grasp of chemistry, geology, and physics principles, creatively applied to a speculative scenario."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
