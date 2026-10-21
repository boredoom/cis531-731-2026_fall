# How to Prime the Generative AI Kit (v2.3)
**Path:** `admin/policies/generative_ai_kit_howto_v2.md`

To use the Generative AI Kit effectively, you must strictly separate the global rules of the course from the specific homework task you are working on. If you paste everything into a single chat, the AI will suffer from context amnesia. 

You must establish a persistent workspace by defining your **TBox** (Terminological Box: the rules and constraints of the course) at the **Project Level**, and submitting your specific **ABox** assertions (your homework payloads) at the **Chat Level**.

*(Note: If you are looking for the Phase 1 / PS 4 initialization guide, see [Generative AI Kit v1.0 How-To](./generative_ai_kit_howto.md).)*

---

## 0. Prepare the Course Files (The TBox)
Before configuring any platform, download the raw `.md` files of the following documents to your local machine:
1. [generative_ai_kit_v2.md](./generative_ai_kit_v2.md) (The System Instructions)
2. [04_term_project_guidelines.md](../syllabus/04_term_project_guidelines.md) (The Milestone Constraints)
3. [05_term_project_taxonomy.md](../syllabus/05_term_project_taxonomy.md) (The 3x5x5 Data Cube)
4. [06_term_project_sourcing_guide.md](../syllabus/06_term_project_sourcing_guide.md) (The Tier 1-3 Source Rules)

---

## 1. Establish the Project Environment
Follow these steps to permanently anchor the TBox in your chosen platform. Do this **once** for the entire semester.

### ChatGPT (Projects) or M365 Copilot (Notebooks)
*   **Create the Space:** In ChatGPT, select **New Project** (requires Plus/Team/Pro). In M365, select **New notebook**. Name it `CIS 531-731 Term Project`.
*   **Establish the TBox (Instructions):** Copy the *entire contents* of `generative_ai_kit_v2.md` and paste it into the **Project instructions** field. 
*   **Establish the Baseline ABox (Knowledge):** Upload `04_term_project_guidelines.md`, `05_term_project_taxonomy.md`, and `06_term_project_sourcing_guide.md` to the project's persistent knowledge base/reference section.

### Claude (Anthropic) or Qwen
*   **Create the Space:** In Claude, click **+ New Project**. In Qwen (Alibaba Model Studio), select **Create Agent Application**. 
*   **Establish the TBox (Instructions):** Paste the complete contents of `generative_ai_kit_v2.md` into the Custom Instructions / System prompt box. 
*   **Establish the Baseline ABox (Knowledge):** Upload the `04`, `05`, and `06` markdown files to the Project Knowledge area.

### Gemini (Google)
*   **Create the Space:** Open Gemini, select **Gems** (or **Skills**), and click **New Gem**. Name it `CIS 531-731 Project Tollbooth`.
*   **Establish the TBox (Instructions):** Paste the complete contents of `generative_ai_kit_v2.md` into the Gem's Instructions field.
*   **Establish the Baseline ABox (Knowledge):** Under **Knowledge**, upload the `04`, `05`, and `06` markdown files directly from your drive (do not use Google Docs links to ensure pure Markdown parsing).

### Perplexity or Grok (xAI)
*   **Create the Space:** In Perplexity, select **Create a Project** (formerly Spaces). In Grok, navigate to **Projects**.
*   **Establish the TBox (Instructions):** Paste the complete contents of `generative_ai_kit_v2.md` into the Space/Project custom instructions field.
*   **Establish the Baseline ABox (Knowledge):** Upload the `04`, `05`, and `06` markdown files to the Space/Project files area.

---

## 2. Execute the Chat (The Assignment ABox)
Once your Project is configured, you will use it to complete individual assignments. **Do not upload the assignments to the Project Knowledge Base.** You must upload them directly to the individual **Chat window** at the exact moment you are working on them.

When you are ready to execute a Tollbooth prompt from the GenAI Kit, download the corresponding raw `.md` assignment file and attach it to your chat message:

*   **For MP 5 (Structured Streaming):** Attach [mp5_structured_streaming.md](../../assignments/machine_problems/mp5_structured_streaming.md) to the chat.
*   **For PS 6 (VDB Schema):** Attach [ps6_semantic_search_vdb_schema.md](../../assignments/homework/ps6_semantic_search_vdb_schema.md) to the chat.
*   **For MP 7 (Few-Shot Classification):** Attach [mp7_genre_classification.md](../../assignments/machine_problems/mp7_genre_classification.md) to the chat.
*   **For PS 8 (Interim Report):** Attach [ps8_interim_report.md](../../assignments/homework/ps8_interim_report.md) to the chat.

### Execution Flow:
1. Open a new chat *inside* your configured Project/Gem/Space.
2. Run the Initialization **"Intake Check"** prompt defined in the kit.
3. **Wait** for the AI to acknowledge your project state.
4. Attach the specific assignment `.md` file to the chat box.
5. Execute the specific Tollbooth prompt for that assignment, providing your data payload (the "Toll").
