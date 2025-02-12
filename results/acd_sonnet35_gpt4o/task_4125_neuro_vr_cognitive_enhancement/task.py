import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        cognitive_functions = [
            {
                'function': 'Working memory',
                'brain_region': 'Prefrontal cortex'
            },
            {
                'function': 'Attention',
                'brain_region': 'Anterior cingulate cortex'
            }
        ]
        
        ai_techniques = [
            'Reinforcement learning',
            'Generative adversarial networks',
            'Federated learning',
            'Neuroevolution'
        ]
        
        return {
            str(i+1): {
                'cognitive_function': function,
                'ai_technique': random.choice(ai_techniques)
            } for i, function in enumerate(cognitive_functions)
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a theoretical neurofeedback-based virtual reality system for cognitive enhancement, focusing on enhancing {t['cognitive_function']['function']} associated with the {t['cognitive_function']['brain_region']}. Your system should incorporate the AI technique of {t['ai_technique']}. Provide your response in the following format:

1. System Architecture (250-300 words):
   a) Describe the key components of your neurofeedback VR system.
   b) Explain how it integrates neurofeedback, virtual reality, and the specified AI technique.
   c) Discuss how your system targets the specified cognitive function and brain region.
   d) Include a high-level diagram or flowchart of your system architecture (described textually).

2. Neurofeedback Mechanism (200-250 words):
   a) Explain the neurofeedback process in your system, including data acquisition and processing.
   b) Describe how your system provides feedback to the user in the virtual environment.
   c) Discuss how the AI technique enhances the neurofeedback loop.

3. Virtual Reality Environment (200-250 words):
   a) Describe the design of your VR environment and how it facilitates cognitive enhancement.
   b) Explain how the environment adapts based on the user's neural activity and performance.
   c) Discuss any novel interaction methods or sensory feedback mechanisms in your VR system.

4. Training Protocol (150-200 words):
   a) Outline a training protocol for users of your system.
   b) Explain how the protocol progressively challenges and enhances the target cognitive function.
   c) Describe how you would measure and track improvements in cognitive performance.

5. Potential Applications (150-200 words):
   a) Propose two potential applications of your neurofeedback VR system beyond general cognitive enhancement.
   b) Explain how these applications could benefit specific populations or address particular challenges.
   c) Discuss any modifications needed to adapt your system for these applications.

6. Ethical Considerations (200-250 words):
   a) Identify potential ethical issues related to cognitive enhancement using your system.
   b) Discuss concerns about equity, access, and potential misuse of the technology.
   c) Propose guidelines for responsible development and use of neurofeedback VR systems.
   d) Consider long-term implications for society if such systems become widespread.

7. Limitations and Future Directions (150-200 words):
   a) Discuss current technological or scientific limitations that might constrain your system.
   b) Propose future research directions to overcome these limitations.
   c) Suggest one potential breakthrough that could significantly advance this field.

Ensure your response demonstrates a deep understanding of neuroscience, virtual reality technology, and artificial intelligence. Use appropriate technical terminology and provide clear explanations for complex concepts. Be innovative in your approach while maintaining scientific plausibility.

Format your response with clear headings for each section. Your total response should be between 1300-1650 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response demonstrates a deep understanding of neuroscience, virtual reality, and artificial intelligence",
            "The system design is innovative, coherent, and scientifically plausible",
            "The integration of neurofeedback, VR, and AI is well-explained and justified",
            "The ethical implications are thoroughly considered",
            "The response addresses all required sections with appropriate depth"
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
