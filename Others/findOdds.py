"""
make a function that returns the number that appear odd times in an array
"""
import unittest


def merge_ranges( meetings ):
    ## Meeting(start, end)
    #sort the array
    meetings.sort()
    # make a pointer in the first position 
    i = 0
    # if we receive just one or an empty metting return the array
    if len( meetings )< 2:
        return meetings

    # go throught the array until the last position minus one,
    # because we are check current vs the next position 
    while i < len( meetings ) - 1:
        # if the if the end hour of our current position is later than
        # the starting hour of my next meeting
        if meetings[ i ][ 1 ] >= meetings[ i+1 ][ 0 ] :
            # save the start hour of my current position
            start = meetings[i][0]
            # save the later hour between the end hour of my current and next meeting as my end 
            end = max(meetings[ i ][ 1 ], meetings[ i + 1 ][ 1 ])
            # save both start and end hour in the first position of my meeting array
            meetings[ i ]= ( start, end )
            # delete the next meeting because in the range of the actual position the we melted before
            del(meetings[ i + 1 ])
        
        else:  
            i += 1
    return(meetings)

















# # Tests

class Test(unittest.TestCase):

    def test_meetings_overlap(self):
        actual = merge_ranges([(1, 3), (2, 4)])
        expected = [(1, 4)]
        self.assertEqual(actual, expected)

    def test_meetings_touch(self):
        actual = merge_ranges([(5, 6), (6, 8)])
        expected = [(5, 8)]
        self.assertEqual(actual, expected)

    def test_meeting_contains_other_meeting(self):
        actual = merge_ranges([(1, 8), (2, 5)])
        expected = [(1, 8)]
        self.assertEqual(actual, expected)

    def test_meetings_stay_separate(self):
        actual = merge_ranges([(1, 3), (4, 8)])
        expected = [(1, 3), (4, 8)]
        self.assertEqual(actual, expected)

    def test_multiple_merged_meetings(self):
        actual = merge_ranges([(1, 4), (2, 5), (5, 8)])
        expected = [(1, 8)]
        self.assertEqual(actual, expected)

    def test_meetings_not_sorted(self):
        actual = merge_ranges([(5, 8), (1, 4), (6, 8)])
        expected = [(1, 4), (5, 8)]
        self.assertEqual(actual, expected)

    def test_one_long_meeting_contains_smaller_meetings(self):
        actual = merge_ranges([(1, 10), (2, 5), (6, 8), (9, 10), (10, 12)])
        expected = [(1, 12)]
        self.assertEqual(actual, expected)

    def test_sample_input(self):
        actual = merge_ranges([(0, 1), (3, 5), (4, 8), (10, 12), (9, 10)])
        expected = [(0, 1), (3, 8), (9, 12)]
        self.assertEqual(actual, expected)


unittest.main(verbosity=2)