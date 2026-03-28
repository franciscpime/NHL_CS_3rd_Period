import itertools
import random


class Minesweeper():
    """
    Minesweeper game representation — with one lying cell.
    """

    def __init__(self, height=8, width=8, mines=8):
        self.height = height
        self.width = width
        self.mines = set()

        self.board = []
        for i in range(self.height):
            row = []
            for j in range(self.width):
                row.append(False)
            self.board.append(row)

        while len(self.mines) != mines:
            i = random.randrange(height)
            j = random.randrange(width)
            if not self.board[i][j]:
                self.mines.add((i, j))
                self.board[i][j] = True

        self.mines_found = set()

        # Pick one safe cell to be the liar (actual count + 1)
        safe_cells = [
            (i, j)
            for i in range(self.height)
            for j in range(self.width)
            if not self.board[i][j]
        ]
        self.lying_cell = random.choice(safe_cells)
        print(f"[DEBUG] Lying cell is: {self.lying_cell}")  # Remove for final submission


    def print(self):
        for i in range(self.height):
            print("--" * self.width + "-")
            for j in range(self.width):
                if self.board[i][j]:
                    print("|X", end="")
                else:
                    print("| ", end="")
            print("|")
        print("--" * self.width + "-")


    def is_mine(self, cell):
        i, j = cell

        return self.board[i][j]


    def nearby_mines(self, cell):
        count = 0

        for i in range(cell[0] - 1, cell[0] + 2):

            for j in range(cell[1] - 1, cell[1] + 2):
                if (i, j) == cell:
                    continue
                
                if 0 <= i < self.height and 0 <= j < self.width:
                    if self.board[i][j]:
                        count += 1

        # If this is the lying cell, return count + 1
        if cell == self.lying_cell:
            return count + 1

        return count


    def won(self):
        return self.mines_found == self.mines


class Sentence():
    """
    Logical statement about a Minesweeper game.
    Tracks which cell originated this sentence for lie detection.
    """

    def __init__(self, cells, count, origin=None):
        self.cells = set(cells)
        self.count = count
        self.origin = origin  # Which revealed cell created this sentence


    def __eq__(self, other):
        return self.cells == other.cells and self.count == other.count


    def __str__(self):
        return f"{self.cells} = {self.count} (from {self.origin})"


    def known_mines(self):
        if len(self.cells) == self.count and self.count != 0:
            return set(self.cells)
        return set()


    def known_safes(self):
        if self.count == 0:
            return set(self.cells)
        return set()


    def mark_mine(self, cell):
        if cell in self.cells:
            self.cells.remove(cell)
            self.count -= 1


    def mark_safe(self, cell):
        if cell in self.cells:
            self.cells.remove(cell)


