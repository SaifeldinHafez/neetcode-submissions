class Solution:
    def isValid(self, s: str) -> bool:
        
        opened = set()
        opened.add("(")
        opened.add("{")
        opened.add("[")

        closed = set()
        closed.add(")")
        closed.add("]")
        closed.add("}")

        match = {
            "(" : ")",
            "[": "]",
            "{": "}"
        }

        if len(s) < 2:
            return False

        seen = []

        for b in s:
            if b in closed and not seen:
                return False
            if b in opened:
                seen.append(b)
            elif b in closed:
                if b != match[seen[len(seen) - 1]]:
                    return False
                else:
                    seen.pop()

        if seen:
            return False

        return True
