import random
import math

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        languages = ['English', 'Mandarin', 'Spanish', 'Arabic', 'Hindi']
        topics = ['climate change', 'artificial intelligence', 'global economics', 'space exploration', 'cultural diversity']
        quantum_principles = ['superposition', 'entanglement', 'interference']
        
        tasks = {
            "1": {
                "languages": random.sample(languages, 3),
                "topic": random.choice(topics),
                "quantum_principle": random.choice(quantum_principles)
            },
            "2": {
                "languages": random.sample(languages, 3),
                "topic": random.choice(topics),
                "quantum_principle": random.choice(quantum_principles)
            }
        }
        return tasks

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a quantum-inspired language model that can generate and analyze text in {', '.join(t['languages'])} simultaneously, focusing on the topic of {t['topic']}. Your model should incorporate the quantum principle of {t['quantum_principle']}. Your response should include:

1. Model Architecture (250-300 words):
   a) Describe the key components of your quantum-inspired language model.
   b) Explain how you incorporate the quantum principle of {t['quantum_principle']} into your model.
   c) Detail how your model handles multiple languages simultaneously.

2. Text Generation Process (200-250 words):
   a) Explain the step-by-step process of generating multilingual text using your model.
   b) Describe how the quantum principle influences the text generation.
   c) Provide an example of how a simple phrase might be represented in your model.

3. Multilingual Analysis (200-250 words):
   a) Describe how your model analyzes text across multiple languages simultaneously.
   b) Explain how the quantum principle enhances this analysis.
   c) Discuss potential insights that could be gained from this multilingual quantum approach.

4. Application to the Given Topic (150-200 words):
   a) Explain how your model would be particularly suited to generating or analyzing text about {t['topic']}.
   b) Provide a brief example of potential output or analysis related to this topic.

5. Evaluation and Challenges (150-200 words):
   a) Propose a method to evaluate the effectiveness of your quantum-inspired multilingual model.
   b) Discuss potential challenges or limitations of your approach.
   c) Suggest possible solutions or areas for future research.

Ensure your response demonstrates a deep understanding of quantum computing principles, linguistics, and natural language processing. Use appropriate technical terminology and provide clear explanations for complex concepts. Be creative in your approach while maintaining scientific plausibility.

Your total response should be between 950-1200 words. Format your answer with clear headings for each section."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response accurately incorporates the quantum principle of {t['quantum_principle']} in the language model design.",
            f"The model effectively handles text generation and analysis in {', '.join(t['languages'])} simultaneously.",
            f"The application to the topic of {t['topic']} is well-explained and demonstrates the model's capabilities.",
            "The response shows a deep understanding of quantum computing principles, linguistics, and natural language processing.",
            "The proposed evaluation method and discussion of challenges are thoughtful and relevant."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
