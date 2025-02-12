import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        tasks = [
            {
                "memory_type": "episodic memory",
                "brain_region": "hippocampus",
                "cognitive_process": "pattern separation and completion"
            },
            {
                "memory_type": "working memory",
                "brain_region": "prefrontal cortex",
                "cognitive_process": "attention and executive control"
            }
        ]
        return {str(i+1): task for i, task in enumerate(tasks)}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a novel cognitive architecture inspired by recent neuroscientific findings, focusing on {t['memory_type']} formation and retrieval processes in the {t['brain_region']}, with emphasis on the cognitive process of {t['cognitive_process']}. Your response should include:

1. Neuroscientific Foundation (250-300 words):
   a) Summarize recent findings related to {t['memory_type']} and the {t['brain_region']}.
   b) Explain the role of {t['cognitive_process']} in memory formation and retrieval.
   c) Discuss relevant neural network structures or dynamics involved, including any computational models that have been proposed.

2. Cognitive Architecture Design (300-350 words):
   a) Propose a novel cognitive architecture that models {t['memory_type']} processes.
   b) Describe at least four key components and their interactions within your architecture.
   c) Explain how your design incorporates the neuroscientific principles discussed earlier.
   d) Detail how your architecture simulates or implements {t['cognitive_process']}.
   e) Provide a simple diagram or schematic representation of your proposed architecture (describe it textually).

3. Computational Implementation (250-300 words):
   a) Outline a potential method for implementing your cognitive architecture computationally, specifying programming languages or frameworks you would use.
   b) Discuss any novel algorithms or data structures required for your implementation.
   c) Explain how your implementation could be validated against empirical neuroscientific data, proposing a specific experiment or dataset.

4. Comparative Analysis (200-250 words):
   Compare your proposed architecture with an existing cognitive architecture. Some well-known architectures include:
   - ACT-R (Adaptive Control of Thought-Rational): A cognitive architecture that aims to define the basic and irreducible cognitive and perceptual operations that enable the human mind.
   - SOAR (State, Operator And Result): A cognitive architecture for developing systems that exhibit intelligent behavior.
   - CLARION (Connectionist Learning with Adaptive Rule Induction ON-line): A cognitive architecture that aims to capture all the essential cognitive processes within a unified framework.
   
   Choose one of these or another established architecture and compare based on:
   a) Biological plausibility
   b) Computational efficiency
   c) Scalability
   d) Ability to model {t['memory_type']} and {t['cognitive_process']}
   
   Discuss at least two potential advantages and two limitations of your design relative to the existing architecture.

5. Practical Applications (150-200 words):
   a) Propose two potential applications of your cognitive architecture in real-world scenarios.
   b) Explain how these applications could benefit from the specific features of your design.
   c) Discuss any potential challenges in implementing these applications.

6. Ethical Implications (100-150 words):
   a) Discuss at least two potential ethical concerns arising from the development or application of your cognitive architecture.
   b) Propose guidelines or safeguards to address these ethical issues.

7. Limitations and Future Directions (100-150 words):
   a) Identify potential limitations or challenges in your proposed architecture.
   b) Suggest areas for future research or improvement.
   c) Propose one novel research question that arises from your design.

Ensure your response demonstrates a deep understanding of neuroscience, cognitive science, and computational modeling. Be creative in your approach while maintaining scientific plausibility and coherence across all sections of your response. Use appropriate technical terminology and provide clear explanations where necessary.

Aim for a total response between 1350-1700 words, but this is a guideline rather than a strict requirement. Organize your answer using clear headings for each section."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response focuses on {t['memory_type']} and the {t['brain_region']}.",
            f"The cognitive architecture incorporates {t['cognitive_process']} in its design.",
            "The design demonstrates understanding of recent neuroscientific findings.",
            "The proposed architecture is novel and creative while remaining scientifically plausible.",
            "The response covers all seven required sections with appropriate detail and coherence.",
            "The computational implementation is feasible and well-explained.",
            "The comparative analysis demonstrates understanding of existing cognitive architectures and covers all specified criteria.",
            "The practical applications are relevant and demonstrate the architecture's potential impact.",
            "The response includes a textual description of a diagram or schematic of the proposed architecture.",
            "The ethical implications section discusses at least two potential concerns and proposes guidelines or safeguards."
        ]
        result = eval_with_llm_judge(instructions, submission, criteria)
        if isinstance(result, bool):
            return 1.0 if result else 0.0
        elif isinstance(result, (int, float)):
            return min(max(result, 0.0), 1.0)
        else:
            return 0.0
