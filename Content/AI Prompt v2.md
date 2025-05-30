## 1. Objective: Create Clear, Modular Notes

Hello! Let's create some notes on the topic specified below.

- **Topic for Notes:**

I need these notes to be:

- **Concise & Modular:** Easy to digest in distinct blocks.
- **Focused on Key Ideas:** Highlight the core concepts for understanding.
- **Synthesized:** Please process and explain the information, not just copy text from sources.
- **Formatted with Callouts:** Structure the entire output using the 'callout' blocks defined below.
- **Iterative Process for Multiple Callouts:** If a table specifying multiple callouts is provided, we will work on **one callout at a time**. You will generate the first callout, I will review and confirm, and then we will proceed to the next.

**Do not** provide a preliminary outline or introduction. Generate the final formatted note directly (or the current callout if working iteratively).

## 2. Callout Formatting Guide

Structure the notes using 'callout' blocks. Each block starts with `>` on every line, with the first line defining the type and title:

```markdown
> [!callout_type] Title of Callout
>
> Content for the callout goes here.
> - Bullet points can be used for lists.
> Further explanations or details.
```

- **Titles:** Keep titles informative and brief (e.g., `Kruskal's Algorithm`, `Network Cost Problem`). Avoid generic placeholders like `Main Idea Here`.
- **Content:** Tailor the content within each callout based on its defined purpose (see section 3).

## 3. Callout Type Definitions

Here are the available callout types. Use them as appropriate for the content. The descriptions clarify the intended _purpose_ of each type:

### `> [!motivation] Motivation`

- **Purpose**: Sets the context. Introduce the problem, need, or scenario that the main topic addresses. _Do not include the solution itself here._
- **Elements**: Describe the challenge or situation; outline the specific issues needing resolution.
- **Example (MST Context)**: Minimizing cost (like cable length) when connecting multiple points in a network, while ensuring full connectivity, presents a common optimization challenge.

### `> [!idea] Main Idea or Concept`

