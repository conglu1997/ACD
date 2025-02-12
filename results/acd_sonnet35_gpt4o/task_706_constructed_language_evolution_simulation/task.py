import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        linguistic_features = [
            "ergative-absolutive alignment",
            "OSV word order",
            "tonal system",
            "evidentiality markers",
            "inclusive-exclusive distinction in pronouns",
            "noun incorporation",
            "logographic writing system"
        ]
        cultural_factors = [
            "nomadic lifestyle",
            "technological advancement",
            "religious shift",
            "political unification",
            "prolonged isolation",
            "frequent contact with other languages",
            "development of a formal education system"
        ]
        environmental_factors = [
            "migration to a new climate",
            "natural disaster",
            "resource scarcity",
            "abundance of new flora and fauna",
            "development of agriculture",
            "urbanization",
            "colonization of a new planet"
        ]
        
        return {
            "1": {
                "linguistic_features": random.sample(linguistic_features, 2),
                "cultural_factor": random.choice(cultural_factors),
                "environmental_factor": random.choice(environmental_factors)
            },
            "2": {
                "linguistic_features": random.sample(linguistic_features, 2),
                "cultural_factor": random.choice(cultural_factors),
                "environmental_factor": random.choice(environmental_factors)
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Your task is to create a constructed language (conlang) and simulate its evolution over time. Follow these steps:

1. Conlang Creation (300-350 words):
   a) Design a conlang incorporating these linguistic features: {', '.join(t['linguistic_features'])}.
   b) Provide 5-7 example words or phrases in your conlang, with translations and explanations.
   c) Briefly describe the conlang's phonology, morphology, and syntax.
   d) Explain how the required linguistic features are implemented in your conlang.

2. Evolution Simulation (400-450 words):
   Simulate how your conlang might evolve over 500 years, considering these factors:
   - Cultural factor: {t['cultural_factor']}
   - Environmental factor: {t['environmental_factor']}
   a) Describe at least 3 significant changes in the language's structure or vocabulary.
   b) Provide examples of words or phrases that demonstrate these changes.
   c) Explain the rationale behind each change, linking it to the given factors.
   d) Discuss any new linguistic features that might emerge during this evolution.

3. Comparative Analysis (200-250 words):
   a) Compare your conlang's evolution to historical changes in natural languages.
   b) Discuss the plausibility of your simulated changes in the context of linguistic theory.
   c) Reflect on how this exercise illustrates the interplay between language, culture, and environment.

Ensure your response demonstrates a deep understanding of linguistic principles, creative application of language creation, and insightful analysis of language change. Use appropriate linguistic terminology throughout your response."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The conlang creation demonstrates a clear understanding and creative implementation of the specified linguistic features.",
            "The evolution simulation presents plausible and well-reasoned changes based on the given cultural and environmental factors.",
            "The comparative analysis shows insight into linguistic theory and the relationship between language, culture, and environment.",
            "The response uses appropriate linguistic terminology and demonstrates a deep understanding of language structures and change.",
            "The overall submission is creative, coherent, and demonstrates strong interdisciplinary problem-solving skills."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
