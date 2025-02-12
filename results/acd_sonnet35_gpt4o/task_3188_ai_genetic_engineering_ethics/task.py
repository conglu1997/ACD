import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        traits = [
            'intelligence',
            'longevity',
            'physical strength',
            'emotional stability'
        ]
        ethical_concerns = [
            'equity and access',
            'unintended consequences',
            'human dignity and identity',
            'biodiversity and ecosystem impact'
        ]
        tasks = [
            {
                'trait': random.choice(traits),
                'ethical_concern': random.choice(ethical_concerns)
            },
            {
                'trait': random.choice(traits),
                'ethical_concern': random.choice(ethical_concerns)
            }
        ]
        return {str(i+1): task for i, task in enumerate(tasks)}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design an AI system for genetic engineering that optimizes the human trait of {t['trait']}, then analyze its ethical implications with a focus on {t['ethical_concern']}, and propose governance frameworks. Your response should include:

1. AI-Driven Genetic Engineering System (300-350 words):
   a) Describe the key components and functionalities of your AI system.
   b) Explain how it identifies and manipulates genetic markers related to {t['trait']}.
   c) Detail the AI algorithms and techniques used (e.g., machine learning, deep learning, evolutionary algorithms).
   d) Discuss how the system ensures precision and minimizes off-target effects.
   e) Propose a novel feature that enhances the system's capabilities or safety.

2. Trait Optimization Analysis (200-250 words):
   a) Explain the genetic basis of {t['trait']} and challenges in its optimization.
   b) Describe how your AI system addresses these challenges.
   c) Discuss potential limitations and risks in optimizing this trait.

3. Ethical Implications (250-300 words):
   a) Analyze the ethical concerns related to {t['ethical_concern']} in the context of your system.
   b) Discuss how these concerns might affect different stakeholders in society.
   c) Explore potential long-term consequences of widespread use of your system.
   d) Propose ethical guidelines for the development and use of AI-driven genetic engineering.

4. Governance Framework (200-250 words):
   a) Propose a comprehensive governance framework for regulating AI-driven genetic engineering.
   b) Describe key components of this framework (e.g., oversight bodies, approval processes, monitoring systems).
   c) Explain how this framework addresses the specific ethical concern of {t['ethical_concern']}.
   d) Discuss potential challenges in implementing this framework globally.

5. Societal Impact (150-200 words):
   a) Analyze potential societal impacts of widespread adoption of your AI genetic engineering system.
   b) Discuss how it might affect social structures, economy, and human evolution.
   c) Propose strategies to mitigate negative impacts and promote equitable access.

6. Future Directions and Reflection (100-150 words):
   a) Suggest potential advancements or iterations for your AI genetic engineering system.
   b) Reflect on the broader implications of AI-driven human enhancement technologies.
   c) Discuss any novel insights gained from this interdisciplinary analysis.

Ensure your response demonstrates a deep understanding of genetics, AI technologies, and ethical reasoning. Use appropriate technical terminology and provide clear explanations for complex concepts. Be creative in your approach while maintaining scientific plausibility and addressing real-world ethical concerns.

Format your response with clear headings for each section. Your total response should be between 1200-1500 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response demonstrates a deep understanding of genetics, AI technologies, and ethical reasoning.",
            "The AI system design is innovative, plausible, and well-explained, integrating concepts from genetics and AI.",
            "The ethical analysis is thorough, addressing multiple perspectives and long-term implications.",
            "The proposed governance framework is comprehensive and addresses the specific ethical concern.",
            "The response maintains a balance between scientific accuracy, ethical consideration, and creative thinking throughout."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
