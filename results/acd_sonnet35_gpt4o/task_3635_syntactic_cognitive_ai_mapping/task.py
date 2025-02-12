import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        cognitive_states = [
            {
                "state": "Decision Making",
                "description": "The process of choosing between two or more courses of action"
            },
            {
                "state": "Analogical Reasoning",
                "description": "The process of identifying and transferring relational information from a source to a target domain"
            }
        ]
        return {
            "1": random.choice(cognitive_states),
            "2": random.choice(cognitive_states)
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design an AI system that maps syntactic structures to the cognitive process of {t['state']}. Your task has the following parts:

1. Syntactic-Cognitive Mapping (250-300 words):
   a) Identify at least three key syntactic structures that could represent aspects of {t['state']}.
   b) Explain how each syntactic structure maps to a specific aspect of the cognitive process.
   c) Provide examples of how these mappings might appear in natural language.

2. AI System Design (300-350 words):
   a) Describe the architecture of an AI system that can recognize and generate language reflecting {t['state']} based on your syntactic-cognitive mapping.
   b) Explain how your system would process input text to identify the relevant cognitive state.
   c) Detail how your system would generate text that reflects this cognitive state.
   d) Include a high-level diagram or pseudocode representing your system architecture (describe it textually).

3. Analysis and Generation Example (200-250 words):
   a) Provide a sample text input that reflects {t['state']}.
   b) Walk through how your AI system would analyze this input, identifying the relevant syntactic structures and mapping them to aspects of the cognitive process.
   c) Demonstrate how your system would generate a new text reflecting the same cognitive state but with different content.

4. Evaluation and Limitations (150-200 words):
   a) Propose a method to evaluate the accuracy and effectiveness of your AI system in mapping syntax to {t['state']}.
   b) Discuss potential limitations of your approach and suggest areas for future improvement.

5. Cognitive Science Implications (100-150 words):
   a) Discuss how your syntactic-cognitive mapping and AI system might contribute to our understanding of human cognition.
   b) Propose a hypothesis about {t['state']} that could be tested using your system.

Ensure your response demonstrates a deep understanding of linguistics, cognitive science, and AI. Use appropriate technical terminology and provide clear explanations for complex concepts. Be creative in your approach while maintaining scientific plausibility.

Format your response with clear headings for each section. Your total response should be between 1000-1250 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response demonstrates a deep understanding of syntactic structures and how they can be mapped to cognitive processes.",
            "The AI system design is innovative, well-explained, and plausibly capable of performing the required tasks.",
            "The analysis and generation example effectively illustrates how the proposed system would work in practice.",
            "The evaluation method and discussion of limitations show critical thinking about the proposed approach.",
            "The cognitive science implications and proposed hypothesis are insightful and scientifically grounded.",
            "The overall response is well-structured, clear, and within the specified word limit."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
