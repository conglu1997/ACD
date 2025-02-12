import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        quantum_concepts = [
            {
                "concept": "superposition",
                "description": "A quantum state where a particle exists in multiple states simultaneously until observed"
            },
            {
                "concept": "entanglement",
                "description": "A quantum phenomenon where particles become interconnected and the state of one instantly affects the other, regardless of distance"
            }
        ]
        
        linguistic_phenomena = [
            {
                "phenomenon": "polysemy",
                "description": "The capacity for a word or phrase to have multiple meanings"
            },
            {
                "phenomenon": "syntactic ambiguity",
                "description": "A situation where a sentence can have multiple structural interpretations"
            }
        ]
        
        return {
            "1": {
                "quantum_concept": random.choice(quantum_concepts),
                "linguistic_phenomenon": random.choice(linguistic_phenomena)
            },
            "2": {
                "quantum_concept": random.choice(quantum_concepts),
                "linguistic_phenomenon": random.choice(linguistic_phenomena)
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""You are a science fiction author with expertise in both quantum physics and linguistics. Your task is to write a short story (400-500 words) that incorporates the quantum computing concept of {t['quantum_concept']['concept']} as a metaphor for the linguistic phenomenon of {t['linguistic_phenomenon']['phenomenon']}. Your story should meet the following criteria:

1. Accurately explain the quantum concept of {t['quantum_concept']['concept']} ({t['quantum_concept']['description']}) within the narrative.

2. Use the quantum concept as a creative and insightful metaphor to illustrate the linguistic phenomenon of {t['linguistic_phenomenon']['phenomenon']} ({t['linguistic_phenomenon']['description']}).

3. Develop a coherent plot that naturally integrates both the quantum and linguistic elements.

4. Create at least one character whose experiences or actions demonstrate the parallel between the quantum concept and the linguistic phenomenon.

5. Conclude the story with a thought-provoking insight about language or communication derived from the quantum-linguistic parallel.

Ensure your story is engaging, scientifically accurate, and effectively communicates complex ideas through narrative and metaphor. Use your creativity to make the connections between quantum physics and linguistics clear and compelling.

After your story, please provide a brief explanation (100-150 words) of how you integrated the quantum concept and linguistic phenomenon, and why you chose to connect them in this particular way."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The story accurately explains the quantum concept of {t['quantum_concept']['concept']}.",
            f"The quantum concept is used effectively as a metaphor for the linguistic phenomenon of {t['linguistic_phenomenon']['phenomenon']}.",
            "The story has a coherent plot that naturally integrates both quantum and linguistic elements.",
            "At least one character's experiences or actions demonstrate the parallel between the quantum concept and the linguistic phenomenon.",
            "The story concludes with a thought-provoking insight about language or communication derived from the quantum-linguistic parallel.",
            "The story is engaging and effectively communicates complex ideas through narrative and metaphor.",
            "The explanation provided after the story clearly articulates how the quantum concept and linguistic phenomenon were integrated and connected."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
