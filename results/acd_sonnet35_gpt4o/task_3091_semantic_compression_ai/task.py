import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        domains = [
            {
                "field": "Medicine",
                "concept": "Diagnosis",
                "application": "AI-assisted medical consultations"
            },
            {
                "field": "Law",
                "concept": "Legal precedent",
                "application": "AI-powered legal research and case analysis"
            },
            {
                "field": "Education",
                "concept": "Learning objectives",
                "application": "Personalized AI tutoring systems"
            },
            {
                "field": "Finance",
                "concept": "Risk assessment",
                "application": "AI-driven investment advisory"
            }
        ]
        return {str(i+1): domain for i, domain in enumerate(random.sample(domains, k=2))}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a semantic compression system for AI-human communication in the field of {t['field']}, focusing on the concept of {t['concept']}. Your system should reduce cognitive load while preserving meaning, and be applicable to {t['application']}. Your response should include the following sections:

1. Semantic Compression Framework (250-300 words):
   a) Explain the principles of semantic compression and its relevance to AI-human communication.
   b) Describe your proposed semantic compression system, including:
      - Method for representing and compressing semantic information
      - Process for encoding and decoding compressed information
      - Mechanism for preserving crucial meaning while reducing cognitive load
   c) Provide a visual representation (diagram or flowchart) of your semantic compression system.

2. Application to {t['field']} (200-250 words):
   a) Demonstrate how your system would compress information related to {t['concept']} in {t['field']}.
   b) Provide an example of original content and its semantically compressed version.
   c) Explain how this compression reduces cognitive load while maintaining essential meaning.

3. AI Integration (200-250 words):
   a) Describe how your semantic compression system could be integrated into an AI system for {t['application']}.
   b) Explain the potential benefits and challenges of this integration.
   c) Discuss how this integration might improve human-AI interaction and decision-making.

4. Cognitive Load Analysis (150-200 words):
   a) Analyze the potential reduction in cognitive load achieved by your system.
   b) Propose a method for measuring this reduction in a real-world setting.
   c) Discuss any potential cognitive trade-offs or limitations of your approach.

5. Ethical Considerations (150-200 words):
   a) Identify potential ethical implications of using semantic compression in AI-human communication for {t['application']}.
   b) Discuss how compressed communication might affect transparency and trust in AI systems.
   c) Propose guidelines to ensure responsible use of semantic compression in AI applications.

6. Future Directions (100-150 words):
   a) Suggest two potential extensions or improvements to your semantic compression system.
   b) Propose a research question that could further explore the impact of semantic compression on human-AI interaction.

Ensure your response demonstrates a deep understanding of semantics, information theory, cognitive science, and AI applications in {t['field']}. Be creative and innovative in your approach while maintaining scientific and practical plausibility. Use concrete examples and analogies to explain abstract concepts where appropriate. Your total response should be between 1050-1350 words.

Please note: The visual representation (diagram or flowchart) requested in section 1c should be described in text format, as if you were explaining it to someone who cannot see the image."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response demonstrates a deep understanding of semantic compression and its application to {t['field']}, particularly regarding {t['concept']}.",
            f"The proposed semantic compression system is innovative, well-explained, and applicable to {t['application']}.",
            "The analysis of cognitive load reduction is thorough and supported by logical arguments.",
            "The ethical considerations are thoughtfully explored and address relevant concerns in AI-human communication.",
            "The response shows creativity and interdisciplinary knowledge application throughout all sections.",
            "The visual representation of the semantic compression system is clearly described and effectively communicates the system's structure and function.",
            "Concrete examples and analogies are used effectively to explain abstract concepts."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
