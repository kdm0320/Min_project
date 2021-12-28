def a(i):
    if i==5:
        print("check_finish")
        return
    print(f"{i} 번째에서 {i+1} 번째 함수를 호출합니다")
    print("check")
    a(i+1)
    print("check1")
    print(i, "번째 재귀함수를 종료합니다.")


a(1)