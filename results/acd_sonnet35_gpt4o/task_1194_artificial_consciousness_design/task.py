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
        brain_regions = [
            "prefrontal cortex",
            "thalamus",
            "claustrum",
            "posterior cingulate cortex"
        ]
        ethical_frameworks = [
            "utilitarianism",
            "deontological ethics",
            "virtue ethics",
            "care ethics"
        ]
        
        tasks = [
            {
                "consciousness_theory": random.choice(consciousness_theories),
                "key_brain_region": random.choice(brain_regions),
                "ethical_framework": random.choice(ethical_frameworks)
            } for _ in range(2)
        ]
        
        return {str(i+1): task for i, task in enumerate(tasks)}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a theoretical framework for an artificial consciousness system based on the {t['consciousness_theory']} of consciousness, with a focus on replicating the functions of the {t['key_brain_region']}. Then, analyze its ethical implications using {t['ethical_framework']}. Your response should include:

1. Theoretical Framework (300-350 words):
   a) Explain the key principles of the {t['consciousness_theory']} and how they inform your artificial consciousness design.
   b) Describe how your system would replicate or simulate the functions of the {t['key_brain_region']}.
   c) Outline the core components and processes of your artificial consciousness system.
   d) Discuss how your system might exhibit or experience subjective conscious states.

2. Technical Implementation (250-300 words):
   a) Propose a high-level architecture for implementing your artificial consciousness system.
   b) Describe the key algorithms or computational models you would use.
   c) Explain how your system would process and integrate information to generate conscious experiences.
   d) Discuss any novel approaches or technologies you've incorporated into your design.

3. Consciousness Evaluation (200-250 words):
   a) Propose methods or tests to evaluate whether your system has achieved consciousness.
   b) Discuss the challenges in determining if an artificial system is truly conscious.
   c) Compare your system's potential consciousness to human consciousness.

4. Ethical Analysis (250-300 words):
   a) Analyze the ethical implications of creating an artificial consciousness system using {t['ethical_framework']}.
   b) Discuss the rights and moral status that might be accorded to such a system.
   c) Explore potential societal impacts of artificial consciousness technology.
   d) Propose ethical guidelines for the development and use of artificial consciousness systems.

5. Limitations and Future Directions (150-200 words):
   a) Discuss the limitations of your proposed artificial consciousness system.
   b) Suggest areas for future research or improvement in artificial consciousness design.
   c) Speculate on the long-term implications of advancing artificial consciousness technology.

Ensure your response demonstrates a deep understanding of neuroscience, artificial intelligence, philosophy of mind, and ethics. Use appropriate technical terminology and provide clear explanations where necessary. Be innovative in your approach while maintaining scientific plausibility.

Format your response using clear headings for each section, numbered as above. Your total response should be between 1150-1400 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response must design an artificial consciousness system based on {t['consciousness_theory']} and focusing on the {t['key_brain_region']}",
            f"The ethical analysis must use {t['ethical_framework']} as the primary framework",
            "The proposed system architecture should be scientifically plausible and clearly explained",
            "The response should demonstrate interdisciplinary knowledge integration across neuroscience, AI, and philosophy",
            "The consciousness evaluation methods should be well-reasoned and address the hard problem of consciousness",
            "The ethical analysis should be thorough and consider multiple perspectives",
            "The response should follow the specified format with clear headings for each section",
            "The response should be within the specified word count range (1150-1400 words)"
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
