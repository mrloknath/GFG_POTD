class Solution:    
    def maximumMeetings(self,n,start,end):
        # code here
        meetings = list(zip(start, end))
        meetings.sort(key=lambda x: x[1])
        last_end_time = -1
        count = 0
        for meeting in meetings:
            if meeting[0] > last_end_time:
                count += 1
                last_end_time = meeting[1]
        return count
