class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"prompt": "Compose a 16-bar melody in C major, using a 4/4 time signature. The melody should have a clear structure with a repeating motif."},
            "2": {"prompt": "Compose a 12-bar blues progression in the key of A, using a 4/4 time signature. The progression should follow a standard 12-bar blues form."}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        if t["prompt"].startswith("Compose a 16-bar melody"):
            return f"""Complete the following task based on the given prompt:

{t["prompt"]}

Ensure that the melody adheres to the following requirements:
1. The melody should be in C major.
2. The time signature should be 4/4.
3. The melody should be 16 bars long.
4. Include a clear structure with a repeating motif.
5. The melody should conclude with a resolving phrase.
6. The melody should have a logical progression and not just random notes.

Submit your response as a plain text string in ABC notation. For example:
"C D E F | G A B c | d e f g | a b c' d' | e' f' g' a' | b' c'' d'' e'' | f'' g'' a'' b'' | c''' d''' e''' f''' | g''' a''' b''' c''''"
"""
        else:
            return f"""Complete the following task based on the given prompt:

{t["prompt"]}

Ensure that the blues progression adheres to the following requirements:
1. The progression should be in the key of A.
2. The time signature should be 4/4.
3. The progression should follow a standard 12-bar blues form.

Submit your response as a plain text string in ABC notation. For example:
"A A A A | D D A A | E D A A"
"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = []
        if t["prompt"].startswith("Compose a 16-bar melody"):
            criteria = ["The melody should be in C major.", "The time signature should be 4/4.", "The melody should be 16 bars long.", "The melody should have a clear structure with a repeating motif.", "The melody should conclude with a resolving phrase.", "The melody should have a logical progression and not just random notes."]
        else:
            criteria = ["The progression should be in the key of A.", "The time signature should be 4/4.", "The progression should follow a standard 12-bar blues form."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
