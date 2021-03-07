#8-1
def get_n_step_up_stairs_pattern(n:int)->int: # O(n)
    pattern_arr = [0 for _ in range(n)]
    pattern_arr[0],pattern_arr[1],pattern_arr[2] = 1,2,4
    for i in range(3,n):
        pattern_arr[i] = pattern_arr[i-3] + pattern_arr[i-2] + pattern_arr[i-1]
    return pattern_arr[n-1]

if __name__ == "__main__":
    print("10 step:{}".format(get_n_step_up_stairs_pattern(10)))
    print("20 step:{}".format(get_n_step_up_stairs_pattern(20)))
    print("30 step:{}".format(get_n_step_up_stairs_pattern(30)))

