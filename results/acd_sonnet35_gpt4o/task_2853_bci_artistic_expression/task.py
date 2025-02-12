class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        tasks = {
            "1": {
                "emotional_state": "nostalgia",
                "artistic_medium": "digital painting",
                "target_audience": "elderly individuals with mild cognitive impairment"
            },
            "2": {
                "emotional_state": "awe",
                "artistic_medium": "interactive 3D sculpture",
                "target_audience": "young adults in urban environments"
            }
        }
        return tasks

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a brain-computer interface (BCI) system for artistic expression, then use it to create and analyze a piece of abstract art based on the emotional state of {t['emotional_state']}. Your system should use {t['artistic_medium']} as the medium and be designed for {t['target_audience']}. Provide your response in the following format:

1. BCI System Design (300-350 words):
   a) Describe the key components of your BCI system for artistic expression.
   b) Explain how your system captures and interprets neural signals related to {t['emotional_state']}.
   c) Detail how the system translates these signals into artistic elements in {t['artistic_medium']}.
   d) Discuss any novel features that make your system particularly suited for {t['target_audience']}.
   e) Include a simple diagram or ASCII representation of your BCI system architecture.

2. Artistic Process and Output (250-300 words):
   a) Describe the step-by-step process of creating art using your BCI system.
   b) Explain how the system ensures the art reflects the emotional state of {t['emotional_state']}.
   c) Provide a detailed description of the resulting abstract art piece, including its visual elements, composition, and how it embodies {t['emotional_state']}.
   d) Discuss how the choice of {t['artistic_medium']} influences the final artistic output.

3. Neuroscientific Analysis (200-250 words):
   a) Analyze the neural correlates of {t['emotional_state']} that your system detects and utilizes.
   b) Explain how your system distinguishes between different emotional states in the brain.
   c) Discuss any challenges in accurately interpreting and translating emotional neural signals into art.

4. Target Audience Considerations (200-250 words):
   a) Explain how your BCI system and artistic output are tailored to {t['target_audience']}.
   b) Discuss potential benefits and risks of using this system with the specified audience.
   c) Propose methods to evaluate the system's effectiveness and impact on the target audience.

5. Ethical Implications (200-250 words):
   a) Discuss the ethical considerations of using BCIs for artistic expression.
   b) Address potential privacy concerns related to capturing and interpreting neural data.
   c) Explore the implications of AI-assisted art creation on the concept of authorship and creativity.
   d) Propose guidelines for the ethical development and use of BCI art systems.

6. Future Directions and Societal Impact (150-200 words):
   a) Speculate on potential future applications of your BCI art system beyond the current use case.
   b) Discuss how widespread use of such systems might impact society, art, and human expression.
   c) Propose areas of research or technological development that could enhance BCI-based artistic expression.

Ensure your response demonstrates a deep understanding of neuroscience, computer science, art theory, and ethics. Be innovative in your approach while maintaining scientific plausibility and addressing ethical concerns. Use appropriate terminology from all relevant fields and provide clear explanations where necessary.

Format your response with clear headings for each section. Your total response should be between 1300-1600 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response demonstrates a deep understanding of brain-computer interfaces, neuroscience, and artistic expression.",
            f"The BCI system design effectively captures and translates neural signals related to {t['emotional_state']} into {t['artistic_medium']}.",
            f"The artistic process and output clearly reflect the emotional state of {t['emotional_state']} and are suitable for {t['target_audience']}.",
            "The neuroscientific analysis provides a plausible explanation of the neural correlates involved in the emotional state and artistic process.",
            f"The response adequately addresses the specific needs and considerations of {t['target_audience']}.",
            "The ethical implications of using BCIs for artistic expression are thoroughly discussed, including privacy concerns and guidelines for responsible use.",
            "The response is creative and innovative while maintaining scientific plausibility.",
            "The future directions and societal impact section provides insightful speculation on the potential applications and effects of BCI art systems.",
            "The response adheres to the specified format and word limit."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
