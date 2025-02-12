import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        brain_regions = [
            {
                "region": "Hippocampus",
                "function": "Memory formation and spatial navigation",
                "problem": "Improving navigation systems for autonomous vehicles"
            },
            {
                "region": "Prefrontal Cortex",
                "function": "Executive function and decision making",
                "problem": "Enhancing strategic decision-making in business AI"
            },
            {
                "region": "Visual Cortex",
                "function": "Visual processing and object recognition",
                "problem": "Developing more accurate medical image analysis systems"
            },
            {
                "region": "Cerebellum",
                "function": "Motor control and learning",
                "problem": "Improving robotic movement and adaptation in dynamic environments"
            }
        ]
        return {
            "1": random.choice(brain_regions),
            "2": random.choice(brain_regions)
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a neural network architecture inspired by the {t['region']} and its function of {t['function']}. Then, apply this architecture to the problem of {t['problem']}. Your task has the following parts:

1. Neurocognitive Architecture Design (250-300 words):
   a) Describe the key features of your neural network architecture, explaining how it mimics the structure and function of the {t['region']}.
   b) Explain how your architecture incorporates the cognitive function of {t['function']}.
   c) Discuss any novel elements in your design that differ from traditional neural network architectures.

2. Implementation for Problem Solving (200-250 words):
   a) Explain how you would apply your neurocognitive architecture to the problem of {t['problem']}.
   b) Describe the input and output structures of your system.
   c) Discuss any data preprocessing or feature engineering techniques you would use.

3. Training and Optimization (150-200 words):
   a) Propose a training methodology for your system, considering the unique aspects of your architecture.
   b) Discuss potential challenges in training and how you would address them.
   c) Suggest optimization techniques that align with the neurocognitive inspiration of your system.

4. Performance Analysis (150-200 words):
   a) Describe how you would evaluate the performance of your system on the given problem.
   b) Propose metrics that capture both the problem-solving capability and the neurocognitive fidelity of your system.
   c) Compare the potential advantages and limitations of your approach to traditional deep learning methods.

5. Ethical Considerations and Future Directions (150-200 words):
   a) Discuss potential ethical implications of using brain-inspired AI for the given problem.
   b) Propose two future research directions that could extend or improve your neurocognitive AI system.

Ensure your response demonstrates a deep understanding of neuroscience, cognitive functions, and AI architectures. Use technical terminology appropriately and provide explanations where necessary. Be creative in your approach while maintaining scientific and technological plausibility.

Format your response using clear headings for each section."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response demonstrates a comprehensive understanding of the {t['region']}'s structure and function.",
            f"The neural network architecture clearly incorporates principles related to {t['function']}.",
            f"The proposed implementation for {t['problem']} is well-explained and feasible.",
            "The training and optimization strategies are appropriate for the neurocognitive architecture.",
            "The performance analysis includes relevant metrics for both problem-solving and neurocognitive fidelity.",
            "Ethical considerations are thoughtfully discussed, and future research directions are innovative and relevant.",
            "The response maintains scientific rigor while showcasing creativity in system design and problem-solving.",
            "The response is well-structured with clear headings for each section as requested."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
