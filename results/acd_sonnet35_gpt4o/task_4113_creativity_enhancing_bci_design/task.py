import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        creative_domains = [
            "Visual Arts",
            "Music Composition",
            "Scientific Discovery",
            "Literary Writing",
            "Architectural Design"
        ]
        cognitive_processes = [
            "Divergent Thinking",
            "Analogical Reasoning",
            "Conceptual Blending",
            "Insight Formation",
            "Cognitive Flexibility"
        ]
        ethical_principles = [
            "Autonomy",
            "Fairness",
            "Transparency",
            "Non-maleficence",
            "Beneficence"
        ]
        return {
            "1": {
                "creative_domain": random.choice(creative_domains),
                "cognitive_process": random.choice(cognitive_processes),
                "ethical_principle": random.choice(ethical_principles)
            },
            "2": {
                "creative_domain": random.choice(creative_domains),
                "cognitive_process": random.choice(cognitive_processes),
                "ethical_principle": random.choice(ethical_principles)
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a hypothetical brain-computer interface (BCI) for enhancing human creativity, focusing on the domain of {t['creative_domain']} and the cognitive process of {t['cognitive_process']}. Then, analyze its potential applications and implications, paying special attention to the ethical principle of {t['ethical_principle']}. Your response should include the following sections:

1. BCI Design (300-350 words):
   a) Describe the key components and functioning of your BCI system.
   b) Explain how it interfaces with the brain to enhance {t['cognitive_process']}.
   c) Detail how the system is specifically tailored for {t['creative_domain']}.
   d) Discuss any novel features that distinguish your design from existing BCIs.

2. Neuroscientific Basis (250-300 words):
   a) Explain the neurological mechanisms involved in {t['cognitive_process']}.
   b) Describe how your BCI interacts with these mechanisms to enhance creativity.
   c) Discuss any potential neuroplastic changes that might result from using your BCI.

3. Creative Process Enhancement (250-300 words):
   a) Provide a detailed scenario of how a user in {t['creative_domain']} would interact with the BCI.
   b) Explain how the BCI enhances specific aspects of the creative process in this domain.
   c) Discuss potential short-term and long-term effects on creative output and cognitive abilities.

4. Ethical Analysis (250-300 words):
   a) Examine the ethical implications of your BCI, focusing on the principle of {t['ethical_principle']}.
   b) Discuss potential conflicts between individual benefits and societal concerns.
   c) Propose guidelines for the ethical development and use of creativity-enhancing BCIs.

5. Societal Impact (200-250 words):
   a) Analyze how widespread adoption of your BCI might impact {t['creative_domain']} and society at large.
   b) Discuss potential changes in creative industries, education, and cognitive enhancement.
   c) Address concerns about inequality of access and potential cognitive divides.

6. Limitations and Future Directions (200-250 words):
   a) Identify current technological or neuroscientific limitations of your BCI design.
   b) Propose two potential advancements or modifications for future development.
   c) Suggest a research agenda for further exploring the intersection of BCIs and creativity enhancement.

Ensure your response demonstrates a deep understanding of neuroscience, brain-computer interfaces, creativity research, and ethics. Use appropriate technical terminology and provide clear explanations for complex concepts. Be innovative in your approach while maintaining scientific plausibility.

Format your response with clear headings for each section. Your total response should be between 1450-1750 words.
"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The BCI design must focus on enhancing creativity in the domain of {t['creative_domain']}.",
            f"The system must specifically target the cognitive process of {t['cognitive_process']}.",
            f"The ethical analysis must thoroughly examine the principle of {t['ethical_principle']}.",
            "The response must include a clear description of the BCI's components and functioning.",
            "The neuroscientific basis for the BCI's operation must be well-explained.",
            "The response must include a detailed scenario of how the BCI would be used in the specified creative domain.",
            "The societal impact analysis must consider both positive and negative potential consequences.",
            "The response must identify limitations and propose future directions for research and development.",
            "The proposed BCI design must be innovative while maintaining scientific plausibility.",
            "The response must be well-structured with clear headings and adhere to the specified word count range."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
