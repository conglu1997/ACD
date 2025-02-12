import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        tasks = [
            {
                "memory_type": "episodic memory",
                "neural_mechanism": "hippocampal replay",
                "ml_application": "reinforcement learning",
                "existing_approach": "experience replay in deep Q-networks"
            },
            {
                "memory_type": "working memory",
                "neural_mechanism": "prefrontal cortex oscillations",
                "ml_application": "attention mechanisms in neural networks",
                "existing_approach": "transformer architecture in natural language processing"
            }
        ]
        return {str(i+1): task for i, task in enumerate(random.sample(tasks, k=2))}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a novel memory encoding system based on neuroscientific principles and apply it to enhance machine learning algorithms. Focus on {t['memory_type']} and the neural mechanism of {t['neural_mechanism']}. Your goal is to apply this to improve {t['ml_application']}. Your response should include the following sections:

1. Neuroscientific Basis (200-250 words):
   a) Explain the key features of {t['memory_type']} and how it functions in the human brain.
   b) Describe the neural mechanism of {t['neural_mechanism']} and its role in memory formation and retrieval.
   c) Discuss any relevant theories or models from cognitive neuroscience that inform your approach.

2. Memory Encoding System Design (250-300 words):
   a) Propose a novel memory encoding system inspired by {t['memory_type']} and {t['neural_mechanism']}.
   b) Describe the key components and processes of your encoding system.
   c) Explain how your system mimics or improves upon biological memory processes.
   d) Discuss potential advantages of your system over traditional computer memory architectures.

3. Information Theoretic Analysis (150-200 words):
   a) Analyze your memory encoding system from an information theory perspective.
   b) Discuss concepts such as information capacity, compression, and noise resilience.
   c) Compare the theoretical efficiency of your system to existing memory encoding methods.

4. Machine Learning Application (200-250 words):
   a) Describe how your memory encoding system could be applied to enhance {t['ml_application']}.
   b) Explain the potential benefits and challenges of integrating your system into existing ML frameworks.
   c) Propose a specific algorithm or model that would particularly benefit from your encoding system.
   d) Compare your approach to the existing approach of {t['existing_approach']}.

5. Implementation and Evaluation (150-200 words):
   a) Outline a high-level approach for implementing your memory encoding system in a computational framework.
   b) Propose metrics and experiments to evaluate the performance of your system in the context of {t['ml_application']}.
   c) Discuss potential challenges in implementation and how they might be addressed.

6. Ethical Considerations and Future Directions (100-150 words):
   a) Address any ethical implications of your neuroscience-inspired memory encoding system.
   b) Suggest areas for future research or potential applications beyond machine learning.

Ensure your response demonstrates a deep understanding of neuroscience, computer science, and information theory. Be creative in your approach while maintaining scientific plausibility and coherence across all sections of your response.

Format your response with clear headings for each section and number your paragraphs within each section for easy reference. Include at least one specific example or application in each section to illustrate your points.

Total word count should be between 1050-1350 words. Include a word count at the end of your response."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response demonstrates a deep understanding of neuroscience, computer science, and information theory.",
            "The proposed memory encoding system is novel, well-explained, and plausibly inspired by the specified neuroscientific principles.",
            "The information theoretic analysis is sound and insightful.",
            "The application to machine learning is clearly explained and shows potential for meaningful improvement.",
            "The implementation and evaluation plan is well-thought-out and feasible.",
            "Ethical considerations are appropriately addressed.",
            "The response includes specific examples or applications in each section.",
            "The proposed approach is compared to the existing approach mentioned in the instructions."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
