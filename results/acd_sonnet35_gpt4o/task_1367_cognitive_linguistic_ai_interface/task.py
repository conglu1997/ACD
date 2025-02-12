import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        tasks = [
            {
                "cognitive_process": "Analogical reasoning",
                "linguistic_feature": "Metaphor",
                "ai_application": "Natural language understanding"
            },
            {
                "cognitive_process": "Episodic memory",
                "linguistic_feature": "Narrative structure",
                "ai_application": "Conversational AI"
            }
        ]
        return {str(i+1): task for i, task in enumerate(random.sample(tasks, k=2))}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a cognitive-linguistic interface for AI systems that integrates the cognitive process of {t['cognitive_process']}, the linguistic feature of {t['linguistic_feature']}, and applies it to the AI application of {t['ai_application']}. Your response should include:

1. Interface Design (300-350 words):
   a) Describe the key components of your cognitive-linguistic interface.
   b) Explain how it integrates {t['cognitive_process']} and {t['linguistic_feature']}.
   c) Discuss how this integration enhances the AI's capabilities in {t['ai_application']}.
   d) Provide a visual representation or diagram of your interface (use ASCII art or a text-based description).

2. Cognitive-Linguistic Mapping (200-250 words):
   a) Explain how {t['cognitive_process']} is represented in your interface.
   b) Describe how {t['linguistic_feature']} is implemented in the system.
   c) Discuss how these elements interact to create a more intuitive AI interaction.

3. AI Implementation (200-250 words):
   a) Propose how your interface could be implemented in an AI system for {t['ai_application']}.
   b) Discuss potential challenges and solutions in this implementation.
   c) Explain how this implementation might improve upon current approaches in {t['ai_application']}.

4. Human-AI Interaction Analysis (150-200 words):
   a) Describe how users would interact with an AI system using your interface.
   b) Analyze potential benefits and limitations of this interaction method.
   c) Suggest how this interface might influence user perception and trust of AI systems.

5. Ethical Considerations (100-150 words):
   a) Discuss potential ethical implications of implementing cognitive-linguistic interfaces in AI systems.
   b) Address any concerns related to privacy, manipulation, or cognitive influence.

6. Future Research Directions (100-150 words):
   a) Propose two potential research projects that could further develop or validate your interface design.
   b) Briefly describe the methodology and expected outcomes of these projects.

Ensure your response demonstrates a deep understanding of cognitive science, linguistics, and artificial intelligence. Use technical terminology appropriately and provide explanations where necessary. Be creative in your design while maintaining scientific plausibility.

Format your response with clear headings for each section. Your total response should be between 1050-1350 words.
"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response demonstrates a deep understanding of cognitive science, linguistics, and artificial intelligence.",
            "The interface design effectively integrates the specified cognitive process and linguistic feature.",
            "The proposed implementation for AI application is innovative and plausible.",
            "The analysis of human-AI interaction is thoughtful and considers both benefits and limitations.",
            "Ethical considerations are thoroughly addressed.",
            "Future research directions are relevant and well-justified."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
