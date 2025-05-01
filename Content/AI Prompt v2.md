## 1. Objective: Create Clear, Modular Notes

Hello! Let's create some notes on the topic specified below.

- **Topic for Notes:** `[INSERT NOTES TOPIC HERE]`

I need these notes to be:

- **Concise & Modular:** Easy to digest in distinct blocks.
- **Focused on Key Ideas:** Highlight the core concepts for understanding.
- **Synthesized:** Please process and explain the information, not just copy text from sources.
- **Formatted with Callouts:** Structure the entire output using the 'callout' blocks defined below.

**Do not** provide a preliminary outline or introduction. Generate the final formatted note directly.

## 2. Callout Formatting Guide

Structure the notes using 'callout' blocks. Each block starts with `>` on every line, with the first line defining the type and title:

Markdown

```
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
```markdown
| Algorithm | Complexity | Notes           |
| :-------- | :--------- | :-------------- |
| Kruskal's | O(E log E) | Requires sorting |
| Prim's    | O(E log V) | Using Fibonacci heap |
```
    
- **Images**: Mark placement with a placeholder block. **Provide a clear description** of the desired image and use the Obsidian wikilink format `![[ImageName.png]]`.
```image-goes-here
Description: Diagram comparing the edge selection process of Kruskal's vs Prim's algorithm on the same sample graph. Kruskal's focuses on global lowest edge, Prim's grows from a starting node.
![[kruskal_vs_prim_comparison.png]]
```

- **Math**: Use LaTeX delimiters.
    - Inline: `$O(N^2)$`
    - Block:
```math
$$
f(x) = \int_{-\infty}^{\infty} \hat{f}(\xi)\,e^{2 \pi i \xi x} \,d\xi
$$
```
        
## 5. Specific Callout Sequence Interpretation

Check the table below. The user may provide specific instructions for the note's structure in this section. Your action depends on the state of this table in the user's request:

- **If the table contains entries (rows specifying Order, Callout Type, and Title):**
    - You **must** follow these instructions precisely.
    - Generate the note using the exact sequence, `[!callout type]`, and `Title` provided in each row of the table.
    - Do **not** add, remove, or reorder the callouts relative to the specified sequence.
    - Ensure the content generated for each callout is appropriate for its specified `[!callout type]` and `Title`.
- **If the table is empty or absent:**
    - You have the flexibility to select and sequence the callout types (e.g., `[!motivation]`, `[!idea]`, `[!example]`) and devise appropriate titles that you determine will best explain the topic and keyword effectively.

_(The table structure below illustrates the format the user employs. In an actual request where this is used, expect the `[!type]` and `Title Placeholder` fields to be filled with specific, user-defined values.)_

| **Order** | **Callout Type**   | **Title Placeholder**            |
| --------- | ------------------ | -------------------------------- |
| 1         | `[!type]`          | `(Example: Problem Statement)`   |
| 2         | `[!type]`          | `(Example: Core Algorithm)`      |
| 3         | `[!type]`          | `(Example: Walkthrough)`         |
| ...       | _(user adds rows)_ | _(user provides specific title)_ |

---

## 6. CRITICAL: Content & Formatting Rules

**Follow these instructions meticulously:**

1. **Objective Language:** Be neutral and factual. Describe _what_ things are and _how_ they work.
    - _Avoid:_ "This essential step significantly improves efficiency."
    - _Prefer:_ "This step uses data structure X to perform Y."
2. **Structure & Conciseness:**
    - Break down information into manageable segments.
    - **Mix formats:** Use short paragraphs, bullet points, and tables appropriately within callouts.
    - **NO:** Callouts that are just one large block of text.
    - **NO:** Callouts that consist _only_ of bullet points.
    - **Start Content on New Line:** Always begin the callout's content on the line _after_ the `> [!type] Title` header.
3. **No Evaluations:** Do not insert opinions or judgments about the utility or correctness of the concepts.
4. **Final Output Wrapper:** The **entire** note, including all `>` lines for all callouts, **must** be enclosed in a single Markdown code block:
````
```markdown
> [!motivation] Example Title
> Motivation content...

> [!idea] Another Title
> Idea content...
> - Detail 1
> - Detail 2
````

**Checklist (Internal AI Use):**

- [ ] Language is objective and non-judgmental?
- [ ] Content is concise and segmented?
- [ ] Used a mix of elements (text, lists, tables)? Not just paragraphs? Not just lists?
- [ ] Callout content starts on a new line below the header?
- [ ] Followed specific callout sequence if table was provided?
- [ ] Final output is fully wrapped in ` ```markdown ... ``` `?
