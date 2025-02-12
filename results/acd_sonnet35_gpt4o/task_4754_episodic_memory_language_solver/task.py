import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        problems = [
            "Optimize urban transportation",
            "Mitigate the effects of climate change",
            "Improve global education accessibility",
            "Enhance cybersecurity in critical infrastructure"
        ]
        memory_types = [
            "Autobiographical",
            "Semantic",
            "Procedural",
            "Episodic"
        ]
        narrative_elements = [
            "Character development",
            "Plot structure",
            "Setting manipulation",
            "Conflict resolution"
        ]
        
        tasks = {
            "1": {
                "problem": random.choice(problems),
                "memory_type": random.choice(memory_types),
                "narrative_element": random.choice(narrative_elements)
            },
            "2": {
                "problem": random.choice(problems),
                "memory_type": random.choice(memory_types),
                "narrative_element": random.choice(narrative_elements)
            }
        }
        return tasks

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design an AI system that uses principles of episodic memory and narrative structure to solve complex problems by generating and manipulating story-based representations. Your task is to apply this system to the problem of {t['problem']}, focusing on {t['memory_type']} memory and the narrative element of {t['narrative_element']}.

For example, if addressing urban transportation using autobiographical memory and character development, your system might generate a story about a city resident's daily commute experiences, using character growth to represent evolving transportation solutions.

Your response should include the following sections:

1. System Architecture (300-350 words):
   a) Describe the key components of your AI system for episodic memory-based problem-solving.
   b) Explain how your system integrates principles of {t['memory_type']} memory and {t['narrative_element']}.
   c) Detail the mechanisms your system uses to generate and manipulate story-based representations.
   d) Discuss how your system evaluates and selects the most relevant narrative elements for problem-solving.

2. Problem Representation (250-300 words):
   a) Generate a story-based representation of the problem "{t['problem']}" using your system.
   b) Explain how this representation incorporates elements of {t['memory_type']} memory.
   c) Describe how the narrative element of {t['narrative_element']} is utilized in this representation.
   d) Discuss how this story-based approach provides new insights or perspectives on the problem.

3. Solution Generation (300-350 words):
   a) Describe how your system manipulates the story-based representation to generate potential solutions.
   b) Provide at least two novel solution ideas derived from your narrative approach.
   c) Explain how these solutions leverage the principles of {t['memory_type']} memory and {t['narrative_element']}.
   d) Discuss the potential advantages and limitations of using this narrative-based approach for problem-solving.

4. Cognitive and AI Implications (200-250 words):
   a) Analyze how your system's approach compares to human cognitive processes in problem-solving and storytelling.
   b) Discuss potential implications of your system for advancing AI reasoning and creativity capabilities.
   c) Explore how this approach might contribute to our understanding of human cognition and memory.

5. Ethical Considerations and Limitations (150-200 words):
   a) Identify potential ethical concerns or implications of using story-based AI systems for problem-solving.
   b) Discuss limitations of your approach and potential biases that might arise from narrative-based reasoning.
   c) Propose guidelines for the responsible development and use of episodic memory-based AI systems.

6. Future Directions (150-200 words):
   a) Suggest two potential enhancements or extensions to your episodic memory-based AI system.
   b) Propose a novel application of your system in a different field or domain.
   c) Discuss how emerging technologies or research in cognitive science might further improve narrative-based AI reasoning.

Ensure your response demonstrates a deep understanding of cognitive psychology, narrative theory, artificial intelligence, and the specific problem domain involved. Be creative in your approach while maintaining scientific plausibility. Use appropriate terminology and provide clear explanations for complex concepts.

Remember to balance creativity with scientific plausibility throughout your design. Your system should be innovative but grounded in current understanding of cognitive science and AI capabilities.

Format your response with clear headings for each section. Your total response should be between 1350-1700 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response demonstrates a deep understanding of cognitive psychology, narrative theory, and artificial intelligence.",
            "The proposed AI system effectively integrates principles of episodic memory and narrative structure for problem-solving.",
            "The story-based representation of the problem is creative and insightful.",
            "The generated solutions leverage the narrative approach in a novel and effective way.",
            "The analysis of cognitive and AI implications is thorough and well-reasoned.",
            "Ethical considerations and limitations are addressed comprehensively.",
            "Future directions and potential applications are innovative and well-considered.",
            "The response is well-structured, clear, and within the specified word count.",
            "The proposed system demonstrates creativity while maintaining scientific plausibility."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
