f = open('test.txt', 'w')
f.write("Incomplete write...")
# File might contain nothing or partial content if interrupted.
