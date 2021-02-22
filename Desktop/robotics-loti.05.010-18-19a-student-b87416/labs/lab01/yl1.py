import gopigo as go
import time
go.set_speed(153)
for i in range(5):
	go.fwd()
	time.sleep(1)
	go.bwd()
	time.sleep(1)
go.stop()
