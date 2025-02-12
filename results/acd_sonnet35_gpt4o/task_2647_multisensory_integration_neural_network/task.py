import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        problems = [
            {
                "problem": "Autonomous vehicle navigation in complex urban environments",
                "sensory_inputs": ["visual", "auditory", "proprioceptive"],
                "brain_region": "Superior colliculus"
            },
            {
                "problem": "Robotic surgery with haptic feedback",
                "sensory_inputs": ["visual", "tactile", "proprioceptive"],
                "brain_region": "Posterior parietal cortex"
            },
            {
                "problem": "Virtual reality for physical rehabilitation",
                "sensory_inputs": ["visual", "vestibular", "proprioceptive"],
                "brain_region": "Insular cortex"
            },
            {
                "problem": "Assistive technology for the visually impaired",
                "sensory_inputs": ["auditory", "tactile", "olfactory"],
                "brain_region": "Thalamus"
            }
        ]
        return {str(i+1): problem for i, problem in enumerate(random.sample(problems, 2))}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a neural network architecture inspired by the human brain's multisensory integration capabilities, specifically focusing on the {t['brain_region']}. Then, use this architecture to address the problem of {t['problem']}. Your design should integrate {', '.join(t['sensory_inputs'])} inputs. Your response should include the following sections:

1. Neuroscientific Basis (200-250 words):
   a) Explain the role of the {t['brain_region']} in multisensory integration.
   b) Describe how this brain region processes and combines different sensory inputs.
   c) Discuss any known computational principles or neural mechanisms involved.

2. Neural Network Architecture (250-300 words):
   a) Propose a novel neural network architecture inspired by the {t['brain_region']}.
   b) Explain how your architecture mimics the multisensory integration capabilities of this brain region.
   c) Describe how your network processes and combines {', '.join(t['sensory_inputs'])} inputs.
   d) Include a diagram or detailed description of your network's structure.

3. Implementation Strategy (250-300 words):
   a) Outline the main algorithms or computational techniques you would use to implement your architecture.
   b) Explain how you would train your network on multisensory data.
   c) Discuss any challenges in implementing this biologically-inspired system and propose solutions.
   d) Provide a short pseudocode snippet (10-15 lines) illustrating a key aspect of your implementation.

4. Application to {t['problem']} (250-300 words):
   a) Describe how your neural network would be applied to solve the problem of {t['problem']}.
   b) Explain how the integration of {', '.join(t['sensory_inputs'])} inputs contributes to solving this problem.
   c) Discuss potential advantages of your approach compared to traditional methods.
   d) Identify any limitations or potential issues in applying your system to this problem.

5. Ethical Considerations and Future Directions (200-250 words):
   a) Discuss ethical implications of using brain-inspired AI for {t['problem']}.
   b) Address potential biases or limitations in your approach and how they might be mitigated.
   c) Propose two future research directions or applications building on your work.

6. Glossary (100-150 words):
   Provide brief definitions for at least 5 key technical terms used in your response.

Ensure your response demonstrates a deep understanding of neuroscience, machine learning, and the specific problem domain. Be creative and innovative in your approach while maintaining scientific plausibility. Use appropriate technical terminology and provide clear explanations where necessary.

Include at least 5 citations to relevant scientific literature throughout your response, using a consistent citation format.

Format your response with clear headings for each section. Your total response should be between 1250-1550 words.
"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response includes a coherent design for a neural network architecture inspired by the {t['brain_region']} that addresses {t['problem']}",
            f"The architecture clearly incorporates and integrates {', '.join(t['sensory_inputs'])} inputs in a meaningful way",
            "The neuroscientific basis is well-explained and scientifically plausible",
            "The implementation strategy is detailed and includes relevant algorithms or computational techniques",
            "The application to the specified problem is thoroughly described, including advantages and limitations",
            "Ethical considerations are thoughtfully addressed",
            "The response demonstrates deep understanding of neuroscience, machine learning, and the problem domain through appropriate use of technical terminology and clear explanations",
            "The writing is clear, well-structured, adheres to the specified format, and falls within the 1250-1550 word count range",
            "At least 5 relevant scientific citations are included and properly formatted",
            "A glossary with at least 5 key technical terms is provided"
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
