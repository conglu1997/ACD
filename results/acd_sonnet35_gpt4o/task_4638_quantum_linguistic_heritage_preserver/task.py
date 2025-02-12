class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "endangered_language": "Ayapaneco",
                "cultural_aspect": "oral storytelling traditions",
                "quantum_principle": "superposition",
                "example_phrase": "Nuumte ki'pshuñ (meaning: 'The sun is setting')"
            },
            "2": {
                "endangered_language": "Sami",
                "cultural_aspect": "reindeer husbandry terminology",
                "quantum_principle": "entanglement",
                "example_phrase": "Boazobargu (meaning: 'reindeer herding area')"
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a quantum computing system that preserves and analyzes the endangered language of {t['endangered_language']}, focusing on the cultural aspect of {t['cultural_aspect']}. Your system should incorporate the quantum principle of {t['quantum_principle']}. Then, use your system to reconstruct a lost aspect of this language's heritage. Consider this example phrase from the language: {t['example_phrase']}.

Your response should include:

1. Quantum System Architecture (300-350 words):
   a) Describe the key components of your quantum linguistic preservation system.
   b) Explain how it incorporates the specified quantum principle in its design.
   c) Detail how the system processes and analyzes linguistic data.
   d) Discuss how quantum computing enhances language preservation and analysis compared to classical methods.
   e) Provide a high-level diagram or pseudocode (in text format) illustrating your system's architecture.

2. Linguistic and Cultural Analysis (250-300 words):
   a) Analyze the challenges in preserving and studying the specified endangered language.
   b) Explain how your system captures and preserves the given cultural aspect.
   c) Describe how quantum computing techniques are applied to linguistic analysis in your system.
   d) Discuss any ethical considerations in working with endangered languages and cultural heritage.

3. Heritage Reconstruction (250-300 words):
   a) Propose a specific lost aspect of the language's heritage that your system aims to reconstruct.
   b) Detail the process by which your quantum system would approach this reconstruction.
   c) Explain how the quantum principle is utilized in this reconstruction process.
   d) Discuss the potential accuracy and limitations of such reconstructions.

4. Implications and Applications (200-250 words):
   a) Discuss the potential impact of your system on linguistic preservation and cultural heritage studies.
   b) Explore how this technology might affect our understanding of language evolution and cultural transmission.
   c) Propose two novel applications of your system beyond linguistic preservation.
   d) Consider any potential risks or unintended consequences of this technology.

5. Future Developments (150-200 words):
   a) Suggest potential enhancements or extensions to your quantum linguistic preservation system.
   b) Discuss how advancements in quantum computing might further improve language preservation and analysis.
   c) Propose an experiment to validate a key aspect of your system's effectiveness.

6. Reflection (100-150 words):
   a) Critically evaluate the feasibility and potential limitations of your proposed system.
   b) Discuss any challenges you encountered in designing this interdisciplinary system.
   c) Reflect on how this task has expanded your understanding of the intersection between quantum computing and linguistics.

Ensure your response demonstrates a deep understanding of quantum computing principles, linguistics, and cultural preservation. Use appropriate technical terminology and provide clear explanations for complex concepts. Be innovative in your approach while maintaining scientific plausibility.

Format your response with clear headings for each section, and include the word count for each section in parentheses at the end of the section. Your total response should be between 1250-1550 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response demonstrates a deep understanding of quantum computing principles and their application to linguistic analysis, specifically incorporating the principle of {t['quantum_principle']}.",
            f"The proposed system effectively addresses the preservation of {t['cultural_aspect']} in the {t['endangered_language']} language.",
            "The approach to linguistic preservation and cultural heritage reconstruction is innovative, plausible, and considers the given example phrase.",
            "The response addresses ethical considerations and potential implications of the technology in the context of endangered languages.",
            "The answer is well-structured, coherent, and adheres to the specified word count and format for each section.",
            "The reflection section demonstrates critical thinking about the feasibility and limitations of the proposed system."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
