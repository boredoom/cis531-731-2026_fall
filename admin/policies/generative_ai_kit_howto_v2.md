# How to Prime the Generative AI Kit (v2.3)
**Path:** `admin/policies/generative_ai_kit_howto_v2.md`

To use the Generative AI Kit effectively, you must permanently configure your AI workspace before you ever type a conversational prompt. 

If you paste instructions directly into a chat window, the AI will drop the context via "amnesia" after a few turns. You must establish a persistent workspace by defining your **TBox** (Terminological Box: the rules and constraints of the course) and your baseline **ABox** (Assertional Box: the specific project guidelines and datasets).

Before configuring any platform, you must download the raw `.md` files of the following documents to your local machine:
1. `generative_ai_kit_v2.md` (The System Instructions)
2. `04_term_project_guidelines.md` (The Milestone Constraints)
3. `05_term_project_taxonomy.md` (The 3x5x5 Data Cube)
4. `06_term_project_sourcing_guide.md` (The Tier 1-3 Source Feasibility Rules)

Below are the exact procedures for establishing this persistent TBox/ABox architecture across the five major AI platforms.

---

### 1. ChatGPT or Microsoft 365 Copilot
*Best for: General QA, methodology brainstorming, and robust Python PySpark/Pandas reasoning.*

**1A. ChatGPT (Projects)**
*   **Create the Space:** In the left sidebar, select **New Project** (requires Plus/Team/Pro). Name it `CIS 531-731 Term Project`.
*   **Establish the TBox (Instructions):** Open the project's `...` menu and select **Project settings**. Copy the *entire contents* of `generative_ai_kit_v2.md` and paste it into the **Project instructions** field. 
*   **Establish the ABox (Knowledge):** In the project view, select **Add files**. Upload the `04`, `05`, and `06` markdown files. These files will now persist across every chat you start in this project.

**1B. Microsoft 365 Copilot (Notebooks)**
*   **Create the Space:** Open M365 Copilot and select **Notebooks** from the left navigation. Select **New notebook**.
*   **Establish the TBox (Instructions):** Paste the complete contents of `generative_ai_kit_v2.md` into the personalization/instructions field.
*   **Establish the ABox (Knowledge):** Open the **Content/References** pane, select **Upload**, and attach the `04`, `05`, and `06` markdown files.

---

### 2. Claude (Anthropic) or Qwen
*Best for: Deep context synthesis, strict adherence to formatting rubrics, and academic writing critique.*

**2A. Claude (Projects)**
*   **Create the Space:** Select **Projects** in the left navigation and click **+ New Project**. 
*   **Establish the TBox (Instructions):** Click **Set project instructions**. Paste the complete contents of `generative_ai_kit_v2.md` here. Claude is highly obedient to constraints and will act as a strict gatekeeper.
*   **Establish the ABox (Knowledge):** In the **Project knowledge** area, select the `+` control and upload the `04`, `05`, and `06` markdown files. 

**2B. Qwen (Alibaba Cloud Model Studio)**
*   **Create the Space:** Open Application Management and select **Create Agent Application**.
*   **Establish the TBox (Instructions):** Paste `generative_ai_kit_v2.md` into the agent's **System prompt**.
*   **Establish the ABox (Knowledge):** Create a knowledge base, upload the `04`, `05`, and `06` files, and connect the knowledge base to the agent.

---

### 3. Gemini (Google)
*Best for: Massive context windows (Gemini 1.5 Pro) and interactive reference filtering.*

*   **Create the Space:** Open Gemini, select **Settings and help**, and click **Gems** (or **Skills**, depending on account rollout). Select **New Gem**. Name it `CIS 531-731 Project Tollbooth`.
*   **Establish the TBox (Instructions):** Paste the complete contents of `generative_ai_kit_v2.md` into the Gem's **Instructions** field.
*   **Establish the ABox (Knowledge):** Under **Knowledge**, select **Add files** and upload the `04`, `05`, and `06` markdown files. *Note: Ensure you are uploading the actual files from your drive, not pasting Google Docs links, to ensure pure Markdown parsing.*

---

### 4. Perplexity
*Best for: Live literature reviews, finding SOTA baselines, and discovering datasets with active links.*

*   **Create the Space:** Open **Spaces** (or **Projects**) from the left navigation and select **Create a Space**.
*   **Establish the TBox (Instructions):** Locate the Space's **Custom instructions** field. Paste the complete contents of `generative_ai_kit_v2.md`. (Perplexity supports up to 8,000 characters, which safely accommodates the kit).
*   **Establish the ABox (Knowledge):** Open the Space's **Files** area and upload the `04`, `05`, and `06` markdown files. 
*   **Usage Note:** Create distinct threads inside this Space (e.g., `Thread 1: MP5 Stream`, `Thread 2: PS6 Chunking`). Your TBox instructions and ABox files will automatically apply to all threads within the Space.

---

### 5. Grok (xAI)
*Best for: Real-time discovery, identifying trending topics, and rapid code generation.*

*   **Create the Space:** Sign in and navigate to **Projects** (https://grok.com/project).
*   **Establish the TBox (Instructions):** Paste the complete contents of `generative_ai_kit_v2.md` into the Project instructions field.
*   **Establish the ABox (Knowledge):** Upload the `04`, `05`, and `06` markdown files to the project context. 

---

### 🚨 Final Grounding Test
Before trusting the AI with your project, start a chat in your configured workspace and run this test:

> **[PROMPT]** I am a CIS 531 undergraduate team. I want to build my own custom JSON schema for PS 6 based on an unbounded social media scrape. Evaluate this plan strictly against the uploaded course documents.

A properly configured Tollbooth will immediately reject this proposal on two grounds: 
1. Social media scraping is a Tier 3 Tarpit (`06_term_project_sourcing_guide.md`).
2. CIS 531 teams are strictly forbidden from generating custom schemas and must use the instructor-provided ontology (`generative_ai_kit_v2.md`). 

If the AI says "That sounds like a great idea!", you failed to load the instructions into the persistent memory. Delete the chat and rebuild the TBox/ABox.
