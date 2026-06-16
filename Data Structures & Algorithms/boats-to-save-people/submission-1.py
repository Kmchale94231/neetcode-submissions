class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        #1 2 4 5
        #1 2 2 3 3   

        people.sort()
        count = 0
        l, r = 0, len(people) - 1

        while l <= r:
            if people[l] + people[r] <= limit:
                count += 1
                r -= 1
                l += 1

            else:
                count += 1
                r -= 1

        return count
            








