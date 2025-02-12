import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        scenarios = [
            {
                "context": "Business negotiation",
                "culture_a": "Japanese",
                "culture_b": "Brazilian",
                "communication_goal": "Reaching a mutually beneficial agreement"
            },
            {
                "context": "Academic conference",
                "culture_a": "German",
                "culture_b": "Indian",
                "communication_goal": "Presenting complex research findings"
            }
        ]
        return {
            "1": random.choice(scenarios),
            "2": random.choice(scenarios)
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Analyze and generate multimodal communication strategies for a cross-cultural scenario, then create a novel communication system based on the insights gained. The scenario is a {t['context']} between {t['culture_a']} and {t['culture_b']} cultures, with the communication goal of {t['communication_goal']}. Your response should include:

1. Cultural Communication Analysis (300-350 words):
   a) Compare and contrast the communication styles of the two cultures in the given context.
   b) Identify potential areas of misunderstanding or conflict due to cultural differences.
   c) Analyze how each culture typically uses text, images, and gestures in the given context.

2. Multimodal Strategy Design (300-350 words):
   a) Propose a multimodal communication strategy that combines text, images, and gestures to achieve the communication goal.
   b) Explain how your strategy addresses the cultural differences identified earlier.
   c) Provide specific examples of text, images, and gestures that would be used in your strategy.
   d) Discuss how your strategy leverages cognitive science principles to enhance communication effectiveness.

3. AI-Assisted Implementation (250-300 words):
   a) Describe how an AI system could assist in implementing your multimodal communication strategy.
   b) Explain what types of data and algorithms the AI would need to effectively support cross-cultural communication.
   c) Discuss potential challenges in developing such an AI system and propose solutions.

4. Novel Communication System (300-350 words):
   Based on the insights from your analysis and strategy, create a new communication system that could be used universally across cultures. Your system should:
   a) Incorporate elements from both cultures in the scenario.
   b) Use a combination of textual, visual, and gestural components.
   c) Be designed to minimize cultural misunderstandings.
   d) Have the potential for easy adoption and learning by people from diverse backgrounds.

5. Ethical Considerations and Limitations (200-250 words):
   a) Discuss potential ethical implications of using AI-assisted multimodal communication in cross-cultural contexts.
   b) Analyze possible limitations or drawbacks of your novel communication system.
   c) Propose guidelines for responsible development and use of AI-assisted cross-cultural communication tools.

Ensure your response demonstrates a deep understanding of cultural communication styles, cognitive science principles, and AI capabilities. Use appropriate terminology and provide clear explanations for complex concepts. Be creative in your approach while maintaining scientific and practical plausibility.

Format your response with clear headings for each section, numbered as above. Your total response should be between 1350-1600 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response demonstrates a deep understanding of cultural communication styles, cognitive science principles, and AI capabilities.",
            "The multimodal communication strategy effectively addresses the cultural differences and communication goal in the given scenario.",
            "The novel communication system is creative, well-designed, and has potential for universal adoption.",
            "The analysis of AI-assisted implementation is thorough and considers both potential benefits and challenges.",
            "Ethical considerations and limitations are thoughtfully discussed, with reasonable guidelines proposed."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
