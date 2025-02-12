import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        language_disorders = [
            'aphasia',
            'dyslexia',
            'stuttering',
            'specific language impairment',
            'anomic aphasia'
        ]
        vr_environments = [
            'simulated classroom',
            'virtual city',
            'interactive storytelling world',
            'language learning laboratory',
            'social interaction simulator'
        ]
        tasks = {}
        for i in range(2):
            tasks[str(i+1)] = {
                'disorder': random.choice(language_disorders),
                'environment': random.choice(vr_environments)
            }
        return tasks

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a virtual reality therapy system based on neurolinguistic principles to treat {t['disorder']} using a {t['environment']}. Your response should include the following sections:

1. Neurolinguistic Framework (200-250 words):
   a) Explain the key neurolinguistic principles relevant to {t['disorder']}.
   b) Describe how these principles inform your approach to treatment.
   c) Discuss any recent research findings that support your framework.

2. VR System Design (250-300 words):
   a) Describe the core components of your VR therapy system.
   b) Explain how the {t['environment']} is specifically tailored to treat {t['disorder']}.
   c) Detail how your system incorporates neurolinguistic principles in its design.
   d) Discuss any AI components used in your system and their functions.
   e) Provide at least two specific examples of VR interactions or exercises within your therapy system.

3. Treatment Protocol (200-250 words):
   a) Outline a sample therapy session using your VR system.
   b) Explain how the system adapts to individual patient needs and progress.
   c) Describe how you would measure and track treatment effectiveness.

4. Potential Impacts (150-200 words):
   a) Discuss the potential benefits of your system compared to traditional therapies.
   b) Analyze possible limitations or challenges of using VR for language therapy.
   c) Explore how this technology might impact the field of speech-language pathology.

5. Ethical Considerations (150-200 words):
   a) Identify potential ethical issues related to using VR and AI for language therapy.
   b) Discuss data privacy and security concerns specific to your system.
   c) Propose guidelines for the ethical implementation of your VR therapy system.
   d) Address potential cultural considerations when implementing this system globally.

6. Future Developments (100-150 words):
   a) Suggest one potential extension or modification to your system.
   b) Propose a research question that arises from your design.
   c) Briefly discuss how this technology might evolve in the next decade.

Ensure your response demonstrates a deep understanding of neurolinguistics, virtual reality technology, and artificial intelligence. Be creative in your design while maintaining scientific plausibility and addressing real-world therapeutic needs. Use appropriate terminology from all relevant fields and provide clear explanations throughout your response.

Format your response with clear headings for each section and adhere to the specified word counts. Your total response should be between 1050-1350 words. Include a word count at the end of your submission."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response demonstrates a deep understanding of neurolinguistics, particularly as it relates to {t['disorder']}.",
            f"The VR system design effectively incorporates the {t['environment']} and is tailored to treat {t['disorder']}.",
            "The treatment protocol is well-explained and incorporates adaptive elements.",
            "The potential impacts are thoughtfully analyzed, including benefits and limitations.",
            "Ethical considerations are thoroughly addressed, including data privacy and security concerns.",
            "The response is creative while maintaining scientific plausibility and addressing real-world therapeutic needs.",
            "The response adheres to the specified format and word count guidelines (1050-1350 words).",
            "At least two specific examples of VR interactions or exercises are provided.",
            "Cultural considerations for global implementation are addressed."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
