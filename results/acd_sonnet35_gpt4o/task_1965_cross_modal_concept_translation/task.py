import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        modalities = [
            "visual",
            "auditory",
            "kinesthetic",
            "olfactory",
            "gustatory",
            "proprioceptive"
        ]
        
        cognitive_frameworks = [
            "spatial reasoning",
            "temporal logic",
            "emotional intelligence",
            "mathematical thinking",
            "musical cognition",
            "linguistic processing"
        ]
        
        abstract_concepts = [
            "justice",
            "beauty",
            "chaos",
            "infinity",
            "consciousness",
            "harmony"
        ]
        
        scenarios = [
            "enhancing cross-cultural communication",
            "developing assistive technologies for sensory impairments",
            "creating immersive virtual reality experiences",
            "improving human-AI interaction",
            "designing novel educational methodologies",
            "advancing artistic expression techniques"
        ]
        
        def generate_task():
            source_modality = random.choice(modalities)
            target_framework = random.choice(cognitive_frameworks)
            concept = random.choice(abstract_concepts)
            scenario = random.choice(scenarios)
            
            return {
                "source_modality": source_modality,
                "target_framework": target_framework,
                "concept": concept,
                "scenario": scenario
            }
        
        return {
            "1": generate_task(),
            "2": generate_task()
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a system capable of translating the abstract concept of '{t['concept']}' from the {t['source_modality']} modality to the {t['target_framework']} framework, then apply it to the scenario of {t['scenario']}. Your response should include:

1. System Architecture (300-350 words):
   a) Describe the key components of your cross-modal concept translation system.
   b) Explain how your system processes and translates information between the {t['source_modality']} modality and the {t['target_framework']} framework.
   c) Discuss any novel algorithms or techniques you've incorporated to enable this translation.
   d) Provide a high-level diagram or flowchart of your system (describe it textually).

2. Concept Analysis (250-300 words):
   a) Analyze how the concept of '{t['concept']}' is typically represented or experienced in the {t['source_modality']} modality.
   b) Explain how this concept might be understood or processed within the {t['target_framework']} framework.
   c) Discuss the challenges and opportunities in translating this concept between these specific modalities and frameworks.

3. Translation Process (250-300 words):
   a) Describe step-by-step how your system would translate '{t['concept']}' from the {t['source_modality']} modality to the {t['target_framework']} framework.
   b) Provide a specific example of how the translated concept might be represented or expressed in the target framework.
   c) Explain how your system preserves the essential meaning or experience of the concept across this translation.

4. Application to Scenario (200-250 words):
   a) Describe how your system would be applied to the scenario of {t['scenario']}.
   b) Explain the potential benefits and challenges of using your cross-modal concept translation in this context.
   c) Provide a concrete example of how your system might enhance or transform the given scenario.

5. Evaluation and Validation (150-200 words):
   a) Propose a method for evaluating the accuracy and effectiveness of your system's translations.
   b) Discuss potential challenges in assessing cross-modal concept translations and how you might address them.
   c) Suggest criteria for validating the practical utility of your system in the given scenario.

6. Ethical Considerations and Limitations (150-200 words):
   a) Analyze potential ethical implications of cross-modal concept translation technology.
   b) Discuss any limitations of your approach and areas for future improvement.
   c) Propose guidelines for the responsible development and use of such systems.

Ensure your response demonstrates a deep understanding of cognitive processes, sensory modalities, and the specified frameworks. Be creative and innovative in your approach while maintaining scientific and technological plausibility. Use appropriate terminology and provide clear explanations where necessary.

Format your response with clear headings for each section. Your total response should be between 1300-1600 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response demonstrates a deep understanding of the {t['source_modality']} modality and the {t['target_framework']} framework.",
            f"The system design effectively translates the concept of '{t['concept']}' between the specified modality and framework.",
            f"The application to the scenario of {t['scenario']} is innovative and well-reasoned.",
            "The response shows creativity and interdisciplinary knowledge integration.",
            "The ethical considerations and limitations are thoughtfully addressed.",
            "The overall response is well-structured, clear, and within the specified word count."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
