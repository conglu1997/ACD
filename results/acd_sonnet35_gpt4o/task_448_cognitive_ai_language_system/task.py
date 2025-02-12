import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        cognitive_models = [
            {
                "name": "Dual-process theory",
                "description": "A theory proposing that human thinking is governed by two distinct types of cognitive processes: rapid, automatic 'System 1' and slower, more deliberate 'System 2'."
            },
            {
                "name": "Connectionist model",
                "description": "A model that views cognitive processes as the emergent processes of interconnected networks of simple units."
            },
            {
                "name": "Embodied cognition",
                "description": "A theory suggesting that many features of cognition are shaped by aspects of the entire body of the organism."
            },
            {
                "name": "Predictive coding",
                "description": "A theory proposing that the brain constantly generates and updates a mental model of the environment to predict sensory input."
            }
        ]
        return {str(i+1): model for i, model in enumerate(random.sample(cognitive_models, 2))}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a hypothetical AI language processing system based on the cognitive model of {t['name']}. {t['description']}

Your task is to:

1. Describe the architecture of your AI system (200-250 words):
   a) Explain how you incorporate the key principles of the cognitive model into your AI system.
   b) Outline the main components of your system and their functions.
   c) Discuss how your system processes and generates language.

2. Analyze a given text using your AI system (150-200 words):
   Analyze the following quote using your AI system: "To be or not to be, that is the question."
   a) Describe how your system would process and interpret this text.
   b) Explain any unique insights or interpretations that might arise from your cognitive model-based approach.

3. Generate text using your AI system (150-200 words):
   Use your AI system to generate a short paragraph (3-4 sentences) on the topic of "The future of artificial intelligence".
   a) Provide the generated text.
   b) Explain how the cognitive model influenced the generation process and the resulting text.

4. Evaluate limitations and ethical considerations (150-200 words):
   a) Discuss at least two limitations of your AI system.
   b) Identify one potential ethical concern related to using this system for language processing or generation.
   c) Propose a mitigation strategy for the ethical concern you identified.

5. Compare with current AI language models (100-150 words):
   Briefly compare your hypothetical system with current large language models (e.g., GPT-3, BERT):
   a) Identify one potential advantage of your cognitive model-based approach.
   b) Discuss one area where current models might outperform your system.

Ensure your response demonstrates a deep understanding of both cognitive science and AI principles. Use technical terminology appropriately and provide explanations where necessary. Be creative in your approach while maintaining scientific plausibility.

Format your response using the following structure:

1. System Architecture
[Your architecture description here]

2. Text Analysis
[Your analysis here]

3. Text Generation
[Your generated text and explanation here]

4. Limitations and Ethical Considerations
[Your discussion here]

5. Comparison with Current AI Models
[Your comparison here]
"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response includes a coherent description of an AI system based on the {t['name']} cognitive model",
            "The system architecture incorporates key principles of the specified cognitive model",
            "The text analysis demonstrates how the system would process language based on the cognitive model",
            "The text generation example is coherent and reflects the influence of the cognitive model",
            "The limitations, ethical considerations, and comparison with current AI models are thoughtfully discussed",
            "The overall response demonstrates both cognitive science understanding and creative AI system design",
            "The response follows the specified format and word count guidelines"
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
