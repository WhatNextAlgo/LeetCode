from typing import List
class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        unable_to_eat = 0
        while unable_to_eat <= len(students)-1 and len(sandwiches) >= 0:
            print(students,sandwiches)
            if students[0] == sandwiches[0]:
                students.pop(0)
                sandwiches.pop(0)
                unable_to_eat = 0
            else:
                student = students.pop(0)
                students.append(student)
                unable_to_eat += 1
        return len(students)

            



if __name__=="__main__":
    s = Solution()
    print(s.countStudents(students = [1,1,1,0,0,1], sandwiches = [1,0,0,0,1,1]))
        