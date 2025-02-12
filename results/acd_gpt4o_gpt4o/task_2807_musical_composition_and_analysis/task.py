class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"composition_spec": "Compose a 16-bar melody in C major. The melody should have a clear structure, use a variety of rhythms, and be suitable for a piano."},
            "2": {"analysis_piece": "Analyze the first 16 bars of Beethoven's 'Für Elise'. Discuss the melodic structure, harmonic progression, and rhythmic patterns."}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        if "composition_spec" in t:
            composition_spec = t["composition_spec"]
            instructions = f"""Your task is to compose a piece of music based on the following specifications:

Specifications: {composition_spec}

Ensure that your composition has a clear structure, uses a variety of rhythms, and is suitable for a piano. Provide your composition in plain text format using ABC notation, which represents musical notes in a text format.
Example format for ABC notation:
X:1
T:Example
M:4/4
K:C
CDEF GABc | d2 cd e2 ed | cBAG F2 EF | G2 GF E2 ED | CDEF GABc | d2 cd e2 ed | cBAG F2 EF | G2 GF E2 ED |

Ensure that your composition is easy to understand and follows the given format."""
        else:
            analysis_piece = t["analysis_piece"]
            instructions = f"""Your task is to analyze the given musical composition based on the following excerpt:

Excerpt: {analysis_piece}

Your analysis should include:
1. A detailed discussion of the melodic structure, including motifs and themes.
2. An examination of the harmonic progression, including chord changes and key modulations.
3. An analysis of the rhythmic patterns, including any notable rhythmic motifs and variations.

Provide your analysis in plain text format. Ensure your analysis is detailed and covers all the specified aspects of the composition with examples where applicable."""
        return instructions

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        if "composition_spec" in t:
            criteria = [
                "The composition should be exactly 16 bars long.",
                "The composition should be in C major.",
                "The composition should have a clear structure.",
                "The composition should use a variety of rhythms.",
                "The composition should be suitable for a piano.",
                "The composition should be provided in ABC notation.",
                "The composition should follow the given format and be easy to understand."]
        else:
            criteria = [
                "The analysis should discuss the melodic structure in detail, including motifs and themes.",
                "The analysis should examine the harmonic progression, including chord changes and key modulations.",
                "The analysis should analyze the rhythmic patterns, including notable rhythmic motifs and variations.",
                "The analysis should be detailed and cover all specified aspects with examples where applicable."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
