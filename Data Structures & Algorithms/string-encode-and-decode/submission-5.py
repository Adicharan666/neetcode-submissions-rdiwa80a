class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = ""
        for s in strs:
            encoded += str(len(s)) + "#" + s
        return encoded
    def decode(self, s: str) -> List[str]:
        decoded = []
        i = 0
        while i < len(s):
            # Find the delimiter position
            j = s.find("#", i)
            # Get the length of the next string
            length = int(s[i:j])
            # Extract the string using the length
            decoded.append(s[j+1:j+1+length])
            # Move pointer to the next encoded string
            i = j + 1 + length
        return decoded