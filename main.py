from openai import OpenAI
import time
from typing import Dict, List, Tuple

class StoryContext:
    def __init__(self):
        self.current_story = ""
        self.main_character = None
        self.setting = None
        self.special_ability = None
        
    def update_story(self, new_segment: str):
        self.current_story += "\n" + new_segment if self.current_story else new_segment
        
    def set_story(self, story: str):
        """Replace the entire story with a new version"""
        self.current_story = story

class InteractiveStoryTeller:
    def __init__(self, api_key: str):
        self.client = OpenAI(api_key=api_key)
        self.context = StoryContext()
        
        self.confusion_phrases = [
            "what", "what?", "huh", "huh?", "don't know", "idk",
            "what does that mean", "i don't understand", "don't get it",
            "what do you mean", "confused", "not sure", "mean",
            "explain", "how", "why", "where", "when",
            "can you explain", "tell me more", "what is"
        ]
        
        self.confusion_responses = {
            "character": [
                "Oh! I'm asking who you want our story to be about!",
                "It could be someone like:",
                "- A brave princess who loves to go on adventures",
                "- A friendly dragon who bakes yummy cookies",
                "- A silly unicorn who changes colors when happy",
                "- A clever mouse who builds amazing inventions",
                "Who would you like to hear a story about?"
            ],
            
            "setting": [
                "Let me explain! I'm asking where our story should take place!",
                "It could be somewhere magical like:",
                "- In a castle made of sparkly crystals",
                "- In a forest where the trees glow at night",
                "- Under the sea in a coral palace",
                "- Up in the clouds in a floating house",
                "Where do you think would be a fun place for our story?"
            ],
            
            "ability": [
                "Oh! I'm asking what special magic or power they should have!",
                "They could do amazing things like:",
                "- Turn invisible whenever they want",
                "- Talk to all the animals in the world",
                "- Make rainbows appear with a wave of their hand",
                "- Fly high in the sky like a bird",
                "What special power would be fun for our friend to have?"
            ]
        }

    def slow_print(self, text: str, delay: float = 0.03):
        """Print text slowly like a storyteller would speak"""
        for char in text:
            print(char, end='', flush=True)
            time.sleep(delay)
        print()

    def get_story_segment(self, prompt: str) -> str:
        """Generate a segment of the story"""
        # If we have previous story content, include it in the prompt but instruct not to repeat it
        if self.context.current_story:
            full_prompt = f"""
            Previous story (for context only, do not repeat this part):
            {self.context.current_story}

            Now add this new part to the story (generate only the new part):
            {prompt}

            Important: Only write the new part of the story. Do not include or repeat any previous parts.
            """
        else:
            full_prompt = prompt

        messages = [
            {
                "role": "system", 
                "content": "You are a warm, engaging storyteller for children ages 5-10. Use simple, clear language that a young child can understand. Each story segment should be less than 7 sentences long and end at a natural pausing point."
            },
            {
                "role": "user",
                "content": full_prompt
            }
        ]
        
        response = self.client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=messages,
            temperature=0.7
        )
        
        return response.choices[0].message.content.strip()

    def get_complete_story(self, prompt: str) -> str:
        """Generate a complete story"""
        messages = [
            {
                "role": "system", 
                "content": """You are a warm, engaging storyteller for children ages 5-10. 
                Create complete, engaging stories using simple language that young children can understand. 
                Make stories magical and fun, with clear beginnings, middles, and endings.
                Use short paragraphs and natural pauses.
                Make sure all sentences are complete and the story flows well."""
            },
            {
                "role": "user",
                "content": prompt
            }
        ]
        
        response = self.client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=messages,
            temperature=0.7
        )
        
        return response.choices[0].message.content.strip()

    def get_child_input(self, prompt: str) -> str:
        """Get input from the child in a friendly way"""
        self.slow_print("\n" + prompt + " ")
        return input("(Tell me what you think): ")

    def handle_confusion(self, question_type: str):
        """Handle confusion with appropriate response for each question type"""
        for line in self.confusion_responses[question_type]:
            self.slow_print(line)

    def handle_character_choice(self) -> str:
        """Handle the character selection interaction"""
        while True:
            character = self.get_child_input("Who should our story be about? (Maybe a princess, a brave knight, a friendly dragon, or someone else?)")
            
            if any(phrase in character.lower() for phrase in self.confusion_phrases):
                self.handle_confusion("character")
                continue
                
            if character.strip():
                self.slow_print(f"Ohh~ Very cool choice!")
                return character
                
            self.slow_print("I didn't quite get you. Who should be in our story?")

    def handle_setting_choice(self, character: str) -> str:
        """Handle the setting selection interaction"""
        while True:
            setting = self.get_child_input(f"Where should our character live? (In a castle, underwater, in space, or somewhere else magical?)")
            
            if any(phrase in setting.lower() for phrase in self.confusion_phrases):
                self.handle_confusion("setting")
                continue
                
            if setting.strip():
                self.slow_print(f"Sure! This sounds like an interesting place to live~")
                return setting
                
            self.slow_print("I didn't quite hear you. Could you tell me again where they should live?")

    def handle_special_ability(self, character: str) -> str:
        """Handle the special ability selection interaction"""
        while True:
            ability = self.get_child_input(f"What special magical power should our character have? (Like being invisible, flying, or making things float?)")
            
            if any(phrase in ability.lower() for phrase in self.confusion_phrases):
                self.handle_confusion("ability")
                continue
                
            if ability.strip():
                self.slow_print(f"That's amazing! Having this power will make our story so magical!")
                return ability
                
            self.slow_print("I missed that. What magical power should they have?")

    def handle_story_progression(self, character: str, ability: str) -> str:
        """Handle the 'what happens next' interaction with specific options"""
        while True:
            prompt = f"""
What should happen next in our story? Do you want to:
- Meet someone who needs help
- Find something magical or mysterious
- Use the special power to solve a problem
- Or something else?
"""
            next_event = self.get_child_input(prompt)
            
            if any(phrase in next_event.lower() for phrase in self.confusion_phrases):
                self.slow_print(f"Let me help you choose! Should {character}:")
                self.slow_print(f"- Help a baby dragon find their way back home")
                self.slow_print(f"- Discover a magical rainbow bridge")
                self.slow_print(f"- Use the special power to help forest animals")
                self.slow_print("Which sounds most fun to you?")
                continue
                
            if next_event.strip():
                self.slow_print("Ooh, let's continue the adventure!")
                return next_event
                
            self.slow_print("I didn't quite catch that. Let me ask again!")

    def handle_ending_choice(self, character: str, ability: str) -> str:
        """Handle the ending selection interaction with specific options"""
        while True:
            prompt = f"""
How should the adventure end? {character} could:
- Use the power to help everyone and make them happy
- Make lots of new friends and have a magical celebration
- Learn something special and share it with others
- Or do you have another fun idea?
"""
            ending = self.get_child_input(prompt)
            
            if any(phrase in ending.lower() for phrase in self.confusion_phrases):
                self.slow_print(f"Let me help you pick a fun ending! Should {character}:")
                self.slow_print(f"- Use their power to {ability} to make everyone smile")
                self.slow_print("- Have a big party with all their new friends")
                self.slow_print("- Share their magical gift with others who need help")
                self.slow_print("Which ending would you like best?")
                continue
                
            if ending.strip():
                self.slow_print("Sure~ That sounds wonderful!")
                return ending
                
            self.slow_print("I didn't quite get that. Let's choose an ending together!")

    def handle_final_feedback(self) -> None:
        """Handle the final feedback and complete story revision if needed"""
        while True:
            feedback = self.get_child_input("Did you enjoy our story?")
            
            if any(phrase in feedback.lower() for phrase in self.confusion_phrases):
                self.slow_print(f"Did you have fun hearing about this adventure?")
                continue
                
            if feedback.lower() in ['no', 'nope', 'not really', 'didn\'t like it', 'bad','n','N','No','NO']:
                dislike_reason = self.get_child_input("Where did you not like the story? Tell me what part wasn't fun!")
                
                self.slow_print("Thank you for telling me! Let me tell you a whole new version of the story...")
                
                revision_prompt = f"""
                Create a completely new, exciting version of this story that addresses this feedback: {dislike_reason}

                Story elements to keep:
                - Main character: {self.context.main_character}
                - Setting: {self.context.setting}
                - Special ability: {self.context.special_ability}

                Original story for reference:
                {self.context.current_story}

                Requirements for the new version:
                1. Create a complete story from beginning to end.
                2. Use very simple words that a 5-year-old can understand.
                3. Make the story more engaging by addressing their feedback.
                4. Include fun moments showing the special ability in action.
                5. Add excitement and magic throughout, by including some twists and turns.
                6. Give a happy, satisfying ending.
                7. Make the story flow naturally with clear paragraphs.

                Important: Tell a completely new adventure while keeping the same character and magic.
                Make this version different and more exciting than the original!
                """
                
                # Generate complete new story
                revised_story = self.get_complete_story(revision_prompt)
                
                self.slow_print(f"\n✨ Here's a whole new adventure about {self.context.main_character}! ✨\n")
                self.slow_print(revised_story)
                
                # Update the story context
                self.context.set_story(revised_story)
                
                # Check if they like the new version
                second_feedback = self.get_child_input("Do you like this version better?")
                if any(word in second_feedback.lower() for word in ['yes', 'yeah', 'better', 'good','ya','yas','yea','yep','definitely','ye','Y','y']):
                    self.slow_print("I'm so glad I could make the story more fun for you!")
                else:
                    self.slow_print("Thank you for helping me improve! I promise I will do better next time :)")
            else:
                self.slow_print("I'm so glad you did!")
            
            break

    def tell_interactive_story(self):
        print("\n🌟 Welcome to Story Time! 🌟")
        
        # Get story elements with proper interaction handling
        character = self.handle_character_choice()
        self.context.main_character = character
        
        setting = self.handle_setting_choice(character)
        self.context.setting = setting
        
        # Generate and show initial story setup
        initial_prompt = f"""
        Write the beginning of a children's story with:
        - Main character: {character}
        - Setting: {setting}
        
        Start with 'Once upon a time' and introduce our character and their magical world.
        Use simple words that a 5-year-old would understand.
        Make it fun and magical! Don't introduce any special power of the character here yet.
        The story opener should be about 3 sentences long, and it should stop right after the character and settings are introduced, with no transition into the actual story. 
        """
        
        story_start = self.get_story_segment(initial_prompt)
        self.slow_print("\n" + story_start)
        self.context.update_story(story_start)
        
        # Get special ability with proper interaction
        ability = self.handle_special_ability(character)
        self.context.special_ability = ability
        
        # Add special ability to story
        ability_prompt = f"""
        Continue the story by showing that {character} has this special ability: {ability}
        Show this ability in action with a fun example. 
        Keep using simple words and make it exciting!
        Write about 3-4 sentences.
        """
        ability_segment = self.get_story_segment(ability_prompt)
        self.slow_print("\n" + ability_segment)
        self.context.update_story(ability_segment)
        
        # Get next event with proper interaction
        next_event = self.handle_story_progression(character, ability)
        
        # Continue story with their suggestion
        middle_prompt = f"""
        Continue the story using this idea: {next_event}.
        Show how {character} uses their special ability of {ability} in this situation. This is the peak of the story so make sure to have some twists and turns.
        Keep it exciting and use simple words! Show the special power in action, and make the story full of imagination, but don't include the ending yet.
        Split this segment into 2 paragraghs, each paragragh contain about 3-4 sentences. End at a natural pause.
        """
        middle_part = self.get_story_segment(middle_prompt)
        self.slow_print("\n" + middle_part)
        self.context.update_story(middle_part)
        
        # Get ending with proper interaction
        ending_idea = self.handle_ending_choice(character, ability)
        
        # Complete the story
        ending_prompt = f"""
        End our story with this idea: {ending_idea}
        Make sure to:
        - Give {character} a happy ending.
        - Show how they used their ability of {ability} to help and grow.
        - Make it feel complete and satisfying.
        Write about 3-5 sentences.
        """
        ending = self.get_story_segment(ending_prompt)
        self.slow_print("\n" + ending)
        self.context.update_story(ending)
        
        # Wrap-up with feedback and possible revision
        self.slow_print("\n✨ The End ✨")
        self.handle_final_feedback()
        self.slow_print("\n🌙 Sweet dreams~ 🌙")

def main():
    api_key = "YOUR_API_KEY_HERE"  # Replace with your OpenAI API key
    # Ensure you set your API key securely, e.g., via environment variables
    storyteller = InteractiveStoryTeller(api_key)
    storyteller.tell_interactive_story()

if __name__ == "__main__":
    main()