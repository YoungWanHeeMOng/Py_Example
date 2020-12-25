
import turtle as t

t.shape('arrow')

n=8
for i in range(n):
	t.fd(100)
	t.rt(360/n)

t.circle(120)

n=60
t.speed('fastest')
for i in range(n):
	t.circle(60)
	t.right(360/n)

t.begin_fill()
for i in range(300):    # 300번 반복
    t.forward(i)        # i만큼 앞으로 이동. 반복할 때마다 선이 길어짐
    t.right(91)         # 오른쪽으로 91도 회전
t.end_fill()

t.mainloop()