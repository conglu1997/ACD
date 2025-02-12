import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        tasks = [
            {
                "biological_inspiration": "lotus leaf",
                "desired_property": "superhydrophobicity",
                "target_industry": "construction"
            },
            {
                "biological_inspiration": "gecko feet",
                "desired_property": "reversible adhesion",
                "target_industry": "robotics"
            }
        ]
        return {str(i+1): task for i, task in enumerate(random.sample(tasks, k=2))}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a novel nanostructured material inspired by the {t['biological_inspiration']}, aiming to achieve {t['desired_property']} for applications in the {t['target_industry']} industry. Your response should include the following sections:

1. Biological Inspiration Analysis (200-250 words):
   a) Describe the key features and mechanisms of the {t['biological_inspiration']} that contribute to its unique properties.
   b) Explain the nanoscale structures or processes that enable these properties.
   c) Discuss any existing research or applications inspired by this biological system.

2. Nanostructure Design (250-300 words):
   a) Propose a novel nanostructured material design inspired by the {t['biological_inspiration']}.
   b) Describe the key components, arrangement, and scale of your nanostructure.
   c) Explain how your design mimics or improves upon the biological system.
   d) Discuss potential fabrication methods for your nanostructured material.

3. Material Properties Analysis (200-250 words):
   a) Analyze the expected properties of your nanostructured material, focusing on {t['desired_property']}.
   b) Compare the theoretical performance of your material to existing solutions.
   c) Discuss any potential trade-offs or limitations in your material's properties.

4. Applications in {t['target_industry']} (200-250 words):
   a) Propose specific applications of your nanostructured material in the {t['target_industry']} industry.
   b) Explain how the material's properties address current challenges or create new opportunities in this industry.
   c) Discuss any modifications or optimizations needed for practical implementation.

5. Cross-industry Potential (150-200 words):
   a) Identify at least two other industries that could benefit from your nanostructured material.
   b) Briefly describe potential applications in these industries.
   c) Explain any adaptations that might be necessary for these alternative uses.

6. Environmental and Ethical Considerations (150-200 words):
   a) Discuss potential environmental impacts of producing and using your nanostructured material.
   b) Address any ethical implications or safety concerns related to its development and application.
   c) Propose strategies to mitigate any negative impacts identified.

Ensure your response demonstrates a deep understanding of materials science, nanotechnology, and the relevant biological systems. Be creative in your approach while maintaining scientific plausibility and coherence across all sections of your response.

Format your response with clear headings for each section and number your paragraphs within each section for easy reference.

Total word count should be between 1150-1450 words. Include a word count at the end of your response."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response demonstrates a deep understanding of materials science, nanotechnology, and the relevant biological systems.",
            "The proposed nanostructured material design is novel, well-explained, and plausibly inspired by the specified biological system.",
            "The material properties analysis is thorough and scientifically sound.",
            "The applications in the target industry are clearly explained and show potential for meaningful impact.",
            "The cross-industry potential is well-considered and demonstrates the versatility of the proposed material.",
            "Environmental and ethical considerations are appropriately addressed.",
            "The response includes specific examples or potential experiments in each section.",
            "The proposed approach demonstrates creativity while maintaining scientific plausibility."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
