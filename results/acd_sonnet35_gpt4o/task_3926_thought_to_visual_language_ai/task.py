import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        tasks = [
            {
                'abstract_concept': 'Time',
                'cognitive_process': 'Episodic memory',
                'ai_paradigm': 'Transformer architecture'
            },
            {
                'abstract_concept': 'Causality',
                'cognitive_process': 'Reasoning',
                'ai_paradigm': 'Neuro-symbolic AI'
            }
        ]
        return {str(i+1): task for i, task in enumerate(tasks)}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a system that translates abstract thoughts into a universal visual language, then analyze how this system could be implemented in an AI model. Focus on the abstract concept of {t['abstract_concept']}, the cognitive process of {t['cognitive_process']}, and consider implementation using the AI paradigm of {t['ai_paradigm']}. Your response should include:

1. Visual Language Design (250-300 words):
   a) Describe the key elements and structure of your universal visual language.
   b) Explain how your visual language represents abstract concepts, particularly {t['abstract_concept']}.
   c) Discuss how your visual language accounts for cultural and linguistic diversity.

2. Thought-to-Visual Translation Process (250-300 words):
   a) Outline the steps involved in translating abstract thoughts into your visual language.
   b) Explain how your system interfaces with the cognitive process of {t['cognitive_process']}.
   c) Discuss potential challenges in capturing the nuances of abstract thoughts and how your system addresses them.

3. Neuroscientific Basis (200-250 words):
   a) Describe the neuroscientific principles underlying your thought-to-visual translation system.
   b) Explain how your system aligns with current understanding of {t['cognitive_process']} in the brain.
   c) Propose a hypothetical neural mechanism that could support this translation process.

4. AI Implementation Analysis (250-300 words):
   a) Analyze how your thought-to-visual translation system could be implemented using {t['ai_paradigm']}.
   b) Describe the key components and architecture of the AI model.
   c) Explain how the AI model would handle the translation process and generate visual outputs.
   d) Discuss any novel techniques or approaches required for this implementation.

5. Evaluation and Validation (150-200 words):
   a) Propose methods to evaluate the accuracy and effectiveness of your thought-to-visual translation system.
   b) Describe potential experiments to validate the AI model's performance.
   c) Discuss how you would measure the system's ability to handle diverse abstract concepts and cognitive processes.

6. Ethical Implications and Societal Impact (150-200 words):
   a) Analyze potential ethical concerns related to translating thoughts into a universal visual language.
   b) Discuss the societal implications of such a system, including potential benefits and risks.
   c) Propose guidelines for responsible development and use of this technology.

Ensure your response demonstrates a deep understanding of linguistics, cognitive neuroscience, and artificial intelligence. Use appropriate technical terminology and provide clear explanations for complex concepts. Be creative and innovative in your approach while maintaining scientific plausibility.

Format your response with clear headings for each section. Your total response should be between 1250-1550 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response demonstrates a deep understanding of linguistics, cognitive neuroscience, and artificial intelligence.",
            f"The visual language design effectively represents abstract concepts, particularly {t['abstract_concept']}.",
            f"The thought-to-visual translation process integrates well with the cognitive process of {t['cognitive_process']}.",
            "The neuroscientific basis is well-explained and aligns with current understanding.",
            f"The AI implementation analysis using {t['ai_paradigm']} is comprehensive and innovative.",
            "The proposed evaluation methods and ethical considerations are thoughtful and thorough.",
            "The response is well-structured, clear, and uses appropriate technical terminology.",
            "The ideas presented are creative and innovative while maintaining scientific plausibility."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
