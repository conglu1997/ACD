import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        biosemiotic_systems = [
            {
                'name': 'Plant-Pollinator Communication',
                'description': 'The complex signaling system between flowering plants and their pollinators, involving visual, olfactory, and tactile cues.'
            },
            {
                'name': 'Bacterial Quorum Sensing',
                'description': 'The ability of bacteria to communicate and coordinate behavior via signaling molecules.'
            },
            {
                'name': 'Epigenetic Gene Regulation',
                'description': 'The system of chemical modifications to DNA and histones that can alter gene expression without changing the DNA sequence.'
            },
            {
                'name': 'Immune System Recognition',
                'description': 'The complex system of signaling and recognition used by the immune system to distinguish self from non-self.'
            }
        ]
        
        tasks = random.sample(biosemiotic_systems, 2)
        return {str(i+1): {'system': system} for i, system in enumerate(tasks)}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design an AI architecture inspired by biosemiotic principles, focusing on the following biological signaling system:

{t['system']['name']}
System description: {t['system']['description']}

Your task is to create an innovative AI architecture that incorporates key aspects of this biosemiotic system to enhance AI's understanding of context and intentionality. Your response should include:

1. Biosemiotic Analysis (200-250 words):
   a) Explain the key semiotic processes in the given biological system.
   b) Identify the types of signs and meanings involved.
   c) Describe how context and intentionality are represented in this system.

2. AI Architecture Design (300-350 words):
   a) Propose a novel AI architecture inspired by the biosemiotic system.
   b) Describe at least four key components of your architecture and their interactions.
   c) Explain how your design incorporates the semiotic principles identified earlier.
   d) Detail how your architecture enhances AI's ability to understand context and intentionality.

3. Implementation Strategy (200-250 words):
   a) Outline a potential method for implementing your AI architecture.
   b) Discuss any novel algorithms or data structures required.
   c) Explain how your implementation could be trained or optimized.

4. Application Scenario (150-200 words):
   a) Describe a specific AI application that could benefit from your biosemiotic architecture.
   b) Explain how the application's performance or capabilities would be enhanced.
   c) Discuss any potential challenges in applying your architecture to this scenario.

5. Comparative Analysis (200-250 words):
   Compare your proposed architecture with a current AI approach (e.g., transformer models, reinforcement learning) in terms of:
   a) Ability to understand and generate context-dependent meaning
   b) Potential for intentionality or goal-directed behavior
   c) Scalability and adaptability to different domains
   d) Interpretability and explainability

6. Ethical and Philosophical Implications (150-200 words):
   a) Discuss the ethical implications of creating AI systems with enhanced understanding of meaning and intentionality.
   b) Explore how your architecture might impact our understanding of machine consciousness or intelligence.
   c) Propose guidelines for responsible development and use of biosemiotic AI systems.

Ensure your response demonstrates a deep understanding of both biosemiotics and artificial intelligence. Be creative in your approach while maintaining scientific plausibility and addressing potential limitations. Use appropriate technical terminology and provide clear explanations where necessary.

Aim for a total response between 1200-1500 words. Organize your answer using clear headings for each section."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response demonstrates a deep understanding of biosemiotic principles and their application to AI.",
            "The proposed AI architecture is innovative and clearly inspired by the given biological signaling system.",
            "The design effectively addresses the enhancement of AI's understanding of context and intentionality.",
            "The implementation strategy and application scenario are well-reasoned and plausible.",
            "The comparative analysis shows insightful connections and distinctions with current AI approaches.",
            "The discussion of ethical and philosophical implications is thoughtful and comprehensive.",
            "The response is well-structured, clear, and adheres to the specified word count and section guidelines."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
