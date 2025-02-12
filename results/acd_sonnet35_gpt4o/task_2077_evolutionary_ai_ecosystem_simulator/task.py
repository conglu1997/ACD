import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        ecosystems = [
            {
                "ecosystem_type": "coral reef",
                "evolutionary_focus": "adaptation to ocean acidification"
            },
            {
                "ecosystem_type": "tropical rainforest",
                "evolutionary_focus": "response to rising temperatures"
            }
        ]
        return {
            "1": random.choice(ecosystems),
            "2": random.choice(ecosystems)
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a hypothetical AI system that simulates and accelerates evolutionary processes in a {t['ecosystem_type']} ecosystem, focusing on {t['evolutionary_focus']}. Then, analyze its potential impacts and ethical implications. 

Note: An LLM (Large Language Model) is an AI model trained on vast amounts of text data to understand and generate human-like text.

Your response should include the following sections:

1. AI System Design (300-350 words):
   a) Describe the key components and architecture of your AI system.
   b) Explain how it models and accelerates evolutionary processes.
   c) Detail how it incorporates genetic algorithms, machine learning, and ecosystem modeling.
   d) Discuss how the system handles complex interactions between species and environmental factors.
   e) Include at least one equation or mathematical model related to your AI system or the evolutionary process it simulates.
   f) Discuss potential limitations or challenges in your AI system design.

2. Evolutionary Simulation Process (250-300 words):
   a) Explain how your system simulates genetic variation, natural selection, and adaptation.
   b) Describe how it accelerates evolutionary timescales while maintaining ecological validity.
   c) Discuss how the system accounts for epigenetic factors and environmental influences on evolution.

3. Ecosystem Impact Analysis (250-300 words):
   a) Predict potential short-term and long-term impacts of accelerated evolution on the {t['ecosystem_type']}.
   b) Analyze how {t['evolutionary_focus']} might affect biodiversity and ecosystem stability.
   c) Discuss potential cascading effects on interconnected ecosystems.

4. Ethical Implications (200-250 words):
   a) Identify at least three ethical concerns raised by this technology.
   b) Discuss the potential for unintended consequences and ecological disruption.
   c) Address the ethics of human intervention in accelerating natural processes.

5. Safeguards and Guidelines (200-250 words):
   a) Propose safeguards to prevent misuse or unintended ecological damage.
   b) Suggest guidelines for responsible development and use of evolutionary AI systems.
   c) Discuss how to balance scientific advancement with ecological preservation.

6. Future Applications and Research Directions (150-200 words):
   a) Propose two potential applications of this technology beyond ecological research.
   b) Suggest areas for future research to enhance the system's capabilities and safety.
   c) Discuss how this technology might inform or change our understanding of evolution.

Ensure your response demonstrates a deep understanding of evolutionary biology, artificial intelligence, and ecological systems. Use appropriate scientific terminology and provide clear explanations for complex concepts. Be innovative in your approach while maintaining scientific plausibility and addressing ethical concerns.

Format your response with clear headings for each section, numbered as above. Your total response should be between 1350-1650 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response demonstrates a deep understanding of evolutionary biology, artificial intelligence, and ecological systems.",
            "The AI system design is innovative, scientifically plausible, and clearly explained, including at least one relevant equation or mathematical model.",
            "The evolutionary simulation process is well-described and accounts for complex biological factors.",
            "The ecosystem impact analysis is thorough and considers multiple ecological factors.",
            "Ethical implications are thoughtfully discussed with consideration of multiple perspectives.",
            "Proposed safeguards and guidelines are practical and address key concerns.",
            "Future applications and research directions are creative and relevant.",
            "The response is well-structured, coherent, and adheres to the specified format and word count.",
            "Potential limitations or challenges in the AI system design are discussed."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
