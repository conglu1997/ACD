import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        quantum_concepts = [
            {
                "principle": "Superposition",
                "terms": ["quantum state", "wavefunction", "collapse", "measurement", "probability amplitude"],
                "narrative_element": "a character facing a life-changing decision"
            },
            {
                "principle": "Entanglement",
                "terms": ["quantum correlation", "spooky action", "Bell state", "non-locality", "quantum teleportation"],
                "narrative_element": "two characters with an inexplicable connection"
            },
            {
                "principle": "Quantum Tunneling",
                "terms": ["potential barrier", "wave-particle duality", "tunneling effect", "decay rate", "quantum penetration"],
                "narrative_element": "overcoming an seemingly insurmountable obstacle"
            },
            {
                "principle": "Heisenberg Uncertainty Principle",
                "terms": ["complementary variables", "position-momentum", "measurement disturbance", "wave packet", "standard deviation"],
                "narrative_element": "a detective trying to solve an elusive mystery"
            }
        ]
        return {
            "1": random.choice(quantum_concepts),
            "2": random.choice(quantum_concepts)
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Create a short story (300-450 words) that incorporates the quantum mechanics principle of {t['principle']}. Your task has three parts:

1. Story Creation (250-350 words):
   a) Write a narrative that metaphorically represents the principle of {t['principle']}.
   b) The story should have a clear beginning, middle, and end.
   c) Incorporate all five quantum terminology terms provided: {', '.join(t['terms'])}.
   d) Include the following narrative element in your story: {t['narrative_element']}.
   e) Ensure that the use of quantum terms is both scientifically accurate and narratively meaningful.

2. Quantum Principle Explanation (50-75 words):
   Briefly explain the quantum principle of {t['principle']} and how it is represented in your story.

3. Linguistic Analysis (50-75 words):
   Discuss how the incorporation of quantum terminology and the specific narrative element affected your storytelling choices and the overall structure of your story.

Ensure your response demonstrates a deep understanding of the quantum principle, creative storytelling, and thoughtful linguistic integration of scientific concepts."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The story accurately incorporates the quantum principle of {t['principle']} in a metaphorical or allegorical manner.",
            f"All five quantum terms ({', '.join(t['terms'])}) are used correctly and meaningfully in the narrative.",
            f"The story includes the specified narrative element: {t['narrative_element']}.",
            "The story has a clear narrative structure with a beginning, middle, and end.",
            "The explanation of the quantum principle is accurate and clearly relates to the story.",
            "The linguistic analysis thoughtfully discusses the integration of quantum terminology and the narrative element into the story."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
