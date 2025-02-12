import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        scenarios = [
            {
                "ecosystem_type": "marine",
                "dominant_signaling_mechanism": "quorum sensing",
                "problem": "resource allocation"
            },
            {
                "ecosystem_type": "terrestrial",
                "dominant_signaling_mechanism": "hormone-like molecules",
                "problem": "predator-prey dynamics"
            },
            {
                "ecosystem_type": "subterranean",
                "dominant_signaling_mechanism": "bioelectric fields",
                "problem": "environmental adaptation"
            }
        ]
        return {str(i+1): scenario for i, scenario in enumerate(random.sample(scenarios, 2))}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design an artificial ecosystem where AI agents communicate using a biosemiotic language based on cellular signaling mechanisms. Your ecosystem should be a {t['ecosystem_type']} environment, with the dominant signaling mechanism being {t['dominant_signaling_mechanism']}. After designing the ecosystem and its language, analyze its emergent properties and propose a solution to the problem of {t['problem']} within the ecosystem.

Your response should include the following sections:

1. Ecosystem Design (250-300 words):
   a) Describe the key components of your {t['ecosystem_type']} artificial ecosystem.
   b) Explain how AI agents in this ecosystem are structured and how they interact.
   c) Discuss how the {t['dominant_signaling_mechanism']} mechanism is implemented in your ecosystem's communication system.

2. Biosemiotic Language (250-300 words):
   a) Describe the fundamental elements and structure of your biosemiotic language.
   b) Explain how this language incorporates principles from cellular signaling and semiotics.
   c) Provide examples of basic 'expressions' in this language and their meanings.
   d) Discuss how the language allows for complex information exchange between AI agents.

3. Emergent Properties Analysis (200-250 words):
   a) Identify and explain at least three emergent properties of your ecosystem.
   b) Discuss how these properties arise from the interactions between agents and their biosemiotic communication.
   c) Compare these emergent properties to those observed in natural ecosystems or complex adaptive systems.

4. Problem-Solving Approach (250-300 words):
   a) Describe your approach to solving the {t['problem']} problem within your ecosystem.
   b) Explain how the biosemiotic language and emergent properties of the ecosystem are utilized in your solution.
   c) Provide a step-by-step breakdown of how your solution would be implemented by the AI agents.

5. Implications and Future Directions (150-200 words):
   a) Discuss the potential implications of your biosemiotic AI ecosystem for understanding natural ecosystems and developing advanced AI systems.
   b) Propose two potential applications of this technology in scientific research or real-world problem-solving.
   c) Suggest future extensions or improvements to your ecosystem design.

Ensure your response demonstrates a deep understanding of cellular biology, semiotics, artificial intelligence, and complex systems. Use technical terminology appropriately and provide explanations where necessary. Be creative in your approach while maintaining scientific plausibility.

Format your response using clear headings for each section. Your total response should be between 1100-1350 words. Include a word count at the end of your submission."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response includes all five required sections with appropriate content",
            "The ecosystem design incorporates the specified environment type and signaling mechanism",
            "The biosemiotic language is well-defined and incorporates cellular signaling principles",
            "The analysis of emergent properties is insightful and well-explained",
            f"The proposed solution to the {t['problem']} problem is creative and utilizes the ecosystem's properties",
            "The response demonstrates deep understanding of biology, semiotics, and AI concepts"
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
