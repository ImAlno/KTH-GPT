# KTH-GPT

**By Students for Students**

KTH-GPT is a specialized AI assistant designed to help KTH students by providing accurate answers based on course materials and university documents. It utilizes Retrieval-Augmented Generation (RAG) to ground its responses in specific source texts, ensuring relevance and reliability.

## 🚀 Features

-   **RAG-Powered Q&A**: Queries a local vector database (ChromaDB) to find relevant context from indexed PDF documents.
-   **Terminal-Style Interface**: A retro, terminal web interface for interacting with the AI.
-   **Local LLM Support**: Built to run with local LLMs via Ollama (defaulting to Mistral).
-   **Source Citations**: Provides sources for the generated answers to ensure transparency.

## 🛠️ Tech Stack

### Frontend
-   **React**: UI library.
-   **Vite**: Build tool and development server.
-   **CSS**: Custom styling for the terminal aesthetic.

### Backend / AI
-   **---**: 
-   **---**: 
-   **---**: 

## 📋 Prerequisites
-   **---**:
-   **---**:
-   **---**:

## 🏃‍♂️ Usage
-   **---**:
-   **---**:
-   **---**:

### Running the Frontend
Start the development server for the web interface:

```bash
# In the website directory
npm run dev
```
Open your browser and navigate to the local URL provided (usually `http://localhost:5173`).

## 💻 Terminal Commands

The terminal interface supports various commands to enhance your experience:

### General Commands
- `help` - Display list of available commands
- `about` - Learn more about KTH-GPT
- `contact` - Get contact information and GitHub link
- `clear` - Clear the terminal screen
- `copy` - Copy the last AI response to clipboard

### Fun Commands
There are also some hidden fun commands to discover! Try exploring with `help` or experimenting with different inputs.

### Theme Customization
Change the terminal appearance with `theme <name>`:

**Available Themes:**
- `default` - Classic green terminal
- `matrix` - Matrix-inspired green on black
- `kth` - KTH blue and white
- `dark` - Modern dark mode
- `retro` - Vintage amber terminal
- `cyberpunk` - Neon cyberpunk aesthetic
- `chroma` - Vibrant rainbow animations
- `purple` - Rich purple tones
- `dracula` - Popular Dracula color scheme
- `monokai` - Monokai editor theme
- `solarized-light` / `solarized-dark` - Solarized themes
- `nord` - Nord color palette
- `synthwave` - Synthwave/vaporwave aesthetic
- `ubuntu` - Ubuntu terminal style
- `red-alert` - Red alert theme
- `blue-screen` - Windows blue screen
- `sakura` - Dark sakura pink
- `soft-sakura` - Light sakura pink

**Example:** `theme chroma` or `theme matrix`

### Tips
- Use **Tab** to autocomplete commands and theme names
- Use **Arrow Up/Down** to navigate command history
- Commands are case-insensitive
