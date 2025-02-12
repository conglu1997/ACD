import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        tasks = [
            {
                "concept": "time",
                "context": "perception of time passing"
            },
            {
                "concept": "knowledge",
                "context": "accumulation and sharing of information"
            },
            {
                "concept": "freedom",
                "context": "personal autonomy in modern society"
            },
            {
                "concept": "balance",
                "context": "maintaining equilibrium in life and work"
            }
        ]
        return {str(i+1): task for i, task in enumerate(random.sample(tasks, k=2))}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"Design an AI system capable of understanding and generating visual metaphors, then use it to interpret and create a metaphorical image for the abstract concept of {t['concept']} in the context of {t['context']}. Your response should include:\n\n1. System Architecture (250-300 words):\n   a) Describe the overall structure of your AI system for visual metaphor processing.\n   b) Explain how your system integrates natural language processing, visual processing, and abstract reasoning.\n   c) Detail the key components that enable the system to understand and generate visual metaphors.\n   d) Discuss any novel algorithms or techniques specific to metaphorical reasoning across modalities.\n\n2. Metaphor Analysis (200-250 words):\n   a) Explain how your system would analyze and interpret existing visual metaphors.\n   b) Provide an example of how it would break down a simple visual metaphor (e.g., 'time is money' depicted as a clock made of coins).\n   c) Discuss how your system handles the nuances and cultural aspects of metaphorical representations.\n\n3. Metaphor Generation Process (200-250 words):\n   a) Describe the step-by-step process your AI uses to generate a visual metaphor for the given concept ({t['concept']}).\n   b) Explain how the system ensures coherence between the abstract concept and its visual representation.\n   c) Discuss how your AI balances creativity and comprehensibility in metaphor creation.\n\n4. Generated Visual Metaphor (250-300 words):\n   a) Present a detailed description of a visual metaphor your system would generate for the concept of {t['concept']} in the context of {t['context']}.\n   b) Explain the reasoning behind each element of the visual metaphor.\n   c) Discuss how this visual metaphor captures the essence of the abstract concept.\n   d) Address potential cultural or individual variations in interpreting this metaphor.\n\n5. Evaluation and Interpretation (200-250 words):\n   a) Propose methods to evaluate the effectiveness and creativity of the generated visual metaphor.\n   b) Describe how you would validate the system's output against human-created visual metaphors.\n   c) Discuss potential applications of this technology in fields such as education, advertising, or art.\n\n6. Ethical and Cognitive Implications (150-200 words):\n   a) Discuss the potential impact of AI-generated visual metaphors on human cognition and communication.\n   b) Address any ethical considerations related to AI systems interpreting and creating metaphorical representations.\n   c) Explore how this technology might influence our understanding of creativity and abstract thinking.\n\n7. Limitations and Future Directions (150-200 words):\n   a) Identify potential limitations or challenges in your AI visual metaphor system.\n   b) Propose two ways to extend or improve your system in future research.\n   c) Suggest a specific experiment to further explore the relationship between AI, visual processing, and metaphorical thinking.\n\nEnsure your response demonstrates a deep understanding of cognitive science, linguistics, visual processing, and artificial intelligence. Be creative in your approach while maintaining scientific plausibility. Use appropriate technical terminology and provide clear explanations for complex concepts.\n\nFormat your response using clear headings for each section, numbered as above. Your total response should be between 1400-1750 words."

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response demonstrates understanding of visual metaphor processing and generation for the concept of {t['concept']}.",
            "The proposed AI system architecture is coherent and scientifically plausible.",
            "The metaphor analysis and generation processes are explained clearly.",
            "A creative and appropriate visual metaphor is generated for the given concept.",
            "Evaluation methods and ethical considerations are addressed.",
            "The response integrates concepts from cognitive science, linguistics, visual processing, and AI.",
            "The response follows the specified structure and addresses all required points."
        ]
        word_count = len(submission.split())
        if word_count < 1350 or word_count > 1800:  # Allowing a small margin of error
            return 0.0
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
