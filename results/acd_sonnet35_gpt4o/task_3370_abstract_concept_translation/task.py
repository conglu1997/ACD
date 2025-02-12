import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        concepts = [
            "entropy",
            "symmetry",
            "recursion",
            "emergence",
            "duality",
            "quantum superposition"
        ]
        domains = [
            "mathematical formulas",
            "visual art",
            "natural language"
        ]
        return {
            "1": {
                "concept": random.choice(concepts),
                "source_domain": random.choice(domains),
                "target_domain": random.choice([d for d in domains if d != "source_domain"])
            },
            "2": {
                "concept": random.choice(concepts),
                "source_domain": random.choice(domains),
                "target_domain": random.choice([d for d in domains if d != "source_domain"])
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design an AI system capable of translating abstract concepts between mathematical formulas, visual art, and natural language, then use it to explore cognitive patterns across these domains. Focus on the concept of {t['concept']}, translating it from {t['source_domain']} to {t['target_domain']}. Your response should include:

1. Conceptual Analysis (200-250 words):
   a) Define and explain the concept of {t['concept']} in the context of {t['source_domain']}.
   b) Discuss the key characteristics or properties of this concept that need to be preserved in translation.
   c) Analyze potential challenges in representing this concept in {t['target_domain']}.

2. AI System Architecture (250-300 words):
   a) Describe the overall structure of your AI system for abstract concept translation.
   b) Explain how your system represents and processes information from different domains.
   c) Detail the key components that enable cross-domain concept translation.
   d) Discuss any novel algorithms or techniques specific to abstract concept manipulation.

3. Translation Process (200-250 words):
   a) Outline the step-by-step process your AI system would use to translate {t['concept']} from {t['source_domain']} to {t['target_domain']}.
   b) Explain how your system preserves the essential properties of the concept during translation.
   c) Describe how your system handles ambiguities or multiple interpretations in the translation process.

4. Output and Interpretation (200-250 words):
   a) Present a detailed description or representation of the translated concept in {t['target_domain']}.
   b) Explain how this translation captures the essence of {t['concept']} from the original domain.
   c) Discuss any emergent properties or insights that arise from this translation.

5. Cognitive Pattern Analysis (200-250 words):
   a) Analyze how the translation process reveals cognitive patterns in understanding {t['concept']}.
   b) Compare and contrast how {t['concept']} is conceptualized across different domains.
   c) Discuss what this translation reveals about the nature of abstract thinking and representation.

6. Implications and Applications (150-200 words):
   a) Discuss potential applications of your abstract concept translation system in fields such as education, scientific research, or artistic creation.
   b) Explore how this technology might enhance human understanding of complex abstract concepts.
   c) Consider potential implications for artificial general intelligence and machine creativity.

7. Evaluation and Future Directions (150-200 words):
   a) Propose methods to evaluate the accuracy and meaningfulness of your system's translations.
   b) Identify potential limitations or challenges in your approach.
   c) Suggest two directions for future research to expand or improve abstract concept translation.

Ensure your response demonstrates a deep understanding of the chosen concept, the source and target domains, and the cognitive processes involved in abstract thinking. Be creative in your approach while maintaining scientific plausibility. Use appropriate technical terminology and provide clear explanations for complex ideas.

Format your response using clear headings for each section, numbered as above. Your total response should be between 1350-1700 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response should describe a plausible AI system for translating the concept of {t['concept']} from {t['source_domain']} to {t['target_domain']}.",
            "The explanation should demonstrate a deep understanding of the chosen concept, the source and target domains, and the cognitive processes involved in abstract thinking.",
            "The proposed translation process and output should be creative yet scientifically plausible.",
            "The response should address all required sections with appropriate depth and insight.",
            "The analysis of cognitive patterns and implications should be thoughtful and well-reasoned."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
