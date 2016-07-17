import Databuffer

Data = Databuffer.Databuffer('D:/Projekte/python/Data.csv', 3)
Data.GetBuffer(Buffer=[])

Time = Databuffer.Databuffer('D:/Projekte/python/Time.csv', 5)
Test=Time.GetBuffer()

print (Test)
Test = Time.Set(12)
print (Test)
Test = Time.Get()
print (Test)





