import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        problems = [
            {
                'network_scale': 'Planetary',
                'information_type': 'Climate data',
                'constraint': 'Minimize energy consumption'
            },
            {
                'network_scale': 'Neural',
                'information_type': 'Sensory input',
                'constraint': 'Maximize processing speed'
            }
        ]
        return {str(i+1): problem for i, problem in enumerate(problems)}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a theoretical communication network inspired by both quantum entanglement and biological synapses, then apply it to solve a complex information routing problem at the {t['network_scale']} scale for {t['information_type']}, while adhering to the constraint to {t['constraint']}. Your response should include the following sections:

1. Theoretical Framework (300-350 words):
   a) Describe the key principles from quantum entanglement and synaptic transmission that inform your network design.
   b) Explain how you integrate these principles to create a novel communication paradigm.
   c) Discuss any theoretical limitations or challenges in combining quantum and biological concepts.

2. Network Architecture (250-300 words):
   a) Outline the structure and components of your biophysical information network.
   b) Explain how information is encoded, transmitted, and received in your system.
   c) Describe any unique features that arise from the integration of quantum and biological principles.
   d) Provide a simple diagram or pseudocode representation of a key mechanism in your network.

3. Information Routing Solution (250-300 words):
   a) Analyze the given information routing problem and its challenges.
   b) Explain how your biophysical network addresses this problem at the specified scale.
   c) Describe how your solution adheres to the given constraint.
   d) Compare your approach to traditional information routing methods.

4. Implementation and Scaling (200-250 words):
   a) Discuss the theoretical and technological requirements for implementing your network.
   b) Explain how your system could be scaled up or down for different applications.
   c) Address any potential obstacles in practical implementation and propose solutions.

5. Implications and Applications (150-200 words):
   a) Explore the potential impact of your biophysical network on fields such as telecommunications, computing, or neuroscience.
   b) Propose two novel applications of your network beyond the given routing problem.
   c) Discuss any ethical considerations or societal implications of this technology.

6. Future Research Directions (150-200 words):
   a) Suggest two areas for further research to enhance or expand your biophysical network.
   b) Explain how these research directions could address current limitations or unlock new capabilities.
   c) Speculate on how this technology might evolve in the next decade.

Ensure your response demonstrates a deep understanding of quantum physics, neurobiology, and information theory. Use appropriate technical terminology and provide clear explanations for complex concepts. Be creative and innovative in your approach while maintaining scientific plausibility.

Format your response with clear headings for each section. Your total response should be between 1300-1600 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response demonstrates a deep understanding of quantum entanglement, synaptic transmission, and information theory.",
            f"The proposed network integrates principles from quantum physics and neurobiology in a novel and plausible way.",
            f"The solution addresses the given {t['network_scale']} scale problem for routing {t['information_type']} while adhering to the constraint to {t['constraint']}.",
            "The response includes creative and scientifically plausible ideas for implementation, scaling, and future applications.",
            "All required sections (Theoretical Framework, Network Architecture, Information Routing Solution, Implementation and Scaling, Implications and Applications, and Future Research Directions) are adequately addressed."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
