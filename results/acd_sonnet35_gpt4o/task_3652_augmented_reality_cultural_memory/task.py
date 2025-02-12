import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        cultural_contexts = ['Indigenous oral traditions', 'Urban neighborhood histories', 'Family genealogies', 'Ancient archaeological sites']
        memory_types = ['Episodic memory', 'Semantic memory', 'Procedural memory', 'Collective memory']
        ar_interfaces = ['Smart glasses', 'Smartphone app', 'Projected holograms', 'Haptic feedback devices']
        
        return {
            "1": {
                "cultural_context": random.choice(cultural_contexts),
                "memory_type": random.choice(memory_types),
                "ar_interface": random.choice(ar_interfaces)
            },
            "2": {
                "cultural_context": random.choice(cultural_contexts),
                "memory_type": random.choice(memory_types),
                "ar_interface": random.choice(ar_interfaces)
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design an augmented reality system that enhances human memory and preserves cultural heritage by overlaying historical and personal information onto the physical world. Your system should focus on the cultural context of {t['cultural_context']}, primarily address {t['memory_type']}, and utilize {t['ar_interface']} as the main interface. Your response should include:

1. System Overview (250-300 words):
   a) Describe the key components and functionality of your AR system.
   b) Explain how it integrates with the physical environment to enhance memory and preserve culture.
   c) Discuss how your system specifically addresses the given cultural context and memory type.

2. User Experience Design (200-250 words):
   a) Detail the user interface and interaction methods for your chosen AR interface.
   b) Explain how users can input, access, and share cultural and personal memories.
   c) Describe any personalization features that adapt the system to individual users or communities.

3. Technical Implementation (250-300 words):
   a) Outline the key technologies and algorithms required for your system.
   b) Explain how your system processes and presents cultural and historical information.
   c) Discuss any challenges in implementing your design and propose solutions.
   d) Address privacy and data security concerns in your implementation.

4. Cognitive and Cultural Impact (200-250 words):
   a) Analyze how your system might affect human memory processes and cultural preservation.
   b) Discuss potential benefits and risks of augmenting memory with AR technology.
   c) Explain how your system supports intergenerational knowledge transfer and cultural continuity.

5. Ethical Considerations (150-200 words):
   a) Identify potential ethical issues related to your AR memory system.
   b) Discuss how these concerns might be addressed or mitigated.
   c) Propose guidelines for responsible development and use of AR in cultural preservation.

6. Evaluation and Future Directions (150-200 words):
   a) Propose methods to evaluate the effectiveness and impact of your system.
   b) Suggest potential improvements or expansions to your AR memory system.
   c) Discuss how this technology might evolve and impact society in the long term.

Ensure your response demonstrates a deep understanding of augmented reality technology, cognitive psychology, and cultural anthropology. Be creative in your approach while considering practical implementation and ethical implications. Use appropriate technical terminology and provide clear explanations for complex concepts.

Format your response with clear headings for each section. Your total response should be between 1200-1500 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response demonstrates a deep understanding of augmented reality technology, cognitive psychology, and cultural anthropology.",
            "The proposed AR system creatively and plausibly addresses the given cultural context and memory type.",
            f"The design effectively utilizes {t['ar_interface']} as the main interface.",
            "The answer covers all required sections with appropriate detail and word count.",
            "The response shows clear interdisciplinary thinking and novel approaches to enhancing human memory and preserving cultural heritage.",
            "The technical implementation is well-explained and addresses potential challenges.",
            "The response thoughtfully analyzes the cognitive and cultural impact of the proposed system.",
            "Ethical considerations are thoroughly discussed with proposed mitigation strategies.",
            "The evaluation methods and future directions are insightful and well-reasoned."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