class MinesweeperAI():
    """
    Minesweeper AI with lie detection and adaptive reasoning.
    """

    def __init__(self, height=8, width=8):
        self.height = height
        self.width = width

        self.moves_made = set()
        self.mines = set()
        self.safes = set()
        self.knowledge = []

        # Lie detection
        self.suspected_liar = None
        self.suspicion_scores = {}      # cell -> contradiction count
        self.ignored_sentences = set()  # indices of quarantined sentences


    def mark_mine(self, cell):
        self.mines.add(cell)
        for sentence in self.knowledge:
            sentence.mark_mine(cell)


    def mark_safe(self, cell):
        self.safes.add(cell)
        for sentence in self.knowledge:
            sentence.mark_safe(cell)


    def add_knowledge(self, cell, count):
        # 1) Mark move made
        self.moves_made.add(cell)

        # 2) Mark cell as safe
        self.mark_safe(cell)

        # 3) Build new sentence from unknown neighbors
        neighbors = set()
        adjusted_count = count
        for i in range(cell[0] - 1, cell[0] + 2):
            for j in range(cell[1] - 1, cell[1] + 2):
                if (i, j) == cell:
                    continue
                if 0 <= i < self.height and 0 <= j < self.width:
                    if (i, j) in self.mines:
                        adjusted_count -= 1
                    elif (i, j) not in self.safes:
                        neighbors.add((i, j))

        new_sentence = Sentence(neighbors, adjusted_count, origin=cell)
        self.knowledge.append(new_sentence)

        # 4) Update knowledge
        self._update_knowledge()

        # 5) Infer new sentences via subset method
        self._infer_new_sentences()

        # 6) Detect contradictions and identify liar
        self._detect_liar()


    def _update_knowledge(self):
        changed = True
        while changed:
            changed = False
            safes_to_mark = set()
            mines_to_mark = set()

            for i, sentence in enumerate(self.knowledge):
                if i in self.ignored_sentences:
                    continue
                safes_to_mark |= sentence.known_safes()
                mines_to_mark |= sentence.known_mines()

            for cell in safes_to_mark - self.safes:
                self.mark_safe(cell)
                changed = True

            for cell in mines_to_mark - self.mines:
                self.mark_mine(cell)
                changed = True

            self.knowledge = [s for s in self.knowledge if len(s.cells) > 0]


    def _infer_new_sentences(self):
        new_sentences = []
        active = [
            s for i, s in enumerate(self.knowledge)
            if i not in self.ignored_sentences
        ]

        for s1 in active:
            for s2 in active:
                if s1 == s2:
                    continue
                if s1.cells and s2.cells and s1.cells.issubset(s2.cells):
                    inferred_cells = s2.cells - s1.cells
                    inferred_count = s2.count - s1.count

                    # Negative count = logical contradiction
                    if inferred_count < 0:
                        self._flag_suspicion(s1.origin)
                        self._flag_suspicion(s2.origin)
                        continue

                    inferred = Sentence(inferred_cells, inferred_count,
                                        origin=s2.origin)
                    if inferred not in self.knowledge and inferred not in new_sentences:
                        new_sentences.append(inferred)

        self.knowledge.extend(new_sentences)
        if new_sentences:
            self._update_knowledge()


    def _detect_liar(self):
        """
        Scans knowledge base for impossible sentences:
        - Negative count
        - Count greater than number of cells
        Also checks for cells marked both safe and mine.
        Promotes top suspect to confirmed liar after 2+ contradictions.
        """
        for i, s in enumerate(self.knowledge):
            if i in self.ignored_sentences:
                continue

            if s.count < 0:
                self._flag_suspicion(s.origin)
                self.ignored_sentences.add(i)

            elif s.count > len(s.cells) and len(s.cells) > 0:
                self._flag_suspicion(s.origin)
                self.ignored_sentences.add(i)

        # Check for cells flagged as both mine and safe
        conflict = self.mines & self.safes
        if conflict:
            print(f"[AI] Conflict —> cell in both safe and mine sets: {conflict}")
            for cell in conflict:
                self._flag_suspicion(cell)

        # Promote top suspect if score is high enough
        if self.suspicion_scores and self.suspected_liar is None:
            top = max(self.suspicion_scores, key=self.suspicion_scores.get)
            if self.suspicion_scores[top] >= 2:
                self.suspected_liar = top
                print(f"[AI] Liar identified: {self.suspected_liar}")
                self._quarantine_liar()


    def _flag_suspicion(self, cell):
        if cell is None:
            return
        self.suspicion_scores[cell] = self.suspicion_scores.get(cell, 0) + 1
        print(f"[AI] Suspicion += {cell} "
              f"(score: {self.suspicion_scores[cell]})")


    def _quarantine_liar(self):
        """Ignores all sentences that came from the suspected liar."""
        for i, s in enumerate(self.knowledge):
            if s.origin == self.suspected_liar:
                self.ignored_sentences.add(i)
        print(f"[AI] Quarantined sentences from {self.suspected_liar}")


    def make_safe_move(self):
        for cell in self.safes:
            if cell not in self.moves_made:
                return cell
        return None


    def make_random_move(self):
        all_cells = [
            (i, j)
            for i in range(self.height)
            for j in range(self.width)
        ]

        # If liar known, prefer cells away from liar's neighbors
        if self.suspected_liar:
            liar_neighbors = self._get_neighbors(self.suspected_liar)
            preferred = [
                c for c in all_cells
                if c not in self.moves_made
                and c not in self.mines
                and c not in liar_neighbors
            ]
            if preferred:
                return random.choice(preferred)

        available = [
            c for c in all_cells
            if c not in self.moves_made and c not in self.mines
        ]

        return random.choice(available) if available else None


    def _get_neighbors(self, cell):
        neighbors = set()
        for i in range(cell[0] - 1, cell[0] + 2):
            for j in range(cell[1] - 1, cell[1] + 2):
                if (i, j) == cell:
                    continue
                if 0 <= i < self.height and 0 <= j < self.width:
                    neighbors.add((i, j))

        return neighbors
    


