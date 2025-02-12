import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        environments = [
            {
                "name": "Coral Reefs",
                "challenge": "Ocean acidification and rising temperatures",
                "microorganism": "Genetically engineered algae"
            },
            {
                "name": "Urban Air",
                "challenge": "Air pollution and smog",
                "microorganism": "Modified bacteria"
            },
            {
                "name": "Contaminated Soil",
                "challenge": "Heavy metal pollution",
                "microorganism": "Engineered fungi"
            },
            {
                "name": "Freshwater Systems",
                "challenge": "Eutrophication and algal blooms",
                "microorganism": "Synthetic cyanobacteria"
            }
        ]
        return {str(i+1): env for i, env in enumerate(random.sample(environments, 2))}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a hypothetical AI system that facilitates symbiotic relationships between humans and {t['microorganism']} for environmental restoration of {t['name']}, addressing the challenge of {t['challenge']}. Then, analyze its potential impacts and ethical implications. Your response should include:

1. AI System Architecture (300-350 words):
   a) Describe the key components of your AI system for facilitating human-microorganism symbiosis.
   b) Explain how the system integrates knowledge from biotechnology, environmental science, and human physiology.
   c) Detail how the AI ensures safe and effective symbiosis between humans and the engineered microorganisms.
   d) Include a brief diagram (described in text) illustrating the main features of your system.
   e) Discuss any novel approaches or technologies used in your design.

2. Symbiosis Mechanism (250-300 words):
   a) Explain the biological mechanism of the symbiotic relationship between humans and the {t['microorganism']}.
   b) Describe how this symbiosis addresses the environmental challenge of {t['challenge']} in {t['name']}.
   c) Discuss how the AI system monitors and maintains the health of both the human host and the microorganism.
   d) Address potential risks or side effects of the symbiosis and how the AI mitigates them.

3. Environmental Impact Analysis (200-250 words):
   a) Predict the potential short-term and long-term impacts of your system on {t['name']}.
   b) Analyze how the symbiosis might affect biodiversity and ecosystem stability.
   c) Discuss any potential cascading effects on interconnected ecosystems.
   d) Explain how the AI system measures and verifies the environmental impact.

4. Ethical Implications (200-250 words):
   a) Identify at least three ethical concerns raised by this technology.
   b) Discuss the potential for unintended consequences on human health and the environment.
   c) Address the ethics of human enhancement and ecological intervention.
   d) Propose guidelines for responsible development and use of human-microorganism symbiosis technology.

5. Societal Impact (150-200 words):
   a) Analyze how this technology might change human relationships with the environment.
   b) Discuss potential socioeconomic implications of widespread adoption.
   c) Consider how it might affect environmental policies and regulations.

6. Future Developments (150-200 words):
   a) Propose two potential advancements or extensions of your AI system.
   b) Suggest areas for future research to enhance the system's capabilities and safety.
   c) Speculate on how this technology might evolve over the next few decades.

Ensure your response demonstrates a deep understanding of biotechnology, artificial intelligence, and environmental science. Use appropriate scientific terminology and provide clear explanations for complex concepts. Be innovative in your approach while maintaining scientific plausibility and addressing ethical concerns.

Format your response with clear headings for each section, numbered as above. Your total response should be between 1250-1550 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response includes a coherent design for an AI system facilitating symbiosis between humans and {t['microorganism']} for environmental restoration of {t['name']}",
            f"The symbiosis mechanism effectively addresses the challenge of {t['challenge']}",
            "The environmental impact analysis is comprehensive and scientifically plausible",
            "The ethical implications are thoroughly discussed with at least three concerns identified",
            "The societal impact analysis considers multiple aspects of human-environment relationships",
            "The response demonstrates interdisciplinary knowledge integration and creative problem-solving",
            "The proposed future developments are innovative and plausible",
            "The response follows the specified format, uses clear headings for each section, and adheres to the 1250-1550 word count guideline"
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
