class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "visual_element": "Color gradients",
                "abstract_concept": "Time perception",
                "reasoning_task": "Sequence prediction",
                "constraint": "Must incorporate quantum computing principles"
            },
            "2": {
                "visual_element": "Geometric shapes",
                "abstract_concept": "Causality",
                "reasoning_task": "Analogical reasoning",
                "constraint": "Must use neuromorphic computing architecture"
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design an AI system capable of generating and interpreting a visual language based on {t['visual_element']}, which can represent and reason about the abstract concept of {t['abstract_concept']}. Then, use this system to solve a complex {t['reasoning_task']} problem. Your system {t['constraint']}. Your response should include the following sections:

1. Visual Language Design (300-350 words):
   a) Describe at least 5 key components and 3 fundamental rules of your visual language based on {t['visual_element']}.
   b) Explain how this visual language represents the abstract concept of {t['abstract_concept']}.
   c) Provide 5 example 'visual words' or 'phrases' in your language, with explanations of their meanings.
   d) Include a detailed ASCII art representation of one of your 'visual words'.

2. AI System Architecture (250-300 words):
   a) Describe the key components of your AI system for generating and interpreting this visual language.
   b) Explain how the system integrates visual processing, semantic understanding, and reasoning capabilities.
   c) Discuss how you've incorporated {t['constraint']} into your system architecture.
   d) Propose a novel AI technique or architecture specifically designed for visual language processing.

3. Reasoning Task Approach (300-350 words):
   a) Present a specific {t['reasoning_task']} problem involving predicting the next 3 elements in a complex visual sequence representing changes in {t['abstract_concept']}.
   b) Describe step-by-step how your AI system would approach this problem, including:
      - Generating relevant visual representations
      - Interpreting these representations
      - Applying reasoning strategies to solve the problem
   c) Provide a hypothetical example of the AI's problem-solving process, including sample 'visual thoughts' in your language.

4. Comparative Analysis (200-250 words):
   a) Compare how solutions generated using this visual language-based system might differ from those of traditional text-based AI systems.
   b) Discuss the potential advantages and limitations of using this visual language approach for abstract reasoning tasks.
   c) Analyze how the incorporation of {t['constraint']} affects the system's performance and capabilities.

5. Cognitive Science Implications (200-250 words):
   a) Discuss how your visual language system relates to theories of human visual cognition and abstract thinking.
   b) Propose a testable hypothesis about how this type of visual language processing might inform our understanding of human cognitive processes.
   c) Suggest an experiment design to validate your hypothesis.

6. Ethical Considerations (150-200 words):
   a) Discuss potential ethical implications of developing and deploying AI systems that use visual languages for reasoning.
   b) Address any concerns related to transparency, interpretability, or potential biases in visual language-based AI systems.
   c) Propose guidelines for the responsible development and use of visual language AI systems.

Ensure your response is creative, logically consistent, and demonstrates a deep understanding of visual cognition, AI, and abstract reasoning. Use clear headings for each section and adhere to the word count guidelines provided.

Your total response should be between 1400-1700 words. Manage your time wisely to address all sections thoroughly."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response provides a detailed and coherent description of a visual language and AI system design, addressing all required aspects and sections.",
            f"The visual language design clearly incorporates {t['visual_element']}, effectively represents the concept of {t['abstract_concept']}, and includes at least 5 components, 3 rules, and 5 example 'visual words' or 'phrases'.",
            f"The AI system architecture demonstrates a deep understanding of visual processing, semantic understanding, and reasoning capabilities, while incorporating {t['constraint']}.",
            f"The approach to the {t['reasoning_task']} problem is well-explained, demonstrates how the visual language is used in the reasoning process, and includes a specific example of predicting the next 3 elements in a visual sequence.",
            "The comparative analysis shows thoughtful consideration of the strengths, limitations, and broader impacts of the proposed system, including the effects of the given constraint.",
            "The cognitive science implications section includes a testable hypothesis and a suggested experiment design.",
            "The ethical considerations section addresses relevant concerns, implications, and proposes guidelines for visual language-based AI systems.",
            "The response includes a detailed ASCII art representation of a 'visual word' example.",
            "The overall response shows exceptional creativity, scientific plausibility, and a deep understanding of visual cognition, AI, and abstract reasoning.",
            "The total word count falls within the specified range of 1400-1700 words."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
