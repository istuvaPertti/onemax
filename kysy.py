import turtle as t
t.up()
t.setpos(-120, 140)
t.down()
t.speed(0)
t.ht()
def fe(lh):
	if lh<5:
		t.fd(lh)
		t.lt(60)
		t.fd(lh)
		t.rt(120)
		t.fd(lh)
		t.lt(60)
		t.fd(lh)
	else:
		fe(lh/2)
		t.lt(60)
		fe(lh/2)
		t.rt(120)
		fe(lh/2)
		t.lt(60)
		fe(lh/2)	
for i in range(1, 51):
	fe(80)
	t.rt(90)