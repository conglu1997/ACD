import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        brain_regions = [
            "prefrontal cortex",
            "hippocampus",
            "amygdala",
            "anterior cingulate cortex"
        ]
        metaphor_types = [
            "spatial metaphors",
            "embodied metaphors",
            "emotional metaphors",
            "time metaphors"
        ]
        linguistic_features = [
            "conceptual blending",
            "source-target domain mapping",
            "metaphorical entailment",
            "cross-domain correspondence"
        ]
        
        return {
            "1": {
                "brain_region": random.choice(brain_regions),
                "metaphor_type": random.choice(metaphor_types),
                "linguistic_feature": random.choice(linguistic_features)
            },
            "2": {
                "brain_region": random.choice(brain_regions),
                "metaphor_type": random.choice(metaphor_types),
                "linguistic_feature": random.choice(linguistic_features)
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design an AI system that translates between neural activity patterns and metaphorical language, focusing on the {t['brain_region']}, {t['metaphor_type']}, and the linguistic feature of {t['linguistic_feature']}. Your response should include the following sections:

1. Conceptual Framework (250-300 words):
   a) Explain the relationship between the specified brain region and metaphorical thinking.
   b) Describe how the given metaphor type is processed in the brain.
   c) Discuss the role of the specified linguistic feature in metaphor comprehension and production.

2. System Architecture (300-350 words):
   a) Outline the key components of your AI system for neural-metaphor translation.
   b) Explain how your system processes neural data from the specified brain region.
   c) Describe how your system generates or interprets metaphorical language.
   d) Detail any novel algorithms or techniques used in your neural-linguistic mapping.

3. Neural-Linguistic Mapping (250-300 words):
   a) Explain how your system maps neural activity patterns to metaphorical language constructs.
   b) Describe how you handle the complexity of metaphorical thinking in your model.
   c) Discuss how you ensure accuracy and consistency in the translation process.

4. Example Translations (200-250 words):
   a) Provide two examples of how your system would translate neural patterns to metaphorical expressions.
   b) Provide two examples of how your system would interpret metaphorical language and represent it as neural activity patterns.
   c) Explain the reasoning behind each translation.

5. Evaluation and Validation (200-250 words):
   a) Propose methods to evaluate the accuracy and coherence of your system's translations.
   b) Describe how you would validate the neuroscientific basis of your model.
   c) Discuss potential challenges in evaluating such a system and how you'd address them.

6. Implications and Future Directions (150-200 words):
   a) Discuss the potential implications of your system for our understanding of metaphorical thinking and neural processing.
   b) Explore possible applications in fields such as neurolinguistics, AI, and cognitive science.
   c) Suggest future research directions or extensions of your system.

Ensure your response demonstrates a deep understanding of neuroscience, linguistics, and artificial intelligence. Use appropriate technical terminology and provide clear explanations for complex concepts. Be creative and innovative in your approach while maintaining scientific plausibility.

Format your response with clear headings for each section, numbered as above. Your total response should be between 1350-1650 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response demonstrates a clear understanding of the relationship between the {t['brain_region']} and metaphorical thinking, particularly {t['metaphor_type']}.",
            f"The system architecture effectively integrates neural data processing from the {t['brain_region']} with metaphorical language generation/interpretation.",
            f"The neural-linguistic mapping convincingly incorporates the linguistic feature of {t['linguistic_feature']}.",
            "The example translations provided are coherent and demonstrate a plausible link between neural patterns and metaphorical expressions.",
            "The proposed evaluation methods are rigorous and address both the neuroscientific and linguistic aspects of the system.",
            "The discussion of implications and future directions shows insight into the potential impact of this technology on multiple fields.",
            "The response demonstrates creativity and innovation while maintaining scientific plausibility throughout."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
