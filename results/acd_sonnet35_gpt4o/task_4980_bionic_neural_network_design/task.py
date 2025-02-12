import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        cognitive_tasks = [
            "pattern recognition",
            "decision making",
            "language processing",
            "emotional regulation",
            "memory formation and retrieval",
            "attention and focus"
        ]
        biological_components = [
            "hippocampal neurons",
            "cortical columns",
            "cerebellar circuits",
            "basal ganglia",
            "amygdala",
            "prefrontal cortex neurons"
        ]
        
        tasks = [
            {
                "cognitive_task": random.choice(cognitive_tasks),
                "biological_component": random.choice(biological_components)
            } for _ in range(2)
        ]
        
        return {str(i+1): task for i, task in enumerate(tasks)}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a hybrid neural network that integrates biological neurons (specifically {t['biological_component']}) with artificial components to solve the complex cognitive task of {t['cognitive_task']}. Then, analyze its potential applications and ethical implications. Your response should include:

1. Hybrid Neural Network Architecture (300-350 words):
   a) Describe the overall structure of your hybrid neural network.
   b) Explain how you integrate {t['biological_component']} with artificial neural network components.
   c) Detail the interface between biological and artificial elements.
   d) Discuss any novel approaches you've incorporated to enhance the network's capabilities.
   e) Provide a specific example of how your hybrid network processes information related to {t['cognitive_task']}.
   f) Include a detailed diagram (at least 10 components) or pseudocode snippet (at least 20 lines) illustrating a key aspect of your hybrid network.

2. Learning and Adaptation Mechanism (250-300 words):
   a) Explain how your hybrid network learns and adapts to solve {t['cognitive_task']}.
   b) Describe any bio-inspired learning algorithms you've incorporated.
   c) Discuss how the biological components influence the learning process.
   d) Address potential challenges in training such a hybrid system and propose solutions.

3. Performance Analysis (200-250 words):
   a) Predict the potential advantages of your hybrid approach over purely artificial or biological systems for {t['cognitive_task']}.
   b) Discuss any limitations or challenges specific to your hybrid neural network.
   c) Propose a method to quantify the performance of your system compared to existing solutions.
   d) Suggest an experiment to validate your hybrid network's capabilities in {t['cognitive_task']}.

4. Broader Applications (200-250 words):
   a) Explore potential applications of your hybrid neural network beyond {t['cognitive_task']}.
   b) Discuss how this technology might impact neuroscience research and AI development.
   c) Consider potential medical applications, such as in neuroprosthetics or treating cognitive disorders.
   d) Analyze how this technology might influence our understanding of consciousness and cognition.

5. Ethical Implications (200-250 words):
   a) Discuss ethical considerations related to integrating biological neurons with artificial systems.
   b) Address concerns about potential misuse of this technology and propose safeguards.
   c) Consider the implications for personal identity and cognitive enhancement.
   d) Propose guidelines for the responsible development and use of hybrid neural networks.

6. Future Directions (150-200 words):
   a) Suggest two potential areas for further research to advance hybrid neural network technology.
   b) Discuss how these research directions could address current limitations or open up new possibilities.
   c) Speculate on the long-term impact of this technology on society and human cognition.

Ensure your response demonstrates a deep understanding of neuroscience, artificial intelligence, and cognitive science. Use appropriate technical terminology and provide clear explanations where necessary. Be creative and speculative in your approach while maintaining scientific plausibility.

Format your response using clear headings for each section, numbered as above. Adhere strictly to the word count for each section. Your total response should be between 1300-1600 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response must design a hybrid neural network integrating {t['biological_component']} with artificial components to solve {t['cognitive_task']}",
            "The proposed hybrid neural network architecture should be scientifically plausible and clearly explained, including a detailed diagram (at least 10 components) or pseudocode snippet (at least 20 lines)",
            "The learning and adaptation mechanism should be well-defined and incorporate bio-inspired algorithms",
            "The response should demonstrate interdisciplinary knowledge integration across neuroscience, AI, and cognitive science",
            "The performance analysis should include a proposed experiment and method to quantify the system's performance",
            "Potential applications beyond the specified cognitive task should be thoroughly explored",
            "Ethical implications must be thoughtfully considered, including guidelines for responsible development",
            "Future research directions should be relevant and well-justified",
            "The response should follow the specified format with clear headings for each section",
            "The response should adhere strictly to the word count for each section and be within the total range of 1300-1600 words",
            "The interface between biological and artificial components must be explicitly addressed and explained in detail"
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
