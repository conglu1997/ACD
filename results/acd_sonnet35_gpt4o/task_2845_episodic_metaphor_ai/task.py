import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        tasks = [
            {
                "domain": "Personal Relationships",
                "context": "First romantic heartbreak",
                "target_concept": "Emotional resilience",
                "example_memory": "The moment you realized your first love was unrequited"
            },
            {
                "domain": "Professional Life",
                "context": "Starting a new job",
                "target_concept": "Adaptability",
                "example_memory": "Your first day at work in an unfamiliar industry"
            }
        ]
        return {str(i+1): task for i, task in enumerate(tasks)}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a hypothetical AI system that simulates human episodic memory to generate and interpret metaphorical language. Apply this system to the domain of {t['domain']}, specifically focusing on the context of {t['context']}. Your task is to use this system to generate and analyze metaphors for the concept of {t['target_concept']}.

Your response should include the following sections:

1. AI System Architecture (300-350 words):
   a) Describe the key components of your AI system, including modules for episodic memory simulation, language processing, and metaphor generation.
   b) Explain how your system represents and stores episodic memories.
   c) Detail the process of how your system generates metaphors based on these memories.
   d) Discuss how your system interprets and understands metaphorical language.
   e) Include a text-based diagram or flowchart illustrating the system's architecture or processes.

2. Episodic Memory Simulation (250-300 words):
   a) Explain how your system simulates the encoding, storage, and retrieval of episodic memories.
   b) Describe how contextual and emotional information is incorporated into these simulated memories.
   c) Discuss how your system handles the temporal aspects of episodic memories.
   d) Provide an example of how your system would represent and process the following episodic memory: "{t['example_memory']}"

3. Metaphor Generation and Analysis (250-300 words):
   a) Provide two example metaphors that your system might generate for {t['target_concept']} in the context of {t['context']}.
   b) Analyze these metaphors, explaining how they relate to the simulated episodic memories and the target concept.
   c) Discuss how your system evaluates the appropriateness and effectiveness of generated metaphors.
   d) Explain how your system would interpret a given metaphor: "{t['target_concept']} is a delicate balance on a tightrope."

4. Cognitive Science Integration (200-250 words):
   a) Explain how your AI system's design is informed by current theories in cognitive science, particularly regarding episodic memory and metaphor comprehension.
   b) Discuss any novel hypotheses about human cognition that your system's design suggests.
   c) Propose an experiment that could test one of these hypotheses.

5. Ethical Implications and Limitations (150-200 words):
   a) Identify potential ethical concerns or misuses of an AI system that can generate and interpret metaphorical language based on simulated personal experiences.
   b) Discuss the limitations of your system and areas for future improvement.
   c) Propose one safeguard to prevent misuse of your system.

6. Interdisciplinary Applications (150-200 words):
   a) Propose two potential applications of your AI system in fields outside of computer science and linguistics.
   b) Briefly explain how these applications could contribute to research or practical problems in those fields.
   c) Describe a potential collaboration between experts in cognitive science and another field to further develop your system.

Ensure your response demonstrates a deep understanding of cognitive science, linguistics, and artificial intelligence. Use appropriate technical terminology and provide clear explanations for complex concepts. Be innovative in your approach while maintaining scientific plausibility.

Format your response with clear headings for each section, numbered as above. Your total response should be between 1300-1600 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response must include all six required sections with appropriate content and word count for each.",
            "The AI system architecture should be innovative, clearly described, and include a text-based diagram or flowchart.",
            "The episodic memory simulation section must include an example of processing the given memory: '{t['example_memory']}'",
            "The metaphor generation and analysis section should include two appropriate metaphors for {t['target_concept']} and an interpretation of the given metaphor.",
            "The cognitive science integration section should propose a specific experiment to test a novel hypothesis.",
            "The ethical implications section must propose a concrete safeguard against misuse.",
            "The interdisciplinary applications section should describe a potential collaboration between cognitive scientists and experts from another field.",
            "The overall response should demonstrate a clear integration of knowledge from cognitive science, linguistics, and artificial intelligence, while being innovative and scientifically plausible."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
