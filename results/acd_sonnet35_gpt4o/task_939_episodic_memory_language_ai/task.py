import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        scenarios = [
            {
                'context': 'job interview',
                'memory_type': 'personal achievements'
            },
            {
                'context': 'emergency situation',
                'memory_type': 'past experiences of danger'
            }
        ]
        return {str(i+1): scenario for i, scenario in enumerate(scenarios)}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design an AI system that simulates episodic memory and its influence on language use and decision-making, then apply it to the scenario of a {t['context']} with a focus on {t['memory_type']}. Your response should include:

1. System Architecture (250-300 words):
   a) Describe the key components of your AI system for simulating episodic memory.
   b) Explain how your system integrates episodic memory with language processing and decision-making modules.
   c) Discuss any novel elements in your design that enable realistic simulation of memory-influenced cognition.

2. Episodic Memory Model (200-250 words):
   a) Explain how your system represents and stores episodic memories.
   b) Describe the mechanisms for memory encoding, retrieval, and updating.
   c) Discuss how your model accounts for memory distortions, forgetting, and emotional salience.

3. Language Processing Integration (200-250 words):
   a) Explain how episodic memories influence language generation and understanding in your system.
   b) Describe how context-dependent language use is achieved through memory integration.
   c) Provide an example of how a specific memory might alter language output in the given scenario.

4. Decision-Making Mechanism (200-250 words):
   a) Describe how your system uses episodic memories to inform decision-making processes.
   b) Explain the algorithms or models used for reasoning under uncertainty with memory input.
   c) Discuss how your system balances reliance on memory with current situational data.

5. Scenario Application (250-300 words):
   a) Apply your AI system to the given scenario of a {t['context']}.
   b) Provide a step-by-step walkthrough of how your system would process the scenario, including:
      - Relevant memories it might access
      - How these memories influence language use
      - Decision-making processes informed by memories
   c) Include example outputs (e.g., generated language, decisions made) at each step.

6. Evaluation and Limitations (150-200 words):
   a) Propose methods to evaluate the realism and effectiveness of your system's memory simulation.
   b) Discuss potential limitations of your approach and areas for future improvement.
   c) Consider ethical implications of AI systems with human-like episodic memory capabilities.

Ensure your response demonstrates a deep understanding of cognitive psychology, neuroscience, and artificial intelligence. Be creative in your approach while maintaining scientific and technological plausibility. Format your response using clear headings for each section."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response includes a detailed design of an AI system simulating episodic memory and its influence on language and decision-making.",
            "The system architecture is clearly described with well-explained components and integration methods.",
            "The episodic memory model is well-defined, including representation, storage, and retrieval mechanisms.",
            "The integration of episodic memory with language processing is thoroughly explained with concrete examples.",
            "The decision-making mechanism incorporating episodic memory is clearly described and justified.",
            f"The system is effectively applied to the given scenario of a {t['context']}, with a detailed walkthrough and example outputs.",
            "Evaluation methods, limitations, and ethical implications are thoughtfully discussed."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
