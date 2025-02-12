import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        brain_regions = [
            {
                "region": "Broca's area",
                "function": "Speech production and language processing",
                "challenge": "Decoding syntactic structures from neural activity",
                "constraint": "The interface must not require invasive surgery"
            },
            {
                "region": "Wernicke's area",
                "function": "Language comprehension and semantic processing",
                "challenge": "Interpreting abstract concepts and metaphors from brain signals",
                "constraint": "The interface must work in real-time with minimal delay"
            },
            {
                "region": "Angular gyrus",
                "function": "Cross-modal integration and complex language processing",
                "challenge": "Translating multimodal thoughts (visual, auditory, etc.) into coherent language",
                "constraint": "The interface must be able to distinguish between intentional and unintentional thoughts"
            }
        ]
        return {
            "1": random.choice(brain_regions),
            "2": random.choice(brain_regions)
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a hypothetical brain-computer interface (BCI) that translates thoughts into language, focusing on {t['region']}. This region is primarily responsible for {t['function']}. Your task is to create a detailed proposal for this neurolinguistic AI interface, addressing the following points:

1. Interface Design (200-250 words):
   - Describe the physical components of the BCI and how they interact with {t['region']}.
   - Explain the data acquisition process from neural activity.
   - Discuss any potential risks or ethical considerations of the interface.
   - Address the following constraint: {t['constraint']}

2. AI Architecture (250-300 words):
   - Propose an AI architecture that can process and interpret the neural signals from {t['region']}.
   - Explain how this architecture addresses the specific challenge of {t['challenge']}.
   - Describe the training process for this AI system, including potential data sources and learning algorithms.
   - Discuss how the AI handles ambiguity or errors in neural signal interpretation.

3. Language Output (200-250 words):
   - Explain how the processed neural signals are converted into coherent language.
   - Discuss potential limitations or ambiguities in the language output.
   - Propose a method for improving the accuracy and naturalness of the generated language.
   - Describe how the system handles different languages or multilingual users.

4. Practical Application (150-200 words):
   - Suggest a specific use case for this neurolinguistic AI interface.
   - Describe how it could benefit users or advance our understanding of language and cognition.
   - Discuss any potential societal implications of this technology.
   - Address potential misuse scenarios and propose safeguards.

5. Future Developments (150-200 words):
   - Propose an innovative extension or improvement to your design.
   - Explain how this enhancement could overcome current limitations in BCIs or AI language processing.
   - Discuss any emerging technologies or research that could contribute to this development.
   - Speculate on how this technology might evolve in the next 20 years.

Ensure your response demonstrates a deep understanding of neuroscience, linguistics, and artificial intelligence. Use technical terminology appropriately and provide explanations where necessary. Be creative in your design while maintaining scientific plausibility. Format your response using clear headings for each section."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response demonstrates a comprehensive understanding of neurolinguistics, brain-computer interfaces, and AI technologies.",
            "The proposed interface design is scientifically plausible, addresses the specific functions of the given brain region, and satisfies the given constraint.",
            "The AI architecture is well-explained and specifically addresses the challenge related to the brain region, including handling of ambiguities and errors.",
            "The language output process is logically described, with thoughtful consideration of limitations, improvements, and multilingual capabilities.",
            "The practical application is innovative, with a thorough discussion of benefits, societal implications, and potential misuse scenarios.",
            "The future developments section demonstrates foresight and creativity in extending the technology.",
            "The response maintains scientific rigor while showcasing creativity in problem-solving and design.",
            "The response is well-structured with clear headings for each section as requested."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
