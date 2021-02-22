import gopigo as go
import time
go.set_speed(125)
for i in range(4):
	go.fwd(4)
	go.left(4)
go.stop()
