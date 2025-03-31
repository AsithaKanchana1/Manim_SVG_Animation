from manim import *

class AnimateSVG(Scene):
    def construct(self):
        # Load the SVG file
        svg_image = SVGMobject("2.svg")  # Replace with your file path

        # Set color for the entire SVG object
        svg_image.set_color(WHITE)  # Set the color of the SVG (optional)

        # Alternatively, set colors for different parts of the SVG (if there are named parts)
        svg_image.set_color_by_gradient(BLUE, GREEN, GREEN)  # Use gradient from red to blue
        
        # Scale and position the SVG (optional)
        svg_image.scale(2)  # Scale the SVG
        svg_image.move_to(ORIGIN)  # Position the SVG at the center of the screen

        # Display the SVG image on screen
        self.play(DrawBorderThenFill(svg_image))  # Draw and fill the SVG
        
        # Additional animations (optional)
        self.play(svg_image.animate.shift(UP))  # Move the image upwards
        self.play(svg_image.animate.scale(0.5))  # Scale the image down

        # Fade the SVG out (optional)
        self.play(FadeOut(svg_image))

