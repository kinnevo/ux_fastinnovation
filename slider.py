from nicegui import ui, run
from typing import Optional, Any

class CardSlider:
    def __init__(self):
        self.current_index = 0
        self.cards = [
            {
                'title': 'Card 1',
                'subtitle': 'First Card',
                'content': 'This is the content of the first card. It demonstrates smooth transitions and responsive design.',
                'color': 'bg-blue-500',
                'icon': '🚀'
            },
            {
                'title': 'Card 2',
                'subtitle': 'Second Card',
                'content': 'This is the content of the second card. You can navigate using arrow keys or mouse clicks.',
                'color': 'bg-green-500',
                'icon': '🎯'
            },
            {
                'title': 'Card 3',
                'subtitle': 'Third Card',
                'content': 'This is the content of the third card. The slider wraps around for continuous navigation.',
                'color': 'bg-purple-500',
                'icon': '⭐'
            }
        ]
        self.slider_container: Optional[Any] = None
        self.indicators = []

    def next_card(self):
        self.current_index = (self.current_index + 1) % len(self.cards)
        self.update_slider()
        
    def prev_card(self):
        self.current_index = (self.current_index - 1) % len(self.cards)
        self.update_slider()
        
    def go_to_card(self, index):
        self.current_index = index
        self.update_slider()
        
    def update_slider(self):
        if self.slider_container:
            # Update transform to show current card
            offset = -self.current_index * 33.333
            self.slider_container.style(f'transform: translateX({offset}%)')
            
            # Update indicators
            for i, indicator in enumerate(self.indicators):
                if i == self.current_index:
                    indicator.classes('bg-white', remove='bg-white/50')
                else:
                    indicator.classes('bg-white/50', remove='bg-white')

    def create_ui(self):
        """Create the slider UI"""
        # Set up the page
        ui.page_title('3-Card Slider')

        # Add custom CSS
        ui.add_head_html('''
        <style>
            body {
                margin: 0;
                padding: 0;
                overflow: hidden;
            }
            
            .slider-container {
                transition: transform 0.3s ease-in-out;
                display: flex;
                width: 300%;
                position: relative;
                left: 0;
            }
            
            .card-content {
                min-height: 100vh;
                display: flex;
                align-items: center;
                justify-content: center;
                width: 33.333%;
                flex-shrink: 0;
                position: relative;
            }
            
            .nav-button {
                transition: all 0.2s ease;
            }
            
            .nav-button:hover {
                transform: scale(1.1);
                background-color: rgba(255, 255, 255, 0.2);
            }
            
            .indicator {
                transition: all 0.3s ease;
                cursor: pointer;
            }
            
            .indicator:hover {
                transform: scale(1.2);
            }
        </style>
        ''')

        # Main container
        with ui.element('div').classes('relative w-full h-screen overflow-hidden'):
            # Slider container
            with ui.element('div').classes('slider-container') as slider_container:
                self.slider_container = slider_container
                
                # Create cards
                for i, card in enumerate(self.cards):
                    with ui.element('div').classes(f'{card["color"]} card-content'):
                        with ui.element('div').classes('text-center text-white p-8 max-w-2xl'):
                            ui.label(card['icon']).classes('text-8xl mb-4')
                            ui.label(card['title']).classes('text-5xl font-bold mb-2')
                            ui.label(card['subtitle']).classes('text-2xl mb-6 opacity-90')
                            ui.label(card['content']).classes('text-lg leading-relaxed')
            
            # Navigation buttons
            with ui.element('div').classes('absolute inset-0 flex items-center justify-between px-4 pointer-events-none'):
                # Left arrow
                left_button = ui.button('❮').classes('nav-button text-white text-2xl p-4 bg-black/30 rounded-full hover:bg-black/50 pointer-events-auto')
                left_button.on('click', lambda: self.prev_card())
                    
                # Right arrow  
                right_button = ui.button('❯').classes('nav-button text-white text-2xl p-4 bg-black/30 rounded-full hover:bg-black/50 pointer-events-auto')
                right_button.on('click', lambda: self.next_card())
            
            # Indicators
            with ui.element('div').classes('absolute bottom-8 left-1/2 transform -translate-x-1/2 flex space-x-3'):
                for i in range(len(self.cards)):
                    indicator = ui.element('div').classes('w-3 h-3 rounded-full bg-white/50 indicator')
                    self.indicators.append(indicator)
                    
                    # Add click handler for each indicator
                    def make_indicator_handler(index):
                        return lambda: self.go_to_card(index)
                    
                    indicator.on('click', make_indicator_handler(i))

        # Set initial active indicator
        self.indicators[0].classes('bg-white', remove='bg-white/50')

        # Keyboard navigation
        def handle_keydown(e):
            if e.args.get('key') == 'ArrowLeft':
                self.prev_card()
            elif e.args.get('key') == 'ArrowRight':
                self.next_card()

        ui.on('keydown', handle_keydown)

        # Add mouse wheel support
        ui.add_head_html('''
        <script>
            document.addEventListener('wheel', function(e) {
                if (e.deltaY > 0) {
                    // Scroll down = next card
                    document.dispatchEvent(new KeyboardEvent('keydown', {key: 'ArrowRight'}));
                } else if (e.deltaY < 0) {
                    // Scroll up = previous card  
                    document.dispatchEvent(new KeyboardEvent('keydown', {key: 'ArrowLeft'}));
                }
            });
        </script>
        ''')

# Create the slider instance
slider = CardSlider()

# Run the app
if __name__ in {"__main__", "__mp_main__"}:
    slider.create_ui()
    ui.run(title='3-Card Slider', port=8080, show=True)