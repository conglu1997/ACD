import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        tasks = [
            {
                "biological_process": "Photosynthesis",
                "environmental_challenge": "Carbon capture and storage",
                "example_organism": "Chloroplasts in plant cells"
            },
            {
                "biological_process": "Whale echolocation",
                "environmental_challenge": "Ocean plastic detection and removal",
                "example_organism": "Sperm whales"
            }
        ]
        return {str(i+1): task for i, task in enumerate(tasks)}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design an AI system inspired by the biological process of {t['biological_process']} (as exemplified by {t['example_organism']}) to address the environmental challenge of {t['environmental_challenge']}. Your response should include the following sections:

1. Biological Process Analysis (200-250 words):
   a) Explain the key mechanisms and principles of {t['biological_process']} in {t['example_organism']}.
   b) Discuss how this process is efficient or effective in nature.
   c) Identify specific aspects that could be valuable for addressing the environmental challenge.

2. AI System Design (250-300 words):
   a) Describe the overall architecture of your biomimetic AI system.
   b) Explain how it incorporates principles from {t['biological_process']}.
   c) Detail how the system addresses the challenge of {t['environmental_challenge']}.
   d) Include a high-level diagram or pseudocode representing a crucial part of your system (describe it textually).

3. Implementation Strategy (200-250 words):
   a) Outline the key steps required to develop and deploy your system.
   b) Discuss any novel AI techniques or algorithms needed.
   c) Address potential challenges in realizing this system and suggest solutions.

4. Environmental Impact Analysis (200-250 words):
   a) Analyze the potential positive impacts of your system on {t['environmental_challenge']}.
   b) Discuss any possible negative consequences or limitations.
   c) Compare your approach to existing non-biomimetic solutions.

5. Scalability and Adaptation (150-200 words):
   a) Explore how your system could be scaled up for global implementation.
   b) Discuss how it might be adapted to address other environmental challenges.

6. Ethical and Societal Implications (150-200 words):
   a) Identify potential ethical concerns related to your biomimetic AI system.
   b) Discuss broader societal impacts of implementing such a system.
   c) Propose guidelines for responsible development and use.

Ensure your response demonstrates a deep understanding of the biological process, environmental science, and artificial intelligence. Use appropriate technical terminology and provide clear explanations for complex concepts. Be innovative in your approach while maintaining scientific plausibility.

Format your response with clear headings for each section, adhering strictly to the word count guidelines provided. Your total response should be between 1150-1450 words.

Include a brief summary (50-100 words) at the end of your response, highlighting the key innovative aspects of your biomimetic AI system and its potential impact on {t['environmental_challenge']}."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response includes a thorough analysis of {t['biological_process']} in {t['example_organism']} and its relevance to {t['environmental_challenge']}",
            f"The AI system design clearly incorporates biomimetic principles from {t['biological_process']}",
            f"The implementation strategy outlines specific steps and addresses at least two potential challenges",
            f"The environmental impact analysis includes at least two positive impacts and one limitation of the proposed system",
            "The response demonstrates creativity and innovation while maintaining scientific plausibility",
            "The ethical and societal implications section identifies at least two potential concerns and proposes at least one guideline for responsible development",
            "The response adheres to the specified word count guidelines for each section",
            "The summary effectively highlights key innovative aspects and potential impact"
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
