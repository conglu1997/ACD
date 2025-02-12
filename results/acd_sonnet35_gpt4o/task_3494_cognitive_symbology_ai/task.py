import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        scenarios = [
            {
                "cognitive_framework": "Dual Process Theory",
                "domain": "Decision Making",
                "concept": "Risk Assessment"
            },
            {
                "cognitive_framework": "Embodied Cognition",
                "domain": "Spatial Reasoning",
                "concept": "Navigation"
            },
            {
                "cognitive_framework": "Predictive Processing",
                "domain": "Perception",
                "concept": "Visual Illusions"
            }
        ]
        return {str(i+1): scenario for i, scenario in enumerate(random.sample(scenarios, 2))}

    @staticmethod
    def get_instructions(t: dict) -> str:
        cognitive_framework_explanations = {
            "Dual Process Theory": "posits two distinct types of cognitive processes: fast, automatic 'System 1' and slow, deliberate 'System 2'",
            "Embodied Cognition": "emphasizes the role of the body and its interactions with the environment in shaping cognitive processes",
            "Predictive Processing": "suggests that the brain constantly generates and updates predictions about sensory inputs"
        }
        return f"""Design an AI system capable of generating and interpreting abstract symbolic languages based on different cognitive frameworks, then apply it to the following scenario:

Cognitive Framework: {t['cognitive_framework']} ({cognitive_framework_explanations[t['cognitive_framework']]})
Domain: {t['domain']}
Concept to Symbolize: {t['concept']}

Example: For the concept of 'Time' in the domain of 'Physics', a simple abstract symbol set might include:
- ◊ : representing a moment in time
- → : representing the flow of time
- ∞ : representing eternity or infinite time
A rule might be: ◊→◊ represents a sequence of moments in time.

Your task has the following parts:

1. AI System Architecture (250-300 words):
   a) Describe the key components of your AI system for generating and interpreting abstract symbolic languages.
   b) Explain how your system incorporates the specified cognitive framework.
   c) Detail how your system generates symbols and assigns meanings based on cognitive principles.
   d) Include a high-level diagram of your system architecture (describe it in text).

2. Symbolic Language Generation (200-250 words):
   a) Generate a set of abstract symbols to represent key elements of the given concept within the specified domain.
   b) Explain the logic behind your symbol choices and their relationships.
   c) Provide a 'grammar' or set of rules for combining these symbols to express complex ideas.

3. Cognitive Framework Integration (200-250 words):
   a) Explain how your symbolic language reflects principles of the specified cognitive framework.
   b) Describe how the symbols and grammar might differ if based on a different cognitive framework.
   c) Discuss any challenges in translating cognitive theories into symbolic representations.

4. Interpretation and Application (250-300 words):
   a) Demonstrate how your AI system would interpret a complex statement written in your symbolic language.
   b) Show how your system would generate a symbolic representation for a novel idea within the given domain.
   c) Explain how this process reflects the underlying cognitive framework.

5. Comparative Analysis (150-200 words):
   a) Compare your AI-generated symbolic language to existing symbolic systems (e.g., mathematical notation, logic symbols).
   b) Discuss potential advantages and limitations of your approach.

6. Ethical and Cognitive Implications (150-200 words):
   a) Discuss potential effects of using such abstract symbolic languages on human cognition and communication.
   b) Address ethical considerations related to AI systems that can generate and manipulate symbolic representations of thought.

Ensure your response demonstrates a deep understanding of cognitive science, symbolic systems, and AI. Be innovative in your approach while maintaining scientific plausibility. Use appropriate terminology and provide clear explanations for complex concepts.

Format your response with clear headings for each section. Your total response should be between 1200-1500 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response should describe an AI system architecture that clearly incorporates the {t['cognitive_framework']} framework",
            f"The response should generate a set of at least 5 abstract symbols for the concept of {t['concept']} in the domain of {t['domain']}, with clear explanations for each",
            f"The response should provide at least 3 rules for combining the symbols to express complex ideas related to {t['concept']}",
            "The response should explicitly explain how the symbolic language reflects the principles of the specified cognitive framework",
            "The response should include a detailed example of interpreting a complex statement and generating a novel idea using the symbolic language",
            "The response should provide a substantive comparison between the AI-generated symbolic language and at least two existing symbolic systems",
            "The response should discuss at least three potential ethical implications or cognitive effects of using the abstract symbolic language",
            "The response should follow the specified format with clear headings for each section",
            "The total response should be between 1200-1500 words"
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
