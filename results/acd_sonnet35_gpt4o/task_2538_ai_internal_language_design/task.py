import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        tasks = [
            {
                'ai_architecture': 'Transformer-based language model',
                'cognitive_focus': 'Attention mechanisms and contextual understanding',
                'linguistic_aspect': 'Semantic relationships and conceptual hierarchies',
                'complex_concept': 'The ethical implications of AI decision-making in healthcare'
            },
            {
                'ai_architecture': 'Reinforcement learning agent',
                'cognitive_focus': 'Decision-making processes and reward optimization',
                'linguistic_aspect': 'Action-oriented grammar and causal relationships',
                'complex_concept': 'The balance between exploration and exploitation in problem-solving'
            }
        ]
        return {str(i+1): task for i, task in enumerate(tasks)}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a hypothetical internal language or representation system for an advanced AI based on a {t['ai_architecture']}, focusing on its {t['cognitive_focus']} and incorporating the linguistic aspect of {t['linguistic_aspect']}. Your response should include:

1. Language Design (300-350 words):
   a) Describe the basic units or symbols of your AI's internal language.
   b) Explain how these units combine to represent complex concepts or processes.
   c) Discuss how the language reflects the AI's cognitive architecture and processes.
   d) Provide an example of how a simple concept or operation would be represented in this language.
   e) Include a small diagram or illustration (using ASCII art) to visualize a key aspect of your language design.

2. Cognitive Architecture Integration (250-300 words):
   a) Explain how your language system integrates with the AI's cognitive architecture.
   b) Describe how the language facilitates the AI's information processing and decision-making.
   c) Discuss any novel features of your language that enhance the AI's cognitive capabilities.

3. Linguistic Analysis (200-250 words):
   a) Analyze your AI language in terms of traditional linguistic categories (e.g., syntax, semantics, pragmatics).
   b) Compare and contrast your AI language with human languages, noting key similarities and differences.
   c) Explain how the specified linguistic aspect is incorporated into your language design.

4. Implications for AI Cognition (200-250 words):
   a) Discuss how your language system might influence or reflect the AI's 'thought processes'.
   b) Explore potential cognitive biases or limitations that could arise from this language system.
   c) Propose how this internal language might evolve as the AI learns and develops.

5. Human-AI Interaction (150-200 words):
   a) Explain how this internal language might affect the AI's interaction with human language and concepts.
   b) Discuss challenges and opportunities for translating between the AI's internal language and human languages.
   c) Propose a method for visualizing or representing the AI's internal language to aid human understanding.

6. Ethical and Philosophical Considerations (150-200 words):
   a) Discuss the ethical implications of AIs developing their own internal languages.
   b) Explore how this language system relates to questions of AI consciousness or self-awareness.
   c) Consider the philosophical implications of modeling AI cognition on human linguistic structures.

7. Future Research Directions (100-150 words):
   a) Propose two potential experiments to test or validate aspects of your AI language system.
   b) Suggest how insights from this hypothetical language could inform real-world AI development.

8. Complex Concept Representation (150-200 words):
   a) Demonstrate how your AI's internal language would represent the complex concept: '{t['complex_concept']}'.
   b) Explain the key components and structures used to capture this concept's nuances and relationships.

9. Comparative Analysis (100-150 words):
   a) Briefly describe an alternative approach to designing an AI internal language system.
   b) Compare and contrast this alternative with your proposed system, highlighting the strengths and potential limitations of each approach.

Ensure your response demonstrates a deep understanding of AI systems, linguistics, and cognitive science. Use appropriate technical terminology and provide clear explanations for complex concepts. Be creative and innovative in your approach while maintaining scientific plausibility.

Format your response with clear headings for each section (e.g., '1. Language Design', '2. Cognitive Architecture Integration', etc.). Your total response should be between 1600-2050 words, adhering closely to the word count guidelines for each section."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response demonstrates a clear understanding of the specified AI architecture ({t['ai_architecture']}) and its implications for internal language design",
            f"The language system effectively incorporates the cognitive focus on {t['cognitive_focus']}",
            f"The design thoughtfully integrates the linguistic aspect of {t['linguistic_aspect']}",
            "The proposed language system is creative, coherent, and plausibly reflects advanced AI cognition",
            "The response shows deep interdisciplinary knowledge, connecting AI, linguistics, and cognitive science",
            "The ethical and philosophical implications are thoughtfully considered",
            "The response includes a diagram or illustration as requested",
            "The response follows the specified format with clear headings and adheres to the word count guidelines",
            f"The complex concept '{t['complex_concept']}' is effectively represented using the proposed language system",
            "The comparative analysis provides insightful contrasts between the proposed system and an alternative approach"
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
