import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        quantum_concepts = [
            "superposition",
            "entanglement",
            "quantum tunneling",
            "wave-particle duality"
        ]
        linguistic_features = [
            "alliteration",
            "metaphor",
            "synecdoche",
            "anaphora"
        ]
        time_aspects = [
            "non-linearity",
            "relativity",
            "entropy",
            "cyclicality"
        ]
        return {
            "1": {
                "quantum_concept": random.choice(quantum_concepts),
                "linguistic_feature": random.choice(linguistic_features),
                "time_aspect": random.choice(time_aspects)
            },
            "2": {
                "quantum_concept": random.choice(quantum_concepts),
                "linguistic_feature": random.choice(linguistic_features),
                "time_aspect": random.choice(time_aspects)
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Create a poem that explores the nature of time through the lens of quantum physics and linguistics. Your task has the following components:

1. Poem Creation (200-250 words):
   a) Write a poem of 14-20 lines (100-150 words) that incorporates the quantum concept of {t['quantum_concept']}, the linguistic feature of {t['linguistic_feature']}, and explores the time aspect of {t['time_aspect']}.
   b) Ensure that the poem has a clear structure and rhythm.
   c) Use the quantum concept as both a literal element and a metaphor for the exploration of time.

2. Quantum-Temporal Analysis (150-200 words):
   a) Explain how your poem incorporates the assigned quantum concept.
   b) Analyze how this quantum concept is used to explore the specified aspect of time.
   c) Discuss any paradoxes or unusual temporal phenomena that emerge from this integration.
   d) Explain how the poem reflects the assigned time aspect of {t['time_aspect']}.

3. Linguistic Breakdown (150-200 words):
   a) Identify and explain specific instances of the assigned linguistic feature in your poem.
   b) Discuss how this linguistic feature enhances the exploration of the quantum concept and time aspect.
   c) Analyze how the linguistic choices affect the reader's perception of time within the poem.

4. Interdisciplinary Synthesis (200-250 words):
   a) Explain how your poem creates connections between quantum physics, linguistics, and the nature of time.
   b) Discuss any novel insights or perspectives on time that emerge from this interdisciplinary approach.
   c) Propose a hypothetical experiment or study inspired by your poem that could further explore these connections.

5. Reflection on Creative Process (100-150 words):
   a) Describe the challenges you faced in integrating these diverse concepts into a coherent poem.
   b) Explain any techniques or strategies you used to overcome these challenges.
   c) Discuss how this task might push the boundaries of AI language models' capabilities.

Ensure your response demonstrates a deep understanding of quantum physics, linguistics, and the philosophy of time. Be creative and innovative in your approach while maintaining scientific accuracy. Use appropriate terminology from each field and provide explanations where necessary.

Format your response with clear headings for each section, numbered as above."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The poem effectively incorporates the quantum concept of {t['quantum_concept']}, the linguistic feature of {t['linguistic_feature']}, and explores the time aspect of {t['time_aspect']}.",
            "The poem meets the specified length requirement of 14-20 lines (100-150 words).",
            "The analysis demonstrates a deep understanding of the quantum concept and its relation to time.",
            "The linguistic breakdown shows a clear grasp of the assigned feature and its impact on the poem.",
            "The interdisciplinary synthesis provides novel insights connecting quantum physics, linguistics, and time.",
            "The reflection on the creative process addresses the challenges and strategies used in completing the task."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
