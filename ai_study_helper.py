#!/usr/bin/env python3
"""
Real AI Study Helper
Uses Claude API to provide intelligent study guidance and explanations
"""

import os
from dotenv import load_dotenv
from anthropic import Anthropic

# Load environment variables
load_dotenv()

class AIStudyHelper:
    def __init__(self):
        api_key = os.getenv('ANTHROPIC_API_KEY')
        if not api_key:
            raise ValueError(
                "❌ ANTHROPIC_API_KEY not found!\n"
                "Please set it in .env file or as environment variable.\n"
                "Get your key at: https://console.anthropic.com/"
            )
        
        self.client = Anthropic()
        self.conversation_history = []
        self.user_name = ""
        self.completed_tasks = 0
        
        self.system_prompt = """You are an intelligent study helper AI designed to guide students through learning tasks.

Your responsibilities:
1. Provide clear, actionable guidance for study tasks
2. Explain concepts in an encouraging and accessible way
3. Adapt explanations based on student responses and understanding
4. Ask clarifying questions when needed
5. Celebrate achievements and provide motivation
6. Remember context from previous messages in the conversation

Tone: Friendly, encouraging, and supportive. Use Vietnamese if the student uses Vietnamese.
Always be honest about what you know and don't know."""
    
    def chat(self, user_message: str) -> str:
        """Send a message to Claude and get a response"""
        # Add user message to history
        self.conversation_history.append({
            "role": "user",
            "content": user_message
        })
        
        # Get response from Claude
        response = self.client.messages.create(
            model="claude-3-5-sonnet-20241022",
            max_tokens=1024,
            system=self.system_prompt,
            messages=self.conversation_history
        )
        
        # Extract and store assistant response
        assistant_message = response.content[0].text
        self.conversation_history.append({
            "role": "assistant",
            "content": assistant_message
        })
        
        return assistant_message
    
    def get_task_help(self, task_description: str) -> str:
        """Get specific help for a study task"""
        prompt = f"""I have this study task: {task_description}
        
Can you:
1. Break down what I need to do
2. Explain why this task helps my learning
3. Give me a step-by-step approach
4. Provide tips for doing it effectively"""
        
        return self.chat(prompt)
    
    def explain_concept(self, concept: str) -> str:
        """Get an explanation of a learning concept"""
        prompt = f"""Please explain the concept of '{concept}' in a way that's easy to understand.
Include:
1. A simple definition
2. Real-world examples
3. Why it matters
4. Common mistakes to avoid"""
        
        return self.chat(prompt)
    
    def clear_history(self):
        """Clear conversation history for a new topic"""
        self.conversation_history = []
    
    def set_user(self, name: str):
        """Set the student's name"""
        self.user_name = name
        return f"Chào {name}! Tôi là AI Study Helper. Sẵn sàng giúp bạn học tập! 🎓"
    
    def complete_task(self):
        """Record a completed task"""
        self.completed_tasks += 1
        return f"✓ Tuyệt vời! Bạn đã hoàn thành {self.completed_tasks} nhiệm vụ!"


def main():
    """Main interactive study helper interface"""
    print("\n" + "="*60)
    print("🤖 REAL AI STUDY HELPER")
    print("="*60)
    print("Powered by Claude AI - Your intelligent study companion!")
    print("Commands: help, explain, task, clear, stats, quit\n")
    
    try:
        helper = AIStudyHelper()
    except ValueError as e:
        print(f"\n{e}")
        return
    
    # Get user name
    user_name = input("What's your name? > ").strip()
    if user_name:
        print(f"\n{helper.set_user(user_name)}\n")
    else:
        print("\nOkay, let's start!\n")
    
    print("Type your question or use commands (type 'help' for options)\n")
    
    while True:
        try:
            user_input = input("You: ").strip()
            
            if not user_input:
                continue
            
            # Handle commands
            if user_input.lower() == 'quit':
                print("\n👋 Great job today! Keep studying!")
                break
            
            elif user_input.lower() == 'help':
                print("""
📚 Available Commands:
  help      - Show this help message
  explain   - Explain a concept (follow prompts)
  task      - Get help with a specific task
  clear     - Clear conversation history (start fresh topic)
  stats     - Show your progress
  quit      - Exit the helper

Or just type any question and I'll help! 🤖
""")
                continue
            
            elif user_input.lower() == 'clear':
                helper.clear_history()
                print("\n✓ Conversation cleared. Starting fresh topic!\n")
                continue
            
            elif user_input.lower() == 'stats':
                print(f"\n📊 Your Progress:")
                print(f"   Name: {helper.user_name or 'Anonymous'}")
                print(f"   Tasks completed: {helper.completed_tasks}")
                print(f"   Messages in conversation: {len(helper.conversation_history)}\n")
                continue
            
            elif user_input.lower().startswith('explain '):
                concept = user_input[8:].strip()
                if concept:
                    print("\n🤔 Thinking...\n")
                    response = helper.explain_concept(concept)
                    print(f"AI: {response}\n")
                continue
            
            elif user_input.lower().startswith('task '):
                task = user_input[5:].strip()
                if task:
                    print("\n🤔 Analyzing task...\n")
                    response = helper.get_task_help(task)
                    print(f"AI: {response}\n")
                continue
            
            elif user_input.lower() == 'done':
                print(helper.complete_task())
                print()
                continue
            
            # Regular conversation
            else:
                print("\n🤔 Thinking...\n")
                response = helper.chat(user_input)
                print(f"AI: {response}\n")
        
        except KeyboardInterrupt:
            print("\n\n👋 Goodbye! Keep learning!")
            break
        except Exception as e:
            print(f"\n❌ Error: {str(e)}")
            print("Make sure your ANTHROPIC_API_KEY is set correctly.\n")


if __name__ == "__main__":
    main()