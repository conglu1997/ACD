import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        tasks = [
            {
                "domain1": "Quantum Physics",
                "domain2": "Ecology",
                "problem": "Design a novel ecosystem monitoring system",
                "key_concepts1": ["superposition", "entanglement", "wave function"],
                "key_concepts2": ["biodiversity", "food web", "ecological succession"]
            },
            {
                "domain1": "Neuroscience",
                "domain2": "Artificial Intelligence",
                "problem": "Develop a new approach to machine learning",
                "key_concepts1": ["neural plasticity", "synaptic pruning", "neurotransmitters"],
                "key_concepts2": ["deep learning", "reinforcement learning", "neural networks"]
            }
        ]
        return {str(i+1): task for i, task in enumerate(tasks)}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design an AI system capable of performing conceptual blending, and use it to solve an abstract problem by combining concepts from disparate domains. Your task involves blending concepts from {t['domain1']} and {t['domain2']} to {t['problem']}.

Key concepts to consider:
{t['domain1']}: {', '.join(t['key_concepts1'])}
{t['domain2']}: {', '.join(t['key_concepts2'])}

Your response should include the following sections:

1. Conceptual Blending AI System Design (300-350 words):
   a) Describe the key components of your AI system for conceptual blending.
   b) Explain how your system represents and processes concepts from different domains.
   c) Detail the mechanisms your system uses to identify potential connections between concepts.
   d) Discuss how your system evaluates and refines the blended concepts it generates.

2. Domain Analysis (200-250 words):
   a) Analyze the key concepts, principles, and structures in {t['domain1']}, focusing on the provided key concepts.
   b) Analyze the key concepts, principles, and structures in {t['domain2']}, focusing on the provided key concepts.
   c) Identify potential areas of overlap or complementarity between the two domains.

3. Conceptual Blend Generation (250-300 words):
   a) Describe the process your AI system uses to generate conceptual blends from the two domains.
   b) Present at least two novel conceptual blends that your system might produce.
   c) Explain the reasoning behind each blend, highlighting how elements from both domains are integrated.

4. Problem-Solving Application (300-350 words):
   a) Apply your conceptual blending AI system to {t['problem']}.
   b) Describe a specific solution or approach derived from your conceptual blends.
   c) Explain how this solution integrates elements from both {t['domain1']} and {t['domain2']}.
   d) Discuss potential advantages and limitations of your blended solution.

5. Cognitive and AI Implications (200-250 words):
   a) Analyze how your conceptual blending AI system's approach compares to human cognitive processes in creative problem-solving.
   b) Discuss potential implications of your system for advancing AI reasoning and creativity.
   c) Explore how this approach might contribute to our understanding of human cognition and creativity.

6. Ethical Considerations and Future Directions (150-200 words):
   a) Identify potential ethical concerns or implications of using conceptual blending AI systems for problem-solving.
   b) Discuss limitations of your approach and potential biases that might arise.
   c) Propose two potential enhancements or extensions to your conceptual blending AI system.

Ensure your response demonstrates a deep understanding of both domains, conceptual blending theory, and artificial intelligence. Be creative in your approach while maintaining scientific plausibility. Use appropriate terminology and provide clear explanations for complex concepts.

Format your response with clear headings for each section. The word counts provided are guidelines to ensure comprehensive coverage of each topic, but slight deviations are acceptable as long as all required elements are addressed thoroughly.

Your response will be evaluated based on the following criteria:
1. Depth of understanding of both specified domains and conceptual blending theory.
2. Innovation and scientific plausibility of the AI system design for conceptual blending.
3. Creativity and coherence of the generated conceptual blends.
4. Novelty and effectiveness of the problem-solving application.
5. Quality of analysis regarding cognitive and AI implications.
6. Adherence to the specified format and comprehensive coverage of all required elements.
7. Originality and creativity of ideas while maintaining scientific and practical plausibility.
"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response demonstrates a deep understanding of both {t['domain1']} and {t['domain2']}, incorporating the provided key concepts",
            "The AI system design for conceptual blending is innovative, well-explained, and scientifically plausible",
            "The conceptual blends generated are creative, coherent, and effectively combine elements from both domains",
            f"The problem-solving application presents a novel and well-reasoned solution to {t['problem']} that genuinely integrates concepts from both domains",
            "The discussion of cognitive and AI implications shows critical thinking and insightful analysis",
            "The response adheres to the specified format and comprehensively covers all required elements",
            "The ideas presented are original and creative while maintaining scientific and practical plausibility"
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
