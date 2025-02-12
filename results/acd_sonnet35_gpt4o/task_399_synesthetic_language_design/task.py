import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        sensory_mappings = {
            'color-sound': 'Colors are perceived as sounds',
            'taste-shape': 'Tastes are perceived as geometric shapes',
            'smell-texture': 'Smells are perceived as textures',
            'sound-emotion': 'Sounds are perceived as emotions',
            'touch-color': 'Tactile sensations are perceived as colors'
        }
        
        tasks = {
            "1": {
                "mapping": random.choice(list(sensory_mappings.items())),
                "concept": random.choice(['time', 'quantity', 'causality', 'negation'])
            },
            "2": {
                "mapping": random.choice(list(sensory_mappings.items())),
                "concept": random.choice(['spatial relationships', 'abstract ideas', 'social hierarchy', 'moral values'])
            }
        }
        return tasks

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a language feature for a species with universal synesthesia, where {t['mapping'][1]}. Your task is to:

1. Create a linguistic structure that expresses the concept of {t['concept']} using this sensory mapping.
   Explain how this structure works and provide an example.

2. Describe how this language feature might affect the species' cognitive processes or worldview.

3. Explain potential challenges in translating this language feature to a non-synesthetic language.

4. Propose an experiment to test whether this language feature enhances or impairs the species' ability to understand or communicate about {t['concept']}.

Ensure your response is creative yet grounded in principles of linguistics and cognitive science. Organize your answer using clear headings for each section. Your total response should be between 300-400 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response demonstrates a clear understanding of synesthesia and its potential impact on language.",
            "The proposed language feature is creative and logically consistent with the given sensory mapping.",
            "The explanation of cognitive effects and translation challenges is well-reasoned and grounded in linguistic and cognitive science principles.",
            "The proposed experiment is relevant and well-designed to test the language feature's effects.",
            "The response is well-organized, clear, and within the specified word limit."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
