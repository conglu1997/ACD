import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        nlp_tasks = [
            "Sentiment Analysis",
            "Named Entity Recognition",
            "Text Summarization",
            "Question Answering",
            "Machine Translation"
        ]
        return {str(i+1): {"nlp_task": task} for i, task in enumerate(random.sample(nlp_tasks, 2))}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a hypothetical natural language processing system that utilizes quantum entanglement principles to enhance {t['nlp_task']}. Your response should include:

1. Quantum-NLP System Architecture (250-300 words):
   a) Describe the key components of your quantum-enhanced NLP system.
   b) Explain how quantum entanglement is incorporated into the system's design.
   c) Detail how your system interfaces between quantum and classical components.
   d) Include a high-level diagram or pseudocode to illustrate your architecture (describe this textually).

2. Quantum Entanglement in NLP (200-250 words):
   a) Explain how quantum entanglement principles are applied to enhance {t['nlp_task']}.
   b) Describe the potential advantages of using quantum entanglement in this NLP task.
   c) Discuss any novel algorithms or techniques you've developed for this application.

3. Implementation Challenges (150-200 words):
   a) Identify at least three major technical challenges in implementing your system.
   b) Propose potential solutions or research directions to address these challenges.
   c) Discuss any trade-offs or limitations of your proposed solutions.

4. Performance Analysis (150-200 words):
   a) Describe how you would evaluate the performance of your quantum-enhanced NLP system.
   b) Propose metrics to compare your system with classical NLP approaches.
   c) Predict potential improvements in accuracy, speed, or capabilities.

5. Ethical and Societal Implications (150-200 words):
   a) Discuss potential ethical concerns raised by your quantum-enhanced NLP system.
   b) Analyze possible societal impacts of widespread adoption of such technology.
   c) Propose guidelines for responsible development and use of quantum-enhanced NLP.

6. Future Developments (100-150 words):
   a) Speculate on how advancements in quantum computing might further enhance your system.
   b) Propose a novel research direction combining quantum NLP with another scientific field.

Ensure your response demonstrates a deep understanding of quantum physics principles, natural language processing techniques, and creative problem-solving. Use appropriate technical terminology and provide clear explanations where necessary. Be innovative in your approach while maintaining scientific plausibility.

Format your response with clear headings for each section. Your total response should be between 1000-1300 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response should include a clear description of a quantum-enhanced NLP system for {t['nlp_task']}",
            "The system architecture should incorporate quantum entanglement principles",
            "The response should address implementation challenges and propose solutions",
            "The answer should include a performance analysis and comparison with classical NLP approaches",
            "Ethical and societal implications should be discussed",
            "The response should demonstrate interdisciplinary thinking and creative problem-solving",
            "The answer should be scientifically plausible and use appropriate technical terminology"
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
