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
        await self.update_right_panel()

    async def update_right_panel(self):
        """Update the right panel content"""
        if hasattr(self, 'right_panel'):
            self.right_panel.clear()
            current_step = self.get_current_step()
            
            with self.right_panel:
                with ui.column().classes('space-y-6'):
                    # Step Header
                    ui.label('HHHHHHHH').classes('text-2xl font-bold text-gray-900')
                    with ui.card().classes('bg-white shadow-sm'):
                        with ui.card_section().classes('p-6'):
                            with ui.row().classes('items-center mb-4'):
                                with ui.element('div').classes(f'w-16 h-16 rounded-xl {current_step.color} flex items-center justify-center mr-4 shadow-sm'):
                                    ui.label(current_step.icon).classes('text-white text-2xl')
                                with ui.column():
                                    ui.label(current_step.name).classes('text-2xl font-bold text-gray-900')
                                    ui.label(f'with {current_step.agent}').classes('text-gray-600')
                    
                    # Step Description
                    with ui.card().classes('bg-white shadow-sm'):
                        with ui.card_section().classes('p-6'):
                            ui.label('Description').classes('text-lg font-semibold text-gray-900 mb-3')
                            ui.label(current_step.description).classes('text-gray-600 leading-relaxed')
                    
                    # Key Questions
                    with ui.card().classes('bg-white shadow-sm'):
                        with ui.card_section().classes('p-6'):
                            ui.label('Key Questions').classes('text-lg font-semibold text-gray-900 mb-3')
                            with ui.column().classes('space-y-3'):
                                for question in current_step.questions:
                                    with ui.row().classes('items-start'):
                                        ui.icon('help_outline').classes('text-blue-500 mr-2 mt-1')
                                        ui.label(question).classes('text-gray-600')

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
        
        with ui.card().classes(card_classes).on('click', lambda: asyncio.create_task(self.switch_step(index))):
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
        
        with ui.column().classes('w-screen h-screen'):
            # First row - full width
            with ui.row().classes('w-screen bg-white border-b border-gray-200 p-6'):
                ui.label('Design Thinking').classes('text-2xl font-bold text-gray-900')
                ui.label('AI-Powered Innovation Journey').classes('text-gray-600 text-sm ml-4')
            
            # Separator line
            with ui.row().classes('w-screen h-[10px] bg-blue-500'):
                pass
            
            # Second row - two columns
            with ui.column().classes('w-[30%] h-full flex-1 bg-white border-r border-gray-200'):
                ui.label('TEST FIRST').classes('text-2xl font-bold text-red-500')
            # with ui.row().classes('flex-1 h-[calc(100vh-80px)] w-screen'):
                # First column - 30% width
                with ui.column().classes('w-[30%] h-full flex-1 bg-white border-r border-gray-200'):
                    with ui.scroll_area().classes('h-full'):
                        with ui.column().classes('p-4 space-y-3'):
                            for i, step in enumerate(self.design_steps):
                                self.create_step_card(step, i)
                
                # Second column - 70% width
                with ui.column().classes('w-[70%] h-full flex-1 bg-white border-r border-gray-200') as self.right_panel:
                    ui.label('TEST HEADER - COLUMN 2').classes('text-2xl font-bold text-red-500')
                #with ui.column().classes('w-[70%] bg-gray-50 p-6 h-full overflow-auto') as self.right_panel:

                    current_step = self.get_current_step()
                    with ui.column().classes('space-y-6'):
                        # Step Header
                        with ui.card().classes('bg-white shadow-sm'):
                            with ui.card_section().classes('p-6'):
                                with ui.row().classes('items-center mb-4'):
                                    with ui.element('div').classes(f'w-16 h-16 rounded-xl {current_step.color} flex items-center justify-center mr-4 shadow-sm'):
                                        ui.label(current_step.icon).classes('text-white text-2xl')
                                    with ui.column():
                                        ui.label(current_step.name).classes('text-2xl font-bold text-gray-900')
                                        ui.label(f'with {current_step.agent}').classes('text-gray-600')
                        
                        # Step Description
                        with ui.card().classes('bg-white shadow-sm'):
                            with ui.card_section().classes('p-6'):
                                ui.label('Description').classes('text-lg font-semibold text-gray-900 mb-3')
                                ui.label(current_step.description).classes('text-gray-600 leading-relaxed')
                        
                        # Key Questions
                        with ui.card().classes('bg-white shadow-sm'):
                            with ui.card_section().classes('p-6'):
                                ui.label('Key Questions').classes('text-lg font-semibold text-gray-900 mb-3')
                                with ui.column().classes('space-y-3'):
                                    for question in current_step.questions:
                                        with ui.row().classes('items-start'):
                                            ui.icon('help_outline').classes('text-blue-500 mr-2 mt-1')
                                            ui.label(question).classes('text-gray-600')

def main():
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
