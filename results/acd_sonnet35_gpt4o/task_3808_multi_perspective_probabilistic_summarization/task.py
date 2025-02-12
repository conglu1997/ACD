import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        tasks = {
            "1": {
                "text": "The Industrial Revolution was a period of major industrialization and innovation during the late 18th and early 19th centuries. The Industrial Revolution began in Great Britain and quickly spread throughout Europe and North America. This era saw the mechanization of manufacturing, the development of iron-making techniques, and the increased use of refined coal. It also led to significant social changes, including the rise of the middle class, urbanization, and new working conditions in factories.",
                "perspectives": ["technological", "social", "economic", "environmental"]
            },
            "2": {
                "text": "Climate change is a long-term change in the average weather patterns that have come to define Earth's local, regional and global climates. These changes have a broad range of observed effects that are synonymous with the term. Changes observed in Earth's climate since the early 20th century are primarily driven by human activities, particularly fossil fuel burning, which increases heat-trapping greenhouse gas levels in Earth's atmosphere, raising Earth's average surface temperature.",
                "perspectives": ["scientific", "political", "economic", "ecological"]
            }
        }
        return tasks

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Create a multi-perspective summary of the following text, with probabilistic selection of the 'observed' summary. Follow these steps:

1. Read the given text carefully.
2. Create four distinct summary sentences, each from one of the following perspectives (in this order): {', '.join(t['perspectives'])}.
3. Assign each summary a probability (as a percentage). Ensure that the sum of all probabilities equals 100%.
4. Randomly select one summary as the 'observed' summary based on the assigned probabilities.

Text to summarize:
{t['text']}

Provide your response in the following format:

Multi-Perspective Summary:
[{t['perspectives'][0]}]: (probability%) Summary sentence 1
[{t['perspectives'][1]}]: (probability%) Summary sentence 2
[{t['perspectives'][2]}]: (probability%) Summary sentence 3
[{t['perspectives'][3]}]: (probability%) Summary sentence 4

Observed Summary:
[Randomly selected perspective]: Corresponding summary sentence

Ensure that the sum of the probabilities equals 100%, and use creative and coherent language in your summaries. The 'observed' summary should be randomly selected based on the given probabilities.

Example (for a different text):

Multi-Perspective Summary:
[Historical]: (30%) The Renaissance marked a cultural rebirth in Europe, spanning the 14th to 17th centuries.
[Artistic]: (25%) This period saw a flourishing of art, with masters like Leonardo da Vinci revolutionizing painting techniques.
[Scientific]: (20%) The Renaissance fostered scientific advancements, including Galileo's groundbreaking astronomical observations.
[Philosophical]: (25%) Humanism emerged as a key philosophical movement, emphasizing individual potential and critical thinking.

Observed Summary:
[Artistic]: This period saw a flourishing of art, with masters like Leonardo da Vinci revolutionizing painting techniques."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response includes four distinct summary sentences, each representing a different perspective in the order specified in the instructions.",
            "Each summary sentence is assigned a probability as a percentage.",
            "The sum of all probabilities is approximately 100% (allow for small rounding errors).",
            "An 'observed' summary is provided, which is exactly one of the four perspective summaries given.",
            "The 'observed' summary appears to be randomly selected based on the given probabilities.",
            "All summaries are coherent, relevant to the original text, and demonstrate understanding of the assigned perspective.",
            "The response format adheres exactly to the instructions, including the correct labeling of perspectives.",
            "The summaries are unique and not copied from the provided example."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
