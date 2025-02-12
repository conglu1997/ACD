import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        philosophical_areas = [
            ("metaphysics", "the nature of reality"),
            ("epistemology", "the limits of knowledge"),
            ("ethics", "moral responsibility"),
            ("philosophy of mind", "the nature of consciousness"),
            ("philosophy of science", "the demarcation of science"),
            ("political philosophy", "the justification of state power"),
            ("aesthetics", "the definition of art"),
            ("philosophy of language", "the relationship between language and reality")
        ]
        scientific_concepts = [
            "quantum entanglement",
            "artificial general intelligence",
            "epigenetics",
            "neuroplasticity",
            "multiverse theory",
            "emergent properties",
            "CRISPR gene editing",
            "brain-computer interfaces"
        ]
        return {
            "1": {
                "philosophical_area": random.choice(philosophical_areas),
                "scientific_concept": random.choice(scientific_concepts)
            },
            "2": {
                "philosophical_area": random.choice(philosophical_areas),
                "scientific_concept": random.choice(scientific_concepts)
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Generate and analyze a novel philosophical thought experiment that explores the question of {t['philosophical_area'][1]} in the area of {t['philosophical_area'][0]}, incorporating concepts from {t['scientific_concept']}. Your thought experiment must be entirely original and not based on any existing philosophical thought experiments.

Your response should include the following sections:

1. Thought Experiment Description (200-250 words):
   a) Present your thought experiment in the following format:
      - Scenario: [Describe the setup of your thought experiment]
      - Question: [State the key philosophical question your experiment raises]
      - Dilemma: [Explain the central conflict or problem in your scenario]
   b) Incorporate elements or principles from {t['scientific_concept']} into your thought experiment.
   c) Ensure your thought experiment is novel and not based on existing philosophical scenarios.

2. Philosophical Analysis (250-300 words):
   a) Analyze the implications of your thought experiment for {t['philosophical_area'][1]}.
   b) Discuss how your thought experiment challenges or supports existing philosophical theories or intuitions.
   c) Explain how the incorporation of {t['scientific_concept']} enhances or complicates the philosophical inquiry.

3. Interdisciplinary Connections (200-250 words):
   a) Explore how your thought experiment bridges {t['philosophical_area'][0]} and {t['scientific_concept']}.
   b) Discuss any novel insights that emerge from this interdisciplinary approach.
   c) Analyze potential objections or limitations to your thought experiment from both philosophical and scientific perspectives.

4. Ethical and Societal Implications (150-200 words):
   a) Discuss any ethical considerations raised by your thought experiment.
   b) Analyze potential societal impacts if the scenario in your thought experiment were to become reality.
   c) Propose guidelines for responsible exploration of the issues raised by your thought experiment.

5. Extensions and Variations (150-200 words):
   a) Suggest at least two variations or extensions of your original thought experiment.
   b) Briefly analyze how these variations might lead to different philosophical conclusions.
   c) Propose a real-world experiment or study that could further explore the issues raised in your thought experiment.

Ensure your response demonstrates a deep understanding of both {t['philosophical_area'][0]} and {t['scientific_concept']}. Be creative and original in your thought experiment while maintaining philosophical rigor and scientific plausibility. Use appropriate terminology and provide clear explanations for complex concepts.

Format your response with clear headings for each section and use the specified structure for the Thought Experiment Description. Your total response should be between 950-1200 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response must include a novel and creative thought experiment that genuinely explores {t['philosophical_area'][1]} while incorporating concepts from {t['scientific_concept']}.",
            "The thought experiment must be presented in the specified format (Scenario, Question, Dilemma) and be entirely original, not based on existing philosophical thought experiments.",
            "The philosophical analysis should be rigorous, demonstrating a deep understanding of the philosophical issues at stake and how they relate to the thought experiment.",
            "The response must draw meaningful and insightful connections between the philosophical area and the scientific concept, showing how they inform each other.",
            "The ethical and societal implications section should present a thoughtful analysis of potential real-world impacts.",
            "The extensions and variations should be creative and logically connected to the original thought experiment.",
            "The response must include all five required sections with appropriate content and adhere to the specified word limits."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
