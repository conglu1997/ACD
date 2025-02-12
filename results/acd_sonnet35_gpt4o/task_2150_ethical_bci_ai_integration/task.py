import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        cognitive_enhancements = [
            {
                "enhancement": "Memory Augmentation",
                "brain_region": "Hippocampus",
                "ai_technique": "Deep Learning"
            },
            {
                "enhancement": "Attention Boosting",
                "brain_region": "Prefrontal Cortex",
                "ai_technique": "Reinforcement Learning"
            }
        ]
        return {str(i+1): enhancement for i, enhancement in enumerate(random.sample(cognitive_enhancements, 2))}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design an AI system that integrates with a brain-computer interface (BCI) to enhance human cognitive abilities, specifically focusing on {t['enhancement']} by interfacing with the {t['brain_region']} and utilizing {t['ai_technique']} as the primary AI technique. Then, analyze its ethical implications and propose safeguards. Your response should include the following sections:

1. System Architecture (300-350 words):
   a) Describe the key components of your BCI-AI integration system.
   b) Explain how the system interfaces with the {t['brain_region']} to achieve {t['enhancement']}.
   c) Detail how {t['ai_technique']} is implemented in your system.
   d) Discuss any novel features that distinguish your system from existing BCI technologies.
   e) Provide a high-level diagram of your system architecture (described in words).

2. Cognitive Enhancement Mechanism (250-300 words):
   a) Explain the neuroscientific basis for your chosen cognitive enhancement.
   b) Describe how your system processes and interprets brain signals.
   c) Detail the feedback loop between the AI system and the human brain.
   d) Provide a step-by-step example of how your system would enhance a specific cognitive task.

3. AI Learning and Adaptation (200-250 words):
   a) Explain how your AI system learns and adapts to individual users.
   b) Discuss at least three potential challenges in maintaining consistent performance across different users.
   c) Propose methods for ensuring the AI's learning process remains safe and controlled.

4. Ethical Analysis (250-300 words):
   a) Identify at least four potential ethical concerns raised by your system.
   b) Analyze the implications of these concerns for individuals and society.
   c) Discuss how your system might impact concepts of human agency and cognitive liberty.
   d) Consider at least two potential misuse scenarios and their consequences.

5. Safeguards and Governance (200-250 words):
   a) Propose at least three technical safeguards to address the ethical concerns you identified.
   b) Suggest policy or regulatory frameworks to govern the development and use of such systems.
   c) Discuss how to ensure equitable access to this technology while preventing exploitation.

6. Future Implications (150-200 words):
   a) Speculate on how widespread adoption of your system might impact society and human evolution.
   b) Propose two potential advancements or extensions of your system for future research.
   c) Discuss how this technology might influence other fields such as education, healthcare, or workforce dynamics.

Ensure your response demonstrates a deep understanding of neuroscience, artificial intelligence, ethics, and human-computer interaction. Use appropriate technical terminology and provide clear explanations for complex concepts. Be innovative in your approach while maintaining scientific plausibility and ethical responsibility.

Remember to address both the technical aspects of the system and its ethical implications thoroughly.

Format your response with clear headings for each section. Your total response should be between 1350-1650 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response includes a well-designed system architecture that integrates BCI with AI for {t['enhancement']}",
            f"The cognitive enhancement mechanism is clearly explained and scientifically plausible",
            f"The AI learning and adaptation process is thoroughly described and addresses at least three potential challenges",
            "The ethical analysis is comprehensive, identifying at least four potential concerns and their implications",
            "At least three technical safeguards are proposed, and governance frameworks are practical and address the identified ethical concerns",
            "The response demonstrates a deep understanding of neuroscience, AI, ethics, and human-computer interaction",
            "The proposed system and analysis are innovative while remaining scientifically grounded",
            "The future implications are thoughtfully considered and speculative yet plausible",
            "The response follows the specified format and is within the word count range (1350-1650 words)",
            "The response adequately addresses both the technical aspects of the system and its ethical implications"
        ]
        score = sum([eval_with_llm_judge(instructions, submission, [criterion]) for criterion in criteria])
        return score / len(criteria)
