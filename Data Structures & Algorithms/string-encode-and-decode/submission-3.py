class Solution:

    def encode(self, strs: List[str]) -> str:
        if not len(strs):
            return "Ǥ"
        if len(strs) == 1:
            return strs[0]
        return "ǽ".join(strs)

    def decode(self, s: str) -> List[str]:
        if s == "Ǥ":
            return []
        spl = s.split("ǽ")
        if not spl:
            return [s]
        return spl
