# strings counting 
def count_substring(string, sub_string):
     cnt = 0
     i = 0
     for _ in range(len(string)):
        s = string.find(sub_string, i)
        if s >= 0:
            cnt += 1
            i = s+1
     return cnt

if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)