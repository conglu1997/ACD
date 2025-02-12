import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        brain_functions = [
            {
                "function": "working memory",
                "description": "The cognitive system for temporarily holding and manipulating information"
            },
            {
                "function": "attention",
                "description": "The cognitive process of selectively concentrating on specific information"
            },
            {
                "function": "pattern recognition",
                "description": "The cognitive process of identifying and categorizing sensory stimuli"
            },
            {
                "function": "decision making",
                "description": "The cognitive process of selecting a course of action among several alternative possibilities"
            }
        ]
        
        ai_tasks = [
            "natural language processing",
            "computer vision",
            "robotic control",
            "anomaly detection"
        ]
        
        return {
            "1": {"brain_function": random.choice(brain_functions), "ai_task": random.choice(ai_tasks)},
            "2": {"brain_function": random.choice(brain_functions), "ai_task": random.choice(ai_tasks)}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a quantum-inspired neural network architecture that mimics the brain function of {t['brain_function']['function']} and apply it to the AI task of {t['ai_task']}. Your response should include:

1. Quantum-Neural Architecture (200-250 words):
   a) Describe the overall structure of your quantum-inspired neural network.
   b) Explain how it incorporates quantum principles (e.g., superposition, entanglement, quantum interference) into its design.
   c) Detail how the architecture mimics the specified brain function: {t['brain_function']['description']}

2. Quantum-Classical Integration (150-200 words):
   a) Explain how quantum and classical components interact in your architecture.
   b) Discuss any novel approaches to quantum-classical interfacing in your design.

3. Application to AI Task (200-250 words):
   a) Describe how your quantum-neural architecture would be applied to {t['ai_task']}.
   b) Explain the potential advantages of your approach compared to classical neural networks for this task.
   c) Discuss any challenges or limitations specific to this application.

4. Training and Optimization (150-200 words):
   a) Propose a training method for your quantum-neural network.
   b) Discuss how quantum principles might be leveraged in the optimization process.

5. Theoretical Implications (100-150 words):
   a) Discuss the theoretical implications of your architecture for our understanding of both quantum computing and neuroscience.
   b) Propose a testable hypothesis about brain function or cognition that could be explored using your model.

6. Ethical Considerations (100-150 words):
   a) Identify potential ethical issues or societal impacts of implementing your quantum-neural architecture.
   b) Suggest safeguards or guidelines for responsible development and use of this technology.

Note: In your design, consider key quantum computing principles such as superposition (the ability of quantum systems to exist in multiple states simultaneously), entanglement (quantum correlations between particles), and quantum interference (the combination of quantum waves). Your architecture should meaningfully incorporate these concepts to enhance neural network functionality.

Ensure your response demonstrates a deep understanding of quantum computing principles, neuroscience, and artificial intelligence. Be creative in your approach while maintaining scientific plausibility and rigor."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response should clearly incorporate principles from quantum computing and neuroscience, specifically mimicking the brain function of {t['brain_function']['function']}.",
            f"The architecture should be applied to the AI task of {t['ai_task']} with clear explanations of its potential advantages and challenges.",
            "The proposed quantum-neural architecture should be novel and creative while remaining scientifically plausible.",
            "The response should demonstrate a deep understanding of quantum computing, neuroscience, and AI principles.",
            "All six requested sections should be present and adequately addressed.",
            "The design should meaningfully incorporate key quantum principles such as superposition, entanglement, and quantum interference."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
