import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        quantum_principles = [
            'superposition',
            'entanglement',
            'quantum tunneling',
            'quantum coherence'
        ]
        linguistic_features = [
            'phonology',
            'syntax',
            'semantics',
            'pragmatics'
        ]
        cultural_aspects = [
            'social hierarchy',
            'belief systems',
            'technological advancement',
            'environmental adaptation'
        ]
        alien_characteristics = [
            'non-carbon based',
            'hive mind',
            'multi-dimensional perception',
            'non-linear time experience'
        ]
        
        tasks = [
            {
                'quantum_principle': random.choice(quantum_principles),
                'linguistic_feature': random.choice(linguistic_features),
                'cultural_aspect': random.choice(cultural_aspects),
                'alien_characteristic': random.choice(alien_characteristics)
            },
            {
                'quantum_principle': random.choice(quantum_principles),
                'linguistic_feature': random.choice(linguistic_features),
                'cultural_aspect': random.choice(cultural_aspects),
                'alien_characteristic': random.choice(alien_characteristics)
            }
        ]
        return {str(i+1): task for i, task in enumerate(tasks)}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a quantum computing system that models the evolution of language and cultural practices in a hypothetical alien civilization, then use it to analyze potential first contact scenarios. Your system should focus on the quantum principle of {t['quantum_principle']}, address the linguistic feature of {t['linguistic_feature']}, model the cultural aspect of {t['cultural_aspect']}, and assume the aliens have the characteristic of being {t['alien_characteristic']}. Your response should include:

1. Quantum-Linguistic-Cultural Model (300-350 words):
   a) Describe the key components of your quantum computing system for modeling alien language and culture.
   b) Explain how it incorporates the specified quantum principle.
   c) Detail how the model represents and evolves the given linguistic feature and cultural aspect.
   d) Discuss how the model accounts for the specified alien characteristic.
   e) Provide a high-level diagram or pseudocode of your model's architecture.

2. Evolutionary Dynamics (250-300 words):
   a) Explain how your model simulates the co-evolution of language and culture.
   b) Describe the key variables and processes in your evolutionary algorithm.
   c) Discuss how quantum effects influence the evolutionary trajectories in your model.
   d) Provide an example of how a specific linguistic or cultural trait might evolve in your system.

3. First Contact Scenario Analysis (250-300 words):
   a) Describe a potential first contact scenario based on your model's predictions.
   b) Explain how the alien's language and culture, as modeled by your system, might impact communication and understanding.
   c) Discuss potential challenges or misunderstandings that could arise due to the quantum nature of your model.
   d) Propose a strategy for establishing meaningful communication based on your model's insights.

4. Comparative Analysis (200-250 words):
   a) Compare your quantum-based approach to traditional methods of modeling language and cultural evolution.
   b) Discuss potential advantages and limitations of your quantum linguistic-cultural model.
   c) Explain how your model might provide unique insights into the nature of language, culture, and intelligence.

5. Ethical and Philosophical Implications (200-250 words):
   a) Discuss the ethical considerations of using quantum models to predict alien civilizations and first contact scenarios.
   b) Explore the philosophical implications of quantum effects in language and culture.
   c) Consider how this approach might impact our understanding of our own language, culture, and place in the universe.

6. Future Research Directions (150-200 words):
   a) Propose two potential advancements or extensions of your quantum linguistic-cultural model.
   b) Suggest a novel research question that arises from your model's predictions.
   c) Speculate on how this approach might influence future SETI (Search for Extraterrestrial Intelligence) efforts.

Ensure your response demonstrates a deep understanding of quantum computing, linguistics, cultural anthropology, and speculative xenology. Use appropriate technical terminology and provide clear explanations for complex concepts. Be creative and innovative in your approach while maintaining scientific plausibility.

Format your response with clear headings for each section, numbered as above. Your total response should be between 1350-1650 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response demonstrates a deep understanding of quantum computing, linguistics, cultural anthropology, and speculative xenology",
            "The quantum-linguistic-cultural model is innovative, coherent, and plausibly incorporates the specified quantum principle, linguistic feature, cultural aspect, and alien characteristic",
            "The analysis of first contact scenarios is thoughtful, creative, and logically derived from the model's predictions",
            "The response shows strong interdisciplinary thinking and explores broader implications of the research",
            "The proposed future research directions are novel and promising"
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
