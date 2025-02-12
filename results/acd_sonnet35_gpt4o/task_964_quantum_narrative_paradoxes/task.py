import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        tasks = [
            {
                "quantum_principle": "Schrödinger's cat",
                "philosophical_paradox": "The Ship of Theseus",
                "narrative_setting": "A futuristic space colony"
            },
            {
                "quantum_principle": "Quantum entanglement",
                "philosophical_paradox": "The Grandfather Paradox",
                "narrative_setting": "A Victorian-era secret society"
            }
        ]
        return {str(i+1): task for i, task in enumerate(random.sample(tasks, k=2))}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Create a short story that incorporates the quantum physics principle of {t['quantum_principle']} as a metaphor for the philosophical paradox known as {t['philosophical_paradox']}. Set your story in {t['narrative_setting']}. Then, analyze the implications of this quantum-philosophical parallel. Your task has four parts:

1. Concept Explanation (100-150 words):
   Briefly explain the quantum principle and philosophical paradox you'll be working with. Ensure you demonstrate a clear understanding of both concepts.

2. Short Story (350-400 words):
   Write a creative narrative that cleverly integrates the assigned quantum principle and philosophical paradox. Ensure that the story is engaging, coherent, and set in the specified narrative setting. The quantum principle should serve as a metaphorical framework for exploring the philosophical paradox. Your story must include at least one character facing a dilemma related to the paradox.

3. Quantum-Philosophical Analysis (250-300 words):
   a) Explain how your story draws parallels between the quantum principle and the philosophical paradox.
   b) Discuss at least two insights or new perspectives on the philosophical paradox that emerge from this quantum analogy.
   c) Analyze how the narrative setting enhances or complicates the exploration of these concepts.
   d) Propose a novel thought experiment inspired by your story that further explores the quantum-philosophical parallel.

4. Implications and Extensions (200-250 words):
   a) Propose a real-world scenario where the quantum-philosophical parallel explored in your story might have practical or theoretical significance.
   b) Suggest how this interdisciplinary approach (combining quantum physics, philosophy, and narrative) might contribute to advancements in either field or in interdisciplinary studies.
   c) Identify at least two limitations or potential misunderstandings that could arise from using quantum principles as metaphors for philosophical concepts.
   d) Briefly outline a potential research project that could further explore the ideas presented in your analysis.

Ensure your response demonstrates a deep understanding of both the quantum principle and the philosophical paradox, as well as creative storytelling ability. Use appropriate terminology from both physics and philosophy, providing clear explanations where necessary. Be innovative in your approach while maintaining scientific and philosophical accuracy.

Format your response with clear headings for each section (e.g., '1. Concept Explanation', '2. Short Story', '3. Quantum-Philosophical Analysis', '4. Implications and Extensions'). Include a word count for each section at the end of that section."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The concept explanation demonstrates a clear understanding of both the quantum principle and the philosophical paradox.",
            "The short story effectively incorporates the quantum principle as a metaphor for the philosophical paradox and includes a character facing a related dilemma.",
            "The narrative is creative, engaging, and set in the specified setting.",
            "The quantum-philosophical analysis provides at least two insights and includes a novel thought experiment.",
            "The implications and extensions section provides insightful and plausible ideas for further exploration, including a potential research project.",
            "The overall response shows strong interdisciplinary knowledge integration, creative problem-solving, and adherence to the specified word counts."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
