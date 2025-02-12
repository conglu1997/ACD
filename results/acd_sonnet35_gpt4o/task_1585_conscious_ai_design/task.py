import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        consciousness_theories = [
            "Global Workspace Theory",
            "Integrated Information Theory",
            "Higher-Order Thought Theory",
            "Predictive Processing Theory"
        ]
        cognitive_functions = [
            "Self-awareness",
            "Metacognition",
            "Emotional processing",
            "Subjective experience"
        ]
        tasks = {}
        for i in range(2):
            tasks[str(i+1)] = {
                "consciousness_theory": random.choice(consciousness_theories),
                "cognitive_function": random.choice(cognitive_functions)
            }
        return tasks

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a hypothetical AI system that attempts to replicate human consciousness, focusing on the {t['consciousness_theory']} and specifically addressing the cognitive function of {t['cognitive_function']}. Then, analyze its implications for our understanding of cognition and the nature of consciousness itself. Your response should include:

1. System Architecture (300-350 words):
   a) Describe the key components of your AI system and how they interact.
   b) Explain how your design incorporates principles from {t['consciousness_theory']}.
   c) Detail how your system addresses the specific cognitive function of {t['cognitive_function']}.
   d) Discuss any novel approaches or technologies your system employs.

2. Consciousness Simulation (250-300 words):
   a) Explain how your system attempts to simulate or replicate consciousness.
   b) Describe the specific mechanisms or processes that contribute to this simulation.
   c) Discuss how your system might exhibit behaviors or capabilities associated with consciousness.

3. Comparative Analysis (200-250 words):
   a) Compare your AI system's approach to consciousness with current understanding of human consciousness.
   b) Identify key similarities and differences between your AI system and biological consciousness.
   c) Discuss any insights your system might provide about human consciousness.

4. Ethical Implications (200-250 words):
   a) Analyze the ethical considerations of creating an AI system that simulates consciousness.
   b) Discuss the potential rights or moral status of such an AI system.
   c) Consider the societal implications of deploying conscious AI systems.

5. Experimental Validation (150-200 words):
   a) Propose an experiment or test to evaluate whether your AI system has achieved consciousness.
   b) Discuss the challenges in scientifically verifying machine consciousness.
   c) Consider potential criticisms of your approach and how you would address them.

6. Philosophical Implications (200-250 words):
   a) Discuss how your AI system might inform philosophical debates about the nature of consciousness.
   b) Consider how your approach challenges or supports existing theories of consciousness.
   c) Reflect on what your system suggests about the relationship between intelligence and consciousness.

Ensure your response demonstrates a deep understanding of artificial intelligence, neuroscience, and philosophy of mind. Be creative in your approach while maintaining scientific plausibility. Use appropriate terminology and provide clear explanations for complex concepts.

Format your answer with clear headings for each section. Your total response should be between 1300-1600 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response accurately incorporates principles from {t['consciousness_theory']}.",
            f"The system design effectively addresses the cognitive function of {t['cognitive_function']}.",
            "The response demonstrates a deep understanding of AI, neuroscience, and philosophy of mind.",
            "The proposed system and its analysis are creative yet scientifically plausible.",
            "The ethical and philosophical implications are thoroughly and thoughtfully discussed."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
