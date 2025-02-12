import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        tasks = [
            {
                "biological_structure": "Spider silk",
                "desired_property": "Tensile strength",
                "application_domain": "Aerospace engineering"
            },
            {
                "biological_structure": "Lotus leaf",
                "desired_property": "Hydrophobicity",
                "application_domain": "Medical implants"
            }
        ]
        return {str(i+1): task for i, task in enumerate(random.sample(tasks, k=2))}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design an AI system that can generate novel biomimetic materials inspired by {t['biological_structure']}, focusing on the property of {t['desired_property']}. Then, analyze its potential applications in {t['application_domain']} and consider the ethical implications. Your response should include:

1. AI System Design (300-350 words):
   a) Describe the architecture of your AI system, including its main components and how they interact.
   b) Explain how your system analyzes the biological structure and extracts relevant features for material design.
   c) Discuss the algorithms or techniques your AI uses to generate novel materials.
   d) Explain how your system evaluates and optimizes the generated materials for the desired property.
   e) Include a visual representation or diagram of your AI system design (describe it textually).

2. Biomimetic Material Analysis (250-300 words):
   a) Describe a hypothetical material your AI system might generate, inspired by {t['biological_structure']}.
   b) Explain how this material mimics or improves upon the {t['desired_property']} of the biological structure.
   c) Discuss the potential advantages of this biomimetic material over existing synthetic materials.
   d) Analyze any potential limitations or challenges in producing this material.

3. Application in {t['application_domain']} (200-250 words):
   a) Propose a specific application of your biomimetic material in {t['application_domain']}.
   b) Explain how the material's properties make it suitable for this application.
   c) Discuss potential benefits and challenges of using this material in the proposed application.
   d) Compare your biomimetic solution to current technologies or materials used in this domain.

4. Ethical Implications (200-250 words):
   a) Identify potential ethical concerns related to the development and use of your AI-generated biomimetic material.
   b) Discuss any environmental impacts, both positive and negative, of producing and using this material.
   c) Consider potential socioeconomic effects of introducing this material into the specified application domain.
   d) Propose guidelines for the responsible development and use of AI-generated biomimetic materials.

5. Future Directions and Interdisciplinary Connections (150-200 words):
   a) Suggest two potential improvements or extensions to your AI system for biomimetic material design.
   b) Propose a research question that bridges your AI-generated biomimetic material with another scientific field not mentioned in the task.
   c) Discuss how this interdisciplinary approach might lead to new insights or innovations.

Ensure your response demonstrates a deep understanding of biology, materials science, artificial intelligence, and ethical reasoning. Use appropriate technical terminology and provide clear explanations for complex concepts. Be creative in your approach while maintaining scientific plausibility.

Format your response with clear headings for each section. Your total response should be between 1100-1350 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The AI system design effectively incorporates analysis of {t['biological_structure']} and generation of materials with {t['desired_property']}.",
            "The biomimetic material analysis is innovative and well-explained.",
            f"The application in {t['application_domain']} is clearly described and demonstrates potential advantages.",
            "The response shows a deep understanding of biology, materials science, and artificial intelligence.",
            "Ethical implications are comprehensively addressed, including environmental and socioeconomic considerations.",
            "The proposed AI system and biomimetic material are creative while maintaining scientific plausibility.",
            "Interdisciplinary connections and future directions are thoughtfully considered."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
