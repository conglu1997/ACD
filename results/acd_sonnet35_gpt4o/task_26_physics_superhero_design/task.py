import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        physics_principles = [
            {
                "principle": "Conservation of Energy",
                "description": "Energy cannot be created or destroyed, only converted from one form to another."
            },
            {
                "principle": "Quantum Entanglement",
                "description": "A quantum phenomenon where particles become interconnected and the state of each particle cannot be described independently of the others."
            },
            {
                "principle": "Bernoulli's Principle",
                "description": "An increase in the speed of a fluid occurs simultaneously with a decrease in pressure or a decrease in the fluid's potential energy."
            }
        ]
        return {str(i+1): principle for i, principle in enumerate(random.sample(physics_principles, 2))}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a superhero based on the following physics principle:

{t['principle']}: {t['description']}

Your task is to create a superhero whose powers are directly based on this principle. Follow these steps:

1. Name your superhero (be creative and relevant to the principle).
2. Describe their primary superpower in 2-3 sentences, explaining how it relates to the physics principle.
3. List two creative applications of this power that the hero could use to solve problems or fight crime.
4. Explain one limitation or weakness of this power, based on the constraints of the physics principle.
5. Describe a potential villain or challenge that would be particularly difficult for this hero to overcome, given their power set.

Provide your response in the following format:

Superhero Name: [Name]
Primary Power: [Description]
Creative Applications:
1. [First application]
2. [Second application]
Limitation: [Description]
Challenge: [Description]

Ensure that your superhero design is scientifically plausible within the constraints of the given physics principle, while also being creative and engaging."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The superhero's power must be based on the principle of {t['principle']}",
            "The primary power description should accurately reflect the given physics principle",
            "The creative applications should be plausible given the described power",
            "The limitation should be logically connected to the constraints of the physics principle",
            "The challenge should be relevant to the hero's powers and limitations",
            "The response should demonstrate both scientific understanding and creativity",
            "The response should follow the specified format"
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
