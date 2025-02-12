class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        tasks = {
            "1": {
                "quantum_concept": "Quantum Superposition",
                "linguistic_theory": "Cognitive Semantics",
                "language_task": "Metaphor Generation"
            },
            "2": {
                "quantum_concept": "Quantum Entanglement",
                "linguistic_theory": "Construction Grammar",
                "language_task": "Syntactic Parsing"
            }
        }
        return tasks

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design an AI system that uses quantum computing principles to analyze and generate language, based on the following specifications:

Quantum Concept: {t['quantum_concept']}
Linguistic Theory: {t['linguistic_theory']}
Language Task: {t['language_task']}

Your response should include the following sections:

1. Theoretical Foundation (250-300 words):
   a) Explain the key principles of the given quantum concept and how they might relate to language processing.
   b) Describe the main ideas of the specified linguistic theory and its approach to the given language task.
   c) Propose an innovative way to integrate these quantum and linguistic concepts in an AI system.

2. Quantum-Linguistic AI Architecture (300-350 words):
   a) Design the main components of your AI system, explaining how each incorporates both quantum and linguistic principles.
   b) Describe how your system would represent language using quantum states or operations.
   c) Explain the process by which your system would perform the specified language task using quantum computations.
   d) Address how classical and quantum components of your system would interact.

3. Example Application (200-250 words):
   Provide a detailed example of how your system would process a specific input or generate an output for the given language task. Include both the quantum and linguistic aspects of this process.

4. Advantages and Challenges (200-250 words):
   a) Discuss potential advantages of your quantum-linguistic approach over classical NLP methods.
   b) Identify at least three significant challenges in implementing or scaling your system.
   c) Propose potential solutions or research directions to address these challenges.

5. Ethical and Philosophical Implications (150-200 words):
   a) Discuss the ethical considerations of using quantum principles in language AI.
   b) Explore how your system might influence our understanding of consciousness, meaning, or the nature of language.

6. Evaluation and Validation (150-200 words):
   a) Propose a method to evaluate the performance and accuracy of your quantum-linguistic AI system.
   b) Describe an experiment that could validate the quantum nature of your system's language processing.

Ensure your response demonstrates a deep understanding of both quantum mechanics and linguistics, as well as creative problem-solving in AI design. Use appropriate technical terminology and provide clear explanations of complex concepts. Be innovative in your approach while maintaining scientific plausibility.

Format your response with clear headings for each section, adhering to the word limits provided."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response demonstrates a deep understanding of the specified quantum concept and linguistic theory, accurately explaining their key principles.",
            "The proposed AI architecture innovatively integrates quantum and linguistic concepts in a plausible manner.",
            "The example application clearly illustrates how the system would use quantum computations for the given language task.",
            "The response identifies significant challenges and proposes thoughtful solutions or research directions.",
            "The ethical and philosophical implications are insightfully discussed.",
            "The proposed evaluation method and experiment are well-designed and appropriate for a quantum-linguistic AI system.",
            "The response is well-structured, adhering to the specified word limits and format requirements."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
