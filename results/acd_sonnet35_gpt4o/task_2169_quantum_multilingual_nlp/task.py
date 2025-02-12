import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        languages = ['Mandarin', 'Spanish', 'English', 'Arabic', 'Hindi', 'Bengali', 'Portuguese', 'Russian', 'Japanese', 'Swahili']
        quantum_principles = ['Superposition', 'Entanglement', 'Quantum Tunneling', 'Quantum Interference']
        nlp_tasks = ['Translation', 'Sentiment Analysis', 'Named Entity Recognition', 'Text Generation']
        
        return {
            "1": {
                "languages": random.sample(languages, 3),
                "quantum_principle": random.choice(quantum_principles),
                "nlp_task": random.choice(nlp_tasks)
            },
            "2": {
                "languages": random.sample(languages, 3),
                "quantum_principle": random.choice(quantum_principles),
                "nlp_task": random.choice(nlp_tasks)
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a quantum-based natural language processing system capable of performing {t['nlp_task']} simultaneously across {', '.join(t['languages'])}. Your system should incorporate the quantum principle of {t['quantum_principle']}. Your response should include:

1. System Architecture (250-300 words):
   a) Describe the key components of your quantum NLP system.
   b) Explain how you incorporate {t['quantum_principle']} into your system design.
   c) Discuss how your system handles the simultaneous processing of {', '.join(t['languages'])}.
   d) Provide a high-level diagram of your system architecture (describe it in words).

2. Quantum-Linguistic Integration (200-250 words):
   a) Explain how you map linguistic features of {', '.join(t['languages'])} onto quantum states or processes.
   b) Describe any novel quantum algorithms you've developed for this NLP task.
   c) Discuss how {t['quantum_principle']} enhances the system's ability to perform {t['nlp_task']}.

3. Implementation Challenges (150-200 words):
   a) Identify at least three major challenges in implementing your system.
   b) Propose potential solutions or approaches to address these challenges.
   c) Discuss any trade-offs or limitations in your proposed solutions.

4. Performance Analysis (200-250 words):
   a) Describe how you would evaluate the performance of your quantum NLP system.
   b) Compare the expected performance of your system to classical NLP approaches for {t['nlp_task']}.
   c) Discuss any potential quantum advantages or disadvantages for this specific NLP task.

5. Ethical Considerations and Future Directions (150-200 words):
   a) Discuss potential ethical implications of using quantum computing for multilingual NLP.
   b) Propose two future research directions to enhance or expand your quantum NLP system.
   c) Speculate on how this technology might impact global communication and language processing.

Ensure your response demonstrates a deep understanding of quantum computing principles, linguistics, and natural language processing. Use appropriate technical terminology and provide clear explanations where necessary. Be creative in your approach while maintaining scientific and technological plausibility.

Format your response with clear headings for each section. Your total response should be between 950-1200 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response must include a detailed description of a quantum NLP system for {t['nlp_task']} in {', '.join(t['languages'])}.",
            f"The system design must incorporate the quantum principle of {t['quantum_principle']}.",
            "The response must explain how linguistic features are mapped onto quantum states or processes.",
            "The submission should identify and address implementation challenges.",
            "The response must include a performance analysis comparing the quantum approach to classical NLP methods.",
            "The submission should discuss ethical considerations and future research directions."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
