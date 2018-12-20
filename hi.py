import pdb #디버깅

class sdoku:
  def __init__(self, inp):   # 9X9크기의 스도쿠 틀을 만든다.
    self.board = [[*map(int,i)] for i in inp.split('\n')]
    self.x = [(i,j) for i in range(9)
                    for j in range(9) if self.board[i][j] == 0]

  def solve(self):
    stc = [self.__solver(self.x[0])]            # self.x[0]에 좌표에 대한 함수 저장
    while stc:
      try:
        tx, ty = self.x[len(stc)-1]            # 현재 채워야하는 빈칸의 좌표값을 tx,ty로 설정
        self.board[tx][ty] = next(stc[-1])     #solver 찾은 중복제거한 값이 next(stc[-1])인데 board[tx][ty]로 들어감 0의값을 바꿈
      except:
        stc.pop()                               # stc 값을 -1
        tx, ty = self.x[len(stc)]               # except가 발생한 좌표값을 설정
        self.board[tx][ty] = 0                  # 해당 좌표값을 0으로 설정
        continue
      if len(stc) == len(self.x):               #len(stc)-->지금까지 채운 빈칸(코드에서는 0)의 횟수, len(self.x)-->0의 갯수  전체 배열에 대해서 빈칸(0)인 값들에 숫자를 넣었는지 확인
        self.__printans()                       #빈칸(0)인곳에 숫자를 모두 채웠으니 스도쿠 답을 프린트 한다.
        return                                  # 최종 스도쿠 끝낸다
      stc.append(self.__solver(self.x[len(stc)]))#스도쿠가 덜 풀렸을 시 배열에 0인값이 아직 있다면 다시 solver함수 호출
    print('정답을 찾을 수 없습니다')

  def __solver(self, v):
    ret = set(self.board[v[0]])    #긴 가로 축 중복값을 제거한다. --> ret에 넣음
    ret |= set(self.board[i][v[1]] for i in range(9)) #긴 세로 축 중복값을 제거한다.
    ret |= set(self.board[i][j] for i in range(3*(v[0]//3), 3*(v[0]//3)+3) #3으로 나눈 몫만큼 3x3을 점검(행관련) i값이 행의 범위를 정해줌 -> 중복값 제거
                                for j in range(3*(v[1]//3), 3*(v[1]//3)+3))#3으로 나눈 몫만큼 3x3을 점검(열관련) j값이 열의 범위를 정해줌 -> 중복값 제거
    ret = set(range(10)) - ret
    yield from ret

  def __printans(self): #스도쿠 답을 프린트 하는 함수
    for i in self.board:
      print(''.join(map(str,i)))
    print()



if __name__ == '__main__':    #해답을 알고싶은 스도쿠의 문제를 넣는다.
  inp = ['''\
087000600
651000200
300046000
973000010
216080593
040000762
000130007
002000345
005000180''',
'''\
901204000
680000320
004563090
050000000
268050479
000000030
090425600
046000053
000608907''']

  for j in (sdoku(i) for i in inp): j.solve()
##################