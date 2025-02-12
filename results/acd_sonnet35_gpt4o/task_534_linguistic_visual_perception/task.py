import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        visual_features = [
            {
                'feature': 'Color categorization',
                'languages': 'Russian (has separate terms for light and dark blue) vs. English',
                'perceptual_task': 'Discriminating between shades of blue'
            },
            {
                'feature': 'Spatial relations',
                'languages': 'Korean (uses body-centric terms) vs. English (uses object-centric terms)',
                'perceptual_task': 'Judging relative positions of objects'
            }
        ]
        return {str(i+1): feature for i, feature in enumerate(random.sample(visual_features, 2))}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Investigate how language influences visual perception and processing, focusing on the relationship between {t['languages']} in the context of {t['feature']}. Your task is to:

1. Linguistic Analysis (150-200 words):
   a) Explain the key differences in how the specified languages encode {t['feature']}.
   b) Discuss how these linguistic differences might theoretically influence visual perception or cognitive processing.

2. Hypothesis Formulation (100-150 words):
   a) Based on your analysis, propose a specific hypothesis about how speakers of these languages might differ in their performance on a {t['perceptual_task']} task.
   b) Explain the reasoning behind your hypothesis, linking it to linguistic and cognitive principles.

3. Experimental Design (250-300 words):
   a) Design an experiment to test your hypothesis. Include:
      - Participant selection criteria
      - Stimuli and apparatus
      - Procedure
      - Control measures
   b) Explain how your experiment controls for potential confounding variables.
   c) Describe the data you would collect and how it relates to your hypothesis.

4. Analysis Plan (150-200 words):
   a) Propose statistical analyses to evaluate your hypothesis.
   b) Explain what results would support or refute your hypothesis.
   c) Discuss how you would interpret potential null results.

5. Broader Implications (150-200 words):
   a) Discuss the potential implications of your study for our understanding of linguistic relativity and visual cognition.
   b) Propose a follow-up study that could extend or clarify your findings.
   c) Speculate on potential real-world applications of this research.

6. Ethical Considerations (100-150 words):
   a) Identify potential ethical issues in conducting this research.
   b) Propose measures to address these ethical concerns.
   c) Discuss the broader societal implications of this line of research.

Ensure your response demonstrates a deep understanding of linguistics, cognitive psychology, and experimental design. Use technical terminology appropriately and provide explanations where necessary. Be creative in your approach while maintaining scientific rigor and plausibility.

Format your response using clear headings for each section. Your total response should be between 900-1200 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response demonstrates a deep understanding of how {t['languages']} differ in encoding {t['feature']}.",
            "The hypothesis is well-formulated and logically connected to the linguistic analysis.",
            f"The experimental design is appropriate for testing the hypothesis about {t['perceptual_task']}.",
            "The analysis plan is statistically sound and addresses potential outcomes.",
            "The discussion of broader implications shows insight into linguistic relativity and visual cognition.",
            "Ethical considerations are thoughtfully addressed.",
            "The response is well-structured, clear, and within the specified word count."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
