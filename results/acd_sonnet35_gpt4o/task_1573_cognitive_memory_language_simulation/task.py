import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        scenarios = [
            {
                "language": "Mandarin Chinese",
                "learning_context": "immersive environment",
                "time_frame": "6 months",
                "recall_delay": "2 years"
            },
            {
                "language": "Arabic",
                "learning_context": "formal classroom setting",
                "time_frame": "1 year",
                "recall_delay": "5 years"
            }
        ]
        return {
            "1": random.choice(scenarios),
            "2": random.choice(scenarios)
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design an AI system that simulates human-like memory processes in language acquisition, recall, and reconstruction. Then, apply your system to the following scenario:

Language to be learned: {t['language']}
Learning context: {t['learning_context']}
Learning time frame: {t['time_frame']}
Recall delay: {t['recall_delay']}

Your response should include the following sections:

1. Cognitive Memory Model (200-250 words):
   a) Describe the key components of human memory relevant to language acquisition and recall.
   b) Explain how your AI system models these components, including encoding, storage, and retrieval processes.
   c) Discuss how your model incorporates forgetting curves and memory reconstruction phenomena.

2. AI System Architecture (250-300 words):
   a) Provide a detailed overview of your AI system's architecture.
   b) Explain how each component contributes to simulating human-like memory processes in language learning.
   c) Describe how your system integrates neurolinguistic principles with AI algorithms.
   d) Include a diagram of your architecture (using ASCII art or a clear textual description).

3. Language Acquisition Simulation (200-250 words):
   a) Explain how your system simulates the acquisition of {t['language']} in the given learning context and time frame.
   b) Describe the strategies your AI employs to mimic human language learning processes.
   c) Discuss how your system models the development of vocabulary, grammar, and pronunciation skills.

4. Memory Recall and Reconstruction (200-250 words):
   a) Detail how your system simulates recall of the learned language after the specified delay.
   b) Explain how your AI models the forgetting process and its impact on language skills.
   c) Describe how your system reconstructs partially forgotten language elements.
   d) Provide an example of how a specific language feature might be recalled or reconstructed by your system.

5. Evaluation Metrics (100-150 words):
   a) Propose three specific metrics to evaluate the performance and accuracy of your memory simulation system.
   b) Explain how these metrics capture both cognitive fidelity and linguistic accuracy.

6. Limitations and Ethical Considerations (100-150 words):
   a) Discuss the limitations of your approach in modeling human memory processes.
   b) Address potential ethical implications of simulating human cognitive processes in AI systems.
   c) Consider the potential misuse or misinterpretation of such a system and propose safeguards.

7. Future Research Directions (100-150 words):
   a) Identify two areas for future research to improve the simulation of human memory in language learning and recall.
   b) Suggest potential applications of this technology in fields such as education, psychology, or human-computer interaction.

Ensure your response demonstrates a deep understanding of cognitive psychology, neurolinguistics, and artificial intelligence. Use technical terminology appropriately and provide explanations where necessary. Be creative and innovative in your approach while maintaining scientific plausibility.

Format your response using clear headings for each section, numbered exactly as above. Begin each section with the heading (e.g., '1. Cognitive Memory Model:') followed by your response for that section. Your total response should be between 1150-1500 words, not including the architecture diagram."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response should clearly describe an AI system capable of simulating human-like memory processes in language acquisition, recall, and reconstruction for {t['language']}.",
            "The cognitive memory model and AI system architecture should be scientifically plausible and well-explained.",
            "The response should demonstrate a deep understanding of cognitive psychology, neurolinguistics, and AI system design.",
            "The language acquisition simulation and memory recall/reconstruction processes should be logically described and relevant to the given scenario.",
            "Evaluation metrics, limitations, ethical considerations, and future research directions should be thoughtfully addressed.",
            "The response should use appropriate technical terminology and provide clear explanations for complex concepts."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
