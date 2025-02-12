import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        tasks = [
            {
                "quantum_effect": "quantum coherence",
                "photosynthetic_component": "light-harvesting complexes",
                "environmental_factor": "temperature fluctuations"
            },
            {
                "quantum_effect": "quantum entanglement",
                "photosynthetic_component": "reaction centers",
                "environmental_factor": "pH variations"
            }
        ]
        return {str(i+1): task for i, task in enumerate(random.sample(tasks, k=2))}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design an AI system to optimize the quantum effect of {t['quantum_effect']} in artificial photosynthesis, focusing on {t['photosynthetic_component']} for atmospheric carbon capture. Then, analyze its potential impact on global climate change mitigation, considering the environmental factor of {t['environmental_factor']}. Your response should include the following sections:

1. Quantum Biology Framework (250-300 words):
   a) Explain the role of {t['quantum_effect']} in natural photosynthesis, particularly in {t['photosynthetic_component']}.
   b) Describe how this quantum effect could be leveraged in artificial photosynthesis for carbon capture.
   c) Discuss the challenges of maintaining quantum effects in ambient conditions, especially considering {t['environmental_factor']}.

2. AI System Design (300-350 words):
   a) Propose an AI architecture to optimize {t['quantum_effect']} in artificial photosynthetic systems.
   b) Explain how your AI system would model and predict quantum behavior in {t['photosynthetic_component']}.
   c) Describe the key algorithms or machine learning approaches your system would use.
   d) Detail how the AI would adapt to and mitigate the effects of {t['environmental_factor']}.

3. Carbon Capture Optimization (200-250 words):
   a) Explain how your AI system would optimize carbon capture efficiency.
   b) Provide quantitative estimates of potential improvements in carbon capture rates.
   c) Discuss any trade-offs or limitations in your approach.

4. Climate Impact Analysis (250-300 words):
   a) Analyze the potential impact of your optimized system on global carbon dioxide levels.
   b) Discuss how this technology could contribute to climate change mitigation strategies.
   c) Consider potential secondary effects on global climate systems.

5. Ethical and Practical Considerations (150-200 words):
   a) Discuss ethical implications of using AI-optimized quantum biological systems for geoengineering.
   b) Address potential risks or unintended consequences of the technology.
   c) Propose guidelines for responsible development and deployment.

6. Future Research Directions (150-200 words):
   a) Suggest two specific areas for future research to enhance your system.
   b) Discuss how advancements in quantum computing might further improve your AI system.

Ensure your response demonstrates a deep understanding of quantum biology, artificial intelligence, and climate science. Use appropriate technical terminology and provide clear explanations for complex concepts. Be innovative in your approach while maintaining scientific plausibility.

Your total response should be between 1300-1600 words. Format your answer with clear headings for each section."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response demonstrates a deep understanding of {t['quantum_effect']} in the context of {t['photosynthetic_component']}.",
            "The AI system design is innovative and well-explained, addressing the optimization of quantum effects in artificial photosynthesis.",
            f"The analysis considers the impact of {t['environmental_factor']} on the system's performance.",
            "The climate impact analysis provides quantitative estimates and considers global implications.",
            "Ethical and practical considerations are thoughtfully addressed.",
            "The response is well-structured, coherent, and within the specified word count range."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
