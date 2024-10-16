student_scores = [8 ,65 ,89 ,86 ,55 ,91 ,64 ,89]
# print(sum(student_scores))
# sum = 0
# for score in student_scores:
#     sum += score
# print(sum)
# print(range(1, 10))

print(max(student_scores))
print(min(student_scores))
max_score = student_scores[0]
min_score = student_scores[0]
for score in student_scores:
    if max_score < score:
        max_score = score
    if min_score > score:
        min_score = score
print(max_score)
print(min_score)