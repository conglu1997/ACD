import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        brain_regions = [
            "Prefrontal cortex",
            "Temporal lobe",
            "Parietal lobe",
            "Cerebellum"
        ]
        musical_elements = [
            "Rhythm",
            "Harmony",
            "Melody",
            "Timbre"
        ]
        creative_domains = [
            "Visual arts",
            "Writing",
            "Scientific problem-solving",
            "Entrepreneurship"
        ]
        return {
            "1": {
                "brain_region": random.choice(brain_regions),
                "musical_element": random.choice(musical_elements),
                "creative_domain": random.choice(creative_domains)
            },
            "2": {
                "brain_region": random.choice(brain_regions),
                "musical_element": random.choice(musical_elements),
                "creative_domain": random.choice(creative_domains)
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design an AI system that uses neurofeedback and musical theory to enhance human creativity, focusing on the {t['brain_region']} and the musical element of {t['musical_element']}. Then, analyze its potential applications in {t['creative_domain']} and broader implications. Your response should include:

1. System Architecture (300-350 words):
   a) Describe the key components of your neuro-musical AI creativity enhancement system.
   b) Explain how your system interfaces with the {t['brain_region']} to monitor and influence neural activity.
   c) Detail how your system incorporates the musical element of {t['musical_element']} to enhance creativity.
   d) Include a high-level diagram of your system architecture (describe it in words).

2. Neuroscientific Basis (200-250 words):
   a) Explain the current understanding of the {t['brain_region']}'s role in creativity.
   b) Describe how your system's neurofeedback mechanism interacts with this brain region.
   c) Discuss any potential neuroplasticity considerations for long-term use of your system.

3. Musical Theory Integration (200-250 words):
   a) Explain how the musical element of {t['musical_element']} relates to cognitive processes involved in creativity.
   b) Describe the specific techniques your system uses to apply this musical element for creativity enhancement.
   c) Discuss how your system adapts its musical input based on real-time neurofeedback.

4. Application to {t['creative_domain']} (250-300 words):
   a) Provide a specific scenario of how your system could be used to enhance creativity in {t['creative_domain']}.
   b) Describe step-by-step how a user would interact with your system in this scenario.
   c) Analyze the potential benefits and limitations of using your system in this domain.

5. AI and Machine Learning Components (200-250 words):
   a) Explain the role of AI and machine learning in your system's functioning.
   b) Describe any novel algorithms or models your system employs.
   c) Discuss how your system learns and adapts to individual users over time.

6. Ethical Considerations (150-200 words):
   a) Identify potential ethical issues arising from the use of AI to enhance human creativity.
   b) Discuss the implications for authenticity, fairness, and cognitive liberty.
   c) Propose guidelines for the ethical development and use of creativity-enhancing AI systems.

7. Future Developments and Broader Impacts (150-200 words):
   a) Speculate on potential advancements or extensions of your system in the next decade.
   b) Discuss how widespread adoption of such systems might impact society, culture, and human cognition.
   c) Suggest areas for further research in the intersection of neuroscience, music, and AI for creativity enhancement.

Ensure your response demonstrates a deep understanding of neuroscience, music theory, artificial intelligence, and the chosen creative domain. Be innovative in your approach while maintaining scientific plausibility. Use appropriate terminology from all relevant fields and provide clear explanations for complex concepts.

Format your response with clear headings for each section, numbered as above. Your total response should be between 1450-1800 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response includes a detailed and scientifically plausible design for a neuro-musical AI creativity enhancement system that effectively incorporates neurofeedback from the {t['brain_region']} and the musical element of {t['musical_element']}.",
            "The explanation of the neuroscientific basis demonstrates a deep understanding of the specified brain region's role in creativity and how neurofeedback can influence it.",
            f"The integration of musical theory, particularly the element of {t['musical_element']}, is well-explained and logically connected to creativity enhancement.",
            f"The application scenario for {t['creative_domain']} is comprehensive, realistic, and clearly demonstrates the potential benefits and limitations of the system.",
            "The AI and machine learning components of the system are well-described, including novel algorithms or models and adaptive learning capabilities.",
            "The ethical considerations are thoughtfully analyzed, covering issues of authenticity, fairness, and cognitive liberty, with proposed guidelines for responsible use.",
            "The discussion of future developments and broader impacts shows foresight and a nuanced understanding of potential societal and cognitive effects.",
            "The overall response demonstrates a strong interdisciplinary approach, integrating knowledge from neuroscience, music theory, artificial intelligence, and the specified creative domain.",
            "The response is well-structured, following the specified format and word count guidelines for each section.",
            "The proposed system is innovative while maintaining scientific plausibility, and complex concepts are explained clearly using appropriate terminology from all relevant fields."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
