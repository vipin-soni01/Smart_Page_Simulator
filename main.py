"""
Operating System Page Replacement Simulator
===========================================

A Python-based interactive simulator developed by Vipin Soni
(B.Tech CSE - AI & ML, Lovely Professional University)

This project simulates and compares different page replacement 
algorithms used in Operating Systems memory management.

Implemented Algorithms:
    • FIFO (First-In-First-Out)
    • LRU (Least Recently Used)
    • Optimal (Belady’s Algorithm)

Project Features:
    • Interactive GUI with step-by-step visualization
    • Console mode for quick testing
    • Color-coded page hits and page faults
    • Real-time frame state updates
    • Performance metrics:
        - Total Page Faults
        - Total Page Hits
        - Hit Ratio
        - Fault Ratio
    • Algorithm comparison using bar charts (Matplotlib)
    • Clean modular structure for scalability

Project Structure:
    main.py
    modules/
        ├── simulation_engine.py   → Core algorithm logic
        ├── visualization.py       → Tkinter GUI interface
        ├── metrics.py             → Performance calculations
        └── utils.py (optional)    → Helper functions

Educational Purpose:
    This simulator helps students understand how memory 
    management works inside an Operating System and how 
    different algorithms impact performance.

Usage:
    python main.py            → Launch GUI mode
    python main.py --console  → Run console mode

Future Enhancements:
    • Dark mode UI
    • Step execution control (Next / Auto-run)
    • Export results as PDF
    • Add Clock (Second-Chance) Algorithm
    • Add graphical memory block animation

Author:
    Vipin Soni
    B.Tech CSE (AI & ML)
    Lovely Professional University
    GitHub: ()

Year:
    2026
"""
#  ------------------ ALGORITHMS ------------------

def fifo(pages, capacity):
    memory = []
    page_faults = 0

    for page in pages:
        if page not in memory:
            if len(memory) < capacity:
                memory.append(page)
            else:
                memory.pop(0)
                memory.append(page)
            page_faults += 1
        print("Memory:", memory)

    return page_faults


def lru(pages, capacity):
    memory = []
    page_faults = 0

    for page in pages:
        if page not in memory:
            if len(memory) < capacity:
                memory.append(page)
            else:
                # Remove least recently used
                lru_page = memory[0]
                for m in memory:
                    if pages[:pages.index(page)].count(m) < pages[:pages.index(page)].count(lru_page):
                        lru_page = m
                memory.remove(lru_page)
                memory.append(page)
            page_faults += 1
        print("Memory:", memory)

    return page_faults


def optimal(pages, capacity):
    memory = []
    page_faults = 0

    for i in range(len(pages)):
        if pages[i] not in memory:
            if len(memory) < capacity:
                memory.append(pages[i])
            else:
                future = pages[i+1:]
                replace = None
                farthest = -1

                for m in memory:
                    if m not in future:
                        replace = m
                        break
                    else:
                        index = future.index(m)
                        if index > farthest:
                            farthest = index
                            replace = m

                memory.remove(replace)
                memory.append(pages[i])

            page_faults += 1

        print("Memory:", memory)

    return page_faults


# ------------------ MAIN ------------------

pages = list(map(int, input("Enter page reference string (space separated): ").split()))
capacity = int(input("Enter number of frames: "))

print("\n--- FIFO ---")
fifo_faults = fifo(pages, capacity)
print("Total Page Faults (FIFO):", fifo_faults)

print("\n--- LRU ---")
lru_faults = lru(pages, capacity)
print("Total Page Faults (LRU):", lru_faults)

print("\n--- OPTIMAL ---")
optimal_faults = optimal(pages, capacity)
print("Total Page Faults (Optimal):", optimal_faults)


# Future enhancements could include:
# 1. Adding a GUI using Tkinter for better visualization.
# 2. Implementing performance metrics like hit ratio and fault ratio.
# 3. Adding more algorithms like Clock (Second-Chance).

