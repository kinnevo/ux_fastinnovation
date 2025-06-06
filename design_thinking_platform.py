#!/usr/bin/env python3
"""
Design Thinking Platform using NiceUI (Python)
A collaborative AI-powered design thinking journey with multiple specialized agents.
"""

from nicegui import ui, app
from typing import Dict, List, Optional
import asyncio
from datetime import datetime
from dataclasses import dataclass, field

@dataclass
class DesignStep:
    name: str
    icon: str
    color: str
    agent: str
    description: str
    questions: List[str]

@dataclass
class Message:
    type: str  # 'user' or 'agent'
    content: str
    timestamp: str

class DesignThinkingPlatform:
    def __init__(self):
        self.current_step = 0
        self.messages: Dict[int, List[Message]] = {}
        self.step_progress = [0] * 10
        self.chat_container = None
        self.progress_cards = []
        
        self.design_steps = [
            DesignStep(
                name='Empathize',
                icon='👥',
                color='bg-pink-500',
                agent='Empathy Agent',
                description='Understand user needs and pain points',
                questions=['What are users struggling with?', 'What emotions are involved?', 'What context matters?']
            ),
            DesignStep(
                name='Define',
                icon='🎯',
                color='bg-purple-500',
                agent='Problem Definition Agent',
                description='Synthesize observations into problem statement',
                questions=['What is the core problem?', 'Who is affected?', 'Why does this matter?']
            ),
            DesignStep(
                name='Ideate',
                icon='💡',
                color='bg-yellow-500',
                agent='Ideation Agent',
                description='Generate creative solutions',
                questions=['What if we tried...?', 'How might we...?', 'What are unconventional approaches?']
            ),
            DesignStep(
                name='Research',
                icon='🔍',
                color='bg-blue-500',
                agent='Research Agent',
                description='Validate assumptions and gather insights',
                questions=['What data supports this?', 'What are competitors doing?', 'What trends are relevant?']
            ),
            DesignStep(
                name='Prototype',
                icon='🔧',
                color='bg-green-500',
                agent='Prototyping Agent',
                description='Build quick, testable versions',
                questions=['What\'s the simplest version?', 'What can we test quickly?', 'What tools should we use?']
            ),
            DesignStep(
                name='Test',
                icon='🧪',
                color='bg-red-500',
                agent='Testing Agent',
                description='Gather feedback and validate solutions',
                questions=['How do users respond?', 'What works/doesn\'t work?', 'What should change?']
            ),
            DesignStep(
                name='Implement',
                icon='🚀',
                color='bg-indigo-500',
                agent='Implementation Agent',
                description='Execute and launch the solution',
                questions=['What\'s our rollout plan?', 'What resources do we need?', 'How do we measure success?']
            ),
            DesignStep(
                name='Learn',
                icon='⭐',
                color='bg-orange-500',
                agent='Learning Agent',
                description='Analyze results and extract insights',
                questions=['What did we learn?', 'What worked well?', 'What would we do differently?']
            ),
            DesignStep(
                name='Iterate',
                icon='➡️',
                color='bg-teal-500',
                agent='Iteration Agent',
                description='Refine based on learnings',
                questions=['How can we improve?', 'What needs adjustment?', 'What\'s the next version?']
            ),
            DesignStep(
                name='Scale',
                icon='📈',
                color='bg-gray-600',
                agent='Scaling Agent',
                description='Expand successful solutions',
                questions=['How do we scale this?', 'What systems are needed?', 'How do we maintain quality?']
            )
        ]
        
        # Initialize with sample messages
        self.messages[0] = [
            Message('agent', 'Hi! I\'m your Empathy Agent. Let\'s dive deep into understanding your users. What problem are you trying to solve?', '10:30 AM'),
            Message('user', 'We\'re working on a productivity app for remote workers who struggle with focus.', '10:31 AM'),
            Message('agent', 'Great starting point! Tell me about the emotional journey these remote workers experience. What does a typical distracted day look like for them?', '10:32 AM')
        ]

    def get_current_step(self) -> DesignStep:
        return self.design_steps[self.current_step]

    async def switch_step(self, step_index: int):
        """Switch to a different design thinking step"""
        self.current_step = step_index
        if step_index not in self.messages:
            self.messages[step_index] = []
        
        # Update UI
        await self.update_chat_display()
        await self.update_header()
        await self.update_input_placeholder()

    async def send_message(self, message_text: str):
        """Send a user message and get agent response"""
        if not message_text.strip():
            return
        
        # Add user message
        timestamp = datetime.now().strftime('%I:%M %p')
        user_message = Message('user', message_text, timestamp)
        
        if self.current_step not in self.messages:
            self.messages[self.current_step] = []
        
        self.messages[self.current_step].append(user_message)
        
        # Update progress
        self.step_progress[self.current_step] = min(100, self.step_progress[self.current_step] + 20)
        
        # Simulate agent response
        await asyncio.sleep(1)
        current_step_data = self.get_current_step()
        import random
        random_question = random.choice(current_step_data.questions)
        
        agent_response = Message(
            'agent',
            f'That\'s an interesting point about "{message_text}". Let me help you explore this further. {random_question}',
            datetime.now().strftime('%I:%M %p')
        )
        
        self.messages[self.current_step].append(agent_response)
        
        # Update UI
        await self.update_chat_display()
        await self.update_progress_display()

    async def update_chat_display(self):
        """Update the chat message display"""
        if self.chat_container:
            self.chat_container.clear()
            
            current_messages = self.messages.get(self.current_step, [])
            
            with self.chat_container:
                for message in current_messages:
                    self.create_message_bubble(message)

    def create_message_bubble(self, message: Message):
        """Create a message bubble for chat display"""
        is_user = message.type == 'user'
        
        with ui.row().classes('w-full justify-end' if is_user else 'w-full justify-start'):
            if not is_user:
                ui.avatar('🤖', size='sm').classes('bg-gray-100')
            
            with ui.column().classes('max-w-md'):
                ui.label(message.timestamp).classes('text-xs text-gray-500 mb-1')
                
                with ui.card().classes(
                    'p-3 ' + 
                    ('bg-blue-600 text-white' if is_user else 'bg-white shadow-sm')
                ):
                    ui.label(message.content).classes('text-sm leading-relaxed')
            
            if is_user:
                ui.avatar('👤', size='sm').classes('bg-blue-600 text-white')

    async def update_header(self):
        """Update the header with current step info"""
        # This would be called to update header elements
        pass

    async def update_input_placeholder(self):
        """Update input placeholder text"""
        # This would update the chat input placeholder
        pass

    async def update_progress_display(self):
        """Update progress indicators"""
        # This would update progress bars and percentages
        pass

    def create_step_card(self, step: DesignStep, index: int):
        """Create a step card for the sidebar"""
        is_active = index == self.current_step
        is_completed = self.step_progress[index] == 100
        progress = self.step_progress[index]
        
        card_classes = 'cursor-pointer transition-all duration-200 hover:shadow-md border-2 '
        if is_active:
            card_classes += 'border-blue-200 bg-blue-50'
        else:
            card_classes += 'border-transparent hover:border-gray-200'
        
        with ui.card().classes(card_classes).on('click', lambda idx=index: asyncio.create_task(self.switch_step(idx))):
            with ui.card_section():
                with ui.row().classes('items-center mb-3'):
                    # Step icon
                    with ui.element('div').classes(f'w-10 h-10 rounded-xl {step.color} flex items-center justify-center mr-3 shadow-sm'):
                        ui.label(step.icon).classes('text-white text-lg')
                    
                    # Step info
                    with ui.column().classes('flex-1 min-w-0'):
                        ui.label(f'{index + 1}. {step.name}').classes(
                            f'font-semibold text-sm truncate ' + 
                            ('text-blue-700' if is_active else 'text-gray-900')
                        )
                        ui.label(step.agent).classes('text-xs text-gray-500 truncate')
                    
                    # Completion status
                    if is_completed:
                        ui.icon('check_circle').classes('text-green-500')
                    else:
                        ui.icon('radio_button_unchecked').classes('text-gray-300')
                
                # Progress bar
                ui.linear_progress(value=progress/100).classes('mb-3')
                
                # Description
                ui.label(step.description).classes('text-xs text-gray-600 leading-relaxed')

    def create_insight_card(self, icon: str, title: str, content: str, color: str):
        """Create an insight card for the right panel"""
        with ui.card().classes(f'bg-{color}-50 border-{color}-200'):
            with ui.card_section().classes('p-3'):
                with ui.row().classes('items-center mb-2'):
                    ui.label(icon).classes(f'text-{color}-600 mr-2')
                    ui.badge(title).classes(f'bg-{color}-100 text-{color}-800 text-xs')
                
                ui.label(content).classes(f'text-xs text-{color}-800 leading-relaxed')

    def build_ui(self):
        """Build the main UI"""
        ui.page_title('Design Thinking Platform')
        
        # Custom CSS for better styling
        ui.add_head_html('''
        <style>
        .gradient-pink { background: linear-gradient(135deg, #ec4899, #db2777); }
        .gradient-purple { background: linear-gradient(135deg, #a855f7, #9333ea); }
        .gradient-yellow { background: linear-gradient(135deg, #eab308, #ca8a04); }
        .gradient-blue { background: linear-gradient(135deg, #3b82f6, #2563eb); }
        .gradient-green { background: linear-gradient(135deg, #10b981, #059669); }
        .gradient-red { background: linear-gradient(135deg, #ef4444, #dc2626); }
        .gradient-indigo { background: linear-gradient(135deg, #6366f1, #4f46e5); }
        .gradient-orange { background: linear-gradient(135deg, #f97316, #ea580c); }
        .gradient-teal { background: linear-gradient(135deg, #14b8a6, #0d9488); }
        .gradient-gray { background: linear-gradient(135deg, #6b7280, #4b5563); }
        </style>
        ''')
        
        with ui.splitter(value=800).classes('h-screen') as splitter:
            # Left Sidebar
            with splitter.before:
                with ui.column().classes('h-full bg-white border-r border-gray-200'):
                    # Header
                    with ui.card_section().classes('p-6 border-b border-gray-100'):
                        ui.label('Design Thinking').classes('text-2xl font-bold text-gray-900 mb-2')
                        ui.label('AI-Powered Innovation Journey').classes('text-gray-600 text-sm')
                    
                    # Steps list
                    with ui.scroll_area().classes('flex-1 p-4'):
                        with ui.column().classes('space-y-3'):
                            for i, step in enumerate(self.design_steps):
                                self.create_step_card(step, i)
            
            # Main content area
            with splitter.after:
                with ui.splitter(value=75, horizontal=False).classes('h-full'):
                    # Chat area
                    with splitter.before:
                        with ui.column().classes('h-full bg-white'):
                            # Chat header
                            with ui.card().classes('border-b border-gray-100 rounded-none'):
                                with ui.card_section().classes('p-6'):
                                    with ui.row().classes('items-center justify-between'):
                                        with ui.row().classes('items-center'):
                                            current_step = self.get_current_step()
                                            with ui.element('div').classes(f'w-12 h-12 rounded-xl gradient-{current_step.color.split("-")[1]} flex items-center justify-center mr-4 shadow-sm'):
                                                ui.label(current_step.icon).classes('text-white text-xl')
                                            
                                            with ui.column():
                                                ui.label(f'{current_step.name} Stage').classes('text-xl font-semibold text-gray-900')
                                                ui.label(f'Chat with {current_step.agent}').classes('text-gray-600 text-sm')
                                        
                                        with ui.row().classes('items-center space-x-4'):
                                            ui.badge(f'{self.step_progress[self.current_step]}% Complete').classes('bg-blue-100 text-blue-800')
                                            ui.avatar('🤖', size='md').classes('bg-blue-100')
                            
                            # Chat messages
                            with ui.scroll_area().classes('flex-1 p-6 bg-gray-50'):
                                self.chat_container = ui.column().classes('space-y-6')
                                # Initialize with current messages
                                current_messages = self.messages.get(self.current_step, [])
                                for message in current_messages:
                                    self.create_message_bubble(message)
                            
                            # Input area
                            with ui.card().classes('border-t border-gray-100 rounded-none'):
                                with ui.card_section().classes('p-6'):
                                    with ui.row().classes('space-x-3 mb-4'):
                                        message_input = ui.input(
                                            placeholder=f'Message {self.get_current_step().agent}...'
                                        ).classes('flex-1')
                                        
                                        async def send_handler():
                                            await self.send_message(message_input.value)
                                            message_input.value = ''
                                        
                                        ui.button('Send', icon='send', on_click=send_handler).props('unelevated')
                                        
                                        # Handle Enter key
                                        message_input.on('keydown.enter', send_handler)
                                    
                                    # Quick questions
                                    ui.label('Suggested prompts:').classes('text-xs text-gray-600 mb-2 font-medium')
                                    with ui.row().classes('flex-wrap gap-2'):
                                        current_step = self.get_current_step()
                                        for question in current_step.questions:
                                            ui.button(
                                                question, 
                                                on_click=lambda q=question: setattr(message_input, 'value', q)
                                            ).props('flat dense').classes('text-xs rounded-full')
                    
                    # Right panel - Insights
                    with splitter.after:
                        with ui.column().classes('h-full bg-white border-l border-gray-100'):
                            # Panel header
                            with ui.card_section().classes('p-6 border-b border-gray-100'):
                                ui.label('Project Insights').classes('text-lg font-semibold text-gray-900')
                            
                            with ui.scroll_area().classes('flex-1 p-6'):
                                with ui.column().classes('space-y-6'):
                                    # Overall Progress
                                    with ui.card():
                                        with ui.card_section().classes('p-4'):
                                            ui.label('Overall Progress').classes('font-medium text-gray-900 mb-4')
                                            with ui.column().classes('space-y-3'):
                                                for i, step in enumerate(self.design_steps):
                                                    with ui.row().classes('items-center justify-between'):
                                                        ui.label(step.name).classes('text-sm text-gray-600')
                                                        ui.badge(f'{self.step_progress[i]}%').classes(
                                                            'bg-green-100 text-green-800' if self.step_progress[i] == 100 
                                                            else 'bg-gray-100 text-gray-800'
                                                        )
                                    
                                    # Key Insights
                                    with ui.card():
                                        with ui.card_section().classes('p-4'):
                                            ui.label('Key Insights').classes('font-medium text-gray-900 mb-4')
                                            with ui.column().classes('space-y-3'):
                                                self.create_insight_card(
                                                    '💡', 'Ideation', 
                                                    'Focus interruption is the core issue for remote workers',
                                                    'yellow'
                                                )
                                                self.create_insight_card(
                                                    '👥', 'User Needs',
                                                    'Need for ambient focus cues and gentle accountability',
                                                    'green'
                                                )
                                    
                                    # Next Steps
                                    with ui.card():
                                        with ui.card_section().classes('p-4'):
                                            ui.label('Recommended Next Steps').classes('font-medium text-gray-900 mb-4')
                                            with ui.column().classes('space-y-3'):
                                                with ui.row().classes('items-center text-sm text-gray-600'):
                                                    ui.icon('arrow_forward').classes('mr-3 text-blue-500')
                                                    ui.label(f'Complete current {self.get_current_step().name} stage')
                                                
                                                with ui.row().classes('items-center text-sm text-gray-600'):
                                                    ui.icon('schedule').classes('mr-3 text-blue-500')
                                                    ui.label('Schedule user interviews')

def main():
    print("XXX Starting Design Thinking Platform...")

    """Main application entry point"""
    platform = DesignThinkingPlatform()
    platform.build_ui()
    
    ui.run(
        title='xDesign Thinking Platform V 0.1',
        port=8080,
        host='0.0.0.0',
        reload=True,
        show=True
    )

if __name__ in {"__main__", "__mp_main__"}:
    main()
