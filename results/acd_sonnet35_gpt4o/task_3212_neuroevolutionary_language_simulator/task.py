import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        neurological_alterations = [
            'Enhanced visual cortex',
            'Reduced lateralization',
            'Expanded working memory',
            'Heightened emotional processing'
        ]
        linguistic_features = [
            'Phonology',
            'Syntax',
            'Semantics',
            'Pragmatics'
        ]
        cultural_factors = [
            'Nomadic lifestyle',
            'Technological advancement',
            'Social hierarchy',
            'Environmental pressures'
        ]
        
        return {
            "1": {
                "alteration": random.choice(neurological_alterations),
                "feature": random.choice(linguistic_features),
                "factor": random.choice(cultural_factors)
            },
            "2": {
                "alteration": random.choice(neurological_alterations),
                "feature": random.choice(linguistic_features),
                "factor": random.choice(cultural_factors)
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design an AI system that simulates the evolution of language in a hypothetical human society with the following specifications:

Neurological Alteration: {t['alteration']}
Linguistic Feature to Focus On: {t['feature']}
Cultural Factor to Consider: {t['factor']}

Your response should include:

1. AI System Architecture (300-350 words):
   a) Describe the key components of your AI system for simulating language evolution.
   b) Explain how your system models the specified neurological alteration and its effects on language development.
   c) Detail how your system incorporates the given cultural factor into the simulation.
   d) Discuss any novel algorithms or approaches used in your design.

2. Neurological-Linguistic Mapping (250-300 words):
   a) Explain how the specified neurological alteration might influence the development of the given linguistic feature.
   b) Describe the mechanisms your system uses to model this influence over time.
   c) Provide an example of how a specific aspect of the linguistic feature might evolve differently due to the neurological alteration.

3. Cultural-Linguistic Interaction (200-250 words):
   a) Analyze how the given cultural factor might interact with the neurological alteration to shape language evolution.
   b) Describe how your system models this interaction.
   c) Discuss potential challenges in accurately simulating cultural influences on language.

4. Simulation Process and Output (250-300 words):
   a) Outline the step-by-step process your system would follow to simulate language evolution.
   b) Describe the types of outputs your system would generate (e.g., vocabulary, grammatical structures, usage patterns).
   c) Explain how your system tracks and represents changes in the language over time.
   d) Provide a hypothetical example of a simulation result, focusing on the specified linguistic feature.

5. Validation and Analysis (200-250 words):
   a) Propose methods to validate the accuracy and plausibility of your system's simulations.
   b) Describe how you would analyze the simulated language to identify key evolutionary trends.
   c) Discuss potential insights this system could provide about the relationship between neurology, culture, and language.

6. Ethical Considerations and Implications (200-250 words):
   a) Discuss ethical considerations in simulating alternative human neurological structures and their effects.
   b) Analyze potential implications of this research for our understanding of linguistic diversity and cognitive differences.
   c) Explore how insights from this system might influence approaches to language education or therapy.
   d) Address potential misuses or misinterpretations of the system's outputs and how to mitigate them.

Ensure your response demonstrates a deep understanding of neuroscience, linguistics, cultural anthropology, and artificial intelligence. Use appropriate terminology from all relevant fields and provide clear explanations where necessary. Be innovative in your approach while maintaining scientific plausibility.

Your total response should be between 1400-1700 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response demonstrates a deep understanding of neuroscience, particularly how {t['alteration']} might affect language development.",
            f"The AI system design effectively models the evolution of {t['feature']} in the context of the given neurological alteration and cultural factor.",
            "The response shows creativity and innovation in combining principles from neuroscience, linguistics, cultural anthropology, and AI.",
            "The simulation process and outputs are clearly explained and scientifically plausible.",
            "The proposed validation methods and ethical considerations are thoughtful and well-reasoned.",
            "The response is well-structured, coherent, and within the specified word count."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
