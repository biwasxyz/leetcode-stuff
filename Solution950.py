class Solution(object):
    def deckRevealedIncreasing(self, deck):
        deck.sort()
        n = len(deck)
        result = [0] * n
        queue = list(range(n))

        for card in deck:
            result[queue.pop(0)] = card
            if queue:
                queue.append(queue.pop(0))

        return result

# Example usage:
solution = Solution()
deck = [17, 13, 11, 2, 3, 5, 7]
print(solution.deckRevealedIncreasing(deck))  # Output: [2, 13, 3, 11, 5, 17, 7]
