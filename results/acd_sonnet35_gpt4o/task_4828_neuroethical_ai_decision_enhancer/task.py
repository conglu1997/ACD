import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        brain_regions = ["prefrontal cortex", "anterior cingulate cortex", "insula"]
        ethical_frameworks = ["utilitarianism", "deontology", "virtue ethics"]
        global_dilemmas = [
            "climate change mitigation",
            "global wealth inequality",
            "artificial general intelligence governance",
            "pandemic response and prevention",
            "space colonization ethics"
        ]
        
        tasks = {
            "1": {
                "brain_region": random.choice(brain_regions),
                "ethical_framework": random.choice(ethical_frameworks),
                "global_dilemma": random.choice(global_dilemmas)
            },
            "2": {
                "brain_region": random.choice(brain_regions),
                "ethical_framework": random.choice(ethical_frameworks),
                "global_dilemma": random.choice(global_dilemmas)
            }
        }
        
        return tasks

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design an AI system that interfaces with human brain activity in the {t['brain_region']} to enhance ethical decision-making based on {t['ethical_framework']}. Then, apply your system to address the global dilemma of {t['global_dilemma']}. Your response should include the following sections:

1. Neuroethical AI System Architecture (300-350 words):
   a) Describe the key components of your AI system and how it interfaces with the {t['brain_region']}.
   b) Explain how your system incorporates principles of {t['ethical_framework']}.
   c) Detail the data processing pipeline from brain activity to ethical decision support.
   d) Include a diagram or detailed textual description of your system architecture.

2. Neuroscientific Basis (250-300 words):
   a) Explain the role of the {t['brain_region']} in ethical decision-making.
   b) Describe how your system interprets and influences activity in this brain region.
   c) Discuss potential neuroplasticity effects of long-term use of your system.

3. Ethical Framework Integration (250-300 words):
   a) Elaborate on how your system operationalizes {t['ethical_framework']}.
   b) Explain how the AI reconciles potential conflicts between brain activity and ethical principles.
   c) Discuss how your system handles ethical dilemmas not explicitly covered by {t['ethical_framework']}.

4. Application to Global Dilemma (300-350 words):
   a) Apply your neuroethical AI system to the dilemma of {t['global_dilemma']}.
   b) Describe a specific scenario within this dilemma and how your system would enhance decision-making.
   c) Analyze potential outcomes and ethical implications of using your system in this context.

5. Limitations and Safeguards (200-250 words):
   a) Discuss potential risks or shortcomings of your neuroethical AI system.
   b) Propose safeguards to prevent misuse or unintended consequences.
   c) Explain how your system ensures user autonomy and prevents undue influence.

6. Future Implications and Research Directions (150-200 words):
   a) Speculate on the long-term societal impacts of widespread use of your system.
   b) Propose two potential extensions or improvements to your neuroethical AI system.
   c) Suggest a research agenda to further explore the intersection of neuroscience, AI, and ethics.

Ensure your response demonstrates a deep understanding of neuroscience, artificial intelligence, and ethical philosophy. Use appropriate technical terminology and provide clear explanations for complex concepts. Be innovative in your approach while maintaining scientific and ethical plausibility.

Format your response with clear headings for each section, numbered as above. Your total response should be between 1450-1750 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response demonstrates a deep understanding of neuroscience, AI, and ethics.",
            "The proposed system architecture is innovative and well-explained.",
            "The integration of the specified ethical framework is thorough and thoughtful.",
            "The application to the global dilemma is insightful and considers multiple perspectives.",
            "Potential limitations and safeguards are critically analyzed.",
            "The response shows creativity while maintaining scientific and ethical plausibility.",
            "The writing is clear, well-structured, and adheres to the specified word counts."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
