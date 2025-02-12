import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        organs = [
            "Brain",
            "Heart",
            "Liver",
            "Lungs",
            "Skin"
        ]
        quantum_principles = [
            "Superposition",
            "Entanglement",
            "Tunneling",
            "Coherence"
        ]
        enhancement_goals = [
            "Improved efficiency",
            "Enhanced regeneration",
            "Increased sensory capability",
            "Extended lifespan",
            "Resistance to disease"
        ]
        constraints = [
            "Minimize energy consumption",
            "Ensure reversibility",
            "Maintain genetic stability",
            "Avoid immune system conflicts",
            "Limit enhancement to specific cell types"
        ]
        
        return {
            "1": {
                "organ": random.choice(organs),
                "quantum_principle": random.choice(quantum_principles),
                "enhancement_goal": random.choice(enhancement_goals),
                "constraint": random.choice(constraints)
            },
            "2": {
                "organ": random.choice(organs),
                "quantum_principle": random.choice(quantum_principles),
                "enhancement_goal": random.choice(enhancement_goals),
                "constraint": random.choice(constraints)
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a hypothetical quantum-inspired biological enhancement for the human {t['organ']}, leveraging the quantum principle of {t['quantum_principle']} to achieve the goal of {t['enhancement_goal']}, while addressing the constraint: {t['constraint']}. Your response should include the following sections:

1. Enhancement Design (300-350 words):
   a) Describe the key components and mechanisms of your quantum-inspired biological enhancement.
   b) Explain how it specifically enhances the {t['organ']} using {t['quantum_principle']}.
   c) Discuss how your design achieves the goal of {t['enhancement_goal']}.
   d) Address how your design considers the constraint: {t['constraint']}.
   e) Include a conceptual diagram or schematic representation of your enhancement (describe it in words, as if you were explaining a visual representation).

2. Scientific Principles (250-300 words):
   a) Explain the underlying quantum and biological principles that make your enhancement effective.
   b) Discuss how {t['quantum_principle']} is integrated with biological processes in the {t['organ']}.
   c) Address potential interactions between your enhancement and existing biological systems.
   d) Cite at least two relevant scientific papers or theories that support your design.

3. Implementation and Challenges (200-250 words):
   a) Outline a theoretical approach for implementing your enhancement in human subjects.
   b) Discuss technological and biological challenges in development and deployment.
   c) Propose methods to monitor and control the effects of your enhancement.
   d) Address how you would overcome challenges related to {t['constraint']}.

4. Potential Impacts (200-250 words):
   a) Analyze potential short-term and long-term impacts of your enhancement on human health and physiology.
   b) Discuss any unintended consequences or side effects.
   c) Consider potential societal impacts if this enhancement becomes widely available.
   d) Evaluate how {t['constraint']} might affect the broader implications of your enhancement.

5. Ethical Analysis (200-250 words):
   a) Identify and discuss key ethical concerns related to your quantum-inspired biological enhancement.
   b) Analyze the moral implications of enhancing human biology with quantum-inspired technologies.
   c) Propose ethical guidelines for the development and use of your enhancement.
   d) Discuss how {t['constraint']} influences the ethical considerations of your design.

6. Future Directions (150-200 words):
   a) Suggest potential extensions or modifications of your enhancement for other biological systems.
   b) Discuss how this technology might evolve and impact human evolution or medical treatments in the future.
   c) Propose areas for further research to advance this field of quantum biology.

Ensure your response demonstrates a deep understanding of quantum physics, biology, and bioengineering principles. Use appropriate scientific terminology and provide clear explanations for complex concepts. Be innovative in your approach while maintaining scientific plausibility and addressing real-world constraints.

Format your response with clear headings for each section. Use in-text citations where appropriate (e.g., [Author, Year]). Your total response should be between 1300-1600 words. Include a word count at the end of your submission."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response clearly describes a quantum-inspired biological enhancement for the {t['organ']}, using {t['quantum_principle']} to achieve {t['enhancement_goal']}, while addressing the constraint of {t['constraint']}.",
            "The design demonstrates a deep understanding of both quantum physics and biological principles, with appropriate use of scientific terminology and citations.",
            "The enhancement is innovative yet scientifically plausible, with a clear explanation of the underlying mechanisms.",
            "The response adequately addresses potential impacts, challenges, and ethical implications, including those related to the given constraint.",
            "The submission is well-structured, following the required sections and word count guidelines, and includes in-text citations.",
            "The proposed enhancement and its analysis show creative problem-solving and interdisciplinary knowledge integration.",
            "The ethical analysis is thorough and considers multiple perspectives."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
