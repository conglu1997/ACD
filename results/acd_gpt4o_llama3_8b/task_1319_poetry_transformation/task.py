class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"original_poem": "Two roads diverged in a yellow wood,\nAnd sorry I could not travel both\nAnd be one traveler, long I stood\nAnd looked down one as far as I could\nTo where it bent in the undergrowth;",
                    "target_form": "Haiku"},
            "2": {"original_poem": "Shall I compare thee to a summer's day?\nThou art more lovely and more temperate:\nRough winds do shake the darling buds of May,\nAnd summer's lease hath all too short a date:\nSometime too hot the eye of heaven shines,",
                    "target_form": "Limerick"}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        original_poem = t["original_poem"]
        target_form = t["target_form"]
        return f"""Transform the following poem into the {target_form} form while retaining its core meaning and emotional impact:

Original Poem:
{original_poem}

Ensure that your transformed poem adheres to the conventions of the {target_form} form.

Haiku: A traditional Japanese three-line poem with a syllable pattern of 5-7-5. Example:
An old silent pond
A frog jumps into the pond—
Splash! Silence again.

Limerick: A five-line poem with a rhyme scheme of AABBA and a specific rhythm pattern. Example:
There once was a man from Peru
Who dreamed he was eating his shoe
He awoke with a fright
In the middle of the night
To find that his dream had come true.

Submit your transformed poem as a plain text string."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The transformed poem should adhere to the conventions of the target form.",
            "The core meaning and emotional impact of the original poem should be retained."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
