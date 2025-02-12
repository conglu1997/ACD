import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        scenarios = [
            {
                "planet_type": "Ocean world with subsurface liquid water",
                "life_form": "Microbial colonies exhibiting collective behavior",
                "human_context": "First manned mission to the exoplanet"
            },
            {
                "planet_type": "Rocky planet with dense atmosphere and extreme pressure",
                "life_form": "Silicon-based crystalline entities with unknown level of sentience",
                "human_context": "Robotic probe mission with potential for sample return"
            }
        ]
        return {
            "1": random.choice(scenarios),
            "2": random.choice(scenarios)
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design and analyze an ethical framework for a first contact scenario with potential extraterrestrial life, considering the following context:

Planet Type: {t['planet_type']}
Life Form: {t['life_form']}
Human Context: {t['human_context']}

Your response should include the following sections:

1. Scientific Assessment (250-300 words):
   a) Analyze the potential characteristics and capabilities of the life form based on the given information.
   b) Discuss the challenges and opportunities presented by the planet type for both the life form and human exploration.
   c) Propose three hypotheses about the life form's biology, ecology, or potential intelligence.

2. Ethical Framework Design (300-350 words):
   a) Develop a comprehensive ethical framework for approaching this first contact scenario.
   b) Explain how your framework balances scientific curiosity, respect for potential life, and human interests.
   c) Discuss how your framework addresses potential conflicts between different ethical principles.
   d) Incorporate perspectives from at least three different philosophical or cultural traditions in your framework.

3. First Contact Protocol (250-300 words):
   a) Outline a step-by-step protocol for initial interaction or observation of the life form.
   b) Explain how each step in your protocol reflects the ethical framework you've designed.
   c) Discuss potential risks and mitigation strategies for both humans and the extraterrestrial life form.

4. Decision-Making Scenarios (200-250 words):
   a) Present two ethical dilemmas that could arise during the mission, based on your scientific assessment.
   b) Analyze these dilemmas using your ethical framework, explaining potential courses of action and their justifications.

5. Long-term Implications (200-250 words):
   a) Discuss the potential long-term consequences of this first contact for humanity and the extraterrestrial life.
   b) Analyze how this discovery might impact human society, philosophy, and our understanding of life in the universe.
   c) Propose guidelines for ongoing interaction or non-interaction with the extraterrestrial life form.

6. Critique and Reflection (150-200 words):
   a) Identify potential weaknesses or biases in your ethical framework and protocols.
   b) Discuss how alternative perspectives might challenge your approach.
   c) Suggest areas for further research or refinement in exoplanet ethics.

Ensure your response demonstrates a deep understanding of astrobiology, ethics, and space exploration. Use appropriate terminology and provide clear explanations for complex concepts. Be creative and speculative in your approach while maintaining scientific plausibility and ethical rigor.

Format your response with clear headings for each section, numbered as above. Your total response should be between 1350-1650 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response demonstrates a deep understanding of astrobiology, ethics, and space exploration, using appropriate terminology and concepts.",
            "The scientific assessment is well-reasoned and speculative while maintaining plausibility given the scenario.",
            "The ethical framework is comprehensive, incorporating multiple philosophical perspectives and addressing potential conflicts.",
            "The first contact protocol is detailed and clearly reflects the proposed ethical framework.",
            "The decision-making scenarios present complex ethical dilemmas with well-reasoned analyses.",
            "The discussion of long-term implications is thoughtful and considers a wide range of potential consequences.",
            "The critique and reflection section demonstrates self-awareness and openness to alternative perspectives.",
            "The response balances creativity and speculation with scientific and ethical rigor throughout all sections.",
            "The response follows the specified format with clear headings and falls within the specified word count range."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
