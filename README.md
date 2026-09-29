# Real AI Study Helper 🤖📚

An intelligent study companion powered by Claude AI that actually understands your learning tasks and provides meaningful guidance.

## Features

✅ **Real AI Understanding** - Uses Claude API to comprehend and respond intelligently
✅ **Multi-turn Conversations** - Maintains context across multiple messages
✅ **Task Guidance** - Get step-by-step help for any study task
✅ **Concept Explanations** - Learn complex ideas in simple terms
✅ **Adaptive Learning** - AI adjusts explanations based on your responses
✅ **Progress Tracking** - Keep track of completed tasks
✅ **Vietnamese Support** - Responds in Vietnamese or English

## Setup

### 1. Install Dependencies
```bash
pip install -r requirements.txt
```

### 2. Get Your Claude API Key
- Go to [console.anthropic.com](https://console.anthropic.com/)
- Create an account or sign in
- Navigate to API Keys
- Create a new API key

### 3. Set Environment Variables

**Option A: Using .env file (recommended)**
```bash
cp .env.example .env
# Edit .env and paste your API key:
# ANTHROPIC_API_KEY=sk-ant-xxxxxxxx...
```

**Option B: Using environment variable**
```bash
export ANTHROPIC_API_KEY="sk-ant-xxxxxxxx..."
```

### 4. Run the Helper
```bash
python ai_study_helper.py
```

## Usage Examples

### Interactive Conversation
```
You: What is photosynthesis?
AI: Photosynthesis is the process where plants convert light energy...

You: Can you explain it more simply?
AI: Sure! Think of it like this...
```

### Get Task Help
```
You: task Read 5 pages of biology and summarize key concepts
AI: Here's a step-by-step approach:
1. Preview the chapter...
2. Read actively...
3. Take notes...
```

### Explain a Concept
```
You: explain quantum mechanics
AI: Quantum mechanics is...
```

### Other Commands
- `clear` - Start a new topic (clears conversation history)
- `stats` - See your progress
- `done` - Mark a task as completed
- `help` - Show all available commands
- `quit` - Exit

## How It's Different From the Static Helper

| Feature | Prescript (Static) | Real AI Helper |
|---------|-------------------|----------------|
| Understands tasks | ❌ Dictionary lookup | ✅ Real comprehension |
| Adaptive responses | ❌ Fixed templates | ✅ Generates new explanations |
| Asks clarifying questions | ❌ No | ✅ Yes |
| Maintains context | ❌ No memory | ✅ Full conversation history |
| Can answer any topic | ❌ Predefined only | ✅ Unlimited knowledge |
| Personalization | ❌ No | ✅ Learns your style |

## Architecture

```
User Input
    ↓
AI Study Helper (Python)
    ↓
Conversation Manager
    ↓
Claude API (via Anthropic SDK)
    ↓
Intelligent Response
    ↓
User Output
```

## System Prompt

The AI is guided by a system prompt that tells it:
- How to be an effective study helper
- How to explain concepts clearly
- How to provide encouragement
- How to remember conversation context
- How to adapt to student needs

## API Costs

- First 3 months: Free (if using credits)
- After: ~$0.003 per 1K input tokens, ~$0.015 per 1K output tokens
- Typical study session: ~50-100 tokens = ~$0.0005-0.001

## Troubleshooting

**Q: "ANTHROPIC_API_KEY not found"**
A: Make sure your .env file exists and has your API key, or set the environment variable.

**Q: API errors**
A: Check that:
- Your API key is valid
- You have internet connection
- Your API key has sufficient credits

**Q: Slow responses**
A: Claude API can take 1-3 seconds. This is normal.

## Next Steps

Potential enhancements:
- Web UI with chat interface
- Integration with Prescript of Self-Study
- Image analysis for math problems
- Multi-language support
- Study plan generation
- Progress analytics dashboard

## License

MIT License - feel free to use and modify!

---

**Made for learners by learners** 🚀