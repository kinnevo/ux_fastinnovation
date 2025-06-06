from nicegui import ui, app
import asyncio

class DesignThinkingApp:
    def __init__(self):
        self.current_step = 0
        self.design_steps = [
            {
                'name': 'Empathize',
                'icon': 'group',
                'color': 'pink-5',
                'description': 'Understanding Your Users Deeply',
                'content': {
                    'overview': 'Empathy is the cornerstone of human-centered design. This stage is about understanding the people you\'re designing for on a deep, emotional level.',
                    'key_activities': [
                        'Conduct user interviews and observations',
                        'Create empathy maps to visualize user experiences',
                        'Immerse yourself in the user\'s environment',
                        'Document emotional journeys and pain points'
                    ],
                    'methods': [
                        {'name': 'User Interviews', 'description': 'One-on-one conversations to understand user needs, motivations, and frustrations'},
                        {'name': 'Shadowing', 'description': 'Observing users in their natural environment to see unspoken behaviors'},
                        {'name': 'Empathy Maps', 'description': 'Visual tools capturing what users say, think, feel, and do'},
                        {'name': 'Journey Mapping', 'description': 'Documenting the user\'s end-to-end experience with touchpoints and emotions'}
                    ],
                    'tips': [
                        'Ask "why" questions to dig deeper into motivations',
                        'Focus on emotions, not just actions',
                        'Avoid leading questions that bias responses',
                        'Document everything - small details matter'
                    ],
                    'deliverables': [
                        'User personas based on real research',
                        'Empathy maps for each user type',
                        'Journey maps highlighting pain points',
                        'Key insights and opportunity areas'
                    ]
                }
            },
            {
                'name': 'Define',
                'icon': 'target',
                'color': 'purple-5',
                'description': 'Synthesizing Insights into Focused Problems',
                'content': {
                    'overview': 'The Define stage is about making sense of everything you learned during Empathize. You\'ll synthesize observations into a clear, actionable problem statement.',
                    'key_activities': [
                        'Analyze and synthesize empathy findings',
                        'Identify patterns and themes in user research',
                        'Create point-of-view statements',
                        'Formulate "How Might We" questions'
                    ],
                    'methods': [
                        {'name': 'Affinity Mapping', 'description': 'Grouping insights to identify patterns and themes'},
                        {'name': 'Point of View Statements', 'description': 'Structured statements defining user needs: [User] needs [need] because [insight]'},
                        {'name': 'How Might We Questions', 'description': 'Reframing problems as opportunities for design'},
                        {'name': 'Problem Prioritization', 'description': 'Ranking problems by impact and feasibility'}
                    ],
                    'tips': [
                        'Base definitions on research, not assumptions',
                        'Keep problem statements human-centered',
                        'Make problems specific and actionable',
                        'Focus on one core problem at a time'
                    ],
                    'deliverables': [
                        'Clear problem statement',
                        'Prioritized user needs',
                        'How Might We questions',
                        'Design challenge definition'
                    ]
                }
            },
            {
                'name': 'Ideate',
                'icon': 'lightbulb',
                'color': 'yellow-5',
                'description': 'Generating Creative Solutions',
                'content': {
                    'overview': 'Ideation is where creativity meets strategy. Generate a wide range of potential solutions before narrowing down to the most promising concepts.',
                    'key_activities': [
                        'Brainstorm multiple solution approaches',
                        'Build on others\' ideas',
                        'Think outside conventional boundaries',
                        'Select and refine top concepts'
                    ],
                    'methods': [
                        {'name': 'Brainstorming', 'description': 'Classic ideation technique focusing on quantity over quality initially'},
                        {'name': 'Worst Possible Ideas', 'description': 'Generate terrible solutions to break mental barriers'},
                        {'name': 'SCAMPER Method', 'description': 'Systematic approach: Substitute, Combine, Adapt, Modify, Put to other uses, Eliminate, Reverse'},
                        {'name': 'Storyboarding', 'description': 'Visual narratives showing how solutions work in context'}
                    ],
                    'tips': [
                        'Defer judgment during initial brainstorming',
                        'Build on ideas rather than shooting them down',
                        'Encourage wild ideas - they often lead to breakthroughs',
                        'Use visual thinking and sketching'
                    ],
                    'deliverables': [
                        'Long list of potential solutions',
                        'Selected concepts for development',
                        'Storyboards or concept sketches',
                        'Solution evaluation criteria'
                    ]
                }
            },
            {
                'name': 'Research',
                'icon': 'search',
                'color': 'blue-5',
                'description': 'Validating Ideas with Evidence',
                'content': {
                    'overview': 'Research validates your concepts with real-world evidence. Understand market context, technical feasibility, and competitive landscape.',
                    'key_activities': [
                        'Conduct market and competitive analysis',
                        'Validate technical feasibility',
                        'Research existing solutions',
                        'Gather supporting evidence for concepts'
                    ],
                    'methods': [
                        {'name': 'Competitive Analysis', 'description': 'Systematic review of existing solutions and their strengths/weaknesses'},
                        {'name': 'Technical Feasibility Study', 'description': 'Assessment of technical requirements and constraints'},
                        {'name': 'Market Research', 'description': 'Understanding market size, trends, and opportunities'},
                        {'name': 'Literature Review', 'description': 'Academic and industry research on related topics'}
                    ],
                    'tips': [
                        'Look for both direct and indirect competitors',
                        'Understand why existing solutions fall short',
                        'Consider technical and business constraints early',
                        'Use research to refine, not replace, user insights'
                    ],
                    'deliverables': [
                        'Competitive landscape analysis',
                        'Technical feasibility assessment',
                        'Market opportunity sizing',
                        'Research-backed concept refinements'
                    ]
                }
            },
            {
                'name': 'Prototype',
                'icon': 'build',
                'color': 'green-5',
                'description': 'Building to Think and Learn',
                'content': {
                    'overview': 'Prototyping makes ideas tangible. Build quick, low-cost versions to test assumptions and communicate concepts effectively.',
                    'key_activities': [
                        'Create low-fidelity prototypes quickly',
                        'Test specific assumptions or features',
                        'Iterate based on learnings',
                        'Communicate ideas through prototypes'
                    ],
                    'methods': [
                        {'name': 'Paper Prototypes', 'description': 'Quick sketches and paper mockups for early concept testing'},
                        {'name': 'Digital Wireframes', 'description': 'Low-fidelity digital representations of interfaces'},
                        {'name': 'Role Playing', 'description': 'Acting out services or experiences to understand interactions'},
                        {'name': 'Wizard of Oz', 'description': 'Simulating automated features manually behind the scenes'}
                    ],
                    'tips': [
                        'Start with the lowest fidelity that tests your hypothesis',
                        'Focus on key interactions and user flows',
                        'Don\'t get attached to any single prototype',
                        'Prototype to learn, not to impress'
                    ],
                    'deliverables': [
                        'Testable prototypes at appropriate fidelity',
                        'Documentation of key assumptions being tested',
                        'User flow diagrams',
                        'Prototype testing plan'
                    ]
                }
            },
            {
                'name': 'Test',
                'icon': 'science',
                'color': 'red-5',
                'description': 'Learning Through User Feedback',
                'content': {
                    'overview': 'Testing validates (or invalidates) your design decisions with real users. It\'s about learning, not proving you\'re right.',
                    'key_activities': [
                        'Plan user testing sessions',
                        'Observe user behavior with prototypes',
                        'Gather qualitative and quantitative feedback',
                        'Identify what works and what doesn\'t'
                    ],
                    'methods': [
                        {'name': 'Usability Testing', 'description': 'Observing users complete tasks with your prototype'},
                        {'name': 'A/B Testing', 'description': 'Comparing different versions to see which performs better'},
                        {'name': 'Feedback Sessions', 'description': 'Structured conversations about user experience'},
                        {'name': 'Analytics Review', 'description': 'Using data to understand user behavior patterns'}
                    ],
                    'tips': [
                        'Test early and often with real users',
                        'Observe behavior, not just feedback',
                        'Ask follow-up questions to understand "why"',
                        'Be prepared to be wrong - that\'s valuable learning'
                    ],
                    'deliverables': [
                        'User testing results and insights',
                        'Identified usability issues',
                        'Validated (or invalidated) assumptions',
                        'Prioritized improvement recommendations'
                    ]
                }
            },
            {
                'name': 'Implement',
                'icon': 'rocket_launch',
                'color': 'indigo-5',
                'description': 'Bringing Solutions to Life',
                'content': {
                    'overview': 'Implementation turns validated prototypes into real solutions. Plan for launch, scale, and ongoing success.',
                    'key_activities': [
                        'Plan development and launch strategy',
                        'Build production-ready solutions',
                        'Coordinate cross-functional teams',
                        'Monitor initial rollout'
                    ],
                    'methods': [
                        {'name': 'Agile Development', 'description': 'Iterative development process with regular check-ins'},
                        {'name': 'Phased Rollout', 'description': 'Gradual release to manage risk and gather feedback'},
                        {'name': 'Cross-functional Collaboration', 'description': 'Working with engineering, marketing, and other teams'},
                        {'name': 'Quality Assurance', 'description': 'Systematic testing to ensure solution meets requirements'}
                    ],
                    'tips': [
                        'Maintain design integrity during development',
                        'Plan for edge cases and error states',
                        'Set up metrics to measure success',
                        'Prepare for user onboarding and support'
                    ],
                    'deliverables': [
                        'Production-ready solution',
                        'Launch plan and timeline',
                        'Success metrics and monitoring',
                        'User onboarding materials'
                    ]
                }
            },
            {
                'name': 'Learn',
                'icon': 'star',
                'color': 'orange-5',
                'description': 'Extracting Insights from Results',
                'content': {
                    'overview': 'Learning transforms post-launch data into actionable insights. Understand what worked, what didn\'t, and why.',
                    'key_activities': [
                        'Analyze usage data and user feedback',
                        'Compare results to success metrics',
                        'Identify unexpected patterns',
                        'Document key learnings'
                    ],
                    'methods': [
                        {'name': 'Data Analysis', 'description': 'Quantitative analysis of user behavior and performance metrics'},
                        {'name': 'User Feedback Collection', 'description': 'Systematic gathering of qualitative user responses'},
                        {'name': 'Performance Review', 'description': 'Assessment against original success criteria'},
                        {'name': 'Retrospective Analysis', 'description': 'Team reflection on process and outcomes'}
                    ],
                    'tips': [
                        'Look for both expected and surprising results',
                        'Combine quantitative data with qualitative insights',
                        'Be honest about what didn\'t work',
                        'Document learnings for future projects'
                    ],
                    'deliverables': [
                        'Performance analysis report',
                        'Key insights and learnings',
                        'Success factors and failure points',
                        'Recommendations for improvement'
                    ]
                }
            },
            {
                'name': 'Iterate',
                'icon': 'refresh',
                'color': 'teal-5',
                'description': 'Improving Based on Learning',
                'content': {
                    'overview': 'Iteration applies learnings to improve your solution. This is where continuous improvement happens.',
                    'key_activities': [
                        'Prioritize improvements based on learnings',
                        'Plan next iteration cycle',
                        'Implement refinements',
                        'Test improvements'
                    ],
                    'methods': [
                        {'name': 'Feature Prioritization', 'description': 'Ranking potential improvements by impact and effort'},
                        {'name': 'Continuous Testing', 'description': 'Ongoing validation of changes and improvements'},
                        {'name': 'Version Planning', 'description': 'Strategic planning of feature releases and updates'},
                        {'name': 'User Co-creation', 'description': 'Involving users in the improvement process'}
                    ],
                    'tips': [
                        'Focus on high-impact, achievable improvements',
                        'Don\'t try to fix everything at once',
                        'Keep testing as you iterate',
                        'Maintain connection with user needs'
                    ],
                    'deliverables': [
                        'Prioritized improvement roadmap',
                        'Updated solution versions',
                        'Continuous testing results',
                        'Evolution documentation'
                    ]
                }
            },
            {
                'name': 'Scale',
                'icon': 'trending_up',
                'color': 'grey-6',
                'description': 'Growing Successful Solutions',
                'content': {
                    'overview': 'Scaling takes proven solutions to new markets, users, or contexts while maintaining quality and effectiveness.',
                    'key_activities': [
                        'Plan scaling strategy and approach',
                        'Adapt solutions for new contexts',
                        'Build systems for growth',
                        'Monitor quality during expansion'
                    ],
                    'methods': [
                        {'name': 'Market Expansion', 'description': 'Systematic approach to entering new user segments or markets'},
                        {'name': 'Platform Development', 'description': 'Building scalable systems and infrastructure'},
                        {'name': 'Partnership Strategy', 'description': 'Leveraging relationships to accelerate growth'},
                        {'name': 'Quality Assurance', 'description': 'Maintaining standards as you scale'}
                    ],
                    'tips': [
                        'Understand what made the original solution successful',
                        'Adapt thoughtfully to new contexts',
                        'Invest in systems and processes for scale',
                        'Don\'t sacrifice quality for growth'
                    ],
                    'deliverables': [
                        'Scaling strategy and roadmap',
                        'Adapted solutions for new contexts',
                        'Scalable systems and processes',
                        'Growth metrics and monitoring'
                    ]
                }
            }
        ]
        
    def navigate_to_step(self, step_index):
        self.current_step = step_index
        self.update_content()
        
    def previous_step(self):
        if self.current_step > 0:
            self.current_step -= 1
            self.update_content()
            
    def next_step(self):
        if self.current_step < len(self.design_steps) - 1:
            self.current_step += 1
            self.update_content()
    
    def update_content(self):
        # Clear and rebuild the main content area
        self.main_content.clear()
        self.build_main_content()
        
        # Update navigation buttons state
        self.prev_button.set_enabled(self.current_step > 0)
        self.next_button.set_enabled(self.current_step < len(self.design_steps) - 1)
        
        # Update step counter
        self.step_counter.set_text(f"Stage {self.current_step + 1} of {len(self.design_steps)}")
        
        # Update current stage indicator in top bar
        self.current_stage_text.set_text(f"{self.current_step + 1} of {len(self.design_steps)}")
        
        # Rebuild the sidebar to update colors
        self.sidebar.clear()
        with self.sidebar:
            # Sidebar header
            with ui.card().classes('w-full border-b border-grey-3 rounded-none p-4'):
                ui.label('Design Process').classes('text-lg font-semibold text-grey-9 mb-2')
                ui.label('Navigate through each stage').classes('text-sm text-grey-6')
            
            # Scrollable steps list
            with ui.scroll_area().classes('flex-1 p-4'):
                for index, step in enumerate(self.design_steps):
                    is_active = index == self.current_step
                    card_classes = 'w-full mb-3 p-4 cursor-pointer transition-all duration-200'
                    if is_active:
                        card_classes += ' bg-blue-500 text-white'
                    else:
                        card_classes += ' bg-white hover:bg-grey-2'
                    
                    with ui.card().classes(card_classes).on('click', lambda i=index: self.navigate_to_step(i)):
                        with ui.row().classes('items-center'):
                            ui.icon(step['icon']).classes(f'text-2xl text-white bg-{step["color"]} rounded-full p-2 mr-3')
                            with ui.column().classes('flex-1'):
                                title_classes = 'font-semibold'
                                if is_active:
                                    title_classes += ' text-white'
                                else:
                                    title_classes += ' text-grey-7'
                                ui.label(f'{index + 1}. {step["name"]}').classes(title_classes)
                                ui.label(step['description']).classes('text-sm text-grey-5')
                            if is_active:
                                ui.icon('check_circle').classes('text-white')

    def build_main_content(self):
        current_step_data = self.design_steps[self.current_step]
        
        with self.main_content:
            # Stage Header
            with ui.card().classes('w-full mb-8 p-6'):
                with ui.row().classes('items-center'):
                    ui.icon(current_step_data['icon']).classes(f'text-6xl text-{current_step_data["color"]} mr-6')
                    with ui.column():
                        ui.label(current_step_data['name']).classes('text-3xl font-bold text-grey-9 mb-2')
                        ui.label(current_step_data['description']).classes('text-xl text-grey-6')
            
            # Overview Section
            with ui.card().classes('w-full mb-8'):
                ui.label('Overview').classes('text-2xl font-semibold text-grey-9 mb-4')
                ui.label(current_step_data['content']['overview']).classes('text-grey-7 leading-relaxed')
            
            # Key Activities Section
            with ui.card().classes('w-full mb-8'):
                ui.label('Key Activities').classes('text-2xl font-semibold text-grey-9 mb-4')
                for activity in current_step_data['content']['key_activities']:
                    with ui.row().classes('items-start mb-3'):
                        ui.icon('circle').classes(f'text-{current_step_data["color"]} text-xs mt-2 mr-3')
                        ui.label(activity).classes('text-grey-7')
            
            # Methods & Tools Section
            with ui.card().classes('w-full mb-8'):
                ui.label('Methods & Tools').classes('text-2xl font-semibold text-grey-9 mb-4')
                with ui.grid(columns=2).classes('gap-4'):
                    for method in current_step_data['content']['methods']:
                        with ui.card().classes('p-4'):
                            ui.label(method['name']).classes('font-semibold text-grey-9 mb-2')
                            ui.label(method['description']).classes('text-grey-6 text-sm')
            
            # Pro Tips Section
            with ui.card().classes('w-full mb-8 bg-yellow-1 border-yellow-3'):
                ui.label('Pro Tips').classes('text-2xl font-semibold text-grey-9 mb-4')
                for tip in current_step_data['content']['tips']:
                    with ui.row().classes('items-start mb-3'):
                        ui.icon('lightbulb').classes('text-yellow-6 text-sm mt-1 mr-3')
                        ui.label(tip).classes('text-grey-7')
            
            # Deliverables Section
            with ui.card().classes('w-full mb-8'):
                ui.label('Key Deliverables').classes('text-2xl font-semibold text-grey-9 mb-4')
                for deliverable in current_step_data['content']['deliverables']:
                    with ui.row().classes('items-start mb-3'):
                        ui.icon('check_circle').classes('text-green-6 text-sm mt-1 mr-3')
                        ui.label(deliverable).classes('text-grey-7')

    def create_ui(self):
        ui.add_head_html('''
            <style>
            :root {
                --nicegui-default-padding: 0rem;
                --nicegui-default-gap: 0rem;
            }
            </style>
        ''')

        # Main container with flexbox layout
        with ui.column().classes('w-screen h-screen'):
            # Top Navigation Bar
            with ui.row().classes('w-full h-24 bg-blue border-b-4 border-black items-center justify-between m-0'):
                with ui.row().classes('items-center justify-between p-4'):
                    with ui.row().classes('items-center'):
                        ui.icon('palette').classes('text-4xl text-white bg-gradient-to-br from-blue-5 to-purple-6 rounded-lg p-2 mr-4')
                        with ui.column():
                            ui.label('Design Thinking Hub').classes('text-xl font-bold text-white')
                            ui.label('Learn the innovation process step by step').classes('text-sm text-white')
                    with ui.column().classes('items-end'):
                        ui.label('Current Stage').classes('text-sm text-white')
                        self.current_stage_text = ui.label(f'{self.current_step + 1} of {len(self.design_steps)}').classes('text-lg font-semibold text-white')

            # Main content area with two columns
            with ui.row().classes('flex-1 h-full w-full'):
                # Left Sidebar - Design Steps
                with ui.card().classes('w-1/3 h-full border-r border-grey-3 rounded-none'):
                    self.sidebar = ui.column().classes('h-full w-full')
                    
                # Right Column - Main Content and Navigation
                with ui.column().classes('w-2/3 h-full'):
                    # Scrollable main content
                    with ui.scroll_area().classes('flex-1 w-full'):
                        self.main_content = ui.column().classes('max-w-4xl mx-auto pt-8 w-full')
                        
                    # Fixed navigation at bottom
                    with ui.card().classes('border-t border-grey-3 rounded-none w-full'):
                        with ui.row().classes('items-center justify-between p-6 max-w-4xl mx-auto w-full'):
                            self.prev_button = ui.button('Previous Stage', on_click=self.previous_step).props('outline').classes('px-4 py-2')
                            self.step_counter = ui.label(f'Stage {self.current_step + 1} of {len(self.design_steps)}').classes('text-sm text-grey-5')
                            self.next_button = ui.button('Next Stage', icon='arrow_forward', on_click=self.next_step).classes('px-4 py-2')
        
        # Initialize content
        self.build_main_content()
        self.update_content()

# Create and run the app
def main():
    app = DesignThinkingApp()
    app.create_ui()
    
    ui.run(
        title='Design Thinking Hub',
        favicon='🎨',
        dark=False,
        reload=True,
        show=True,
        host='0.0.0.0',
        port=8080
    )

if __name__ in {"__main__", "__mp_main__"}:
    main()