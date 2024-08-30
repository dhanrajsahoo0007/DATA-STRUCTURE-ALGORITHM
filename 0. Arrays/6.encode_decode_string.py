


class Solution:

    def encode(self, strs: list[str]) -> str:
        final_str = ""
        for n in strs :
            final_str = final_str+str(len(strs))+"#" + n
        print(final_str)
        return final_str
