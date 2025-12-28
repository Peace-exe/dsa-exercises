def maxNumberOfBalloons(text: str) -> int:

                counter = {}
                balloon = "balloon"
                for i in balloon:
                    counter[i]=0
                
                for c in text :
                    if c in balloon:
                        counter[c]+=1
                
                if all(c not in counter for c in balloon):
                    return 0
                else:
                    return min(counter['b'],counter['a'],counter['l']//2,counter['o']//2,counter['n'])