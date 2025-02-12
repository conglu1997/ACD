import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        word_pairs = [
            ('democracy', 'autocracy'),
            ('quantum', 'classical'),
            ('empathy', 'apathy'),
            ('entropy', 'order'),
            ('innovation', 'tradition'),
            ('paradox', 'consistency'),
            ('metaphor', 'literal'),
            ('qualia', 'objectivity'),
            ('emergence', 'reductionism'),
            ('syntax', 'semantics')
        ]
        operations = ['complex_analogy', 'semantic_projection', 'conceptual_blending']
        
        task1 = {
            'word_pair': random.choice(word_pairs),
            'operation': random.choice(operations)
        }
        
        task2 = {
            'word_pair': random.choice(word_pairs),
            'operation': random.choice(operations)
        }
        
        return {
            "1": task1,
            "2": task2
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        word1, word2 = t['word_pair']
        
        if t['operation'] == 'complex_analogy':
            return f"""Explore the complex relationship between '{word1}' and '{word2}' in the word embedding space. Your task is to:

1. Analyze the multidimensional semantic relationship between these two concepts, considering potential non-linear interactions in the embedding space.

2. Propose a complex analogy that captures this relationship, in the form 'A is to B as C is to D, while E is to F'. Explain the nuanced parallels in your analogy.

3. Suggest a series of mathematical operations on word vectors that could represent this complex relationship. Consider combinations of addition, subtraction, scaling, and non-linear transformations. Justify your approach.

4. Hypothesize a novel concept that might emerge from applying these operations to a different set of words. Explain its potential significance in a scientific or philosophical context.

5. Propose an innovative application of this type of complex semantic manipulation in an interdisciplinary field (e.g., cognitive science, complex systems theory, or artificial general intelligence).

Format your response with clear headings for each part of the task."""
        
        elif t['operation'] == 'semantic_projection':
            return f"""Consider the words '{word1}' and '{word2}' as axes in a semantic subspace. Your task is to:

1. Describe what this semantic subspace might represent and how other concepts could be projected onto it.

2. Propose three diverse words or phrases that would have interesting projections in this subspace. Explain their projected positions and implications.

3. Suggest a method to mathematically compute these projections using vector operations on word embeddings. Consider potential non-linearities in the projection process.

4. Hypothesize how this projection concept could be extended to create a higher-dimensional 'semantic coordinate system'. What new insights might this system offer?

5. Propose an innovative application of semantic projections in a field unrelated to linguistics (e.g., social network analysis, economic modeling, or artistic creation). Explain its potential impact.

Format your response with clear headings for each part of the task."""
        
        elif t['operation'] == 'conceptual_blending':
            return f"""Explore the possibility of 'blending' the concepts '{word1}' and '{word2}' in the word embedding space. Your task is to:

1. Describe how these two concepts might be combined in the embedding space to create a novel conceptual blend.

2. Propose a new term or short phrase that represents this conceptual blend. Explain its meaning and potential usage.

3. Suggest a mathematical approach to achieve this conceptual blending using vector operations and potentially non-linear transformations on word embeddings.

4. Hypothesize how this blending process could be extended to combine three or more concepts simultaneously. What challenges and opportunities might arise?

5. Propose an innovative application of conceptual blending in a creative or scientific domain (e.g., speculative fiction writing, scientific hypothesis generation, or innovative product design).

Format your response with clear headings for each part of the task."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        word1, word2 = t['word_pair']
        
        criteria = [
            "The response demonstrates an advanced understanding of multidimensional semantic spaces and their complex interactions.",
            "The explanation of semantic relationships shows depth, nuance, and consideration of non-linear aspects.",
            "The proposed mathematical operations are sophisticated, well-justified, and consider potential non-linearities in semantic space.",
            "The response exhibits exceptional creativity in generating analogies, projections, or conceptual blends.",
            "The ideas presented are highly original and demonstrate advanced interdisciplinary thinking.",
            f"The response correctly addresses the complex relationship between '{word1}' and '{word2}', going beyond surface-level associations.",
            "The proposed applications are innovative, well-explained, and have potential for significant impact in their respective fields.",
            "The response follows the specified format with clear headings for each part and maintains coherence throughout.",
            "The hypothesized novel concepts or extensions show a deep understanding of the potential and limitations of semantic space manipulations."
        ]
        
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
