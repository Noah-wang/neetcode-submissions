class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        current_string = ""
        current_count = 0

        for ch in s:
            if ch.isdigit():
                current_count = current_count * 10 + int(ch)
            elif ch == "[":
                stack.append((current_string, current_count))
                current_count = 0
                current_string = ""
            elif ch == "]":
                previous_string, repeat_count = stack.pop()
                current_string =  previous_string + current_string * repeat_count
            else:
                current_string += ch


        return current_string