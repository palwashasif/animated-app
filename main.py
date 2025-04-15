import tkinter as tk
import random
import math

class AnimatedApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Animated Particles")
        
        # Create canvas
        self.canvas = tk.Canvas(root, width=800, height=600, bg='black')
        self.canvas.pack()
        
        # Initialize particles
        self.particles = []
        for _ in range(50):
            self.create_particle()
            
        # Bind click event
        self.canvas.bind('<Button-1>', self.add_particles)
        
        # Start animation
        self.animate()
    
    def create_particle(self):
        x = random.randint(0, 800)
        y = random.randint(0, 600)
        size = random.randint(2, 5)
        speed = random.uniform(1, 3)
        angle = random.uniform(0, 2 * math.pi)
        color = '#{:02x}{:02x}{:02x}'.format(
            random.randint(50, 255),
            random.randint(50, 255),
            random.randint(50, 255)
        )
        particle = self.canvas.create_oval(
            x-size, y-size, x+size, y+size,
            fill=color, outline=color
        )
        self.particles.append({
            'id': particle,
            'x': x,
            'y': y,
            'size': size,
            'speed': speed,
            'angle': angle
        })
    
    def add_particles(self, event):
        for _ in range(10):
            self.create_particle()
    
    def animate(self):
        for p in self.particles:
            # Update position
            p['x'] += math.cos(p['angle']) * p['speed']
            p['y'] += math.sin(p['angle']) * p['speed']
            
            # Wrap around screen edges
            if p['x'] < 0:
                p['x'] = 800
            elif p['x'] > 800:
                p['x'] = 0
            if p['y'] < 0:
                p['y'] = 600
            elif p['y'] > 600:
                p['y'] = 0
            
            # Move particle
            self.canvas.coords(
                p['id'],
                p['x']-p['size'],
                p['y']-p['size'],
                p['x']+p['size'],
                p['y']+p['size']
            )
        
        # Schedule next animation frame
        self.root.after(16, self.animate)  # ~60 FPS

if __name__ == '__main__':
    root = tk.Tk()
    app = AnimatedApp(root)
    root.mainloop()
