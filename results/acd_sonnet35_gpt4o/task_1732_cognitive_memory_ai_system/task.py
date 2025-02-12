import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        memory_processes = [
            "Encoding",
            "Storage",
            "Retrieval"
        ]
        learning_domains = [
            "Language acquisition",
            "Motor skill learning",
            "Abstract concept formation"
        ]
        tasks = {}
        for i in range(2):
            tasks[str(i+1)] = {
                "memory_process": random.choice(memory_processes),
                "learning_domain": random.choice(learning_domains)
            }
        return tasks

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design an AI system that mimics human memory consolidation processes, with a focus on the {t['memory_process']} aspect of memory. Then, apply this system to enhance learning in the domain of {t['learning_domain']}. Your response should include:

1. System Architecture (300-350 words):
   a) Describe the key components of your AI memory system.
   b) Explain how it models the interplay between short-term and long-term memory.
   c) Detail how it incorporates the {t['memory_process']} process.
   d) Provide a diagram or pseudocode representation of a key component in your system.

2. Neuroscientific Basis (200-250 words):
   a) Explain the neuroscientific principles underlying your system's design.
   b) Discuss how your system models specific brain structures or processes involved in memory consolidation.
   c) Address any simplifications or abstractions made in translating biological processes to AI.

3. Learning Enhancement Application (250-300 words):
   a) Describe how your system could be applied to enhance learning in {t['learning_domain']}.
   b) Explain the specific mechanisms by which your system would improve learning outcomes.
   c) Provide a detailed case study or example scenario illustrating your system's application.
   d) Discuss any potential limitations or challenges in applying your system to this domain.

4. Comparative Analysis (200-250 words):
   a) Compare your AI memory system to the Long Short-Term Memory (LSTM) neural network architecture.
   b) Discuss the potential advantages and disadvantages of your bio-inspired approach.
   c) Speculate on how your system might perform compared to human learners in the specified domain.

5. Evaluation Method (150-200 words):
   a) Propose a method for evaluating the effectiveness of your system in enhancing learning.
   b) Describe specific metrics or experiments you would use to measure performance.
   c) Discuss how you would validate your system's fidelity to human memory processes.

6. Ethical Considerations (150-200 words):
   a) Identify potential ethical implications of using AI systems that mimic human cognitive processes.
   b) Discuss any privacy concerns related to AI systems with human-like memory capabilities.
   c) Propose guidelines for the responsible development and use of such systems.

7. Future Developments (150-200 words):
   a) Suggest two potential improvements or expansions to your system.
   b) Discuss how emerging technologies in neuroscience or AI could enhance your system's capabilities.
   c) Propose a related cognitive process that could be modeled using a similar approach.

Ensure your response demonstrates a deep understanding of cognitive neuroscience, artificial intelligence, and learning theories. Be creative in your approach while maintaining scientific plausibility. Use appropriate technical terminology and provide clear explanations for complex concepts.

Format your response with clear headings for each section, numbered as above. Your total response should be between 1400-1750 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response includes all seven required sections with appropriate content",
            f"The system design clearly incorporates the {t['memory_process']} process and addresses {t['learning_domain']}",
            "The response includes a diagram or pseudocode representation of a key system component",
            "The learning enhancement application includes a detailed case study or example scenario",
            "The comparative analysis specifically compares the proposed system to LSTM architecture",
            "The response proposes a concrete method for evaluating the system's effectiveness",
            "The response demonstrates a deep understanding of cognitive neuroscience, AI, and learning theories",
            "The response is creative, scientifically plausible, and well-explained"
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
