arr = [10, 22, 9, 33, 41, 50, 41, 60]
longest_len, longest_seq = 0, []
current_seq = []
for i in arr:
    if not current_seq or i > current_seq[-1]:
        current_seq.append(i)
    else:
        if len(current_seq) > longest_len:
            longest_len = len(current_seq)
            longest_seq = current_seq
        current_seq = [i]
if len(current_seq) > longest_len:
    longest_len = len(current_seq)
    longest_seq = current_seq
print("Length:", longest_len)
print("Sequence:", longest_seq)