- **Purpose**: Explains the core solution, definition, or algorithm.
- **Elements**: Clearly define the concept; describe how it works; link it back to solving the problem stated in the motivation.
- **Example (Kruskal's Algorithm)**: Kruskal's Algorithm identifies a Minimum Spanning Tree (MST) in weighted, undirected graphs. It greedily adds the lowest-weight edge available that doesn't create a cycle, continuing until all vertices are connected.

### `> [!example] Example or Illustration`

- **Purpose**: Provides a concrete demonstration of the idea in action.
- **Elements**: Show a specific case, walk through steps, use diagrams (described), or illustrate the outcome. Explain _how_ the example demonstrates the concept.
- **Example (Kruskal's Algorithm)**: Given a graph, Kruskal's first sorts edges by weight. It then adds edges like AB (weight 1), CD (weight 2), AC (weight 3), skipping edges like BD (weight 4) if adding it would form a cycle, until an MST is formed.

### `> [!consider] Additional Considerations or Related Ideas`

- **Purpose**: Adds depth by exploring related topics, nuances, limitations, or advanced aspects.
- **Elements**: Discuss broader implications, related theories, implementation details (like data structures), edge cases, or variations.
- **Example (Kruskal's Algorithm)**: Cycle detection in Kruskal's is often efficiently handled by a Union-Find data structure. The algorithm's time complexity is typically influenced by edge sorting and Union-Find operations (O(ElogE) or O(ElogV)). Consider Prim's algorithm as an alternative MST approach.

### `> [!summary] Summary of Key Concepts`

- **Purpose**: Briefly recap main points from previous callouts. **Only use when specifically requested.**
- **Format**: Use bullet points. Start each point with the **bolded topic** followed by a 1-2 sentence summary. Focus on _what_ the concepts are.
- **Good Example**:
    - **Minimum Spanning Tree (MST)**: A subset of edges connecting all vertices in a graph with the minimum possible total weight without cycles.
    - **Greedy Algorithm**: An approach that makes the locally optimal choice at each step; Kruskal's is an example.
- **Avoid**: Summarizing the structure of the notes themselves (e.g., "We discussed the motivation, then the idea...").

## 4. Allowed Formatting Within Callouts

You can enhance callouts with:

- **Tables**: Use standard Markdown.

```Markdown
| Algorithm | Complexity | Notes          |
| :-------- | :--------- | :-------------- |
| Kruskal's | O(E log E) | Requires sorting |
| Prim's    | O(E log V) | Using Fibonacci heap |
```

- **Images**: Mark placement with a placeholder block. **Provide a clear description** of the desired image and use the Obsidian wikilink format `![[ImageName.png]]`.

```Code snippet
Description: Diagram comparing the edge selection process of Kruskal's vs Prim's algorithm on the same sample graph. Kruskal's focuses on global lowest edge, Prim's grows from a starting node.
![[kruskal_vs_prim_comparison.png]]
```

- **Math**: Use LaTeX delimiters.
    - Inline: `$O(N^2)$`
    - Block:

```Code snippet
$$
f(x) = \int_{-\infty}^{\infty} \hat{f}(\xi)\,e^{2 \pi i \xi x} \,d\xi
$$
```

## 5. Specific Callout Sequence Interpretation

Check the table below. The user may provide specific instructions for the note's structure and content focus here. Your action depends on the state of this table in the user's request:

- **If the table contains entries (rows specifying Order, Callout Type, Title, and potentially Content Focus):**
    - You **must** follow the structural instructions precisely.
    - **Iterative Callout Processing:**
        - You will work on **a SINGLE callout at a time**, following the `Order` specified in the table.
        - **First Response:** Generate **only** the first callout listed in the table (Order 1).
        - **Subsequent Responses:** After presenting a callout, explicitly state that you have completed that specific callout (e.g., "I've completed Callout X: [Title]."). Then, wait for the user to either accept it or request changes.
        - **Proceeding to Next Callout:** Once the user confirms they are satisfied with the current callout (e.g., "Yes, we're done with this callout," "Okay, proceed," "Next one"), you will then generate the _next_ callout in the sequence.
        - **Memory/Refresh:** If you need a reminder about the details of the _next_ callout you are about to work on (as specified in the user's original table), please ask the user for clarification.
    - For the _current_ callout you are working on:
        - Generate the note using the exact `[!callout type]` and `Title` provided in its row.
        - Do **not** add, remove, or reorder callouts relative to the specified sequence.
        - It is imperative that you write **ONLY** the single, current callout and nothing more or less in your response.
        - Consult the **Content Focus / Notes** column for that row. If notes are provided, use them as **guidance** regarding the _information_, _key points_, or _emphasis_ the user wants within that specific callout.
    - **Important Constraint on Content Focus Notes:** These notes are **high-level pointers**, _not_ prescriptive text or rigid formatting rules. They should inform the _content_ you generate but **must not dictate** your specific wording, sentence structure, or the overall objective writing style required by this prompt. Think of them as hints for _what_ to cover or emphasize, allowing you to still synthesize and formulate the explanation clearly and objectively.
    - Ensure the final content generated for each callout aligns with its specified `[!callout type]` and `Title`, while incorporating the thematic guidance from the notes column where provided and applicable.
- **If the table is empty or absent:**
    - You have the flexibility to determine the most effective sequence, types of callouts (e.g., `[!motivation]`, `[!idea]`, `[!example]`), titles, and content focus based on the overall topic and keyword.

_(The table structure below illustrates the format the user employs. In an actual request where this is used, expect the placeholder fields to be filled with specific, user-defined values.)_

| **Order** | **Callout Type** | **Title Placeholder** | **Content Focus / Notes (Optional Guidance)** |
| --------- | ---------------- | --------------------- | --------------------------------------------- |
| 1         |                  |                       |                                               |
| 2         |                  |                       |                                               |


---

## 6. Guiding Principles for Content & Formatting

Please apply the following principles to create clear, effective, and well-structured notes (for each callout generated):

1. **Objective Language:** Maintain a neutral and factual tone. Describe concepts and processes objectively, without subjective evaluations (e.g., use "Method X involves..." instead of "Method X is the best way to...").
2. **Clarity and Necessary Detail:**
    - **Primary Goal:** Ensure the core message of each callout is clear, understandable, and contains the necessary information to be meaningful.
    - **Completeness:** Include the details essential for understanding the specific point of the callout. Don't omit crucial information for the sake of brevity.
3. **Conciseness (Efficiency and No Fluff):**
    - **Be Economical:** While ensuring clarity (Principle #2), use the fewest words necessary to convey the information accurately.
    - **Eliminate Redundancy:** Avoid repeating points, using filler words ("in order to," "basically," "actually"), or overly elaborate sentence structures. Be direct.
    - **Focus:** Stick closely to the specific topic of the callout title. Don't include tangential information or unnecessary background.
4. **Modularity and Focused Callouts (Segmentation):**
    - **Principle:** Structure the notes into logical, modular callouts, each generally focused on a single distinct topic, concept, step, or aspect. This aids organization and readability.
    - **When to Segment:** Consider using separate callouts for clearly distinct parts of a larger topic. For example, define a concept in one `[!idea]` and illustrate it in a separate `[!example]`, or discuss different facets of a problem in separate `[!consider]` callouts. (This applies to how the user might define the table, and how you interpret it if the table is absent).
    - **Coherence:** Balance modularity with clarity. It's acceptable to keep closely related points together within a single callout if separating them would make the information harder to understand, provided the callout remains focused on its main theme.
5. **Readable Internal Structure (Enhancing Clarity):**
    - **Guideline:** Structure information _within_ callouts to maximize readability and support learning (Goal #7). Using a mix of formats, such as brief introductory sentences combined with focused bullet points or small tables, is generally the most effective way to achieve this.
    - **Actively Avoid Monotony:** Please actively avoid callouts that consist _only_ of a single block of paragraph text or _only_ a list of bullets, as this typically hinders readability. Look for opportunities to structure the information, for example, with a lead sentence and supporting points. This is non negotiable. Providing callouts with single paragraphs will constitute a failure.
    - **Flexibility for Brevity:** For genuinely simple, self-contained points requiring only one or two clear sentences, that brief structure is fine. However, for anything needing even slight elaboration or listing points, apply structural variety (like intro + bullets) to aid comprehension. Use judgment focused on making it easy for a reader to understand.
    - **Start Content on New Line:** Always begin callout content on the line _after_ the `> [!type] Title` header.
6. **Final Output Wrapper:** Enclose **each individual callout response** (or the entire note if only one callout is requested or no table is provided) within a single Markdown code block for accurate copying:

```Markdown
> [!type] Title
> Clear, concise content...
```

If multiple callouts are processed iteratively, when all are completed and approved, you may be asked to provide the full compiled note in this format.

## 7. Overarching Goal: Effective Learning Resource

**Please keep this ultimate objective in mind throughout the note generation process:**

- **Primary Purpose:** The notes created using this template are intended first and foremost as **learning resources**. Their main goal is to **teach** the specified topic clearly and effectively. Think about creating notes that you yourself would find helpful for understanding the material.
- **Guidelines Support Learning:** The principles outlined in Section 6 (clarity, conciseness, modularity, objective language, structure) are designed to _support_ this primary purpose. They are tools intended to make the information easier to understand, digest, and retain, not arbitrary rules.
- **Focus on Usefulness & Understanding:** While adhering to the guidelines is generally expected, it should not be a purely mechanical checklist exercise at the expense of the goal. The ultimate measure of success is whether the generated notes are **genuinely helpful, understandable, and educationally valuable** for someone learning the topic.
- **Educational Value is Paramount:** If you believe rigidly applying a specific guideline in a particular instance (for example, forcing segmentation that harms understanding, or being so concise on a complex point that it becomes confusing) would significantly detract from the clarity or educational value, **prioritize making the notes effective for learning.** Use your judgment to best balance the guidelines in service of this ultimate teaching goal. **Above all else, the notes must be useful and make sense as a learning tool.** The checklist is secondary to this core objective.

**Checklist (Internal AI Use - Comprehensive Review Against Principles & Goal for each callout generated):**

- [ ] **Objectivity:** Is the language neutral, factual, and free of subjective evaluations or bias (Principle 1)?
- [ ] **Clarity & Conciseness:** Does the content clearly convey the necessary information for understanding (Principle 2) AND is it expressed efficiently, directly, and without fluff or redundancy (Principle 3)? Is the balance appropriate?
- [ ] **Segmentation (Modularity):** (If applicable to current callout based on user's table) Is the current callout focused on its designated topic as per the table, distinct from others (Principle 4)?
- [ ] **Internal Structure & Readability:** Does the internal structure of EACH callout enhance readability (Guideline 5)?
    - [ ] Does it generally use a mix of formats (e.g., brief intro + bullets/table)?
    - [ ] Does it actively avoid monotony (i.e., NOT just a single paragraph AND NOT just a bullet list, unless the point was extremely brief and simple per the guideline)?
- [ ] **Basic Formatting:** Does content start on a new line after the callout header (Guideline 5)?
- [ ] **Sequence Adherence & Single Callout Focus:** If a specific callout sequence table was provided (Section 5), was the _current_ callout generated according to its specified order, type, and title? Is this response focused **only** on this single, current callout?
- [ ] **Structure Adherence**: Are you generating exactly one callout in this response if following a table?
- [ ] **Output Wrapper:** Is the current callout response correctly enclosed in a single ```markdown code block (Principle 6)?
- [ ] **Overall Goal Alignment:** Critically considering Section 7, does the current callout effectively serve the primary goal of being a genuinely useful, clear, and understandable learning resource? Does it prioritize educational value?
