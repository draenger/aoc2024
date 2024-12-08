from collections import defaultdict
from math import gcd

class AntennaSystem:
    def __init__(self):
        pass
        
    def find_antennas(self, grid):
        """Znajduje wszystkie anteny i ich pozycje."""
        antennas = defaultdict(list)
        for y in range(len(grid)):
            for x in range(len(grid[0])):
                if grid[y][x] != '.':
                    antennas[grid[y][x]].append((x, y))
        return antennas

    def find_antinodes_part1(self, antenna1, antenna2):
        """Dla części 1:
           Znajduje dwa antinody dla pary anten, 
           na podstawie warunków z części pierwszej."""
        x1, y1 = antenna1
        x2, y2 = antenna2
        # Dwa antinody znajdują się w punktach:
        # (2*x1 - x2, 2*y1 - y2) i (2*x2 - x1, 2*y2 - y1)
        return [(2*x1 - x2, 2*y1 - y2), (2*x2 - x1, 2*y2 - y1)]

    def solve_part1(self, input_data):
        """Rozwiązuje zadanie z części 1."""
        grid = [list(line.strip()) for line in input_data.strip().split('\n')]
        height = len(grid)
        width = len(grid[0])
        
        antennas = self.find_antennas(grid)
        antinodes = set()
        
        for freq, positions in antennas.items():
            # Dla każdej pary anten o tej samej częstotliwości
            for i in range(len(positions)):
                for j in range(i + 1, len(positions)):
                    new_antinodes = self.find_antinodes_part1(positions[i], positions[j])
                    for x, y in new_antinodes:
                        if 0 <= x < width and 0 <= y < height:
                            antinodes.add((x, y))
        
        return len(antinodes)

    def solve_part2(self, input_data):
        """Rozwiązuje zadanie z części 2."""
        grid = [list(line.strip()) for line in input_data.strip().split('\n')]
        height = len(grid)
        width = len(grid[0])
        
        antennas = self.find_antennas(grid)
        antinodes = set()
        
        for freq, positions in antennas.items():
            # Jeśli mniej niż 2 anteny o tej częstotliwości, brak antinodów
            if len(positions) < 2:
                continue

            # Dla każdej pary anten o tej samej częstotliwości
            for i in range(len(positions)):
                for j in range(i+1, len(positions)):
                    x1, y1 = positions[i]
                    x2, y2 = positions[j]
                    
                    dx = x2 - x1
                    dy = y2 - y1
                    g = gcd(dx, dy)
                    dx_norm = dx // g
                    dy_norm = dy // g
                    
                    # Generuj antinody wzdłuż linii w obie strony
                    # w kierunku (dx_norm, dy_norm) i (-dx_norm, -dy_norm)
                    
                    # Zacznij od (x1,y1) i idź do przodu
                    k = 0
                    while True:
                        nx = x1 + k*dx_norm
                        ny = y1 + k*dy_norm
                        if 0 <= nx < width and 0 <= ny < height:
                            antinodes.add((nx, ny))
                            k += 1
                        else:
                            break
                    # Wstecz
                    k = -1
                    while True:
                        nx = x1 + k*dx_norm
                        ny = y1 + k*dy_norm
                        if 0 <= nx < width and 0 <= ny < height:
                            antinodes.add((nx, ny))
                            k -= 1
                        else:
                            break
        
        return len(antinodes)
