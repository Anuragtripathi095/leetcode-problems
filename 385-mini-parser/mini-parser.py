class Solution:
    def deserialize(self, s: str) -> NestedInteger:
        # Single integer case
        if s[0] != '[':
            return NestedInteger(int(s))

        stack = []
        num = ""
        curr = None

        for ch in s:
            if ch == '[':
                if curr is not None:
                    stack.append(curr)

                curr = NestedInteger()

            elif ch == ']':
                if num:
                    curr.add(NestedInteger(int(num)))
                    num = ""

                if stack:
                    parent = stack.pop()
                    parent.add(curr)
                    curr = parent

            elif ch == ',':
                if num:
                    curr.add(NestedInteger(int(num)))
                    num = ""

            else:
                num += ch

        return curr